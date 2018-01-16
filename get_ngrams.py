import operator
f = open('text.done.data.accLangDB-wsj_train.transcription.it6','r')
data = f.readlines()
bigrams = {}
trigrams = {}
for line in data :
	line = line.split("\"")
#	print line[1]
	words = line[1].split()
	for w in range(len(words)):
		if w==0:
			h = ""
		else:
			h = words[w-1]
			bi = (h,words[w])
			if bi not in bigrams:
				bigrams[bi] = 1
			else:
				bigrams[bi] += 1
			if w == 1:
				h1 =""
			else:
				h = words[w-1]
				h1 = words[w-2]
				tri = (h1,h,words[w])
				if tri not in trigrams:
					trigrams[tri] = 1
				else:
					trigrams[tri] += 1


#print bigrams
sorted_x = sorted(bigrams.items(), key=operator.itemgetter(1),reverse=True)
#print sorted_x[:50]
sorted_y = sorted(trigrams.items(), key=operator.itemgetter(1),reverse=True)

#Writing to bigram addenda file
g = open('cmu_us_ceb_addenda_bigram.scm','w')
j = open('cmu_us_ceb_addenda_trigram.scm','w')
ndata = []
for bi in sorted_x:
		#(('AH', 'N'), 5331)
		bi = list(bi)
		pair = '_'.join(bi[0])
		phone = ' '.join(bi[0]).lower()
		#print pair
        #l = line.split()
        #if pair=='SIL':
        #        n_line ="(lex.add.entry '("+pair+" nil (((pau) 0))))"
        #else:
		n_line ="(lex.add.entry '("+pair+" nil ((("+phone+") 0))"
		print n_line
		g.write(n_line+'\n')

print "Bigrams : ", len(bigrams.keys())
s = raw_input()
for tri in sorted_y:
		#(('AH', 'N'), 5331)
		tri = list(tri)
		pair = '_'.join(tri[0])
		phone = ' '.join(tri[0]).lower()
		#print pair
        #l = line.split()
        #if pair=='SIL':
        #        n_line ="(lex.add.entry '("+pair+" nil (((pau) 0))))"
        #else:
		n_line ="(lex.add.entry '("+pair+" nil ((("+phone+") 0))"
		print n_line
		j.write(n_line+'\n')

print "Trigrams : ", len(trigrams.keys())
