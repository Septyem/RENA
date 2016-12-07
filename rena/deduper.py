class Deduper(object):
    '''
    Payload deduplicator with certain policy
    '''
    def __init__(self, threshold_min=0, threshold_max=300):
        self.THRESHOLD_MIN = threshold_min
        self.THRESHOLD_MAX = threshold_max

    def duplicate_check(self, p1, p2):
        '''Check if two payloads are likely duplicate

        Arguments:
            p1(string), p2(string): the received payloads
        
        Current policy: two payloads with same length and around 80% identical contents are duplicate
        '''
        if len(p1) != len(p2):
            return False

        threshold = len(p1) / 5
        if threshold < self.THRESHOLD_MIN:
            threshold = self.THRESHOLD_MIN
        if threshold > self.THRESHOLD_MAX:
            threshold = self.THRESHOLD_MAX
        threshold = ((threshold-1)/4+1)*4 # since addresses are always aligned

        diffs = 0
        for i in xrange(len(p1)):
            if p1[i] != p2[i]:
                diffs += 1

        if diffs <= threshold:
            return True
        else:
            return False

