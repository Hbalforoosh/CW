nest = [["apple", "banana", "apple"], ["orange", "banana"], ["grape", "apple", "grape"]]
def x (nest):
    fru1 = set()
    for i in nest :
        for fru2 in i: 
            fru1.add(fru2)
    
    fru3 = " , ".join(fru1)
    return fru3
y = x(nest)
print(y)