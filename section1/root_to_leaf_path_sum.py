class Node:
	def __init__(self):
		pass

	data = -1
	left = None
	right = None
class new_node():
	def __init__(self,data):
		self.data = data
		self.left = None
		self.right = None

class Queue:
	def __init__(self):
		pass

	data = None
	next = None


class bt:
	def __init__(self):
		pass

	def in_order(self, head):
		if head:
			self.in_order(head.left)
			print head.data,
			self.in_order(head.right)

	def pre_order(self, head):
		if head:
			print head.data,
			self.pre_order(head.left)
			self.pre_order(head.right)

	def post_order(self, head):
		if head:
			self.post_order(head.left)
			self.post_order(head.right)
			print head.data,

	@staticmethod
	def add(q, temp):
		if q:
			new = Queue()
			new.data = temp
			new.next = None
			tail = q
			if tail.next is None:
				tail.next = new
			else:
				while tail.next.next:
					tail = tail.next
				tail.next.next = new
		else:
			q = Queue()
			q.data = temp
		return q

	@staticmethod
	def is_empty(q):
		if q:
			return False
		return True

	@staticmethod
	def peek(q):
		return q.data

	@staticmethod
	def poll(q):
		if q:
			q = q.next
		return q

	def bfs(self, head):
		if head:
			q = self.add(None, head)
			while not self.is_empty(q):
				temp = self.peek(q)
				q = self.poll(q)
				print temp.data,
				if temp.left:
					q = self.add(q, temp.left)
				if temp.right:
					q = self.add(q, temp.right)

	@staticmethod
	def create_bt():
		head = Node()
		print "Enter data:",
		head.data = input()
		head.left = None
		head.right = None
		return head

	def insert_bt(self, head, temp):
		if head:
			q = self.add(None, head)
			while not self.is_empty(q):
				tail = self.peek(q)
				q = self.poll(q)
				if tail.left is None:
					tail.left = temp
					break
				elif tail.right is None:
					tail.right = temp
					break
				if tail.left:
					q = self.add(q, tail.left)
				if tail.right:
					q = self.add(q, tail.right)
			return head
		return temp
	def hasPathSum(self, node, s): 
		if node is None:
			return (s == 0)
		else:
			ans = 0
			subSum = s - node.data 
			if(subSum == 0 and node.left == None and node.right == None):
				return True
			if node.left is not None:
				ans = ans or self.hasPathSum(node.left, subSum)
			if node.right is not None:
				ans = ans or self.hasPathSum(node.right, subSum)
			return ans
	def print_paths(self, node, sum_value):
		path = []
		self.print_path_recursive(node, path, sum_value)
	def print_path_recursive(self, node, path, sum_value):
		if node is None:
			return
		path.append(node.data)
		if node.left is None and node.right is None:
			if sum(path) == sum_value:
				print path
		else:
			self.print_path_recursive(node.left, path, sum_value)
			self.print_path_recursive(node.right, path, sum_value)
		path.pop()
	def start(self):
		print "Enter\n1-insert values satisfying binary tree properties-------dynamically inserts the nodes using Queue\n2-randomly------we have to manually insert the nodes in the code"
		ch = input()
		if ch == 1:
			head = None
			while True:
				print "1-insert\n2-print\n3-search_path\n5-exit"
				ch = input()
				if ch == 1:
					if head is None:
						head = self.create_bt()
					else:
						print "Enter data:",
						temp = Node()
						temp.data = input()
						temp.left = None
						temp.right = None
						head = self.insert_bt(head, temp)
				elif ch == 2:
					print "1-inorder\n2-preorder\n3-postorder\n4-bfs"
					ch_1 = input()
					if ch_1 == 1:
						self.in_order(head)
					elif ch_1 == 2:
						self.pre_order(head)
					elif ch_1 == 3:
						self.post_order(head)
					elif ch_1 == 4:
						self.bfs(head)
					print
				elif ch == 3:
					print "Enter sum_value:",
					x = input()
					self.print_paths(head,x)
				elif ch == 5:
					break
		else:
			tree = bt()
			root = new_node(5)
			root.left = new_node(4)
			root.right = new_node(8)
			root.left.left = new_node(11)
			root.right.left = new_node(13)
			root.right.right = new_node(4)
			root.left.left.left = new_node(7)
			root.left.left.right = new_node(2)
			root.right.right.left = new_node(5)
			root.right.right.right = new_node(1)
			print "Enter sum_value:",
			x = input()
			tree.print_paths(root, x)


obj = bt()
obj.start()