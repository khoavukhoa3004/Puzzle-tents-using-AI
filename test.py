from data import data
from node import Node
temp = Node(data["size6"]["testcase1"]["matrix"], 6, None)
list1 = [temp]
temps = Node(data["size6"]["testcase1"]["matrix"], 6, None)
if temps in list1: 
   print("ok")
else: 
   print("false")