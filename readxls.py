#coding=utf-8
import xlrd
def print_xls(path):
	data=xlrd.open_workbook(path)   #打开excel
	table=data.sheets()[0] #打开excel的第几个sheet
	nrows=table.nrows   #捕获到有效数据的行数
	books=[]
	for i in range(nrows):
		ss=table.row_values(i)   #获取一行的所有值，每一列的值以列表项存在
	#print ss
	for i in range(len(ss)):
		print ss[i]            #输出一行中各个列的值
	print '+++++++++++++++++++'

if __name__=='__main__':
	print_xls('data.xls')