def pig_latin(text):
      say = ""
  # Separate the text into words
  words = text.split()
  pig_sentence = []
  for word in words:
    # Create the pig latin word and add it to the list
    delim = " "
    first_word = word[0]
    word_body = word[1:]
    pig_word = word_body + first_word + "ay"
    pig_sentence.append(pig_word)

    # Turn the list back into a phrase
  return delim.join(pig_sentence)
		
print(pig_latin("hello how are you")) # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun")) # Should be "rogrammingpay niay ythonpay siay unfay"