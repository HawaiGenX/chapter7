prompt = "Choose pizza toppings from the list"
prompt += f"\nOnce you done enter 'exit' "

topping = True

while topping:
    order = input(prompt)
    if order == 'exit':
        topping = False
    else:
        print(order)
    