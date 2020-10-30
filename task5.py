import re
import collections
print ("Archana's Marksheet")
D = {}
n = int(input("Number of subjects: "))
subjects = []
for i in range(0, n):
    x, y = input("Enter the Subject Name and it's Marks: ").split()
    subjects.append((y, x))
subjects = sorted(subjects, reverse=True)
for i in subjects:
    print(i[1], i[0])



