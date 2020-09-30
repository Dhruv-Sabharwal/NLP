## Sentiment Analysis

### Dataset
Large Movie Review Dataset: available from http://ai.stanford.edu/~amaas/data/sentiment/aclImdb_v1.tar.gz. The dataset consists of reviews from IMDB. There are no more than 30 reviews per movie and the number of positive and negative reviews are equal (negative reviews have scores less or equal than 4 out of 10 while a positive review have score greater or equal than 7 out of 10. Neutral reviews are not included). The 50,000 reviews are divided evenly into the training and test set.

### Method
<ol>
<li>The reviews are first normalized, lemmatized, tokenized and the punctuations, as well as stopwords, are removed.
<li>I am using the bag of words approach. I realized keeping all the words would make the bag too big and computationally expensive. Hence, I decided to use the words which give the most information about the sentiment of the review i.e. the adjectives.
<li>A Parts of Speech (POS) tagger is used and only the adjectives are retained in the reviews.
<li>I built the vocabulary (bag) which contains all the adjectives. I then calculated the frequency distribution of the adjectives in this vocabulary and used the 2000 most frequent adjectives to create my bag of words (other sizes were tried, however 2000 seemed to work best). This helped to reduce the computational costs further.
<li>After creating the bag of words, I trained a Naïve Bayes Classifier on the training data. For this I had to create special features which can be sent as input to the classifier. The input is a list of tuples. Every tuple has a dictionary as its first element and either 'pos' (for positive) or 'neg' (for negative) as its second element. The dictionary is the features i.e. the dictionary is of the form {'boring': True, 'bad': True, 'fun': False, ....} showing which all adjectives from the vocabulary are present in that particular review.
</ol>

### Tools Used
<ul>
<li>Classifier: Naïve Bayes Classifier from nltk
<li>POS tagger: Averaged Perceptron Tagger from nltk
<li>Several other pre-processing tools from nltk
</ul>

### Results
Once the model is trained it can be used to find the goodness figures of the classifier on the testing dataset: 
<ul>
<li>True Positives: 9678
<li>False Positives: 2107 
<li>True Negatives: 10393 
<li>False Negatives: 2822 
<li>Accuracy: 80.284 %
</ul>
