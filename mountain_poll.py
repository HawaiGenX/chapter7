responses = {}

#Set the flag to indicate that the polling is active

polling_active = True

while polling_active:
    name = input("\nWhat is your name? ")
    response = input("Which moutain would you like to climb someday? ")
#Store the response in the dictionary responses
    responses[name] = response
#find out if anyone else is goint to take the poll
    question = input("Do you know anyone would like to participate in this polling? (yes/no) ")
    if  question == "yes":
        polling_active = True
    else:
        polling_active = False
print("\n")
#Polling is complete show the results
print("--------Poll Results--------")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")
#Find the winning mountain (the one chosen the most)
print("\n")
votes = list(responses.values())
winner = max(set(votes), key=votes.count)
print(f"\nThe winning mountain is {winner.title()} with {votes.count(winner)}")