import random
import csv

A = [ i+1 for i in range(1000000)]
random.shuffle(A)

with open('data.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(A)