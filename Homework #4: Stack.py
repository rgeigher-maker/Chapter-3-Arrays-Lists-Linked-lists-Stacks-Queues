def getUserInput():
    user_input = input("Please enter numbers separated by spaces: ")

    data_list = []
    for x in user_input.split():
        data_list.append(int(x))
    return data_list


def reverseArray(arr):

    stack = []

    for item in arr:
        stack.append(item)

    for i in range(len(arr)):
        arr[i] = stack.pop()

    return arr


def main():

    myArray = getUserInput()
    if not myArray:
        print("Array is empty.")
        return

    print(f"\nOriginal Data: {myArray}")


    reversedData = reverseArray(myArray)
    print(f"Reversed Data: {reversedData}")



if __name__ == "__main__":
    main()
