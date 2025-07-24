sentence = ["I love Python", "Lambda functions are powerful", "Map is very useful"]
word_counter = list(map(lambda x: len(x.split()), sentence))
print(word_counter)
