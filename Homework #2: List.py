def selectionSort(arr):
    n = len(arr)

    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j

        arr[i], arr[max_idx] = arr[max_idx], arr[i]

    return arr


def average(arr):
    total = 0
    count = 0

    for x in arr:
        if x % 2 == 0:
            total += x
            count += 1

    return total/count if count > 0 else 0


list = [2, 5, 3, 1, 4, 7, 6]

print("Your list in descending order: ")
print(selectionSort(list.copy()))
print()
print("Your average of even numbers is: ")
print(average(list))
