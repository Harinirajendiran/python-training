"""n = 12345
total=0
while n > 0:
    last = n % 10#5
    total = total + last#5 (total +=last)
    n = n // 10 #0
print("Sum of digits:", total)"""




"""n=[1,2,3,4]
if 4 in n:
    print("present")
else:
    print("not present")"""





"""num = "1001"
palindrome = num[::-1]#slicing
print (palindrome)"""





#64 32 16 8 4 2 1
#0  0  0 1 0 0 1
"""n=9
left=0
right=n.bit_length()
while left < right:
    l= (n >> left) & 1#1001>>0
    r= (n >> right) & 1#1001>>4
    if l != r:
        break
    left += 1
    right -= 1
print(n)"""

"""print(5 & 1)
bitwise operator:
and or not xor right shift left shift
& | ~ ^ >> <<"""





"""#singly linked list
class Node:
    def _init_(self,value):
        self.data=value
        self.next=None
class linkedlist:
    def _init_(self):
        self.head=None
    def add_at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None): #while(current.next)
                current = current.next
            current.next = new_node
    def add_at_beg(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def display(self):
        if self.head is None:
            print("linked list empty")
            return
        current = self.head
        while(current is not None):
            print(f"Data - {current.data}",end=" ")
            current = current.next
ll = linkedlist()
ll.display()
ll.add_at_end(10)
ll.add_at_end(20)
ll.add_at_end(30)
ll.add_at_end(40)
ll.add_at_end(50)
ll.add_at_beg(60)
ll.display()"""





"""#doubly linked list
class Node:
    def __init__(self,value):
        self.data=value
        self.next=None
        self.prev=None
class linkedlist:
    def __init__(self):
        self.head=None
    def add_at_end(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while(current.next is not None): #while(current.next)
                current = current.next
            current.next = new_node
            new_node.prev = current#doubly linked list
    def add_at_beg(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.head.prev = None
    
    def delete_at_end(self):
        if not self.head is None:
            print("Linked list empty")
            return
        else:
            current=self.head#4000
            while(current.next is not None):
                current=current.next#1000-2000-3000
            current.prev.next=None
            
    def delete_at_beg(self):
        if  self.head is None:
            print("Linked list empty")
            return
        else:
            self.head=self.head.next
            self.head.prev=None#dubly

    def display(self):
        if self.head is None:
            print("linked list empty")
            return
        current = self.head
        while(current is not None):
            print(f"Data - {current.data}",end=" ")
            current = current.next
ll = linkedlist()
ll.display()
ll.add_at_end(10)
ll.add_at_end(20)
ll.add_at_end(30)
ll.add_at_end(40)
print("------------")
ll.delete_at_end()
ll.display()
print("\n------------")
ll.delete_at_beg()
ll.display()"""




"""
#stack implementation using list
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)
        print(value, "pushed into stack")

    def pop(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print(self.stack.pop(), "popped from stack")

    def peek(self):
        if self.is_empty():
            print("Stack is empty")
        else:
            print("Top element:", self.stack[-1])

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print("Stack elements:", self.stack)


# Example usage
s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.display()
s.pop()
s.peek()"""


"""
#queue implementation using list
class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        print(value, "added to queue")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue.pop(0), "removed from queue")

    def front(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Front element:", self.queue[0])

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print("Queue elements:", self.queue)


# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.front()
"""

"""
#graph implementation using adjacency list       
class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
            print("Vertex added:", vertex)

    def add_edge(self, v1, v2):
        if v1 in self.graph and v2 in self.graph:
            self.graph[v1].append(v2)
            self.graph[v2].append(v1)  # Undirected graph
            print(f"Edge added between {v1} and {v2}")
        else:
            print("Add vertices first")

    def display(self):
        print("Graph (Adjacency List):")
        for vertex in self.graph:
            print(vertex, "->", self.graph[vertex])


# Example usage
g = Graph()

g.add_vertex('A')
g.add_vertex('B')
g.add_vertex('C')
g.add_vertex('D')

g.add_edge('A', 'B')
g.add_edge('A', 'C')
g.add_edge('B', 'D')

g.display()
"""


from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(graph[vertex])

# Call BFS
bfs(g.graph, 'A')
