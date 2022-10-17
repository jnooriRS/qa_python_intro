# Exercise - Create variables for the following data types: string, int, float, boolean, array 
# Use a print function to print the content of those variables 
# Stretch goal - Experiment with formatting your print statement to make it interesting 'print("price: " + price)'


from email import message


string_message = "hello world"
print(string_message)

price = 5
print(int)

print(f"price = ${price} for !{string_message}! to be your logo on a shirt")
print("message is " + (string_message))

print("THE PRICE IS " +  str(price))
other_input = int(input("please enter a number: "))

customer_dog = int(input("How old is your dog in human years? "))
dog_name = str(input("what is your dogs name ? "))
custromer_dog_years = customer_dog * 7
print(f"{dog_name} is {custromer_dog_years}" )

#else v elif
#elif is a statement to comapre
#else is a defualt response