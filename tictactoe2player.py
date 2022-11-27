grid = ["_"]*9

def showboard():
  print("  1 2 3")
  print("a "+" ".join(grid[0:3])) # a 0 1 2
  print("b "+" ".join(grid[3:6])) # b 3 4 5
  print("c "+" ".join(grid[6:9])) # c 6 7 8

possiblemoves = set(["a1","a2","a3","b1","b2","b3","c1","c2","c3"])

def askmove(x):
  move = input("Enter "+x+"'s move: ")
  while move not in possiblemoves:
    move = input("Enter "+x+"'s move: ")
  possiblemoves.remove(move)
  if move[0]=="a":
    return int(move[1])-1
  elif move[0]=="b":
    return int(move[1])+2
  elif move[0]=="c":
    return int(move[1])+5

def checkwin():
  wins = ["012","345","678","036","147","258","048","246"]
  for way in wins:
    if grid[int(way[0])]==grid[int(way[1])] and grid[int(way[1])]==grid[int(way[2])] and grid[int(way[0])]!="_":
      print(str(grid[int(way[0])])+" WINS!")
      return True
  return False

showboard()
print("Enter moves like a1,b2,c3")

while True:
  # ask for O's move
  move = askmove("O")
  grid[move] = "O"
  showboard()
  if checkwin():
    break
  if len(possiblemoves)==0:
    print("DRAW!")
    break
  # ask for X's move
  move = askmove("X")
  grid[move] = "X"
  showboard()
  if checkwin():
    break
  if len(possiblemoves)==0:
    print("DRAW!")
    break