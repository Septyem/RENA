import sqlite3
import os

from .deduper import *
from .payload import *

class Database(object):
    '''
    Database handler
    '''
    def __init__(self, dbname, chals):
        self._dbname = dbname
        self._chals = chals
        if not os.path.exists(self._dbname):
            self._initdb()
        self._deduper = Deduper()

    def _initdb(self):
        conn = sqlite3.connect(self._dbname)
        c = conn.cursor()
        for chal in self._chals:
            c.execute('CREATE TABLE %s (raw text, payload blob, payload_size integer)' % chal['id'])
            #c.execute("INSERT INTO %s VALUES ('2006-01-05',X'ff0132333435',100)" % chal['id'])
        conn.commit()
        conn.close()

    def check_and_insert(self, p, table):
        '''Check if the payload has already been in the table. Insert it if not

        Arguments:
            p(Payload): the payload to insert
            table(string): the table name

        Return whether the insert is successful
        '''
        conn = sqlite3.connect(self._dbname)
        c = conn.cursor()
        recved = p.recved_idata()
        size = len(recved)
        raw = p.raw_data()
        isnew = True
        
        for row in c.execute('SELECT payload FROM %s WHERE payload_size=%d' % (table, size)):
            if self._deduper.duplicate_check(recved, str(row[0])):
                isnew = False
                break

        if isnew:
            c.execute("INSERT INTO %s VALUES ('%s',X'%s',%d)" % (table, raw, recved.encode('hex'), size))
            conn.commit()
        conn.close()
        return isnew

    def display(self, table):
        '''Display the payloads collected

        Arguments:
            table(string): the table to display
        '''
        conn = sqlite3.connect(self._dbname)
        c = conn.cursor()
        for row in c.execute('SELECT raw FROM %s' % table):
            p = Payload(row[0])
            p.display(p.recved_data())
            print '---'
