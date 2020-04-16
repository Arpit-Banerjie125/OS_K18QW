disk = []
print("Enter current request: ")
disk.append(int(input()))
print("Enter number of requests: ")
n=int(input())
for i in range(n):
    disk.append((int(input())))
total = 0
direction = 1
pointer = disk.pop(0)
seq = [pointer]
while len(disk)>0:
    pointer += direction
    total += 1
    if pointer in disk:
        disk.remove(pointer)
        seq.append(pointer)
    if pointer == 4999:
        direction = -1
    if pointer == 0:
        direction = 1
print ("Total: ", total,"\nSequence: ", seq)