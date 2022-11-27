import random

words = ["border","image","film","promise","random","lungs","doll","rhyme","damage","plants","python","program","smile"]

guessed = set()
wrong = 0
w = random.randint(0,len(words)-1)
state = ["_"]*len(words[w])
print("Welcome to hangman! Guess 6 letters wrong to lose! Let's begin!")

while True:
  print("".join(state))
  if len(guessed)>0:
    print("Guessed letters: "+",".join(guessed))
  g = input("Guess a letter: ")
  guessed.add(g)
  if g in words[w]:
    for i in range(len(words[w])):
      if words[w][i] == g:
        state[i] = g
    if "".join(state)==words[w]:
      print("".join(state))
      print("YOU WIN! Good job!")
      break
  else:
    wrong = wrong + 1
    print("WRONG! You have now guessed "+str(wrong)+" letter(s) wrong!")
    if wrong>5:
      print("The word was: "+words[w])
      print("GAME OVER")
      break