'''
I have used something similar to the slot approach discussed in class to design this chatbot. There are certain keywords
associated with each of the 5 questions. If the query contains all these keywords, then the respective answer is provided.
If the query does not contain the keywords for any curated question, the chatbot responds with "I can't answer that.
Please contact the branch." The system tries to take into consideration inputs with misspellings upto edit distance = 2.

Assumptions:
1. Assuming the account is of only one type, simply called account (no difference between savings or checking).
2. Maximum edit distance in case of misspellings will be 2. You can manually control this in the wordDistance function.

'''

import re

# Curated Questions
QA = {
    "accBalance" : "Balance: ₹ 25,000",                                    # keywords: balance account
    "debitTrans" : "Last debit: Amount: ₹ 3,000   Timestamp: 18:00 2/9/20",   # keywords: last debit transaction
    "creditTrans" : "Last credit: Amount: ₹ 5,000   Timestamp: 11:00 5/9/20",  # keywords: last credit transaction
    "outstandingCC" : "Outstanding in credit card account: ₹ 7,000",            # keywords: outstanding credit card account
    "dueCC" : "Due on credit card: ₹ 4,500 due on 26th September, 2020."              # keywords: payment due credit card {when}
}

cond_1_1 = r"[Bb]alance"
cond_1_2 = r"[Aa]ccount"

cond_2_1 = r"[Ll]ast"
cond_2_2 = r"[Dd]ebit"
cond_2_3 = r"[Tt]ransaction"

cond_3_1 = r"[lL]ast"
cond_3_2 = r"[Cc]redit"
cond_3_3 = r"[Tt]ransaction"

cond_4_1 = r"[Oo]utstanding"
cond_4_2 = r"[Cc]redit"
cond_4_3 = r"[Cc]ard"
cond_4_4 = r"[Aa]ccount"

cond_5_1 = r"[Pp]ayments?"
cond_5_2 = r"[Dd]ue"
cond_5_3 = r"[Cc]redit"
cond_5_4 = r"[Cc]ard"

myKeywords = ['balance', 'account', 'last', 'debit', 'transaction', 'credit', 'outstanding', 'card', 'payment', 'due']

# Ref: https://www.geeksforgeeks.org/edit-distance-dp-5/
def editDistance(str1, str2, m, n):
    if m == 0: 
         return n 
        
    if n == 0: 
        return m 

    if str1[m-1]== str2[n-1]: 
        return editDistance(str1, str2, m-1, n-1) 

    return 1 + min(editDistance(str1, str2, m, n-1),    # Insert 
                   editDistance(str1, str2, m-1, n),    # Remove 
                   editDistance(str1, str2, m-1, n-1)    # Replace 
                   )

def wordDistance(word):
    for i in range(len(myKeywords)):
        res = editDistance(myKeywords[i], word, len(myKeywords[i]), len(word))
        if (res<=2):    # Maximum edit distance in case of misspelling = 2
            return myKeywords[i]
    return None

def getWordList(query):
    query_no_punc = re.sub("[^\w\s]", "", query)
    words = query_no_punc.split()
    for i in range(len(words)):
        words[i] = words[i].lower()
    return words

def ansQuery(query):
    if ((re.search(cond_1_1, query)!= None) and (re.search(cond_1_2, query)!= None)):
        return(QA["accBalance"])
    elif ((re.search(cond_2_1, query)!= None) and (re.search(cond_2_2, query)!= None) and (re.search(cond_2_3, query)!= None)):
        return(QA["debitTrans"])
    elif ((re.search(cond_3_1, query)!= None) and (re.search(cond_3_2, query)!= None) and (re.search(cond_3_3, query)!= None)):
        return(QA["creditTrans"])
    elif ((re.search(cond_4_1, query)!= None) and (re.search(cond_4_2, query)!= None) and (re.search(cond_4_3, query)!= None) and (re.search(cond_4_4, query)!= None)):
        return(QA["outstandingCC"])
    elif ((re.search(cond_5_1, query)!= None) and (re.search(cond_5_2, query)!= None) and (re.search(cond_5_3, query)!= None) and (re.search(cond_5_4, query)!= None)):
        return(QA["dueCC"])
    else:
        return('Wrong')


while (True):
    query = input("How can I help you? ")
    if (query == 'stop'):
        break
    ans = ansQuery(query)
    if (ans != 'Wrong'):
        print(ans)
        print("\n")
    else:
        words = getWordList(query)
        newQuery=''
        for i in range(len(words)):
            newWord = wordDistance(words[i])
            if (newWord!=None):
                newQuery += ' ' + str(newWord)
            else:
                newQuery += ' ' + str(words[i])
        #print(newQuery)
        ans = ansQuery(newQuery)
        if (ans != 'Wrong'):
            print(ans)
            print("\n")
        else:
            print("I can't answer that. Please contact the branch.")
            print("\n")