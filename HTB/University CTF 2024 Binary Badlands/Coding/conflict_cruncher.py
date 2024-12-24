dict1_str = input()
dict2_str = input()

str1 = dict1_str[1:-1].split(",")
str2 = dict2_str[1:-1].split(",")

dict1 = {}
for element in str1:
    key, value = element.split(":")
    key = key.strip().strip("'").strip('"')
    value = int(value.strip())
    dict1[key] = value

dict2 = {}
for element in str2:
    key, value = element.split(":")
    key = key.strip().strip("'").strip('"')
    value = int(value.strip())
    dict2[key] = value

print(dict1 | dict2)