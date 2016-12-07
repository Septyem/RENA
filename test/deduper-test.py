from rena import deduper

a=deduper.Deduper()
p1='1234'
p2='1234'
assert a.duplicate_check(p1,p2)==True
p1='1234'
p2='5678'
assert a.duplicate_check(p1,p2)==False
p1='1234'
p2='12345'
assert a.duplicate_check(p1,p2)==False
p1='1234'*11
p2='1234'*10+'4321'
assert a.duplicate_check(p1,p2)==True
print 'OK'
