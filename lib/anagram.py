





class Anagram:
    def __init__(self, word):
        self.sort = sorted([letter for letter in word])

    def match(self, word_list):
        all = []
        for i in word_list:
            j = sorted(i)
            if j == self.sort:
                all.append(i)
        return all
      

a = Anagram("listen")
print(a.match(['enlists', 'google', 'inlets', 'banana']))