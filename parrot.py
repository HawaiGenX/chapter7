prompt = f"\nTell me something, and I will repeat it back to you"
prompt += f"\nEnter 'quit' to end the program:  " 


message = " "
while message != "quit":
    message = input(prompt)
    print(message)