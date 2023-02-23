# Final Project Submission 2
# Jake Choi and Leo Zhi
# December 4, 2022

import pygame
import draw
import cmpt120image as cmpt
import random as r

###############################################################
# Keep this block at the beginning of your code. Do not modify.
def initEnv():
    print("\nWelcome! Before we start...")
    env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    while env not in "mri":
        print("Environment not recognized, type again.")
        env = input("Are you using mu w/pygame0 (m), replit (r) or idle (i)? ").lower()
    print("Great! Have fun!\n")
    return env

# Use the playSound() function below to play sounds. 
# soundfilename does not include the .wav extension, 
# e.g. playSound(apples,ENV) plays apples.wav
def playSound(soundfilename,env):
    if env == "m":
        exec("sounds." + soundfilename + ".play()")
    elif env == "r":
        from replit import audio
        audio.play_file("sounds/"+soundfilename+".wav")
    elif env == "i":
        pygame.mixer.init()
        pygame.mixer.music.load("sounds/"+soundfilename+".wav")
        pygame.mixer.music.play()

ENV = initEnv()
###############################################################

# define functions
def learn(difficulty):
  for i in range(difficulty):
    cmpt.showImage(draw.distributeItems(cmpt.getWhiteImage(400,300),
    cmpt.getImage(images[i]), 1))
    playSound(sounds[i], ENV)
    input(str(i+1) + '. Press Enter to continue...')
    cmpt.showImage(cmpt.getWhiteImage(400,300))


# define variables
sounds = []
images = []
level = 3

# create lists of sound names and image names
file = open('blackfoot.csv')
for line in file:
    name = line.strip('\n')
    sounds.append(name)
    images.append('images/'+name+'.png')

# main menu
while True:
  print("""\nMAIN MENU
1. Learn - Word Flashcards
2. Play - Seek and Find Game
3. Settings - Change Difficulty
4. Exit\n""")

  option = input("Choose an option: ")
  print('')

  # if user chooses 1
  if option == "1":
    print("LEARN")
    learn(level)

  # if user chooses 2, PLAY
  elif option == "2":
    numRounds = input("""PLAY
This is a seek and find game. You will hear a word.
Count how many of that item you find!

How many rounds would you like to play? """)

    # Repeat PLAY for specified number of rounds
    for i in range(int(numRounds)):
    
      cmpt.showImage(cmpt.getWhiteImage(400,300))

      # Create random challenge list
      challengeList = []
      
      for i in range(level):
        challengeList.append(sounds[i])
  
      r.shuffle(challengeList)

      # First word in challengeList will be the word played to the user
      key = challengeList[0]

  
      firstIteration = True
      for name in challengeList:
        image = cmpt.getImage('images/'+name+'.png')
        
        # recolour as a random dark colour
        randomColour = [r.randint(30,180),r.randint(30,180),r.randint(30,180)]
        new = draw.recolorImage(image, randomColour)
  
        # mirror
        mir = r.choice([True,False])
        if mir == True:
          new = draw.mirror(new)
        
        # minify
        min = r.choice([True, False])
        if min == True:
          new = draw.minify(new)
  
        # distribute items random number of times (up to 4)
        ranNum = r.randint(1,4)
  
        if firstIteration == True:
          newCanvas = draw.distributeItems(cmpt.getWhiteImage(400,300), new, ranNum)
          numKey = ranNum
          firstIteration = False
        else:
          newCanvas = draw.distributeItems(newCanvas, new, ranNum)

      # show final canvas and play audio file of word user is looking for
      cmpt.showImage(newCanvas)
      playSound(key, ENV)

      # accept input from user and check if correct
      answer = int(input("Listen to the word. How many of them can you find? "))
      
      if answer == numKey:
        input("Right! Press Enter to continue...\n")
      else:
        input("Sorry, there were " + str(numKey) + ". Press Enter to continue.\n")

  # if user chooses 3, SETTINGS
  elif option == "3":
    print("SETTINGS \nYou are currently learning " + str(level) + " words.")
    level = int(input('How many would you like to learn? (3-12) '))
    if level > len(sounds) or level < 3:
      print("Sorry, that's not a valid number. Resetting to 3 words.")
      level = 3

  # if user chooses 4, EXIT
  elif option == "4":
    break

print('Goodbye!')