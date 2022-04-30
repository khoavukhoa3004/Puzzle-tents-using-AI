from searching import Searching

if __name__ == "__main__":
   temp = Searching()
   choose = int(input("chose bfs: 1 or aStar: 2"))
   if choose == 1:
      print("bfs")
      temp.bfs()
   elif choose == 2:
      temp.aStar()
   print(temp.path)
