print('Jonas')
print("Ndayizeye")

#quotes inside quotes

print("jonathan")
print("He is called 'jonathan'")
print('he is called "Ndayizeye"')

#Assign string to a variable 

j = "Jonathan"
print(j)

#multiline Strings

a = """ Jonas is a dev"""
print(a)


#Strings are Arrays

a = "Rwanda"
print(a[1])

j = 'Jonathan'
print(j[4])

#Looping Through a String

for x in "banana":
    print(x)

# String Length, to get the length of a string use the len() function

a = "Ndayizeye"
print(len(a))


# To check is a certain character is present in a string, we can use the keyword in.

txt = "God is Good!"
print("God" in txt)

txt = "Jonathan is learning a new programming language called Python"
if "Python" in txt:
    print("Yes, 'Python' is present.")

txt = "Coding is good"
print("python" not in txt)

txt = "PK is the Great Present in Africa"
if "Kigali" not in txt:
    print("No, 'Kigali' is NOT present")