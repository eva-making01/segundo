class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


node1 = Node(15)
node2 = Node(5)
node3 = Node(26)
node4 = Node(50)

node1.next = node2
node2.next = node3
node3.next = node1

head = node1

current = head
while current:
    print(current.data, end="->")
    current = current.next
print("None")