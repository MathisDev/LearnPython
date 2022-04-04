from random import shuffle
from statistics import *

notes = [8,12,10,9,4,20]
result = statistics.mean(notes)
print("la moyen est de {}".format(notes))

print(notes)
shuffle(notes)
print(notes)


