text = input("Enter a sentence: ").lower()

positive = ["good", "great", "happy", "love", "excellent", "amazing"]
negative = ["bad", "sad", "hate", "poor", "terrible", "worst"]

pos = sum(word in text for word in positive)
neg = sum(word in text for word in negative)

if pos > neg:
    print("Sentiment: Positive 😊")
elif neg > pos:
    print("Sentiment: Negative 😞")
else:
    print("Sentiment: Neutral 😐")