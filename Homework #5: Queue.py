from collections import deque


def userInput():
    try:
        user = input("Please enter the integers for the array (Note: make sure they are separated by spaces): ")
        arr = [int(x) for x in user.split()]
        return arr

    except ValueError:
        print("Error: Please enter only integers.")
        return []


def reverseArray(arr):
    if not arr:
        return []

    queue = deque()
    stack = []


    for element in arr:
        queue.append(element)

    while len(queue) > 0:
        stack.append(queue.popleft())

    reversed_arr = []
    while len(stack) > 0:
        reversed_arr.append(stack.pop())

    return reversed_arr


def main():
    arr = userInput()

    if arr:
        print(f"\nOriginal Array: {arr}")

        reversed_result = reverseArray(arr)

        print("Output: ", end="")
        print(*(reversed_result))


if __name__ == "__main__":
    main()