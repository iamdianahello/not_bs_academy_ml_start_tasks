import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer
nltk.download('wordnet')
from nltk.corpus import wordnet
nltk.download('averaged_perceptron_tagger')
nltk.download('punkt')

lemmatizer = WordNetLemmatizer()


def ntlk_to_wordnet(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return wordnet.NOUN # default wordnet 

with open('clean_data.txt', 'r', encoding='utf-8', errors='ignore') as file:
	raw_data = file.read()
	
	#getting word-pos pair. 
	word_and_ntlkpos_list = nltk.pos_tag(nltk.word_tokenize(raw_data)) 
	
	#now pos in a wrong format, to be converted
	word_and_wordnetpos_list = []
	for pair in word_and_ntlkpos_list:
		word_and_wordnetpos_list.append([pair[0], ntlk_to_wordnet(pair[1])])

	
	#now every word-pos pair will be lemmatized
	i = 0
	normalized_words_list = []
	while i < len(word_and_wordnetpos_list):
		word = lemmatizer.lemmatize(str(word_and_wordnetpos_list[i][0]), word_and_wordnetpos_list[i][1])
		normalized_words_list.append(word)
		i = i +1
		
	with open('clean_normalized_data.txt', 'w') as output:
    		output.write(' '.join(normalized_words_list))
	
    
    

