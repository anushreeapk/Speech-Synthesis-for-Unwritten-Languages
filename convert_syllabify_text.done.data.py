f=open('syllabified_text.done.data','r')
data = f.readlines()
newlines=[]

for line in data:
	line = line.strip('((')
	line = line.strip('))\n')
	line = line.split(') (')
	#print line
	
	#print "--------------------------"

	for w in range(len(line)):
		words = line[w].split()
		#print words
		line[w] = '_'.join(words)
		line[w] = line[w].upper()
	newlines.append(line)


	#s = raw_input()
#print newlines


'''
## Create new file
g = open('text.done.data.it8','r')
data = g.readlines()
c = 0
h = open('text.done.data.syllabify','w')
for line in data:
	line = line.split("\"")
	line[1]= ' '.join(newlines[c])
	c=c+1
	h.write(' '.join(line))

print "Done"
'''
ngrams = {}
#Code to create addenda file
for line in newlines:
	for word in line:
		if word not in ngrams:
			ngrams[word] = 1
		else:
			ngrams[word] +=1
l = open('cmu_us_ceb_addenda_syllabify.scm','w')
for bi in ngrams:
		#(('AH', 'N'), 5331)
		#bi = list(bi)
		pair = bi
		#pair = '_'.join(bi[0])
		phone=pair.strip('_')
		phone = phone.replace('_',' ')
		phone = phone.lower()

		if pair=='SIL':
			n_line ="(lex.add.entry '("+pair+" nil (((pau) 0))))"
		else:
			n_line ="(lex.add.entry '("+pair+" nil ((("+phone+") 0))"
		print n_line
		l.write(n_line+'\n')

print " ngram addenda file generated."
