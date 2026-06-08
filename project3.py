import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load dataset
data = pd.read_csv("jobs.csv")

# Convert skills into TF-IDF vectors
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(data["Skills"])

# Take user input
print("Enter your skills (space separated):")
user_input = input()

# Transform user input
user_vec = vectorizer.transform([user_input])

# Calculate similarity
similarity = cosine_similarity(user_vec, tfidf_matrix)

# Get scores
data["Score"] = similarity[0]

# Sort results
result = data.sort_values(by="Score", ascending=False)

# Show top 3 recommendations
print("\nTop 3 Recommendations:\n")
print(result[["Job Role", "Score"]].head(3))