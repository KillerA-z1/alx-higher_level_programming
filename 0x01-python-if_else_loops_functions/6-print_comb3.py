#!/usr/bin/python3
for i in range(1, 90):
    if i % 10 == 0:
        i += i // 10 + 1
        continue
    print(f"{i:02d}", end=", " if i < 89 else "\n")
