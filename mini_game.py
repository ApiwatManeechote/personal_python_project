# Mini Game 1: Traffic Lights
## we import time and cycle as it's the core to the traffic lights.

import time
from itertools import cycle

lights = [
	('Green', 3),
	('Yellow', 1.5),
	('Red', 5)
]

colors = cycle(lights)
while True:
	colors, seconds = next(colors)
	print(colors)
	time.sleep(seconds)
	
## More long and manual way to create the traffic lights.

import time

lights = [
    ('Green', 3),
    ('Yellow', 1.5),
    ('Red', 5)
]

loop = 0
while True:
    color, seconds = lights[i]
    print(color)
    time.sleep(seconds)
    
    if loop == len(lights) - 1:
        loop = 0
    else:
        loop += 1


# Mini Game 2: # Just a simple chatbot
## Just create a chat where you must only answer Jojo's Bizarre Adventure to break the loop.

def ilovejojo_chatbot():
	fav_anime = []
	while True:
		fav_animation = input("What's your fav anime? ")
		fav_anime.append(fav_anime)
		if fav_animation == "Jojo's Bizarre Adventure":
			return "You're a stand user!"


# Mini Game 3: Bank Account Transaction
## We are going to create some kind of bank account transaction whether it's deposit, withdraw or transfer with OOP (Object Oriented Programming). Let's roll!

class ATM:
	def __init__(self, name, bank, balance):
		self.name = name
		self.bank = bank
		self.balance = balance

	def deposit(self, plus):
		self.balance += plus
		print(f"[{self.bank}] {self.name} deposited {plus}. New balance: {self.balance}\n") ### I add \n in the end of each function to make it look clean when we run the codes.

	def withdraw(self, deduct):
		if deduct > self.balance:
			print(f"[{self.bank}] Insufficient Fund! {self.name} tried to withdraw {deduct}, but has only {self.balance}.\n")
		else:
			self.balance -= deduct
			print(f"[{self.bank}] {self.name} withdrew {deduct}. New balance: {self.balance}\n")

	def transfer(self, receiver, amount):
		if amount > self.balance:
			print(f"[{self.bank}] Transfer Failed! Not enough balance to send {amount} to {receiver.name}.\n")
		else:
			self.balance -= amount
			receiver.balance += amount
			print(f"[{self.bank}] {self.name} transferred {amount} to [{receiver.bank}] {receiver.name}")
			print(f" Current {self.name}'s balance: {self.balance}")
			print(f" Current {receiver.name}'s balance: {receiver.balance}\n")

	def __str__(self):
		return f"[{self.bank}] {self.name} currently has balance: {self.balance}"

## Our preparation is done. Now let's test if it works or not.

## Let's create some accounts.
jotaro = ATM("Jotaro", "KBank", 20000)
josuke = ATM("Josuke", "SCB", 15000)
giorno = ATM("Giorno", "KTB", 30000)

# Now try something not quite complicated like deposit and withdraw.
jotaro.deposit(2000)
jotaro.withdraw(5000)
giorno.withdraw(5000)

# Then, let's see how will it work on transfer between accounts.
jotaro.transfer(josuke, 3000)
josuke.transfer(giorno, 2000)

# In conclusion, each of them should have...
print(jotaro)  ### 14,000
print(josuke)  ### 16,000
print(giorno)  ### 27,000
