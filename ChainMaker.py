import markovify

with open("ParsedLyricsPop.txt", "r") as f:
	songLyrics = f.read()

text_model = markovify.Text(songLyrics)
def songWriter(text_parsed):


	for i in range(5):
		print(text_model.make_sentence())
	
	for i in range(5):
		print( text_model.make_sentence())
	
	for i in range(6):
		print( text_model.make_sentence())
		
songWriter(songLyrics)