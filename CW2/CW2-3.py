def colors(list1):
    for i in range(len(list1)):
        color = list1[i]
        if not color[0].isupper():
            list1[i] = color.capitalize()
    return list1
print(colors(["red", "blue", "green"]))