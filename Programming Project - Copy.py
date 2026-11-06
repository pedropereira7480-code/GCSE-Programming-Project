count = 1
game = ""
over = ""
Points = 0
Guesses = 0
authorised = ["Alexandre", "Max", "Muheed"]
user = ""
while user not in authorised:
  user = str(input("What is your authorised name?"))
MyFile = open("song list.txt")
while game != "over":
 SongAndArtist = MyFile.readline()
 words = SongAndArtist.split(",")
 Song = words[0]
 Artist = words[1]
 songWords = Song.split()
 print(Artist)
 for words in songWords:
  print(words[0])
 guess =input("Type your guess")
 if guess == Song:
  Points = Points + 3
  print("Correct, next song")
 else:
  print("try again")
  guess =input("Type your guess")
  if guess ==   Song: 
   Points = Points + 1
   print("Correct, next song")
  else:
   print("Game over, your score is",str(Points))
   game = "over" 
print(str(Points)+","+user)
filescores = []
myFile = open("scores.txt", "a+")
for i in range(5):
    leaderboard = myFile.read()
##    x = leaderboard.split(",")
##    x[0] = int(x[0])
##    filescores.append(x[0])
##print(filescores)
##for i in range(0,4):
##  if Points > filescores[i]:
##    print("done")
##    MyFile.write(final)
##    break
##  else:
##    print("Next attempt")
##    count = count + 1
  
