from rena import DB
from rena import payload
import os

os.system('rm try.db')
defaultcon = {
"chals": [
    {"id":"bin1","binary": "bin", "port": 666}, 
    {"id":"bin2","binary": "bin", "port": 667}], 
"name": "comp"}

a = DB.Database('try.db',defaultcon['chals'])
p1 = payload.Payload(open('testdata').read())
p2 = payload.Payload(open('testdata').read())
p3 = payload.Payload(open('testdata2').read())
assert a.check_and_insert(p1,'bin1')==True
assert a.check_and_insert(p2,'bin1')==False
assert a.check_and_insert(p3,'bin1')==True
print 'OK'
