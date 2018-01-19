import operator,re
f = open('etc/text.done.data.it8','r')
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
top_bigrams = sorted_x[:50]
#print top_bigrams
#line = top_bigrams[0]
#print line
#print 'AH' in line[0]
#sorted_y = sorted(trigrams.items(), key=operator.itemgetter(1),reverse=True)
#s = raw_input()
#Make changes to the text.done.data file
h = open('etc/text.done.data.it8','w')
for line in data:
	phonemes = line
	line = line.split("\"")
	words = line[1].split()
	for w in range(len(words)-1):
		for bigram in top_bigrams:
			if words[w] in bigram[0][0]:
				if words[w+1] in bigram[0][1]:
					#print bigram[0]
					phonemes = phonemes.replace(words[w]+" "+words[w+1],words[w]+'_'+words[w+1])
					
	h.write(phonemes)	
print " ngrams written to text.done.data"			
					#s=raw_input()
#Writing to bigram addenda file
h.close()
g = open('festvox/cmu_us_ceb_addenda.scm','w')
#j = open('cmu_us_ceb_addenda_trigram.scm','w')
ndata = []
for bi in top_bigrams:
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
		#print n_line
		g.write(n_line+'\n')

print " ngram addenda file generated."

#print "Bigrams : ", len(bigrams.keys())
#s = raw_input()












"""for tri in sorted_y:
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
"""
