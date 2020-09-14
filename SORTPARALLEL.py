import time
import multiprocessing
import random
import sys
def sleep_sort(seconds,out):

    time.sleep(0.2*seconds)
    #print(seconds)
    out.put(seconds)

    return seconds
def generate(N,R):
    ray=[5,4,2,6,7,1,3]
    ra=[]
    for i in range(1,R):
        ra.append(i)
    return random.sample(ra, N)
def parralel(N,R):
    array = generate(N, R)
    print("Generated List", array)
    processes = []
    q=multiprocessing.Queue()
    for i in range(0, len(array)):
        p = multiprocessing.Process(target=sleep_sort, args=(array[i], q))
        p.start()
        processes.append(p)
    for process in processes:
        process.join()
    out=[]
    while q.empty() is False:
        out.append(q.get())
    print("Sorted List",out)
def main():
    N=(int(sys.argv[1]))
    R=(int(sys.argv[2]))
    parralel(N,R)
if __name__ == "__main__":
    main()
