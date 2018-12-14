import sentiment_analysis as sa
import sys
print("Prediting sentiment in ",sys.argv[1],"... ");
sentiment = sa.predict_audio(sys.argv[1])
print(sentiment)
