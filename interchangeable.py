import random
import time
from collections import defaultdict, Counter

class interchangeable:
    def __init__(self, *args):
        self.functions = args
        self.learning = False
        self.times = defaultdict(lambda: defaultdict(list))

    #TODO process kargs
    def __call__(self, *args, **kargs):
        if self.learning:
            ret_vals = []
            for func in self.functions:
                result = self.call(func, *args, **kargs)
                ret_vals.append(result)
                print "function", func.func_name, "returned", result, "in", self.times[func][self.process_args(*args)][-1], "seconds"
            return ret_vals[-1]
        else:
            func = self.select_fastest(*args, **kargs)
            return self.call(func, *args, **kargs)

    def select_fastest(self, *args, **kargs):
        fastest = None
        fastest_time = float("inf")
        for f in self.times.keys():
            times = self.times[f][self.process_args(*args)]
            if times:
                if sum(times)/float(len(times)) < fastest_time:
                    fastest = f
                    fastest_time = sum(times)/float(len(times))
        if fastest:
            return fastest
        else:
            return random.choice(self.functions)

    def process_args(self, *args, **kargs):
        return str(args)

    def call(self, func, *args, **kargs):
        start = time.time()
        ret = func(*args, **kargs)
        end = time.time()
        self.times[func][self.process_args(*args)].append(end - start)
        return ret


