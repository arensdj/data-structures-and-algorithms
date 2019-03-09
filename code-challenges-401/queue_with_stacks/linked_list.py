class LinkedList():
    """
    Summary of LinkedList class:  The purpose of this class is to provide a data structure to
    create a sequence of Node objects that are connected/linked to each other.

    Attributes:
    head: Initially assigned value of None.

    Returns:
    An empty linked list
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
        self.tail = None

    def append_item(self, new_value):
        """
        Summary of append_item method:  traverses the linked list and appends a new value after the last item in the linked list

        Parameters:
        self (LinkedList): which is the current linked list object
        new_Value (string): a string value 

        Returns:
        True if value found
        False if value not found
        """
        node = Node(new_value)

        if not self.head:
            self.head = node
            self.tail = node
        else:
            current = self.head

            try:
                while current._next:
                    current = current._next

                current._next = node
                self.tail = current
            except StopIteration:
                print("Can't find the next object in linked list.")

    def find_from_end(self, k):
        """
        Summary of find_from_end method:  traverses linked list searching for a value that
        is k values from the end of linked list

        Parameters:
        k (string): string a value 

        Returns:
        A string value that is k from the end of the linked list
        """
        vals = []
        current = self.head

        if not self.head:
            return ''
        
        while current:
            vals.append(current.value)
            current = current._next

        if k > len(vals):
            print("Value k not found")
            return ''
        else:
            try:
                return vals[len(vals) - 1 - k]
            except IndexError:
                print("Value k not found")
            except:
                print("Value k not found")

    def includes(self, value):
        """
        Summary of includes method:  traverses linked list searching for a value

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

    def insert(self, value):
        """
        Summary of insert method: takes an input value as an argument and adds a new node with that value to the head of the list 

        Attributes:
        value (string):  a string value to insert at the head of linked list

        Returns:
        Nothing
        """
        # Instantiate a new Node object that will contain the input value
        node = Node(value)

        # when head is not assigned to a node, assign a node to it
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node._next = self.head
            self.head = node

    def insert_after(self, value, new_value):
        """
        Summary of insert_after method:  traverses the linked list searching for the 
        input value and inserts a new value after that value

        Parameters:
        self (LinkedList): which is the current linked list object
        value (string): a string value in linked list
        new_Value (string) a string value 

        Returns:
        Nothing
        """
        current = self.head

        node = Node(new_value)
        while current._next:
            if current.value == value:
                node._next = current._next
                current._next = node
                return

            current = current._next
        
        current._next = node
        self.tail = current

    def insert_before(self, value, new_value):
        """
        Summary of insert_before method:  traverses the linked list searching for the 
        input value and inserts a new value before that value

        Parameters:
        self (LinkedList): which is the current linked list object
        value (string): a string value in linked list
        new_Value (string) a string value 

        Returns:
        Nothing
        """
        current = self.head

        node = Node(new_value)
        while current._next:
            if current._next.value == value:
                node._next = current._next
                current._next = node
                return

            current = current._next

    def ll_merge(self, list2):
        """
        Summary of ll_merge method:   takes two linked lists as arguments. Zip the two linked lists together into
        one so that the nodes alternate between the two lists and return a reference to the head of the zipped list.

        Parameters:
        self (LinkedList): linked list
        list2 (LinkedList): a linked list

        Returns:
        reference to head of zipped list
        """
        head1 = self.head
        head2 = list2.head

        if head1 or head2:
            curr1 = head1
            curr2 = head2

            while curr1:
                ref1 = curr1._next
                ref2 = curr1

                if curr2: 
                    self.insert_after(curr1.value, curr2.value)
                    curr1 = ref1
                    curr2 = curr2._next
                else:
                    return head1

            if curr2:
                curr1 = ref2._next
                curr1._next = curr2
            
            return head1

        elif head1 == None:
            return head2
        else:
            return head1

    def print(self):
        """
        Summary of print method:  Prints the values in linked list to standard output

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

    def remove_from_list_end(self):
        """
        Summary of remove_from_list_end method:  traverses to the end of the linked list and removes   
        the last node

        Parameters:
        self (LinkedList): which is the current linked list object

        Returns:
        Nothing
        """
        current = self.head
        temp = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return
        else:
            while current._next != self.tail:
                current = current._next
        
            self.tail = current
            temp._next = None

    def remove_from_top(self):
        """
        Summary of remove_from_top method:  removes first node on the linked list

        Parameters:
        self (LinkedList): which is the current linked list object

        Returns:
        Nothing
        """
        current = self.head
        temp = self.head

        if current:
            current = current._next
            self.head = current
            temp._next = None

            return temp.value
        else:
            self.head.value = ''

            return self.head.value

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

# if __name__ == "__main__":