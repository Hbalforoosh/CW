try:    
    with open ("f10.txt","rt") as f:
        if f.readlines()==[ ]:
            raise ValueError("file emptyyy")
        print(f.readlines())

except FileNotFoundError:
    print("file not found")    
except ValueError as error:
    print(error)
    print("file empty")
        
except Exception as error: 
    print(error)
    print("ERROR")

