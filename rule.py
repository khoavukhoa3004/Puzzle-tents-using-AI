
from turtle import pos

from numpy import size
from node import Node
import copy

def getAllPossiblePosition(posible: list, size):
   ans = []
   if posible[0] + 1 < size:
      ans.append([posible[0]+ 1, posible[1]])
      if posible[1] + 1 < size:
         ans.append([posible[0] + 1, posible[1] + 1])
      if posible[1] - 1 >= 0:
         ans.append([posible[0] + 1, posible[1] - 1])
   if posible[0] - 1 >= 0:
      ans.append([posible[0] -1, posible[1]])
      if posible[1] + 1 < size: 
         ans.append([posible[0] - 1, posible[1] + 1])
      if posible[1] - 1 >= 0:
         ans.append([posible[0] - 1, posible[1] - 1])
   if posible[1] + 1 < size:
      ans.append([posible[0], posible[1] + 1])
   if posible[1] - 1 >= 0:
      ans.append([posible[0], posible[1] - 1])
   return ans

def getHorAndVerPosition(posible: list, size):
   ans = []
   if posible[0] + 1 < size: 
      ans.append([posible[0]+ 1, posible[1]])
   if posible[0] - 1 >= 0:
       ans.append([posible[0] -1, posible[1]])
   if posible[1] + 1 < size:
      ans.append([posible[0], posible[1] + 1])
   if posible[1] - 1 >= 0:
      ans.append([posible[0], posible[1] - 1])
   return ans 

def checkValidPosition(temp: Node, position: list)->bool:
   '''
   Check 
   '''
   i = position[0]
   j = position[1]
   if temp.matrix[i][j] == 2:
      return False
   list1 = getAllPossiblePosition(position, temp.size)
   for item in list1:
      if temp.matrix[item[0]][item[1]] == 2:
          return False
   list2 = getHorAndVerPosition(position, temp.size)
   for item in list2:
      if temp.matrix[item[0]][item[1]] == 1:
         return True

   return  False

def canAssign(temp: Node, row: list, col: list, position: list)->bool:
   if not(checkValidPosition(temp, position)):
      return False
   count = 1
   for i in range(temp.size):
      if temp.matrix[position[0]][i] == 2:
         count += 1
      if count > row[position[0]]:
         return False
   count = 1
   for i in range(temp.size):
      if temp.matrix[i][position[1]] == 2:
         count += 1  
      if count > col[position[1]]:
         return False
   return True

def isGoalState(temp: Node, row: list):
   if temp.countCamp == sum(row):
      return True
   return False

def AstarFunction(temp: Node)-> int:
   return  temp.countCamp * -4 + temp.step

   
def generateNode(current: Node, row: list, col: list)->list:
   ans = []
   for i in range(current.size):
      for j in range(current.size):
            if current.matrix[i][j] == 0 and canAssign(current, row, col, [i,j]):
               temp = Node(copy.deepcopy(current.matrix), current.size, current)
               temp.matrix[i][j] = 2
               temp.countCamp = current.countCamp + 1
               ans.append(temp)
   return ans
      