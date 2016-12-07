from rena import crash

defaultcon = {
"chals": [
    {"id":"bin1","binary": "./overflow", "port": 666}],
"name": "comp"}

a = crash.Crash(defaultcon['chals'][0])
assert a.crashed('123') == False
assert a.crashed('%23') == True
print 'OK'
