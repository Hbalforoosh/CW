numbers = []
texts = []
with open("data.txt","r") as f:
    line = f.readline()
    while line:
        line = line.strip()
        if line.replace('.','', 1).isdigit():
            numbers.append(float(line))
        elif line:
            texts.append(line)
        line = f.readline()        
print("N:", numbers)
print("T:", texts)   

