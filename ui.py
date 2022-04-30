from numpy import matrix
import pygame
from data import data
from searching import Searching
from button import Button
from node import Node
widthscreen = 800
heightscreen = 800

khaki = (240,230,140)
slate_gray = (112,128,144)
white = (255,255,255)
brown = (165,42,42)
darkgreen = (0,100,0)
green = (152,251,152)
red = (255,0,0)
black = (0,0,0)
pygame.init()

font1 = pygame.font.Font(None,30)


clock = pygame.time.Clock()

length_between_2_button = 5


class CampButton:
   def __init__(self, display_surface,location: list, width, height) -> None:
      self.display_surface = display_surface
      self.location = location #()
      self.width = width
      self.press = False
      self.height = height
      self.button = pygame.Rect(location, (width, height))
      self.buttonColor = white
      self.clicked = False
      self.setCamp = False
      self.action = False
   def draw(self):
      self.action = False
      pos = pygame.mouse.get_pos()
      if self.button.collidepoint(pos):
         if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
            self.clicked = True
            self.action = True
      if pygame.mouse.get_pressed()[0] == 0:
         self.clicked = False
      return self.action
   def display(self):
      if self.setCamp:
         self.displayCamp()
      else:
         self.displayNULL()

   def displayCamp(self):
      pygame.draw.rect(self.display_surface, green,self.button)
      pygame.draw.polygon(self.display_surface, slate_gray, [(self.location[0] + self.width/4, self.location[1]+ self.height*(3/4)), (self.location[0] + self.width/2, self.location[1] +self.height/4), (self.location[0] + self.width*(2/4), self.location[1] + self.height*3/4)] )
      pygame.draw.polygon(self.display_surface, white, [(self.location[0] + self.width/2, self.location[1]+ self.height*(3/4)), (self.location[0] + self.width/2, self.location[1] +self.height/4), (self.location[0] + self.width*(3/4), self.location[1] + self.height*3/4)] )
   def displayNULL(self):
      pygame.draw.rect(self.display_surface, self.buttonColor,self.button)


class TreeButton:
   def __init__(self, display_surface, location, width, height) -> None:
      self.display_surface = display_surface
      self.location = location
      self.width = width
      self.height = height
      self.button = pygame.Rect(location, (width, height))
   def display(self):
      pygame.draw.rect(self.display_surface, green,self.button)
      temp1 = pygame.Rect((self.location[0] + self.width/4 + self.width/8, self.location[1] + self.height*3/4),(self.width/4,self.height/4))
      pygame.draw.rect(self.display_surface, brown,temp1)
      temp2 = pygame.Rect((self.location[0] + self.width/4, self.location[1] + self.height/4), (self.width/2, self.height/2))
      pygame.draw.ellipse(self.display_surface,darkgreen, temp2)


class GameControl:
   def __init__(self, data, path, size, initLocation, width, height) -> None:
      self.path = path
      self.widthEle = width
      self.heightEle = height
      self.display_surface = pygame.display.set_mode((widthscreen, heightscreen))
      self.display_surface.fill(khaki)
      pygame.display.set_caption("Tent-puzzle")
      img = pygame.image.load("kakashi.jpg")
      pygame.display.set_icon(img)
      self.size = size
      self.row = data["idxRow"]
      self.col = data["idxCol"]
      self.initLocation = initLocation
      self.interfaceMatrix = []
      self.step = 0
      self.setData(self.path[0])
      

      self.nextStep = Button((625,600), 100, 50, "next")
      self.previousStep = Button( (500,600), 100, 50, "previous")

       
   def setData(self, temp):
      self.matrix = temp
      self.interfaceMatrix = []
      for i in range(self.size):
         for j in range(self.size):
            if j == 0:
               if(self.matrix.matrix[i][j] == 0 or self.matrix.matrix[i][j] == 2):
                  self.interfaceMatrix.append([CampButton(self.display_surface,(self.initLocation[0] + j *(self.widthEle + length_between_2_button), self.initLocation[1] + i *(self.heightEle + length_between_2_button)), self.widthEle,self.heightEle)])
               else:
                  self.interfaceMatrix.append([TreeButton(self.display_surface, (self.initLocation[0] + j *(self.widthEle + length_between_2_button), self.initLocation[1] + i *(self.heightEle + length_between_2_button)), self.widthEle,self.heightEle)])
            else:
                  if(self.matrix.matrix[i][j] == 0 or self.matrix.matrix[i][j] == 2):
                     self.interfaceMatrix[i].append(CampButton(self.display_surface, (self.initLocation[0] + j *(self.widthEle + length_between_2_button), self.initLocation[1] + i *(self.heightEle + length_between_2_button)), self.widthEle,self.heightEle))
                  else:
                     self.interfaceMatrix[i].append(TreeButton(self.display_surface, (self.initLocation[0] + j *(self.widthEle + length_between_2_button), self.initLocation[1] + i *(self.heightEle + length_between_2_button)), self.widthEle,self.heightEle))       
            if self.matrix.matrix[i][j] == 2:
               self.interfaceMatrix[i][j].setCamp = True

   def changeData(self, temp):
      for i in range(self.size):
         for j in range(self.size):
            if temp.matrix[i][j] == 0:
               self.interfaceMatrix[i][j].setCamp = False
            elif temp.matrix[i][j] == 2: 
               self.interfaceMatrix[i][j].setCamp = True

   def display(self):
      title = font1.render("Puzzle - tents", True, red)
      self.display_surface.blit(title, (300, 75))
      stepDispay = font1.render("Step: " + str(self.step), True, brown)
      self.display_surface.blit(stepDispay, (50,50))
      for i in range(self.size):
         if not(self.checkCol(i)):
            autoTurnOn =font1.render(str(self.col[i]) , True, red)          
         else: 
            autoTurnOn =font1.render(str(self.col[i]) , True, black)
         self.display_surface.blit(autoTurnOn, (150 + i*(self.widthEle + length_between_2_button) + self.widthEle/3, 125))

      for i in range(self.size):
         if not(self.checkRow(i)):
            autoTurnOn =font1.render(str(self.row[i]) , True, red)
         else:
            autoTurnOn =font1.render(str(self.row[i]) , True, black)
         self.display_surface.blit(autoTurnOn, (125, 150 + i*(self.heightEle + length_between_2_button) + self.heightEle/3))
      
      for i in range(self.size):
         for j in range(self.size):
            if isinstance(self.interfaceMatrix[i][j], CampButton):
               if self.interfaceMatrix[i][j].draw():
                  self.interfaceMatrix[i][j].setCamp = not(self.interfaceMatrix[i][j].setCamp)
                  print(i,j)
            self.interfaceMatrix[i][j].display()
      if self.nextStep.draw(self.display_surface):
         self.next()
      elif self.previousStep.draw(self.display_surface):
         self.previous()

         '''
         
            if isinstance(self.interfaceMatrix[i][j], CampButton):
               if self.interfaceMatrix[i][j].setCamp:
                  print(i,j)
         '''
   def next(self):
      if self.step < len(self.path) - 1:
         self.step += 1
         self.changeData(self.path[self.step])
         self.display()
         pygame.display.update()
   
   def previous(self):
      if self.step > 0:
         self.step -= 1
         self.changeData(self.path[self.step])
         self.display()
         pygame.display.update()

         
   def checkCol(self, temp):
      '''
      return True if no col error, else return False
      '''
      count = 0
      for j in range(self.size):
         if isinstance( self.interfaceMatrix[j][temp], CampButton):
            if self.interfaceMatrix[j][temp].setCamp:
               count += 1
            if count > self.col[temp]:
               return False
      return True

   def checkRow(self, temp):
      '''
      return True if no row error, else return False
      '''
      count = 0
      for j in range(self.size):
         if isinstance( self.interfaceMatrix[temp][j], CampButton):
            if self.interfaceMatrix[temp][j].setCamp:
               count += 1
            if count > self.row[temp]:
               return False
      return True




if __name__ == "__main__":
   temp = Searching()
   choose = int(input("chose bfs: 1 or dfs: 2 or aStar: 3 -> "))
   if choose == 1:
      print("Solving BFS. Please wait...")
      temp.bfs()
   elif choose == 3:
      temp.aStar()
      print("Solving A*. Please wait...")
   elif choose == 2:
      temp.dfs()
      print("Solving DFS. Please wait...")
   head = GameControl(temp.inputTESTCASE,temp.path, temp.size, (150,150), 30, 30)
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running ==False
            pygame.quit()
            exit(0)
      head.display_surface.fill(khaki)
      head.display()
      
      pygame.display.update()


