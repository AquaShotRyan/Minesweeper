from classes.board_class import Board

class MinesweeperBoard:
  MINE = 9 # how mines are defined in the board
  EMPTY = 0  # how non-mines are defined in the board
  FLAG = "|"  # how falgs are defined in the flag board

  def __init__(self, size:int = 10):
    self.__mines = 0
    self.__safeTilesFound = 0
    self.__size = size
    self.__displayBoard = Board(size, "")
    self.__mineBoard = Board(size, self.EMPTY)
    self.__gameOver = False

    # add mines
    for _ in range(10):
      self.__mineBoard.setRandom(self.MINE)

    # count mines
    for i in iter(self.__mineBoard.getAllIndices()):
      if (self.__mineBoard.get(i[0], i[1]) == self.MINE):
        self.__mines += 1


    # set up tiles next to mines
    mBoardIt = iter(self.__mineBoard.getAllIndices())
    for i in mBoardIt: # loop through all indices in the board
      curRow = i[0]
      curCol = i[1]
      curTile = self.__mineBoard.get(curRow, curCol)

      adjIt = iter(self.__mineBoard.getAllAdjIndex(curRow, curCol))
      for adj in adjIt: # loop through all adjacent indices
        adjRow = adj[0]
        adjCol = adj[1]

        if adjRow != None and adjCol != None:
          adjTile = self.__mineBoard.get(adjRow, adjCol)
          if adjTile == self.MINE and curTile != self.MINE:
            self.__mineBoard.set(curRow, curCol, curTile+1)
            curTile = self.__mineBoard.get(curRow, curCol)

  def placeFlag(self, row: int, col: int):
    tile = self.__displayBoard.get(row, col)
    if tile == "":
      self.__displayBoard.set(row, col, self.FLAG)
    elif tile == self.FLAG:
      self.__displayBoard.set(row, col, "")
    elif tile.isdigit():
      return
    
  def clickTile(self, row: int, col: int):
    displayTile = self.__displayBoard.get(row, col)
    mineTile = self.__mineBoard.get(row, col)
    print(self.__safeTilesFound)
    if mineTile == 0:
      self.autoClickTile(row, col)

    elif mineTile > 0:
      if mineTile == self.MINE:
        self.__gameOver = True;
        return
      elif displayTile == self.FLAG:
        return
      self.__displayBoard.set(row, col, mineTile)
      self.__safeTilesFound += 1
    
    
    
  # recursively reveal 0's if you click a 0
  def autoClickTile(self, row: int, col: int):
    displayTile = self.__displayBoard.get(row, col)
    mineTile = self.__mineBoard.get(row, col)

    if displayTile == "" and mineTile == 0:
      self.__displayBoard.set(row, col, mineTile)
      self.__safeTilesFound += 1
      adjTilesIndexes = iter(self.__mineBoard.getAllAdjIndex(row, col))
      for i in adjTilesIndexes:
        r = i[0]
        c = i[1]
        if r != None and c != None:
          self.autoClickTile(r, c)
    elif displayTile == "" and mineTile != self.MINE:
      self.clickTile(row, col)

  # getters
  def getMineBoard(self):
    return self.__mineBoard
  
  def getDisplayBoard(self):
    return self.__displayBoard
  
  def isWin(self):
    return (self.__size)**2-self.__mines == self.__safeTilesFound
  
  def isGameOver(self):
    return self.__gameOver
  
  def getSize(self):
    return self.__size
  
  def getMine(self):
    return self.MINE
  
  def getFlag(self):
    return self.FLAG


  
def test():
  testBoard = MinesweeperBoard()
  print(testBoard.getMineBoard())
  testBoard.clickTile(0, 0)
  print(testBoard.getDisplayBoard())

test()
        

        
          
          