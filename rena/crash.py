from subprocess import Popen, PIPE
import signal

def _timeout(signum, frame):
    raise Exception("time out")

class Crash(object):
    '''
    Test whether binary will crash with the payload 
    '''
    def __init__(self, chal, maxtime=5):
        self._chal = chal
        self._maxtime = maxtime


    def crashed(self, payloads):
        '''Do the test with one payload

        Arguments:
            payloads(string list): the payload string to test
        '''
        try:
            signal.signal(signal.SIGALRM, _timeout)
            signal.alarm(self._maxtime)
            fw = open("/dev/null", "wb")
            proc = Popen([self._chal['binary']], stdin = PIPE, stdout = fw, stderr = fw, bufsize = 1)
            for p in payloads:
                proc.stdin.write(p)
                proc.stdin.flush()
            proc.wait()
            if proc.returncode == 0:
                return False
            else:
                return True
        except Exception,e:
            return False




