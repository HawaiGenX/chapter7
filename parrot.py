prompt = f"\nTell me something, and I will repeat it back to you"
prompt += f"\nEnter 'quit' to end the program:  " 


active = True #flag variable
while active:
    message = input(prompt)
    
    if message == "quit":
        active = False
    else:
        print(message)