import rena

context = {
"chals": [
    {"id":"bin1","binary": "./overflow", "port": 666}], 
"ip": "1.1.1.1",
"name": "comp"}

a=rena.PCAP(context=context)
a.run('test-defcon.cap')
a.display()
