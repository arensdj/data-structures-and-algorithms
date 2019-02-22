class LinkedList():
	# pass

	head = None

	def insert(self, value):
		#pass
		node = Node(value)

		# when head is not assigned, assign a node to it
		if not self.head:
			self.head = node
		else:
			current = self.head

			# the head node does reference another node.  Find end of list and insert
			while current._next:
				current = current._next
			
			current._next = node

		# print(str(current))

	def includes(self, value):
		current = self.head

		# traverse linked list and fine value
		while current:
			if current.value == value:
				return True

			# set current to point to the next node
			current = current._next

		return False
	
	def print(self):
		current = self.head
		output = ''

		while current:
			output += current.value + ','
			current = current._next
		
		return output

class Node():
	# constructor
	def __init__(self, value):
		self.value = value
		self._next = None

	

