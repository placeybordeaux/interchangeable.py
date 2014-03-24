import time
from interchangeable import interchangeable

def naive_intersection(lista,listb):
    intersection = []
    for element in lista:
        if element in listb:
            intersection.append(element)
    return intersection

def set_intersection(lista,listb):
    return list(set(lista).intersection(set(listb)))

if __name__ == "__main__":
    intersection = interchangeable(naive_intersection, set_intersection)
    start = time.time()
    intersection.learning = True
    for i in range(350):
        intersection(range(i),range(i*2))
    print "learning took ", time.time() - start, " seconds"
    intersection.learning = False
    start = time.time()
    for i in range(350):
        intersection(range(i),range(i*2))
    choosing_time = time.time() - start
    print "choosing took ", choosing_time, " seconds"
    start = time.time()
    for i in range(350):
        naive_intersection(range(i),range(i*2))
    print "naive took ", (time.time() - start) - choosing_time, " more seconds than choosing"
    start = time.time()
    for i in range(350):
        set_intersection(range(i),range(i*2))
    print "set intersection took ", (time.time() - start) - choosing_time, " more seconds than choosing"
