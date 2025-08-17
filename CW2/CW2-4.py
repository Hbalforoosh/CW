def most_r(lst):
    max = 0
    most = None
    for i in lst:
        count = lst.count(i)
        if count > max:
            max = count
            most = i

    print(f"Most repeat is '{most}' : '{max}'.")