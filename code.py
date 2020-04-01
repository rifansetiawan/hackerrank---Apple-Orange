age = int(input())
arr = sorted(map(int, input().rstrip().split()))
maximal = max(arr)

jumlah_max = 0
array = list(arr)
for x in range(len(arr)):
    array[x] = arr[x]
    if(array[x] == maximal):
        jumlah_max = jumlah_max + 1

print(jumlah_max)
