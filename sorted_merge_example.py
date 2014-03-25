import time
import random
from interchangeable import interchangeable

def naive_merge(lista,listb):
    return sorted(lista + listb)

def triple_sort_merge(lista,listb):
    return sorted(sorted(lista) + sorted(listb))

def merge_sort_merge(lista,listb):
    a = sorted(lista)
    b = sorted(listb)
    i = 0
    j = 0
    ret = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            ret.append(a[i])
            i += 1
        else:
            ret.append(b[j])
            j += 1
    return ret

if __name__ == "__main__":
    merge = interchangeable(naive_merge, merge_sort_merge, triple_sort_merge)
    start = time.time()
    merge.learning = True
    for i in range(350):
        a = range(i)
        b = range(i,351)
        random.shuffle(a)
        random.shuffle(b)
        merge(a,b)
    print "learning took ", time.time() - start, " seconds"
    merge.learning = False
    start = time.time()
    for i in range(350):
        a = range(i)
        b = range(i,351)
        random.shuffle(a)
        random.shuffle(b)
        merge(a,b)
    choosing_time = time.time() - start
    print "choosing took ", choosing_time, " seconds"
    start = time.time()
    for i in range(350):
        a = range(i)
        b = range(i,351)
        random.shuffle(a)
        random.shuffle(b)
        naive_merge(a,b)
    print "naive took ", (time.time() - start) - choosing_time, " more seconds than choosing"
    start = time.time()
    for i in range(350):
        a = range(i)
        b = range(i,351)
        random.shuffle(a)
        random.shuffle(b)
        merge_sort_merge(a,b)
    print "merge_sort_merge took ", (time.time() - start) - choosing_time, " more seconds than choosing"
    start = time.time()
    for i in range(350):
        a = range(i)
        b = range(i,351)
        random.shuffle(a)
        random.shuffle(b)
        triple_sort_merge(a,b)
    print "triple_sort_merge took ", (time.time() - start) - choosing_time, " more seconds than choosing"
