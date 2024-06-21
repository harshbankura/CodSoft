import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

# Sample dataset of movies with descriptions
data = {
    'item_id': ['The Shawshank Redemption', 'The Godfather', 'The Dark Knight', 'Pulp Fiction', 'Forrest Gump', 'Fight Club'],
    'description': ['Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.',
                    'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant son.',
                    'When the menace known as the Joker wreaks havoc and chaos on the people of Gotham, Batman must accept one of the greatest psychological and physical tests of his ability to fight injustice.',
                    'The lives of two mob hitmen, a boxer, a gangster and his wife, and a pair of diner bandits intertwine in four tales of violence and redemption.',
                    'The heartwarming journey of a simple man who unwittingly becomes a part of key historical moments in America.',
                    'A dark and anarchic exploration of masculinity and consumer culture through an underground fight club']
}


df = pd.DataFrame(data) #loading data into data frame

# Define a TF-IDF Vectorizer
tfidf = TfidfVectorizer(stop_words='english')

# Convert text descriptions into TF-IDF matrix
tfidf_matrix = tfidf.fit_transform(df['description'])

# Calculate cosine similarity matrix
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

def get_recommendations(item_id, cosine_sim=cosine_sim):
    item_id = item_id.lower() # Converting into lower case due to case sensitivity
    
    # Check if item_id exists in the DataFrame
    if item_id not in df['item_id'].str.lower().values:
        return "Item not found in the database."
    
    idx = df[df['item_id'].str.lower() == item_id].index[0] # Finds index of item
    
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Get top 5 similar items
    item_indices = [i[0] for i in sim_scores]
    return df['item_id'].iloc[item_indices]

# Get recommendation for an item
item_id = 'Forrest Gump' #(You can replace 'Forrest Gump' with any other movie name from dataset )
recommendations = get_recommendations(item_id)
print("Top recommendations for", item_id)
print(recommendations)
