#encoding = utf-8
import json

def test():
	s = [{'name' : 'amy', 'age':'18'},{'name' : 'jack', 'age':'21'}]
	js = json.dumps(s)
	print js
	os = json.loads(js)
	name = os.get('name')
	print name
