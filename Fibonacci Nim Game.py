import random
from colorama import Fore

print("Hello,\nThis game is from 2 players we have 3 rows random number of Poles sulfur and the last player to take the Poles sulfur will win.")

first_row = random.randint(1,50) # The number of rows randomly
second_row = random.randint(1,50)
third_row =  random.randint(1,50)

def print_fun(): # Function that Print the wind of the Game
  list1 = []
  for i in range(0,first_row): # the part in code that make list of the Poles sulfur
    n = "|"
    list1.append(n)

  list2= []
  for i in range(0,second_row):
    m = "|"
    list2.append(m)

  list3 = []
  for i in range(0,third_row):
    k = "|"
    list3.append(k)

  def list_to_string(list): # Function that convert the list to be string
        str1 = " "
        return (str1.join(list))

  print(Fore.WHITE+"""
       /------------------------------------------------------------------------
       /
       / {0}
       /
       /
       / {1}
       /
       /
       / {2}
       /
       /------------------------------------------------------------------------
       """.format(list_to_string(list1),list_to_string(list2),list_to_string(list3)))



def gameover(): # Function that check for the Game End
    if first_row == 0 and second_row == 0 and third_row == 0:
        return True
    else:
        return False

def player1(): # Function that makes the first player choose number to take it 
    global first_row , second_row , third_row
    print_fun()
    print(Fore.RED+"<Player1>")
    print("First_row = ",first_row,",Second_row = ",second_row,",Third_row = ",third_row)
    number_of_row = int(input("Select the row you will take from [1,2,3] :"))

    if number_of_row ==3 or number_of_row == 2 or number_of_row == 1:
      if number_of_row == 1:
        move = int(input('Please enter the number of box you choose from {} to 0 :'.format(first_row)))
        first_row = first_row - move
        
      elif number_of_row == 2:
        move = int(input('Please enter the number of box you choose from {} to 0 :'.format(second_row)))
        second_row = second_row - move
        
      else:
        move = int(input('Please enter the number of box you choose from {} to 0 :'.format(third_row)))
        third_row = third_row - move
    else:
        print("Your choose is wrong Enter it agin")
        player1()
        
    if gameover():
        print("<Player1> win\nEnd Game")
    else:
        player2()
    
def player2(): # Function that makes the second player choose number to take it 
    global first_row , second_row ,third_row
    print_fun()
    print(Fore.BLUE+"<Player2>")
    print("First_row = ",first_row,",Second_row = ",second_row,",Third_row = ",third_row)
    number_of_row = int(input("Select the row you will take from [1,2,3] :"))
    if number_of_row == 1 or number_of_row ==2 or number_of_row == 3:
       if number_of_row == 1:
        move = int(input('Please enter the number of box you choose from {} to 0 :'.format(first_row)))
        first_row = first_row - move

       elif number_of_row == 2:
        move = int(input('Please enter the number of box you choose from {} to 0 :'.format(second_row)))
        second_row = second_row - move
      
       else:
        move = int(input('Please enter the number of box you choose from {} to 0 :'.format(third_row)))
        third_row = third_row - move
    else:
        print("Your choose is wrong Enter it agin")
        player2()

    if gameover():
        print("<Player2> win")

    else:
        player1()

player1()
