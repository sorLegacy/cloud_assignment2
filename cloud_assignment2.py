# import the needed libraries 
import spacy
import nltk
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
nlp = spacy.load("en_core_web_sm")
nltk.download('stopwords')
nltk.download('punkt')
#get and prepare the text
print(stopwords.words('english'))
with open("/app/paragraphs.txt") as data :
 content = [next(data) for i in range(6) ]
print (content)
my_string = ",".join(str(element) for element in content)
doc = nlp(my_string)
word_tokens = word_tokenize(my_string)
print(my_string)
stop_words = set(stopwords.words('english'))

#making lists of removed stop words and filtered words
filtered_words = [token.text for token in doc if not token.is_stop]
removed_stopwords=[token.text for token in doc if token.is_stop]
clean_text = ' '.join(filtered_words)
print("Original Text:", my_string)
print("Text after Stopword Removal:", clean_text)
print(removed_stopwords)
print(Counter(removed_stopwords))
words_frequency = Counter(removed_stopwords)


#visualize the results
words_frequency_dict = dict(words_frequency)
elements = list(words_frequency_dict.keys())
counts = list(words_frequency_dict.values())
plt.bar(elements, counts)
plt.xticks(rotation="vertical")
plt.xlabel('stop words')
plt.ylabel('frequency')
plt.title('removed stop words frequency')
plt.show()
