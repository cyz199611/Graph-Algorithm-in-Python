#!/anaconda/bin/python3

import heapq



class Edge(object):
	"""docstring for Edge"""
	def __init__(self, start, end, weight):
		self.startVertex = start
		self.endVertex = end
		self.weight = weight

	def __lt__(self, otherEdge):
		return self.weight < otherEdge.weight



class AdjacencyList(object):
	"""docstring for AdjacencyList"""
	def __init__(self, V, E): 
		# V is a list of vertices names
		# E is a list of edge tuples with format (startVertex, endVertex, weight)
		self.ptr = {v: list() for v in V} # dictionary representing the adjacency list
		for e in E:
			self.addEdge(e)

	def addEdge(self, e):
		self.ptr[e[0]].append(Edge(e[0],e[1],e[2]))
		self.ptr[e[1]].append(Edge(e[1],e[0],e[2]))



class Prim(object):
	"""docstring for Prim"""
	def __init__(self, vertexList, edgeList):
		# vertexList is a list containing the names of input vertices
		# edgeLIst has the format (vertexName, vertexName, edgeWeight)
		self.vertexToIndex = self._mapVertexToIndex(vertexList)
		self.indexToVertex = self._mapIndexToVertex(vertexList)

		self.vertexList = self._makeVertexList(vertexList)
		self.edgeList = self._makeEdgeList(edgeList)
		self.inMst = self._inMst(self.vertexList)
		self.graph = AdjacencyList(self.vertexList, self.edgeList)

		self.mst = []
		self._mstSize = 0
		self._heap = []
		self.startVertexName = 0


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

			temp[count] = (vertexId1, vertexId2, weight)
			count += 1

		return temp


	def _inMst(self, vertexList):
		# boolean array that indicates whether a vertex is already in MST
		return [False for v in vertexList]


	def _visit(self, start):
		self.inMst[start] = True

		for edge in self.graph.ptr[start]:
			end = edge.endVertex

			if not self.inMst[end]:
				heapq.heappush(self._heap, edge)


	def lazyMst(self):
		numVertices = len(self.vertexList)

		self._visit(self.startVertexName)

		while self._heap != [] and self._mstSize < numVertices - 1:
			minEdge = heapq.heappop(self._heap)
			end = minEdge.endVertex

			if self.inMst[end]:
				continue

			self.mst.append(minEdge)
			self._mstSize += 1
			self._visit(end)

		return self.mst



graph = { 'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G'], \
	'E': [('A','B',2), ('A','C',6), ('A','E',5), ('A','F',10), ('B','D',3), \
	('B','E',3), ('C','D',1), ('C','F',2), ('D','E',4), ('D','G',6), ('F','G',5)] }	

test = Prim(graph['V'], graph['E'])
testResult = test.lazyMst()

for edge in testResult:
	u = test.indexToVertex[edge.startVertex]
	v = test.indexToVertex[edge.endVertex]
	print(u, '-', v, '=', edge.weight)		

	
		