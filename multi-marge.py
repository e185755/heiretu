import time
import random
from concurrent.futures import ThreadPoolExecutor
import csv

data = []

def CSV_read(file, list):
    with open(file, encoding='utf8', newline='') as f:
        csvreader = csv.reader(f)
        for row in csvreader:
            for i in row:
                data.append(int(i))

#統合部
def merge(A, left, mid, right):
    #リストを左右に分ける。
    L = A[left:mid]
    R = A[mid:right]
    for i in range(left,right):
        if len(L) == 0:#
            A[i] = R.pop(0)
        elif len(R) == 0:
            A[i] = L.pop(0)
        elif L[0] <= R[0]:
            A[i] = L.pop(0)
        else:
            A[i] = R.pop(0)

#分割部
def mergesort(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2  
        """executor = ThreadPoolExecutor(max_workers=2)
        executor.submit(mergesort, A, left, mid)
        executor.submit(mergesort, A, mid, right)"""
        mergesort(A, left, mid)
        mergesort(A, mid, right)
        merge(A, left, mid, right)
        return A

def firstmerge(A, left, right):
    if left + 1 < right:
        mid = (left + right)//2 
        with ThreadPoolExecutor(max_workers=4, thread_name_prefix="thread") as executor:
            executor.submit(mergesort, A, left, mid)
            executor.submit(mergesort, A, mid, right)
        merge(A, left, mid, right)
        #print(A)

"""
A = [ i+1 for i in range(1000000)]
random.shuffle(A)
print(A)
"""
CSV_read("data.csv", data)
start = time.time()
firstmerge(data,0,len(data))
print("fin")
print(data)
elapsed_time = time.time() - start
print ("elapsed_time:{0}".format(elapsed_time) + "[sec]")