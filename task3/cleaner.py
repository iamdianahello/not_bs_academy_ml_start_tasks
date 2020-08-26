import nltk
nltk.download("stopwords")
from nltk.corpus import stopwords


english_stopwords = stopwords.words('english')
#print(english_stopwords)


def no_trash(data):
	no_trash_data = data.replace('\n', ' ').replace('*', '')
	#print(no_trash_data)
	return no_trash_data
	
def no_stopwords(data):
	no_stopwords_data = data
	for stopword in english_stopwords:
		no_stopwords_data = no_stopwords_data.replace( ' ' + stopword + ' ', ' ')
	#print(no_stopwords_data)
	return no_stopwords_data
	
	

with open('eng_text.txt', 'r', encoding='utf-8', errors='ignore') as file:
	raw_data = file.read()
	data_no_trash = no_trash(raw_data)
	clean_data = no_stopwords(data_no_trash)
	with open('clean_data.txt', 'w') as output:
    		output.write(clean_data)
    
    
    

	
