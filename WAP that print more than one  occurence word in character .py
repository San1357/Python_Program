
string = input("Enter a string: ")
lst1 = []
for char in string:
    if char not in lst1:
        lst1.append(char)
for item in lst1:
    if string.count(item) >1:
        print (item)
