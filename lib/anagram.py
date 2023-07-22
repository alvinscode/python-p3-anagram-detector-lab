class Anagram:
    def __init__(self, word):
        self.word=word

    def match(self, word_list):
        lowercase_word = self.word.lower()
        lowercase_word_list = [w.lower() for w in word_list]
        
        anagrams = [w for w in lowercase_word_list if sorted(w) == sorted(lowercase_word)]
        anagrams = [w for w in anagrams if w != lowercase_word]

        anagram = [word_list[lowercase_word_list.index(w)] for w in anagrams]

        return anagram