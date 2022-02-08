# Kibo FPWP Final Project 
# Click the "Instructions" tab for instructions 
# Put your final project code in this file for submission 
# Add the names of the authors here 
# Then, you can remove these instruction comments
play = "1"
while play == "1":
  import time
  import emoji
  import colorama
  from colorama import Fore
  from colorama import init
  init(autoreset=True)

  import turtle
  from turtle import Screen
  jim = turtle.Turtle()
  screen1 = Screen()
  screen1.colormode(255)
  window1 = turtle.Screen()
  window1.setup(width=1.0, height=1.0, startx=None, starty=None)

  jim.write("WELCOME TO JIMMY'S QUIZ ARENA", align = "center", font=("Calibri", 15, "bold"))
  jim.hideturtle()

  name = input("ENTER YOUR NAME: ").upper()
  print("WELCOME "+name+" TO JIMMY'S QUIZ ARENA")
  print("__________________________________________________")

  print("****INSTRUCTIONS****")
  print("Enter the option (A,B,C or D) that correctly answers each given question")
  print("_______________________________________________")
  print("LOADING...")
  time.sleep(5)

  def question1():
      global score1
      global answer1
      answer1 =""
      score1 = 0
      print("1. Where is Stonehenge located? ")
      print(" A. Finland \n B. Norway \n C. Iceland \n D. England")
      reply = input("Enter your option ").upper()
      OPTIONS1 = ["A","B","C","D"]
      if reply not in OPTIONS1:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question1()
      elif reply == "D":
          score1+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer1 = "1. D. England"
          print(Fore.RED + u'\N{cross mark}')

          
  def question2():
      global score2
      global answer2
      answer2 = ""
      score2 = 0
      print("2. Where was the fortune cookie invented? ")
      print(" A. Tokyo \n B. Beijing \n C. Seoul \n D. San Francisco")
      reply = input("Enter your option ").upper()
      OPTIONS2 = ["A","B","C","D"]
      if reply not in OPTIONS2:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question2()
      elif reply == "D":
          score2+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer2 = "2. D. San Francisco"
          print(Fore.RED + u'\N{cross mark}')
  def question3():
      global score3
      global answer3
      answer3 =""
      score3 = 0
      print("3. The only planet whose English name is not taken from Greek mythology is? ")
      print(" A. Mercury \n B. Earth \n C. Mars \n D. Jupiter")
      reply = input("Enter your option ").upper()
      OPTIONS3 = ["A","B","C","D"]
      if reply not in OPTIONS3:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question3()
      elif reply == "B":
          score3+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer3 = "3. B. Earth"
          print(Fore.RED + u'\N{cross mark}')
          
  def question4():
      global score4
      global answer4
      answer4 = ""
      score4 = 0
      print("4. Who is the founder of apple company? ")
      print(" A. Tim Cook \n B. Steve Jobs \n C. Bill Gates \n D. Jeff Benzos")
      reply = input("Enter your option ").upper()
      OPTIONS4 = ["A","B","C","D"]
      if reply not in OPTIONS4:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question4()
      elif reply == "B":
          score4+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer4 = "4. B. Steve Jobs"
          print(Fore.RED + u'\N{cross mark}')
          
  def question5():
      global score5
      global answer5
      answer5 =""
      score5 = 0
      print("5. Proteus is a moon of which planet? ")
      print(" A. Neptune \n B. Jupiter \n C. Earth \n D. Mars")
      reply = input("Enter your option ").upper()
      OPTIONS5 = ["A","B","C","D"]
      if reply not in OPTIONS5:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question5()
      elif reply == "A":
          score5+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer5 = "5. A. Neptune"
          print(Fore.RED + u'\N{cross mark}')

  def question6():
      global score6
      global answer6
      answer6=""
      score6 = 0
      print("6. Combining red and blue together makes? ")
      print(" A. Cyan \n B. Black \n C. Green \n D. Magenta")
      reply = input("Enter your option ").upper()
      OPTIONS6 = ["A","B","C","D"]
      if reply not in OPTIONS6:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question6()
      elif reply == "D":
          score6+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer6 = "6. D. Magenta"
          print(Fore.RED + u'\N{cross mark}')
      
  def question7():
      global score7
      global answer7
      answer7=""
      score7 = 0
      print("7. The most shoplifted food in the world is? ")
      print(" A. Bread \n B. Cheese \n C. Candy \n D. Noodles")
      reply = input("Enter your option ").upper()
      OPTIONS7 = ["A","B","C","D"]
      if reply not in OPTIONS7:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question7()
      elif reply == "B":
          score7+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer7 = "7. B. Cheese"
          print(Fore.RED + u'\N{cross mark}')
  def question8():
      global score8
      global answer8
      answer8=""
      score8 = 0
      print("8. Who said the most powerful knowledge quote? ")
      print(" A. Nelson Mandela \n B. Mahatma Gandhi \n C. Sir Francis Bacon \n D. Albert Einstein")
      reply = input("Enter your option ").upper()
      OPTIONS8 = ["A","B","C","D"]
      if reply not in OPTIONS8:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question8()
      elif reply == "C":
          score8+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer8 = "8. C. Sir Francis Bacon"
          print(Fore.RED + u'\N{cross mark}')

  def question9():
      global score9
      global answer9
      answer9 =""
      score9 = 0
      print("9. Which Vitamin is present in Citrus fruit? ")
      print(" A. Vitamin A \n B. Vitamin B Complex \n C. Vitamin C \n D. Vitamin E")
      reply = input("Enter your option ").upper()
      OPTIONS9 = ["A","B","C","D"]
      if reply not in OPTIONS9:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question9()
      elif reply == "C":
          score9+=1
          print(Fore.GREEN + u'\N{check mark}')
      else:
          answer9 = "9. C. Vitamin C"
          print(Fore.RED + u'\N{cross mark}')
  def question10():
      global score10
      global answer10
      answer10=""
      score10 = 0
      print("10. Which Country is the owner of SAMSUNG? ")
      print(" A. China \n B. Japan  \n C. South Korea \n D. North Korea")
      reply = input("Enter your option ").upper()
      OPTIONS10 = ["A","B","C","D"]
      if reply not in OPTIONS10:
          print("__________________________________________________________________________")
          print("Please enter one of A,B,C or D as answer")
          print("__________________________________________________________________________")
          question10()
      elif reply == "C":
          score10+=1
          print(Fore.GREEN + u'\N{check mark}')
      else: 
          answer10 = "10. C. South Korea"
          print(Fore.RED + u'\N{cross mark}')
  def allQuestions():
      question1()
      print("___________________________________________________")
      question2()
      print("___________________________________________________")
      question3()
      print("___________________________________________________")
      question4()
      print("___________________________________________________")
      question5()
      print("___________________________________________________")
      question6()
      print("___________________________________________________")
      question7()
      print("___________________________________________________")
      question8()
      print("___________________________________________________")
      question9()
      print("___________________________________________________")
      question10()
      print("___________________________________________________")
          
  allQuestions()
  scoresSheet = [score1, score2, score3, score4, score5, score6, score7, score8, score9, score10]
  answers = [answer1,answer2,answer3,answer4,answer5,answer6,answer7,answer8,answer9,answer10]
  scores = sum((scoresSheet))

  jim.penup()
  jim.right(90)
  jim.forward(20)

  jim.write("SCORE = "+ str(scores), align = "center", font=("Calibri", 10, "bold"))
  jim.penup()
  jim.forward(20)
  jim.write("PRECENTAGE = "+ str((scores/10)*100)+"%",align = "center", font=("Calibri", 10, "bold"))
  jim.hideturtle()

  time.sleep(5)
  if 0<scores<4:
      print("TRY TO DO BETTER NEXT TIME")
      print(Fore.RED + u'\N{graduation cap}')
  elif 4<scores<7:
      print("YOUR RESULT IS QUITE OKAY NEVERTHERLESS, YOU CAN DO BETTER")
      print(Fore.YELLOW + u'\N{trophy}')
  elif 7<scores<=10:
      print("GREAT!! YOU REALLY ARE A GENIUS")
      print(Fore.YELLOW + u'\N{crown}')

  for x in answers:
      if x !="":
          print(x)

  jim.reset()

  import turtle 
  import random
  from turtle import Screen
  screen = Screen()
  screen.colormode(255)
  window = turtle.Screen()
  window.setup(width=1.0, height=1.0, startx=None, starty=None)
  window.bgcolor('black')

  # Create a turtle, named Kevin
  jimmy = turtle.Turtle()
  jimmy.speed(0)
  #variable to show how far the turtle should travel

  r = random.randint(0,255)
  g = random.randint(0,255)
  b = random.randint(0,255)
  # function to draw fireworks 
  def draw_firework(t):
    #distance to be moved by turtle
    distance = random.randint(5,100)
    x = random.randint(-180,180)
    y = random.randint(-180,180)

    jimmy.penup()
    jimmy.goto(x,y)
    jimmy.pendown()
    
    # TODO #1: create a variable to change the firework size then use that variable in the forward and backward methods 
    for i in range(36):
      jimmy.forward(distance)
      jimmy.backward(distance)
      jimmy.right(10)
      

  # Draw five fireworks
  for i in range(5):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    #TODO #2: Create three variables r, g, and b and set their values equal to a random number between 0 and 255. Replace the color blue with jimmy.color(r,g,b)
    jimmy.color(r,g,b)
    draw_firework(jimmy)
  #changing turtle color to white
  jimmy.color('white')
  x = random.randint(-180,180)
  y = random.randint(-180,180)
  z = 0
  while z <= 100:
    jimmy.penup()
    jimmy.goto(x,y)
    jimmy.pendown()
    for i in range(5):
      jimmy.forward(10)
      jimmy.right(144)
    z += 1
    x = random.randint(-180,180)
    y = random.randint(-180,180)

  jimmy.reset()
  window = turtle.Screen()
  window.setup(width=1.0, height=1.0, startx=None, starty=None)
  window.bgcolor('white')

  jimmy.write("THANKS FOR HAVING FUN WITH US", align = "center", font=("Calibri", 15, "bold"))
  jimmy.hideturtle()
  opt = ["1","2"]
  print("                        ")
  play = input("1. Replay\n2. Quit\nEnter reply here ")
  print("                           ")
  while play not in opt:
    print("Enter either 1 or 2")
    play = input("1. Replay\n2. Quit\nEnter reply here ")
    print("                           ")
  jimmy.reset()
      
