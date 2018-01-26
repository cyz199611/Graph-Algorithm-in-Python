#!/anaconda/bin/python3



class Node(object):
	"""docstring for Node"""
	def __init__(self, name):
		self.name = name
		self.minDistance = float('inf')
		self.visited = False # indicate whether the node is in queue or not
		self.predecessor = None



class Bellman_Ford(object):
	"""docstring for Bellman_Ford"""
	def __init__(self, V, E, startVertexName):
		self.vertexList = V
		self.edges = E
		self.HAS_NEG_CYCLE = False
		self.nodes = {v: Node(v) for v in self.vertexList}
		self.startVertexName = startVertexName

		if startVertexName == None:
			raise Exception('ERROR ! No start vertex specified ... ')


	def calculateShortestPath(self, startVertexName = None):
		graphNodes = self.nodes
		graphNodes[self.startVertexName].minDistance = 0

		for i in range(1, len(self.vertexList)):
			for edge in self.edges:
				startVertex = graphNodes[edge[0]]
				endVertex = graphNodes[edge[1]]
				weight = edge[2]

				newDistance = startVertex.minDistance + weight 
				if newDistance < endVertex.minDistance:
					endVertex.minDistance =  newDistance
					endVertex.predecessor = startVertex

		for edge in self.edges:
			startVertex = graphNodes[edge[0]]
			endVertex = graphNodes[edge[1]]
			weight = edge[2]

			newDistance = startVertex.minDistance + weight 
			if newDistance < endVertex.minDistance:
				self.HAS_NEG_CYCLE = True
				raise Exception('ERROR ! Negtive Cycle Detected !')


	def getShortestPath(self, endVertexName = None):
		if endVertexName == None:
			raise Exception('ERROR ! No end vertex specified ... ')
		else:
			graphNodes = self.nodes

			print('The minimum distance from', self.startVertexName, 'to', endVertexName, 'is', 
				graphNodes[endVertexName].minDistance)
			
			target = graphNodes[endVertexName]
			while target != None:
				print(target.name)
				target = target.predecessor

			print('\n')



testGraph = { 'V': ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'], \
	'E': [('A','B',5), ('A','E',9), ('A','H',8), ('B','H',4), ('B','C',12), ('B','D',15), \
	('C','D',3), ('C','G',11), ('D','G',9), ('E','H',5), ('E','F',4), ('E','G',20), \
	('F','C',1), ('F','G',13), ('H','C',7), ('H','F',6)] }

test = Bellman_Ford(testGraph['V'], testGraph['E'], 'A')

test.calculateShortestPath()
for item in testGraph['V'][1:]:
	test.getShortestPath(item)


