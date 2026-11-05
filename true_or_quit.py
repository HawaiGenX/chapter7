prompt = f"\nPlease enter the name of the city you would love to visited before"
prompt += f"Enter 'quit' when you are finished "

while True:
    city = input(prompt)
    
    if city == 'quit':
        break
    else:
        print(f"I'd love to go to {city.title()}!")
    