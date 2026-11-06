### Strings, lists, tuples, comprehensions
### strings
a = "back" ##double/single quoute any variable is string
# print(a)

b = '''
1. Celsius → Fahrenheit
2. Fahrenheit → Celsius
3. Kilometers → Miles
4. Miles → Kilometers
5. Kilograms → Pounds
6. Pounds → Kilograms
7. Quit
'''
# print(b) ###multline strings

# string slicing
# x = "python"
# print(x, type(x))
# print(x[-1  : - len(x) - 1 :-1])

# strings inbuilt methods
# print(x.upper())
# print(x.lower())
# print(x.capitalize())
# print(x.count("h"))
# print(x.endswith("a"))
# print(x, len(x))
# print(x.lstrip(), len(x.lstrip()))
# print(x.index("y"))
# print(x, len(x))
# print(x.strip(), len(x.strip()))
# print(x.capitalize().startswith("P"))
# print(x.zfill(8))
# print(x.replace("n", "a", 2))
# print(x.split(","))
# print(x.find("yho")) ## not found -> -1, found then index 1st letter
# print(x.index("thno")) ###  (raises ValueError if not found)

# try:
#     a = x.index("thno")
#     print(a)
# except Exception as e: 
#     print(e)


# try:
#     x[1] = "p"
#     print(x) ### strings are immutable
# except Exception as e: 
#     print(e)

# p = "hello world"
# print(p.title()) 


### lists
l = ["2", 2.2, "apple"]

#### slicing
# print(l[:len(l)])
# print(l[::-1])
# print(l[-1 : -4 : -1])


#### list methods
l.append("ball")
l.append("cat")
l.append(["red", "blue"])
# print(l, l[-1][1])
l.extend(["green", "red", "yellow"])
# l.clear()  ## empty list
# print(l.count("red")) 
# print(l.index("red"))
# print(l.insert(5, "skyblue"))
# print(l.pop(1))
# l.remove("red")
# l.reverse()
# nums = [3, 1, 4]
# res = nums.sort()
# print(res, nums)
# print(l)
# l.sort(key= str)
# print(sorted(l, key = str))
# print(len(l))
# del l[5]
# print(len(l))
# print(l)

### list comprehensions
# l = []
# for i in range(1, 11):
#     l.append(i)
# print(l)

# l = [i for i in range(1, 11)]
# print(l)

### tuples
# tuple is ordered and immutable collection
cord = (22, 30)
x, y = cord
print(x, y)
