responses = {}

# Set the flag variable
dream_vacation = True

print("if you could visit one place in the world, where would like to visit?")
while dream_vacation:
    name = input("Tell us your name: ")
    response = input("What is your answer to the question?: ")
    # Create a dictionary of names and their responses
    responses[name] = response
    
    question = input("Do you have anyone in mind and their vacation of dream vacation? (yes/no): ")
    
    if question == "yes":
        dream_vacation = True #continue, could also be used here inplace of dream_vacation = True
    else:
        dream_vacation = False #break, could also be used here inplace of dream_vacation = False

print(responses)
