#!/usr/bin/python3
for i in range(1, 90):
    if i % 10 == 0:
        i += i // 10 + 1
        continue
    print("{:02d}".format(i), end=", " if i < 89 else "\n")
