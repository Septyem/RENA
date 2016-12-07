import subprocess
import logging
import time
import os

from .context import defaultcon
from .payload import *
from .DB import *
from .pcaploader import *
from .crash import *

class PCAP(object):
    '''
    Main class
    '''
    def __init__(self, dbname=None, context=defaultcon, test_crash=True):
        self._context = context
        self._test_crash = test_crash
        if dbname is None:
            self._dbname = self._default_dbname()
        else:
            self._dbname = dbname
        self._check_deps()
        self._DB = Database(self._dbname, self._context['chals'])

    def _default_dbname(self):
        return "%s%s.db" % (self._context['name'], time.strftime("%Y%m"))

    def _check_deps(self):
        DEPS = [["tshark","-v"],
                ["sqlite3","-version"]]
        DEPS = ["tshark -v",
                "sqlite3 -version"]
        for dep in DEPS:
            try:
                os.system(dep+">/dev/null")
            except Exception,e:
                raise Exception("%s not found!" % dep[:dep.find(' ')])

    def run(self, filename):
        '''Processing one pcap file. The result will be inserted into corresponding database.

        Arguments:
            filename(string): the pcap file to process
        '''
        ip = self._context['ip']
        chals = self._context['chals']
        for chal in chals:
            print "work on %s" % chal['id']
            loader = Loader(ip, chal['port'])
            payloads = loader.load(filename)
            c = Crash(chal)
            cnt = 0
            for p in payloads:
                if self._test_crash and (not c.crashed(p.recved_idata())):
                    continue
                if self._DB.check_and_insert(p, chal['id']):
                    cnt += 1
            print "Totally %d payloads inserted for %s" % (cnt, chal['id'])
            
    def display(self, chalid=None):
        '''Display the payloads collected

        Arguments:
            chalid(string): the challenge id to display. None for all challenges
        '''
        if chalid is None:
            chalids = []
            for chal in self._context['chals']:
                chalids.append(chal['id'])
        else:
            chalids = [chalid]

        for cid in chalids:
            self._DB.display(cid)
