
class WeirdSequenceCounter(object):
    def __init__(self):
        self.sequence = [3,3,3,2]
        self.index = 1
        self.count = {3: 3, 2: 1}

    def length(self):
        return len(self.sequence)

    def iterate_once(self):
        instruction = self.sequence[self.index]
        self.index += 1
        self.count[3] += instruction
        self.count[2] += 1
        self.sequence.extend([3]*instruction+[2])
        return None

    def iterate_n_times(self, n=10):
        for i in range(n):
            self.iterate_once()
        status = (self.count[3], self.count[2], (1.0*self.count[3])/self.count[2])
        print "3s: %d, 2s: %d, ratio: %.6f" % status
        return status[2]

    def iterate_until_stability(self, n=100000, threshold=0.00000001):
        previous_ratio = 10
        while(True):
            new_ratio = self.iterate_n_times(n)
            if abs(new_ratio - previous_ratio) < threshold:
                break
            previous_ratio = new_ratio


counter = WeirdSequenceCounter()
counter.iterate_until_stability()
import pdb; pdb.set_trace()
