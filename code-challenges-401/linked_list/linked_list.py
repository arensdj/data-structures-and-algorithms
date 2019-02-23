class LinkedList():
	"""
	Summary of LinkedList class:  The purpose of this class is to provide a data structure to
	create a sequence of Node objects that are connected/linked to each other.

	Attributes:
	head: Initially assigned value of None.
	
	Returns:
	An empty of a linked list
	"""

	# Initializer / Instance Attributes
	def __init__(self):
		"""
		Summary of constructor:  initializes an empty linked list

		Attributes:
		self.head 

		Returns:
		An empty of a linked list
		"""		
		self.head = None

	def insert(self, value):
		"""
		Summary of insert method:  inserts a value at the end of linked list

		Attributes:
		value (string):  a string value to insert at the end of linked list
		
		Returns:
		Nothing
		"""		
		# Instantiate a new Node object that will contain the input value
		node = Node(value)

		# when head is not assigned to a node, assign a node to it
		if not self.head:
			self.head = node
		else:
			current = self.head

			try:
				# Iterate over linked list to find the end.
				while current._next:
					current = current._next

				# Found end of list. Insert value by setting current to the node.
				current._next = node
			except StopIteration:
				print("Can't find the next object in linked list.")				

	def includes(self, value):
		"""
		Summary of includes function:  traverses linked list searching for a value

		Parameters:
		value (string): string a value used to search linked list
		
		Returns:
		True if value found
		False if value not found
		"""
		current = self.head

		try:
			# traverse linked list and find value
			while current:
				if current.value == value:
					return True

				# set current to point to the next node
				current = current._next
		except StopIteration:
			print("Can't find the next object in linked list.")

		return False
	
	def print(self):
		"""
		Summary of print function:  Prints the values in linked list to standard output

		Parameters:
		self which is the current linked list object
		
		Returns:
		A string containing the values in linked list. 
		If linked list if empty, returns an empty string.
		"""
		current = self.head
		output = ''

		try:
			while current:
				output += current.value + ','
				# set current to point to the next node
				current = current._next  	
		except StopIteration:
			print("Can't find the next object in linked list.")

		return output

class Node():
	"""
	Summary of Node class:  Class definition of a node which is an individual item contained in a linked list. Each node contains the data for each item.

	Attributes:
	value (string): a string value
	_next: a property of Node class that will reference the next Node object in a linked list
	
	Returns:
	A new instance of a Node class.
	"""
	# constructor
	def __init__(self, value):
		self.value = value
		self._next = None
