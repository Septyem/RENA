import string

class Payload(object):
    '''
    Payload 
    '''
    def __init__(self, raw_str):
        self._raw = raw_str
        self.r_cache = None
        self.s_cache = None

    def raw_data(self):
        '''Return the raw data
        '''
        return self._raw

    def _parse(self, data, recv=True):
        payload = []
        cur = 0
        for i in range(6):
            cur = data.find('\n',cur)+1
        end = data.rfind('\n', 0, len(data)-1)+1
        while cur != end:
            nxt = data.find('\n',cur)
            if recv and data[cur] != '\t':
                payload.append(data[cur:nxt].decode('hex'))
            if (not recv) and data[cur] == '\t':
                payload.append(data[cur+1:nxt].decode('hex'))
            cur = nxt+1
        return payload

    def recved_data(self):
        '''Return the fragmented received data in string format
        '''
        if self.r_cache is None:
            self.r_cache = self._parse(self._raw, True)
        return self.r_cache

    def recved_idata(self):
        '''Return the intergated received data in string format
        '''
        return ''.join(self.recved_data())

    def sent_data(self):
        '''Return the fragmented sent data in string format
        '''
        if self.s_cache is None:
            self.s_cache = self._parse(self._raw, False)
        return self.s_cache

    def sent_idata(self):
        '''Return the intergated sent data in string format
        '''
        return ''.join(self.sent_data())

    def display(self, data, num=8):
        '''Display data. Only support string input now

        Arguments:
            data(string): the data to display
            num(int): the number of bytes per line
        '''
        if type(data) == type(''):
            self._display(data, num)
        elif type(data) == type([]):
            for part in data:
                self._display(part, num)
        else:
            raise Exception("not supported data type for display")

    def _display(self, data, num):
        printable=string.printable[:-5]
        for i in range((len(data)-1)/num+1):
            tmp = data[num*i:num*(i+1)]
            print "%s\t%s" % (tmp.encode('hex').ljust(num*2),
                              ''.join(map(lambda x:x if x in printable else '.',tmp)))
