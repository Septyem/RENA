import subprocess

from .payload import *
from .deduper import *


class Loader(object):
    '''
    Loading pcap file with selected address and port
    '''
    def __init__(self, addr, port):
        self._addr = addr
        self._port = port
        self._deduper = Deduper()

    def load(self, filename):
        '''Do loading

        Arguments:
            filename(string): the pcap file to load

        Return the loaded Payload list
        '''
        payloads = []
        streams = set()
        a = subprocess.check_output(['tshark' ,'-r', filename ,'-Y' ,'ip.addr eq %s and tcp.port eq %d' % (self._addr, self._port) ,'-T' ,'fields' ,'-e' ,'tcp.stream']).split('\n')
        for ele in a:
            if ele !='':
                streams.add(int(ele))

        for stream in streams:
            #print stream
            raw=subprocess.check_output(['tshark' ,'-r' ,filename ,'-q' ,'-z' ,'follow,tcp,raw,%d' % stream])
            p = Payload(raw)
            unique = True
            for old in payloads:
                if self._deduper.duplicate_check(p.recved_idata(), old.recved_idata()):
                    #print stream, old._raw[:200]
                    unique = False
                    break
            if unique:
                payloads.append(p)
        #print len(payloads)

        return payloads

    
