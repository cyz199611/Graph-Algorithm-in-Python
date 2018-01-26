#!/anaconda/bin/python3



class Edge(object):
	"""docstring for Edge"""
	def __init__(self, start, end, weight):
		self.startVertex = start
		self.endVertex = end
		self.weight = weight

	def __lt__(self, otherEdge):
		return self.weight < otherEdge.weight

	''' By default, __gt__() and __lt__() are each other’s reflection

	def __gt__(self, otherEdge):
		return self.weight > otherEdge.weight

	'''



class DisjointSet(object):
	"""docstring for DisjointSet"""
	def __init__(self, vertexList):
		self._rank = [0 for v in vertexList]
		self._parent = [0 for v in vertexList]
		self._setCount = 0

		self.makeSets(vertexList)


	def makeSets(self, vertexList):
		for v in vertexList:
			self._makeSet(v)

	def _makeSet(self, v):
		self._parent[v] = v
		self._rank[v] = 0
		self._setCount += 1


	def find(self, v):
		if v != self._parent[v]:
			self._parent[v] = self.find(self._parent[v])

		return self._parent[v]


	def union(self, v1, v2):
		id1 = self.find(v1)
		id2 = self.find(v2)
		
		if id1 == id2:
			return # they are in the same set

		if self._rank[id1] < self._rank[id2]:
			self._parent[id1] = id2
		else:
			self._parent[id2] = id1
			if self._rank[id1] == self._rank[id2]:
				self._rank[id1] += 1

		self._setCount -= 1



class Kruskal(object):
	"""docstring for Kruskal"""
	def __init__(self, vertexList, edgeList):
		# vertexList is a list containing the names of input vertices
		# edgeLIst has the format (vertexName, vertexName, edgeWeight)
		self.vertexToIndex = self._mapVertexToIndex(vertexList)
		self.indexToVertex = self._mapIndexToVertex(vertexList)

		self.vertexList = self._makeVertexList(vertexList)
		self.edgeList = self._makeEdgeList(edgeList)
		self.disjointSet = DisjointSet(self.vertexList)

		self.mst = []


	def _mapVertexToIndex(self, vertexList):
		# map the name of vertex to a unique index
		vertexToIndex = dict()
		count = 0

		for v in vertexList:
			vertexToIndex[v] = count
			count += 1

		return vertexToIndex

	def _mapIndexToVertex(self, vertexList):
		# map the name of vertex to a unique index
		indexToVertex = dict()
		count = 0

		for v in vertexList:
			indexToVertex[count] = v
			count += 1

		return indexToVertex

	def _makeVertexList(self, vertexList):
		temp = [None for v in vertexList]

		for v in vertexList:
			vertexId = self.vertexToIndex[v]
			temp[vertexId] = vertexId

		return temp

	def _makeEdgeList(self, edgeList):
		temp = [None for e in edgeList]
		count = 0

		for e in edgeList:
			vertexId1 = self.vertexToIndex[e[0]]
			vertexId2 = self.vertexToIndex[e[1]]
			weight = e[2]

			temp[count] = Edge(vertexId1, vertexId2, weight)
			count += 1

		return temp

	def calcMST(self):
		self.edgeList.sort()

		for edge in self.edgeList:
			v1 = edge.startVertex
			v2 = edge.endVertex

			id1 = self.disjointSet.find(v1)
			id2 = self.disjointSet.find(v2)

			if id1 != id2:
				self.mst.append(edge)
				self.disjointSet.union(v1, v2)

				if self.disjointSet._setCount == 1:
					break

		return self.mst



graph = { 'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], \
	'E': [('A','B',2), ('A','C',6), ('A','E',5), ('A','F',10), ('B','D',3), \
	('B','E',3), ('C','D',1), ('C','F',2), ('D','E',4), ('D','G',6), ('F','G',5)] }	

test = Kruskal(graph['V'], graph['E'])
testResult = test.calcMST()

for edge in testResult:
	u = test.indexToVertex[edge.startVertex]
	v = test.indexToVertex[edge.endVertex]
	print(u, '-', v, '=', edge.weight)


'''
for v in test.vertexList:
	print(v.name)
	node = v.node
	while node is not None:
		if node._parent is not None:
			print(node.nodeID, node._parent.nodeID, node._rank)
		else: print(node.nodeID, node._parent, node._rank)
		node = node._parent
print(test.vertexList[test.vertexToIndex['F']].node._parent.nodeID)
test.disjointSet.find(test.vertexList[test.vertexToIndex['F']].node)
print(test.vertexList[test.vertexToIndex['F']].node._parent.nodeID)
'''	

