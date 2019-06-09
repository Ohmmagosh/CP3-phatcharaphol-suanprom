number = int(input())
counts = number-1
space = ""
text = ""
text2 = ""
for x in range(number):
    space =""
    for z in range(counts):
       space +=" "
    for y in range(x):
        text +="*"
    counts = counts -1
    for w in range(x-1):
        text2 +="*"

    print(space+text+text2)
    text = ""
    text2 = ""
