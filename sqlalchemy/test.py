#encoding=utf-8
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

#connecting
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/mine',echo=True)

#使用命令式语言创建一个类，用于描述与之对应的数据库表结构。
Base = declarative_base()
#通过declarative_base创建了一个基本类，基于这个base类可以创建一系列的扩展类，与数据库中的table相映射。

class User(Base):
	"""docstring for User"""
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String(64))
	password = Column(String(64))

	def __repr__(self):
		return "<User (name = '%s', password = '%s')>" % (self.name, self.password)


#创建一个schema
#当我们使用declarative系统声明一个class，declarative系统会自动创建一个Table对象。这个Table对象是MetaData（元数据）的成员。可以通过__table__属性查看Table对象。
User.__table__
#output:
#Table('users', MetaData(bind=None), Column('id', Integer(), table=<users>, primary_key=True, nullable=False), Column('name', String(length=64), table=<users>), Column('password', String(length=64), table=<users>), schema=None)

#会找到Base的所有子类，对不存在的表，创建表
Base.metadata.create_all(engine)

#创建Session
Session = sessionmaker(bind=engine)
#或者可以分两步
Session = sessionmaker()
Session.configure(bind=engine)
#上面通过sessionmaker创建了自定义的Session类，通过engine绑定到了我们的数据库。
#当需要和数据库进行交互的时候，就初始化一个session实例。
session = Session()

#增加和更新对象

#创建一个User的对象,使用add()持久化User对象。
user1 = User(name='amy', password='iloveyou')
session.add(user1)
#此时实例的状态是pending，插入的sql语句还没有在数据库中执行。Session将会在需要的时候对该语句进行持久化操作，也就是flush操作。
#如果我们query数据库，所有pending状态的信息都会被flush进数据库。
s_user1 = session.query(User).filter_by(name='amy').one()

#也可以使用add_all()来持久化多个User对象
session.add_all([
	User(name='wendy', password='foobar'),
	User(name='mary', password='xxg527'),
	User(name='fred', password='blah')])

#更新对象user1, 直接对对象实例进行操作即可。
user1.password = 'ilovelife'

#提交事务
session.commit()  #我测试下来，query操作并没有将之前的对象进行持久化。commit完之后，才进行了持久化。flush和commit之后的持久化概念好像不一样

#commit操作执行之后，session对象所持有的连接资源将会被还给连接池。

#回退事务。
session.rollback()

#建立关系

class Address(Base):
	__tablename__ = 'addresses'
	id = Column(Integer, primary_key=True)
	email_address = Column(String(64), nullable=False)
	user_id = Column(Integer, ForeignKey('users.id')) #对Address类定义了约束条件，user_id必须是users.id，也就是外键.

	user = relationship("User", back_populates='addresses')

	def __repr__(self):
		return "<Address(email_address='%s')>" % self.email_address

User.addresses = relationship("Address", order_by=Address.id, back_populates='user')

#relationship()定义式语言告诉ORM，Address类应当被链接到User类。使用Address.user指向对应的User实例。
#relationship()中的参数back_populations指定了对应的反向连接。使用User.addresses指向对应的Address实例列表。
#user = relationship("User", back_populates='addresses') 定义了Address.user和User.addresses的双向关系。

Base.metadata.create_all(engine) #创建不存在的表，跳过已存在的表

#创建一个user对象的时候，将会生成一个空的集合，默认使用list。
jack = User(name='jack', password='gjffdd')
jack.address
jack.addresses=[
	Address(email_address='jack@google.com'), 
	Address(email_address='jack@yahoo.cn')]
session.add(jack)
session.commit()

#使用join进行查询

query = session.query(User).join(Address)
print query
#SELECT users.id AS users_id, users.name AS users_name, users.password AS users_password 
#FROM users INNER JOIN addresses ON users.id = addresses.user_id

#使用隐式的join操作
query =  session.query(User, Address).filter(User.id==Address.user_id)
print query
#SELECT users.id AS users_id, users.name AS users_name, users.password AS users_password, addresses.id AS addresses_id, addresses.email_address AS addresses_email_address, addresses.user_id AS addresses_user_id 
#FROM users, addresses 
#WHERE users.id = addresses.user_id

#使用子查询。比如需要查询User表中每一个用户的addres记录数。也就是嵌套查询。
sta = session.query(Address.user_id, func.count('*').label('address_count')).group_by(Address.user_id).subquery()
res = session.query(User, sta.c.address_count).outerjoin(sta, User.id==sta.c.user_id).order_by(User.id)
print res
#SELECT users.id AS users_id, users.name AS users_name, users.password AS users_password, anon_1.address_count AS anon_1_address_count 
#FROM users LEFT OUTER JOIN (SELECT addresses.user_id AS user_id, count(%s) AS address_count 
#FROM addresses GROUP BY addresses.user_id) AS anon_1 ON users.id = anon_1.user_id ORDER BY users.id
res.all() #取回结果

#删除
#表User和Address存在一对多的对应关系，如果单独删除User中的一条数据，对应的Address表中的数据依然存在。
#重新设置删除时的级联操作属性（Cascade）
session.close()
#2018-06-19 17:23:46,520 INFO sqlalchemy.engine.base.Engine ROLLBACK
Base = declarative_base()

class User(Base):
	"""docstring for User"""
	__tablename__ = 'users'

	id = Column(Integer, primary_key=True)
	name = Column(String(64))
	password = Column(String(64))

	addresses = relationship("Address", order_by=Address.id, back_populates='user',cascade="all, delete, delete-orphan")

	def __repr__(self):
		return "<User (name = '%s', password = '%s')>" % (self.name, self.password)

class Address(Base):
	__tablename__ = 'addresses'
	id = Column(Integer, primary_key=True)
	email_address = Column(String(64), nullable=False)
	user_id = Column(Integer, ForeignKey('users.id')) #对Address类定义了约束条件，user_id必须是users.id，也就是外键.

	user = relationship("User", back_populates='addresses')

	def __repr__(self):
		return "<Address(email_address='%s')>" % self.email_address


