class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
      self.storage.append(value)
      self._bubble_up(len(self.storage) - 1)

  def delete(self):
    if len(self.storage) == 0:
      return None
    elif len(self.storage) == 1:
      return self.storage.pop()
    else:
      deleted = self.storage[0]
      self.storage[0] = self.storage[len(self.storage) - 1]
      self.storage.pop()
      self._sift_down(0)
      return deleted

  def get_max(self):
    if self.storage[0] == None:
      return None
    else: 
      return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    while index > 0:
      parent = (index - 1) // 2
      if self.storage[index] > self.storage[parent]:
        self.storage[index], self.storage[parent] = self.storage[parent], self.storage[index]
        index = parent
      else:
        break

  def _sift_down(self, index):
    left = (2 * index) + 1
    right = (2 * index) + 2
    max_child = index
    if len(self.storage) > left and self.storage[max_child] < self.storage[left]:
      max_child = left
    if len(self.storage) > right and self.storage[max_child] < self.storage[right]:
      max_child = right
    if max_child == index:
      return
    else:
      temp = self.storage[index]
      self.storage[index] = self.storage[max_child]
      self.storage[max_child] = temp
      self._sift_down(max_child)