import pandas as pd
from textblob import TextBlob

df = pd.read_csv('your_file_name.csv', sep=',')
text = df['The_column_where_your_text_is_in']

sentiment = []
sentiment_temp = []
result = []


def Average(lst):
    return sum(lst) / len(lst)


def main():
    for elem in text:
        blob = TextBlob(elem)
        for sentence in blob.sentences:
            sentiment_temp.append(sentence.sentiment.polarity)
        sentiment = Average(sentiment_temp)
        result.append(sentiment)

    df['Sentiment'] = result
    df.to_csv("./new_file_name.csv", sep=',', index=False)


if __name__ == "__main__":
    main()
