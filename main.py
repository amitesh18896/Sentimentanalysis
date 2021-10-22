from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
nltk.download('vader_lexicon')
user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
user_input = input("Please Rate Our Services >>: ")
sid = SentimentIntensityAnalyzer()
score = sid.polarity_scores(user_input)
if score["neg"] != 0:
      print("Negative")
else:
      print("Positive")

      import streamlit as st
      import nltk
      from nltk.sentiment.vader import SentimentIntensityAnalyzer

      st.write("# Real Time Sentiment Analysis")

      user_input = st.text_input("Please rate our services >>: ")
      nltk.download("vader_lexicon")
      s = SentimentIntensityAnalyzer()
      score = s.polarity_scores(user_input)

      if score == 0:
          st.write(" ")
      elif score["neg"] != 0:
          st.write("# Negative")
      elif score["pos"] != 0:
          st.write("# Positive")