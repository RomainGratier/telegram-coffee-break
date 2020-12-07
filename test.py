import pandas as pd
from sklearn.linear_model import LogisticRegressionCV, LogisticRegression
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
import spacy
import multiprocessing

# Load English language model
sp = spacy.load('en_core_web_sm')

def tokenize_function(text):
    # Create token object, which is used to create documents with linguistic annotations.
    sp_obj = sp(text)

    # Lemmatize each token and convert each token into lowercase
    mytokens = [ word.lemma_.lower().strip() if word.lemma_ != "-PRON-" else word.lower_ for word in sp_obj ]
    
    a = a

    return mytokens

def train_model():
    df_train = pd.read_csv('https://raw.githubusercontent.com/sfrancey/Real-or-Not-NLP-with-Disaster-Tweets_Team_Blancpain/main/Data/training_data.csv')
    df_test = pd.read_csv('https://raw.githubusercontent.com/sfrancey/Real-or-Not-NLP-with-Disaster-Tweets_Team_Blancpain/main/Data/test_data.csv')
    
    model = LogisticRegressionCV(solver='lbfgs', 
                                max_iter=2000, 
                                random_state=50,
                                cv=10,
                                n_jobs=multiprocessing.cpu_count())
    
    model = Pipeline([('tfidf', TfidfVectorizer(tokenizer=tokenize_function, ngram_range=(1, 2))),
                      ('clf', model)])
    
    df_train_eval, df_validation = train_test_split(df_train, test_size=0.2, random_state = 50)

    y_train_eval = df_train_eval[["target"]]
    y_validation = df_validation[["target"]]

    X1_train_eval = list(df_train_eval['text'])
    X1_validation = list(df_validation['text'])
    
    model.fit(X1_train_eval, y_train_eval)
    
    # -------------------------------------- Eval data --------------------------------------
    train_accuracy_score = accuracy_score(y_train_eval, model.predict(X1_train_eval))
    print(f"The training accuracy is : {train_accuracy_score}")

    validation_accuracy_score = accuracy_score(y_validation, model.predict(X1_validation))
    print(f"The validation accuracy is : {validation_accuracy_score}")
    
    results = {'train' : train_accuracy_score,
               'test' : validation_accuracy_score}
    
    return results


from telegrambotalarm import TelegramBot
import traceback

TOKEN = 'nnnnnnnnn:xxxxxxxxxxxxxxxxxxxxxxx'
MYID = 'nnnnnnnn'

bot = TelegramBot(TOKEN, MYID)

# Run this
try:
    results = train_model()

# If error occurs, send the error with its trace
except Exception as e:
    print(traceback.format_exc())
    bot.send_error_message(traceback.format_exc())

bot.send_message(results)
