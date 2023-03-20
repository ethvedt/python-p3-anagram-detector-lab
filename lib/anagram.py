class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, list):
        matched_words = []
        for test_word in list:
            if sorted(test_word) == sorted(self.word):
                matched_words.append(test_word)
        return matched_words