import copy
class Node:
   def __init__(self, matrix: list, size, previous: None) -> None:
      self.size = size
      self.matrix = copy.deepcopy(matrix)
      self.previous = previous
      if (self.previous == None):
         self.step = 0
         self.countCamp = 0
      else:
         self.step = self.previous.step + 1 
         self.countCamp = self.previous.countCamp + 1
   def __eq__(self, __o: object) -> bool:
      if isinstance(__o, Node):
         for i in range(self.size):
            for j in range(self.size):
               if self.matrix[i][j] != __o.matrix[i][j]:
                  return False
         return True
      return False
   def __bool__(self):
      if len(self.matrix) == 0:
         return False
      return True   