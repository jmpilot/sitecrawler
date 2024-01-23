import markovify

with open('lyrics.txt','r',encoding='utf-8') as f:
	text = f.read()

text_model = markovify.NewlineText(text)

for i in range(5):
	print(text_model.make_sentence())