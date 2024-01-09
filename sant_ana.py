#Develop a function that analyzes a social media post and returns the sentiment (positive, negative, neutral) and keywords used.
#Expand the function to identify emojis and potential trends.

def comment_analyze (bad_comment,good_comment,neutral_comment):
    if comment in bad_comment:
        print ("your commment is negative :(  ")
    elif comment in good_comment:
        print("your comment is positive :)   ")
    elif comment in neutral_comment:
        print("your comment is neutral :\ ")
    else:
        print("cant understand the comment, can u define it ? ")

comment = input("enter ur comment :")
bad_comment = ["bad","not","not good","ugly","worst"]
good_comment = ["good","nice","yes","wow","cool","beautiful"]
neutral_comment = ["huh","what","idk"]

comment_analyze (bad_comment,good_comment,neutral_comment)
