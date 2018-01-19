#(print (cmulex_syllabify_maxonset '(s t r eh m p r aa n t)))
f = open('text.done.data.it8','r')
g = open('syllabify.scm','w')
data = f.readlines()
for line in data:
	line = line.split("\"")
	line = line[1].lower()
	syll = "(print (cmulex_syllabify_maxonset \'("+line+")))"
	print syll
	g.write(syll+'\n')
g.close()
f.close()
	#words = line[1].split()
	#print words