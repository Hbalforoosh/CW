class FilteredEditor:
    alternative_words = {
        "soal": "question",
        "tamrin": "practice",
        "javab": "answer"
    }

    def __init__(self, sample_file) -> None:
        self.file = sample_file
        self.old_word = None
        self.new_word = None

    def __enter__(self):
        with open(self.file, 'r', encoding='utf-8')as f:
            self.old_word = f.read()
        self.new_word = self.old_word
        for old, new in self.alternative_words.items():
            self.new_word = self.new_word.replace(old, new)
        return self

    def __exit__(self, arg1, arg2, arg3):
        print("finall")


with FilteredEditor("text1.txt") as test:
    print(test.old_word)
    print("-" * 100)
    print(test.new_word)
