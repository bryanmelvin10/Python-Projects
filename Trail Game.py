import random
print("welcome to the Trail Game")
print("You took a trip to New York and your goal is to come back home")

import random
print("welcome to the Trail Game")
print("You took a trip to New York and your goal is to come back home")

print("instructions:")
step_1 = ("1) choose your username")
step_2 = ("2) set a year you want it to be")
step_3 = ("3)Choose your mode")
step_4 = ("4) Try to SURVIVE")
print(step_1+"\n"+step_2+"\n"+step_3+"\n"+step_4+"\n")

username = input("what is your name: ")
print("Hello "+ username)
year_set = input("what year would you like it to be")
print("the year is "+ year_set)
    

command = input("do you want to start the game")
print("Type start to begin game")
while command != "start":
    print = input("what is your command; ")
    if command == "start":
        print("the game now begins!!!!")
    elif command == "stop":
        print("Cya later")
        quit()

option = int(input("What mode would you like to play in"))
while option == 1 or option == 2 or option == 3:
    option = int(input("Pick option 1, 2, or 3: "))
    if option ==1:
        print("You chose option 1 (easy)")
        food_num = 1000
        health_num = 10
        break
    elif option ==2:
        print("You chose option 2 (hard)")
        food_num = 500
        health_num = 5
        break
    elif option ==3:
        print("You chose option 3(impossible)")
        food_num = 100
        health_num = 4
        break
    else:
        print("That wasnt a option")
print("Type start to begin game")
while command != "start":
    command = input("what is your command; ")
    if command == "start":
        print("the game now begins!!!!")
    elif command == "stop":
        print("Cya later")
        quit()
    else:
        print("Don't understand you")
 

player_move_distance = 0
month_num = 3
days_pass = 1
total_days = 0
MONTHS_WITH_31_DAYS = [1, 3, 5, 7, 8, 10, 12]
random_result = 0
health_d1 = random.randint(1, 31)
health_d2 = random.randint(1, 31)
acident_appear = random.randint(1, 30)
travel_total_num = 0
rest_total_num = 0
hunt_total_num = 0
status_total_num = 0
month_appear = 'March'

def add_days(min, max):
  global days_pass
  global month_num
  global MONTHS_WITH_31_DAYS
  global random_result
  global food_num
  global health_num
  global health_d1
  global health_d2
  global total_days
  global acident_appear

  random_result = random.randint(min, max)
  print('Now',random_result,"days passed..")
  days_pass_min = days_pass
  check_big = days_pass + random_result

  if acident_appear >= days_pass and acident_appear <= check_big:
    a_number = random.randint(1, 3)
    a_health_num = random.randint(1, 2)
    if a_number == 1:
      print('During this time, you crossed a river.')
    if a_number == 2:
      print('During this time, you had a dysentery.')
    if a_number == 3:
      print('During this time, you saw a beautiful girl and had a good time with her.')
    random_result2_food = random.randint(1, 10)
    random_result2_day = random.randint(1, 10)
    print('As a result, you eat '+str(random_result2_food)+' lbs extra food.')
    print('It also took up eatra '+str(random_result2_day)+' days.')
    if a_health_num == 1:
      print('And you also lose 1 health')
      health_num -= 1
    food_num = food_num - random_result2_food - random_result2_day*5
    days_pass += random_result2_day
    total_days += random_result2_day
  
  check_big = days_pass + random_result
  if health_d1 >= days_pass_min and health_d1 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')
  if health_d2 >= days_pass_min and health_d2 <= check_big:
    health_num -= 1
    print('Unfortunately, you lose 1 health during this time.')


  days_pass += random_result
  total_days += random_result
  food_num -= random_result * 5

  if days_pass >= 30:
    if month_num not in MONTHS_WITH_31_DAYS:
      if days_pass > 30:
        days_pass -= 30
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)
    else:
      if days_pass > 31:
        days_pass -= 31
        month_num += 1
        health_d1 = random.randint(1, 30)
        health_d2 = random.randint(1, 30)
        acident_appear == random.randint(1, 30)


def travle1(movedistance):
  global days_pass
  global travel_total_num
  add_days(3,7)
  movedistance = movedistance + random.randint(30, 60)
  travel_total_num += 1
  return movedistance

def rest(health):
  global days_pass
  global rest_total_num
  add_days(2,5)
  health = health + 1
  rest_total_num += 1
  return health

def hunt(hunting_food):
  global days_pass
  global hunt_total_num
  add_days(2,5)
  hunting_food = hunting_food + 100
  print('Gain: 100 lbs food')
  hunt_total_num += 1
  return hunting_food


def month_appear_fun():
  global month_appear
  if month_num == 1:
    month_appear = 'January'
  elif month_num == 2:
    month_appear = 'February'
  elif month_num == 3:
    month_appear = 'March'
  elif month_num == 4:
    month_appear = 'April'
  elif month_num == 5:
    month_appear = 'May'
  elif month_num == 6:
    month_appear = 'June'
  elif month_num == 7:
    month_appear = 'July'
  elif month_num == 8:
    month_appear = 'August'
  elif month_num == 9:
    month_appear = 'September'
  elif month_num == 10:
    month_appear = 'October'
  elif month_num == 11:
    month_appear = 'November'
  elif month_num == 12:
    month_appear = 'December'
  return month_appear

while player_move_distance < 2000 and food_num > 0 and health_num > 0 and month_num < 13:
  month_appear_fun()
  if food_num <= 50:
    print('Warning! You only have '+ str(food_num) + " lbs food now.")
    print('You need hunt now.')
  if health_num <= 2:
    print('Warning! You only have '+ str(health_num) + " health now.")
    print('You need a rest.')
  print(str(username) + ', now it is ' + month_appear + ' '+str(days_pass) + ', ' + str(year_set) + ", and you have travled " + str(player_move_distance) + " miles.")
  choice = input('Pick your choice: travel, rest, hunt, status, help, quit, suicide')
  if choice == 'travel':
    player_move_distance = travle1(player_move_distance)
  elif choice == 'rest':
    if health_num < 5:
      print("You get 1 heath!")
      health_num = rest(health_num)
    if health_num >= 5:
      print("Your health is full, the maximum number for health is 5!")
  elif choice == 'hunt':
    food_num = hunt(food_num)
  elif choice == 'status':
    print('-Dear ' + str(username) + ', now is '+str(month_num)+'/'+str(days_pass)+'/'+str(year_set)+".")
    print('-Food:',food_num,"lbs")
    print('-Health:',health_num)
    print('-Distance traveled:',player_move_distance)
    distance_left = 2000 - player_move_distance
    print('-'+str(total_days) +' days have passed.')
    print('-You have travled ' + str(player_move_distance) + " miles, there is still " + str(distance_left) + ' miles left.')
    status_total_num += 1
  elif choice == 'help':
    print('travel: moves you randomly between 30-60 miles and takes 3-7 days (random).')
    print('rest: increases health 1 level (up to 5 maximum) and takes 2-5 days (random).')
    print('hunt: adds 100 lbs of food and takes 2-5 days (random).')
    print('status: lists food, health, distance traveled, and day.')
    print('quit: will end the game.')
  elif choice == 'quit':
    quit_choice = input('Are you sure that you want to quit?(yes/no)')
    if quit_choice == 'yes':
      print('Game over...I cannot believe that you quit...')
      break
  elif choice == 'suicide':
    quit_choice2 = input('Are you sure?(yes/no)')
    if quit_choice2 == 'yes':
      print('Game over...You killed youself...')
      break
 
  else:
    print("This Choice is not available, please try again.")

if player_move_distance >= 2000:
  print('Nice job! you have arrived at your house')


if food_num <= 0:
  print('Game over, you have no food now.')

if health_num <= 0:
  print('Game over, you have no health now.')

if month_num >= 13:
  print('Game over, you run out of time!')
  
print('During the whole game, you:')
print('Travel ' + str(travel_total_num) +' times.')
print('Rest ' + str(rest_total_num) +' times.')
print('Hunt ' + str(hunt_total_num) +' times.')
print('Status ' + str(status_total_num) +' times.')
