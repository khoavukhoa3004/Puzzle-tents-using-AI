from tracemalloc import start
from node import Node
import rule
from data import data
import time

class Searching:
   def __init__(self) -> None:
      self.size = int(input("Choose size: "))

      temp = input("Choose testcase: ")
      self.inputTESTCASE = data["size" + str(self.size)]["testcase" +str(temp)]
      
      self.initNode = Node(self.inputTESTCASE["matrix"],self.size,  None)
      self.row = self.inputTESTCASE["idxRow"]
      self.col = self.inputTESTCASE["idxCol"]
      self.path = []
   def getPath(self, endNode: Node)->list:
      ans = []
      temp = endNode
      while temp != None:
         ans.insert(0, temp)
         temp = temp.previous
      return ans
   def bfs(self):
      startTime = time.time()
      queue = [self.initNode]
      visited = []
      while len(queue) != 0:
         currentNode = queue.pop(0)
         visited.append(currentNode)
         if rule.isGoalState(currentNode, self.row):
            self.path = self.getPath(currentNode)

            executeTime = time.time() - startTime
            print("Time for searching: ", str(round(executeTime, 4)))
            print("Total node generated: ", len(visited) + len(queue))
            return
         
         generateNodeList = rule.generateNode(currentNode, self.row, self.col)
         for item in generateNodeList:
            if item not in visited and item not in queue:
               queue.append(item)


   def dfs(self):
      startTime = time.time()
      stack = []
      stack.append(self.initNode)
      visited = []
      while len(stack) != 0:
         currentNode = stack.pop(len(stack) - 1)
         visited.append(currentNode)
         if rule.isGoalState(currentNode, self.row):
            self.path = self.getPath(currentNode)
            executeTime = time.time() - startTime
            print("Time for searching: ", str(round(executeTime, 4)))
            print("Total node generated: ", len(stack) + len(visited)) 
            return
         generateNodeList = rule.generateNode(currentNode, self.row, self.col)
         for item in generateNodeList:
            if item not in visited and item not in stack:
               stack.append(item)
                  

      
   def aStar(self):
      startTime = time.time()
      openList = []
      closeList = []
      openList.append([rule.AstarFunction(self.initNode) ,self.initNode])
      while(len(openList) != 0):
         currentNode = openList.pop(0)
         #print(len(openList), currentNode[1].countCamp)
         closeList.append(currentNode[1])
         if rule.isGoalState(currentNode[1], self.row):
            self.path =  self.getPath(closeList[len(closeList) - 1])

            executeTime = time.time() - startTime
            print("Time for searching: ", str(round(executeTime, 4)))
            print("Total node: ", len(openList) + len(closeList))
            return
         generateNodeList = rule.generateNode(currentNode[1], self.row, self.col)
         for item in generateNodeList:
            if item not in closeList and item not in (subitem for subitem in openList):
               openList.append([rule.AstarFunction(item), item])
         openList.sort(key=lambda x: int(x[0]))

      self.path = self.getPath(closeList[len(closeList) - 1])