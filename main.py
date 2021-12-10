from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

again = True
bidders = {}
print(art.logo)
print("Welcome to the secret auction program")
while again == True :
  name = input("What is your name ?")
  bid = int(input("What's your bid ? $"))
  bidders[name] = bid
  answer = ""
  while not (answer == "yes" or answer == "no") :
    answer = input("Are there any other bidders ? Type 'yes' or 'no'")
  if answer == "yes" :
    clear()
  else :
    max = 0
    for key in bidders : 
      if bidders[key] > max :
        winner = key
    print(f"The winner is {winner} with a bid of ${bidders[winner]} ")
    again = False

      



