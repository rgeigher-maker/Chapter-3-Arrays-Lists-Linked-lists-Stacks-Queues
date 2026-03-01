class Node:

    def __init__(self, data):
        self.data = data
        self.next = None


def inputData():
    print("Enter the integers (please separate them by spaces): ")

    nums = list(map(int, input().split()))
    if not nums: return None

    head = Node(nums[0])
    curr = head

    for i in range(1, len(nums)):
        curr.next = Node(nums[i])

        curr = curr.next
    return head


def average(head):
    total = 0
    count = 0
    curr = head

    while curr:

        if curr.data % 2 == 0:
            total += curr.data

            count += 1

        curr = curr.next

    return total / count if count > 0 else 0


def split(head):
    if not head or not head.next:
        return None

    length = 0
    curr = head

    while curr:
        length += 1
        curr = curr.next

    curr = head

    for _ in range((length // 2) - 1):
        curr = curr.next

    second_half = curr.next
    curr.next = None  # Break the link

    return second_half


def merge(first, second):
    if not first: return second

    if not second: return first

    if first.data <= second.data:
        first.next = merge(first.next, second)
        return first

    else:
        second.next = merge(first, second.next)

        return second


def merge_sort(head):
    if not head or not head.next:
        return head

    second = split(head)
    head = merge_sort(head)
    second = merge_sort(second)

    return merge(head, second)


def print_list(head):
    curr = head

    while curr:
        print(curr.data, end=" -> " if curr.next else "")
        curr = curr.next
    print()


def main():
    head = inputData()

    if head:
        avg = average(head)

        print(f"\nAverage of even elements: {avg}")
        print()

        head = merge_sort(head)

        print("Sorted Linked List:")

        print_list(head)


if __name__ == "__main__":
    main()