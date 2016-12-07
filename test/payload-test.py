from rena import payload

a = payload.Payload(open('testdata').read())
r = a.recved_data()
print len(r)
print r[5]
r = a.recved_data()
print len(r)
r = a.recved_data()
print len(r)
print r[5]
a.display(a.sent_idata())
a.display(a.recved_data())
test = ''
for i in range(256):
    test += chr(i)
a.display(test)
