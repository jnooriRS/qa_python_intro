user_input=str(input("Enter a word >>> "))
print(len(user_input))
vowels = ['a' , 'e' , 'i' ,'o' , 'u']
counter = 0
for letter in user_input:
    if letter in vowels:
        counter += 1
print(f"Number of vowels in your word: {counter}")


# count = 0
# vowels = set("aeiou")
# for letter in s:
#     if letter in vowels:
#         count += 1
