#!/anaconda/bin/python3

from math import sqrt



class ReadInput(object):
	"""docstring for ReadInput"""
	def __init__(self):
		self.V, self.E = self.readFile('usa.txt')

	def readFile(self, filaName):
		with open(filaName) as f:
			numV, numE = [int(num) for num in f.readline().strip().split()]
			V = [None for index in range(numV)]
			E = [None for index in range(numE)]

			for index in range(numV):
				name, x, y = [int(num) for num in f.readline().strip().split()]
				V[name] = (name, x, y)
			
			f.readline()

			for index in range(numE):
				vertex1, vertex2 = [int(num) for num in f.readline().strip().split()]
				E[index] = (vertex1, vertex2, 
					self.calcDistance(V[vertex1][1:], V[vertex2][1:]))

		return [v[0] for v in V], E

	def calcDistance(self,a,b):
		# take the distance as integer
		return int(sqrt( (a[0] - b[0])**2 + (a[1] - b[1])**2 ))



class Vertex(object):
	"""docstring for Vertex"""
	def __init__(self, name):
		self.name = name
		self.minDistance = float('inf')
		self.isInQueue = False # indicate whether the node is in queue or not
		self.predecessor = None 

	def __lt__(self, other):
		return self.minDistance < other.minDistance

	''' By default, __gt__() and __lt__() are each other’s reflection

	def __gt__(self, otherEdge):
		return self.weight > otherEdge.weight

	'''



class minHeap(object):
	"""define a completeBinaryTree, which is a binary max heap, using 0-based index"""
	def __init__(self):
		self.heap = []
		self.pos = dict() # store the index of each node 
		self.size = 0

	# parent index of a node
	def parent(self,i): 
		return (i - 1)//2

	# leftChild index of a node
	def leftChild(self,i):
		return 2*i + 1

	# rightChild index of a node
	def rightChild(self,i):
		return 2*i + 2

	# size of the heap
	def isEmpty(self): 
		return self.size == 0

	def _siftup(self, node):
		i = self.pos[node.name]
		
		while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
			# must update pos first
			self.pos[self.heap[self.parent(i)].name] = i
			self.pos[self.heap[i].name] = self.parent(i)
			# then update heap
			self.heap[self.parent(i)], self.heap[i] = self.heap[i], self.heap[self.parent(i)]
			i = self.parent(i)

	def _siftdown(self, node):
		i = self.pos[node.name]
		minIndex = i
		l = self.leftChild(minIndex)
		r = self.rightChild(minIndex)
		if l < self.size and self.heap[minIndex] > self.heap[l]:
			minIndex = l
		if r < self.size and self.heap[minIndex] > self.heap[r]:
			minIndex = r
		if i != minIndex:
			# must update pos first
			self.pos[self.heap[minIndex].name] = i
			self.pos[self.heap[i].name] = minIndex
			# then update heap
			self.heap[minIndex], self.heap[i] = self.heap[i], self.heap[minIndex]
			self._siftdown(node) 

	def push(self, node):
		self.size += 1 # increment size
		self.heap.append(node) # put the value at the end of the heap
		node.isInQueue = True
		self.pos[node.name] = self.size - 1
		self._siftup(node) 

	# Delete the root
	def extractMin(self): 
		if self.size == 0:
			raise Exception("ERROR ! The heap is EMPTY ! Cannot extract Min !")
			return

		root = self.heap[0]
		root.isInQueue = False
		lastNode = self.heap.pop()
		self.size -= 1

		if not self.isEmpty():
			self.heap[0] = lastNode
			self.pos[lastNode.name] = 0
			self._siftdown(self.heap[0])		
		
		return root

	def decreaseDistance(self, node):
		self._siftup(node)



class AdjacencyList(object):
	"""docstring for AdjacencyList"""
	def __init__(self, V, E): 
		# V is a list of vertices names
		# E is a list of edge tuples with format (startVertex, endVertex, weight)
		self.ptr = {v: list() for v in V} # dictionary representing the adjacency list
		self.nodes = {v: Vertex(v) for v in V}
		for e in E:
			self.addEdge(e)

	def addEdge(self, e):
		edge0 = (e[1],e[2])
		edge1 = (e[0],e[2])
		self.ptr[e[0]].append(edge0)
		self.ptr[e[1]].append(edge1)



class Dijkastra(object):
	"""docstring for Dijkastra"""
	def __init__(self, V, E, startVertexName = None):
		self.vertexList = V
		self.edgeList = E
		self.heap = minHeap() # heap that stores the graph node objects
		self.graph = AdjacencyList(self.vertexList, self.edgeList)
		self.startVertexName = startVertexName

		if self.startVertexName == None:
			raise Exception('ERROR ! No start vertex specified ... ')


	def calculateShortestPath(self):
		graphNodes = self.graph.nodes
		startVertex = graphNodes[self.startVertexName]

		startVertex.minDistance = 0

		self.heap.push(startVertex)

		while not self.heap.isEmpty():
			actualVertexName = self.heap.extractMin().name
			actualVertex = graphNodes[actualVertexName]
	
			for endVertexName, weight in self.graph.ptr[actualVertexName]:
				endVertex = graphNodes[endVertexName]
				newDistance = actualVertex.minDistance + weight

				if newDistance < endVertex.minDistance:				
					endVertex.minDistance = newDistance
					endVertex.predecessor = actualVertex
					if endVertex.isInQueue: 
						self.heap.decreaseDistance(endVertex)
					else:
						self.heap.push(endVertex)


	def getShortestPath(self, endVertexName = None):
		if endVertexName == None:
			raise Exception('ERROR ! No end vertex specified ... ')
		else:
			graphNodes = self.graph.nodes

			print('The minimum distance from', self.startVertexName, 'to', endVertexName, 'is', 
				graphNodes[endVertexName].minDistance)
			
			target = graphNodes[endVertexName]
			while target is not None:
				print(target.name)
				target = target.predecessor

			print('\n')


	def getShortestDistance(self):
		resultDistance = [None for index in self.graph.nodes.keys()]

		for key, node in self.graph.nodes.items():
			resultDistance[key] = node.minDistance

		return resultDistance




'''
testGraph = { 'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], \
	'E': [('A','B',5), ('A','E',9), ('A','H',8), ('B','H',4), ('B','C',12), ('B','D',15), \
	('C','D',3), ('C','G',11), ('D','G',9), ('E','H',5), ('E','F',4), ('E','G',20), \
	('F','C',1), ('F','G',13), ('H','C',7), ('H','F',6)] }

test = Dijkastra(testGraph['V'], testGraph['E'])

test.calculateShortestPath('A')

for item in testGraph['V'][1:]:
	test.getShortestPath(item)
'''
	

testGraph = ReadInput()
startVertex = 0
test = Dijkastra(testGraph.V, testGraph.E, startVertex)
test.calculateShortestPath()
testResult = test.getShortestDistance()

with open('result_1.txt', 'w') as f:
	for endVertex in range(len(testResult)):
		line = str(startVertex) + ' -> ' + str(endVertex) + '  =  '\
				+ str(testResult[endVertex]) + '\n'
		f.write(line)
