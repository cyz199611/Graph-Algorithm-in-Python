#!/anaconda/bin/python3

class Node(object):
	"""docstring for Node"""
	def __init__(self, key):
		self.key = key
		self.next = None
		
class Queue(object):
	def __init__(self):
		self.head = None
		self.tail = None

	def isEmpty(self):
		return self.head == None

	def queuePrint(self):
		tempNode = self.head
		tempList = []
		while tempNode:
			tempList.append(tempNode.key)
			tempNode = tempNode.next
		print('The queue is', tempList, '\n')

	def enqueue(self, key):
		tempNode = Node(key)

		if self.isEmpty():
			self.head = tempNode
			self.tail = tempNode
		else:
			self.tail.next = tempNode
			self.tail = tempNode

	def dequeue(self):
		if self.isEmpty():
			raise Exception('Cannot dequeue. The queue is empty !!!')

		tempNode = self.head

		if self.head == self.tail: # the queue contains only one node
			self.head = None
			self.tail = None
		else:
			self.head = self.head.next

		return tempNode.key


class AdjacencyList(object):
	def __init__(self, V, E):
		self.ptr = {v: list() for v in V} # dictionary representing the adjacency list
		self.visited = {v: False for v in V}
		for e in E:
			self.addEdge(e)

	def addEdge(self, e):
		self.ptr[e[0]].append(e[1])
		self.ptr[e[1]].append(e[0])


class BreadthFirstSearch(object):
	"""docstring for BreadthFirstSearch"""
	def __init__(self, graph):
		self.graph = AdjacencyList(graph['V'], graph['E'])

	def bfs(self, startVertexName):
		queue = Queue() # constructing a queue

		queue.enqueue(startVertexName)
		print('visiting vertex', startVertexName)
		self.graph.visited[startVertexName] = True

		# BFS --> queue
		while not queue.isEmpty():
			queue.queuePrint()
			actualVertexName = queue.dequeue()
			
			for vertexName in self.graph.ptr[actualVertexName]:
				if not self.graph.visited[vertexName]:
					print('visiting vertex', vertexName)
					self.graph.visited[vertexName] = True
					queue.enqueue(vertexName)

		print('BFS finish')



testGraph1 = { 'V': ['a','b','c','d','e'], 'E': [('a','b'),('a','c'),('a','d'),('b','e'),('d','e')] }
bfs = BreadthFirstSearch(testGraph1)
bfs.bfs('a')

print('\n\n\n')

testGraph2 = { 'V': [1,2,3,4,5,6], 'E': [(1,2),(1,3),(2,4),(2,5),(3,5),(4,5),(4,6),(5,6)] }
bfs = BreadthFirstSearch(testGraph2)
bfs.bfs(1)

print('\n\n\n')

testGraph3 = { 'V': [1,2,3,4,5,6,7,8], 'E': [(1,2),(1,3),(1,4),(2,5),(2,6),(4,7),(4,8)] }
bfs = BreadthFirstSearch(testGraph3)
bfs.bfs(1)

