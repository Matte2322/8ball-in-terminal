import random

def possibleAnswers():
   possibleAnswersHere = [
      "*Green* It is decidedly so.",
      "*Green* Without a doubt",
      "*Green* Yes definitely.",
      "*Green* You may rely on it.",
      "*Green* Signs point to yes."
      "*Yellow* Reply hazy, try again."
      "*Yellow* Ask again later."
      "*Yellow* Better not tell you now.",
      "*Yellow* Cannot predict now.",
      "*Yellow* Concentrate and ask again.",
      "*Red* Don't count on it.",
      "*Red* My reply is no.",
      "*Red* My sources say no.",
      "*Red* Outlook not so good.",
      "*Red* Very doubtful.",
      "*Red* Get fucked in the ass.",
      "*Red* You actually thought?",
      "*Red* RIP, BOZO."
   ]
   output8ball = random.choice(possibleAnswersHere)
   return output8ball
