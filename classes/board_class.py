import random

class Board:
  def __init__(self, size: int = 10, initValue = 0):
    self.__size = size
    self.__board = []

    for _ in range (self.__size):
      self.__board.append([initValue] * self.__size)

    # array of all (row, col) indices
    self.__indices = []
    for row in range (self.__size):
      for col in range (self.__size):
        self.__indices.append((row, col))
    self.__indices = tuple(self.__indices)

    # for iterator
    self.__row = 0
    self.__col = -1


  def setRandom(self, x):
    randRow = random.randint(0, self.__size-1)
    randCol = random.randint(0, self.__size-1)
    self.set(randRow, randCol, x)

  # returns an iterator that iterates through all adjacent tile indices
  def getAllAdjIndex(self, row, col):
    indices = []
    r, c = self.getAdjNIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjEIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjSIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjWIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjNEIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjSEIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjSWIndex(row, col)
    indices.append((r, c))
    r, c = self.getAdjNWIndex(row, col)
    indices.append((r, c))

    return tuple(indices)

  # setters that set the adjacent indices to x
  def setAdjN(self, row: int, col: int, x):
    r, c = self.getAdjNIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.set(r, c, x)
  
  def setAdjE(self, row: int, col: int, x):
    r, c = self.getAdjEIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.set(r, c, x)
  
  def setAdjS(self, row: int, col: int, x):
    r, c = self.getAdjSIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.set(r, c, x)
  
  def setAdjW(self, row: int, col: int, x):
    r, c = self.getAdjWIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.set(r, c, x)
  
  def setAdjNE(self, row: int, col: int, x):
    r, c = self.getAdjNEIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.gset(r, c, x)
  
  def setAdjSE(self, row: int, col: int, x):
    r, c = self.getAdjSEIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.set(r, c, x)

  def setAdjSW(self, row: int, col: int, x):
      r, c = self.getAdjSWIndex(row, col)
      if r == None or c == None:
        return None, None
      return self.set(r, c, x)
  
  def setAdjNW(self, row: int, col: int, x):
    r, c = self.getAdjNWIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.set(r, c, x)

  # getters that get the value of adjacent tiles
  def getAdjN(self, row: int, col: int):
    r, c = self.getAdjNIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)
  
  def getAdjE(self, row: int, col: int):
    r, c = self.getAdjEIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)
  
  def getAdjS(self, row: int, col: int):
    r, c = self.getAdjSIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)
  
  def getAdjW(self, row: int, col: int):
    r, c = self.getAdjWIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)
  
  def getAdjNE(self, row: int, col: int):
    r, c = self.getAdjNEIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)
  
  def getAdjSE(self, row: int, col: int):
    r, c = self.getAdjSEIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)

  def getAdjSW(self, row: int, col: int):
      r, c = self.getAdjSWIndex(row, col)
      if r == None or c == None:
        return None, None
      return self.get(r, c)
  
  def getAdjNW(self, row: int, col: int):
    r, c = self.getAdjNWIndex(row, col)
    if r == None or c == None:
      return None, None
    return self.get(r, c)

  # getters that get the index of adjacent tiles
  def getAdjNIndex(self, row: int, col: int):
    if row == 0:
      return None, None
    return row-1, col
  
  def getAdjEIndex(self, row: int, col: int):
    if col == self.__size-1:
      return None, None
    return row, col+1
  
  def getAdjSIndex(self, row: int, col: int):
    if row == self.__size-1:
      return None, None
    return row+1, col
  
  def getAdjWIndex(self, row: int, col: int):
    if col == 0:
      return None, None
    return row, col-1
  
  def getAdjNEIndex(self, row: int, col: int):
    r, _ = self.getAdjNIndex(row, col)
    _, c = self.getAdjEIndex(row, col)
    return r, c
  
  def getAdjSEIndex(self, row: int, col: int):
    r, _ = self.getAdjSIndex(row, col)
    _, c = self.getAdjEIndex(row, col)
    return r, c
  
  def getAdjSWIndex(self, row: int, col: int):
    r, _ = self.getAdjSIndex(row, col)
    _, c = self.getAdjWIndex(row, col)
    return r, c
  
  def getAdjNWIndex(self, row: int, col: int):
    r, _ = self.getAdjNIndex(row, col)
    _, c = self.getAdjWIndex(row, col)
    return r, c

  # basic getter and setter
  def get(self, row: int, col: int):
    return self.__board[row][col]
  
  def set(self, row: int, col: int, x):
    if row >= self.__size or col >= self.__size:
      return False;
    self.__board[row][col] = x
    return True;

  def getAllIndices(self):
    return self.__indices

  # other
  def __iter__(self):
    self.row = 0
    self.col = -1
    return self
  
  def __next__(self):
    if self.__col == self.__size-1:
      if self.__row == self.__size-1:
        raise StopIteration
      self.__row += 1
      self.__col = 0
    else:
      self.__col += 1
    return self.get(self.__row, self.__col)

  def __str__(self):
    return str(numpy.matrix(self.__board))

