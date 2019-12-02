'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    if len(word) == 0:
      print('Is this failing?')
      return 0

    total = 0

    def counter(word, total):
      if word.count('t') == 0:
        print('total:', total, word)
        return total

      if word.count('t') > 0:
        print(word)
        if word[word.find('t')] == word[len(word)-1]:
          total += 1
          word = word[:-1]
          print('New Word:', word)
          return counter(word, total)
        elif word[word.find('t')+1] == 'h':
          total += 1
          word = word[:word.find('t')] + word[word.find('t') + 2:] 
          print('New Word:', word)
          return counter(word, total)
        elif word.find('t') > 0:
          word = word[:word.find('t')] + word[word.find('t') + 1:] 
          print('New Word:', word)
          return counter(word, total)

    return counter(word, total)

# count_th("thhtthht")
print(count_th("thhtthht"))