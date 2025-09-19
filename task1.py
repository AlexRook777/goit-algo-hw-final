class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
        return self

    def merge_sort(self):
        if not self.head or not self.head.next:
            return self

        def split(head):
            slow = head
            fast = head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge(left, right):
            dummy = Node(0)
            tail = dummy
            while left and right:
                if left.data < right.data:
                    tail.next = left
                    left = left.next
                else:
                    tail.next = right
                    right = right.next
                tail = tail.next
            tail.next = left or right
            return dummy.next

        def merge_sort_rec(head):
            if not head or not head.next:
                return head
            left, right = split(head)
            left = merge_sort_rec(left)
            right = merge_sort_rec(right)
            return merge(left, right)

        self.head = merge_sort_rec(self.head)
        return self

def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    tail = dummy
    a = list1.head
    b = list2.head
    while a and b:
        if a.data < b.data:
            tail.next = a
            a = a.next
        else:
            tail.next = b
            b = b.next
        tail = tail.next
    tail.next = a or b
    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list

if __name__ == "__main__":
    # Приклад використання:
    l1 = LinkedList()
    for x in [3, 1, 5]:
        l1.append(x)

    l2 = LinkedList()
    for x in [4, 6, 2]:
        l2.append(x)

    # Виведення списків
    print("List 1:", l1.to_list())  # [3, 1, 5]
    print("List 2:", l2.to_list())  # [4, 6, 2]

    # Сортування списків
    sorted_l1 = l1.merge_sort()
    sorted_l2 = l2.merge_sort()
    print("Sorted list 1:", sorted_l1.to_list())  # [1, 3, 5]
    print("Sorted list 2:", sorted_l2.to_list())  # [2, 4, 6]

    # Злиття двох відсортованих списків
    merged = merge_sorted_lists(sorted_l1, sorted_l2)
    print("Merged list:", merged.to_list())  # [1, 2, 3, 4, 5, 6]

    # Реверс списку
    reversed = merged.reverse()
    print("Reversed list:", reversed.to_list())  # [6, 5, 4, 3, 2, 1]

