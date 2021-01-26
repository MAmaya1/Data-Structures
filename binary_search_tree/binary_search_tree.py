class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if value < self.value and self.left:
      self.left.insert(value)
    elif value < self.value:
      self.left = BinarySearchTree(value)
    elif value > self.value and self.right:
      self.right.insert(value)
    elif value > self.value:
      self.right = BinarySearchTree(value) 

  def contains(self, target):
    if target == self.value:
      return True
    elif target > self.value and self.right:
      return self.right.contains(target)
    elif target < self.value and self.left:
      return self.left.contains(target)
    else:
      return False

  def get_max(self):
    if self.right is None:
      return self.value
    else:
      return self.right.get_max()

  def for_each(self, cb):
    cb(self.value)
    if self.left is None and self.right is None:
      return
    else:
      if self.left is not None:
        self.left.for_each(cb)
      if self.right is not None:
        self.right.for_each(cb)