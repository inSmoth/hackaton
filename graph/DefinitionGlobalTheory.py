from graph import Graph


class DefinitionGlobalTheory:
	"""Определитель глобальной гипотезы."""

	def __init__(self, graph: Graph):
		self.graph = graph
		self.last_node = graph.priority_node
		self.history = {self.last_node, }
		self.restricted = self.last_node.incompatibles.copy()

	def calculate(self):
		node = self.last_node

		priority_node = None

		while (node.connections - self.history) - self.restricted:
			# print(self.history, self.restricted)

			for connection in node.connections:
				# if connection.indx == 9:
				# 	print(connection.incompatibles)

				if connection in self.history or connection in self.restricted:
					continue
				if priority_node is None:
					priority_node = connection
				elif connection.priority > priority_node.priority:
					priority_node = connection

			self.history.add(priority_node)
			node = priority_node
			self.restricted.update(priority_node.incompatibles)
			priority_node = None

		return self.history
