from ballans import possibleAnswers
import os 
import sys

print("Green = Good, Yellow = Satisfactory, and Red = Not so good.")
userInput = input("Say something for magic 8ball: ")

while True:
   if userInput:
      print(possibleAnswers())

   play_again = input("Do you want to play again. Type 'y' (yes) or 'n' (no): ")
   if play_again == 'y' or play_again == 'yes':
      os.execl(sys.executable, os.path.abspath(__file__), *sys.argv)
   elif play_again == 'n' or play_again == 'no':
      print("Have a good one.")
      break
   else: 
      print("Try again.")
      if play_again:
          userInput = False 
