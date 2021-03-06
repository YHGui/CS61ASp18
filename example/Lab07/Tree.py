class Tree():
	"""A tree is a label and a list of branches"""
	def __init__(self, label, branches = []):
		self.label = label
		for branch in branches:
			assert isinstance(branch, Tree)
		self.branches = list(branches)

	def __repr__(self):
		if self.branches:
			branch_str = ', ' + repr(self.branches)
		else:
			branch_str = ''
		return 'Tree({0}{1})'.format(self.label, branch_str)
	def __str__(self):
		return '\n'.join(self.indented())

	def indented(self, k = 0):
		indented = []
		for b in self.branches:
			for line in b.indented(k + 1):
				indented.append('  ' + line)
		return [str(self.label)] + indented

	def is_leaf(self):
		return not self.branches

def memo(f):
	cache = {}
	def memoized(n):
		if n not in cache:
			cache[n] = f(n)
		return cache[n]
	return memoized

@memo
def fib_tree(n):
	if n == 0 or n == 1:
		return BTree(n)
	else:
		left = fib_tree(n - 2)
		right = fib_tree(n - 1)
		fib_n = left.label + right.label
		return BTree(fib_n, left, right)

def leaves(tree):
	if tree.is_leaf():
		return [tree.label]
	else:
		s = []
		for b in tree.branches:
			s.extend(leaves(b))
		return s
def prune_repeates(t, seen):
	t.branches = [b for b in t.branches if b not in seen]
	seen.append(t)
	for b in t.branches:
		prune_repeates(b, seen)

class BTree(Tree):
	"""A tree with exactly two branches which may be empty"""
	empty = Tree(None)
	def __init__(self, label, left = empty, right = empty):
		for b in (left, right):
			assert isinstance(b, BTree) or b is BTree.empty
		Tree.__init__(self, label, (left, right))

	@property
	def left(self):
		return self.branches[0]

	@property
	def right(self):
		return self.branches[1]

	def is_leaf(self):
		return [self.left, self.right] == [BTree.empty] * 2

	def __repr__(self):
		if self.is_leaf():
			return 'BTree({0})'.format(self.label)
		elif self.right is BTree.empty:
			left = repr(self.left)
			return 'BTree({0}, {1})'.format(self.label, left)
		else:
			left, right = repr(self.left), repr(self.right)
			if self.left is BTree.empty:
				left = 'BTree.empty'
			template = 'BTree({0}, {1}, {2})'
			return template.format(self.label, left, right)
def contents(t):
	if t is BTree.empty:
		return []
	else:
		return contents(t.left) + [t.label] + contents(t.right)
def balanced_bst(s):
	"""Contruct a binary search tree from a sorted list"""
	if not s:
		return BTree.empty
	else:
		mid = len(s) // 2
		left = balanced_bst(s[:mid])
		right = balanced_bst(s[mit+1:])
		return BTree(s[mid], left, right)

def adjoin(s, v):
	if s is BTree.empty:
		return BTree(v)
	elif s.root == v:
		return s
	elif s.root < v:
		return BTree(s.root, s.left, adjoin(s.right, v))
	elif s.root > v:
		return BTree(s.root, adjoin(s.left, v), s.right)