input_text = input()  

text = input_text.lower()
text_list = text.split()

dict1 = {}
for element in text_list:
    if element in dict1:
        count = dict1.get(element)
        dict1[element] = count + 1
    else:
        dict1[element] = 1

print(max(dict1, key=dict1.get))
