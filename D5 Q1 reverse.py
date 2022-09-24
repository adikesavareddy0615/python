def rev_sentence(sentence):
 words = sentence.split(' ')
 reverse_sentence=""
 for i in words:
  reverse_sentence+=i[::-1]+' '
 return reverse_sentence
input = "Hello World"
print (rev_sentence(input))
