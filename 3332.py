from fractions import Fraction

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

class WeirdSequenceExpander(object):
    def __init__(self, seed="3"):
        self.count = {3: 0, 2: 0}
        for i in (int(c) for c in seed if c in '23'):
            self.count[i] += 1

    def expand_once(self):
        self.count = {
                3: 3*self.count[3]+2*self.count[2],
                2: self.count[3]+self.count[2]
                }
        return Fraction(self.count[3], self.count[2])

    def expand_n_times(self, n=10):
        for i in range(n):
            ratio = self.expand_once()
        print "ratio: %.70f" % float(ratio)
        return ratio

    def expand_until_stability(self, n=15, threshold=0.000000000000000001, m=1):
        previous_ratio = 10
        for i in range(m):
            new_ratio = self.expand_n_times(n)
            if False: #abs(new_ratio - previous_ratio) < threshold:
                break
            previous_ratio = new_ratio
        return new_ratio


counter = WeirdSequenceExpander()
result = counter.expand_until_stability()
print result
counter = WeirdSequenceExpander("2")
result = counter.expand_until_stability()
print result
counter = WeirdSequenceExpander("23332222222222222223332233")
result = counter.expand_until_stability()
print result
