#!/anaconda/bin/python3

class AdjacencyList(object):
	def __init__(self, V, E):
		self.ptr = {v: list() for v in V} # dictionary representing the adjacency list
		self.visited = {v: False for v in V}
		for e in E:
			self.addEdge(e)

	def addEdge(self, e):
		self.ptr[e[0]].append(e[1])
		self.ptr[e[1]].append(e[0])


class DepthFirstSearch(object):
	"""docstring for BreadthFirstSearch"""
	def __init__(self, graph):
		self.graph = AdjacencyList(graph['V'], graph['E'])

	def dfs(self, startVertexName):
		self.graph.visited[startVertexName] = True
		print('visiting vertex', startVertexName)

		for vertexName in self.graph.ptr[startVertexName]:
			if not self.graph.visited[vertexName]:
				self.dfs(vertexName)


testGraph1 = { 'V': ['a','b','c','d','e'], 'E': [('a','b'),('a','c'),('a','d'),('b','e'),('d','e')] }
dfs = DepthFirstSearch(testGraph1)
dfs.dfs('a')

print('\n\n\n')

testGraph2 = { 'V': [1,2,3,4,5,6,7], 'E': [(1,2),(1,3),(1,5),(2,4),(2,6),(6,5),(3,7)] }
dfs = DepthFirstSearch(testGraph2)
dfs.dfs(1)

print('\n\n\n')

testGraph3 = { 'V': [1,2,3,4,5,6,7,8], 'E': [(1,2),(1,3),(1,4),(2,5),(2,6),(4,7),(4,8)] }
dfs = DepthFirstSearch(testGraph3)
dfs.dfs(1)

