# -------------------------------------------------------------------------
# AUTHOR: Sunjay N. Guttikonda
# FILENAME: similarity.py
# SPECIFICATION: Find the two most similar documents using cosine similarity.
# FOR: CS 5990 (Advanced Data Mining) - Assignment #1
# TIME SPENT: 1 hour
# -----------------------------------------------------------*/

# IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy,
# pandas, or other sklearn modules.
# You have to work here only with standard dictionaries, lists, and arrays

import csv
import math

# Read the documents from the CSV file
documents = []
with open('cleaned_documents.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)  # Skip the header
    #rows = list(reader)
    for row in reader:
        documents.append((int(row[0]), row[1].split()))

#Build the vocabulary
vocabulary = set()
for _, words in documents:
    vocabulary.update(words)
vocabulary = sorted(vocabulary)
word_to_index = {word: idx for idx, word in enumerate(vocabulary)}

#Construct the document-term matrix
docTermMatrix = []
doc_vectors = {}
for doc_id, words in documents:
    vector = [0] * len(vocabulary)
    for word in set(words):
        vector[word_to_index[word]] = 1
    doc_vectors[doc_id] = vector
    docTermMatrix.append((doc_id, vector))

#Calculate cosine similarity between all document pairs
def cosine_similarity(vec1, vec2):
    dot_product = sum(x * y for x, y in zip(vec1, vec2))
    magnitude1 = math.sqrt(sum(x ** 2 for x in vec1))
    magnitude2 = math.sqrt(sum(x ** 2 for x in vec2))
    return dot_product / (magnitude1 * magnitude2) if magnitude1 and magnitude2 else 0

max_similarity = -1
most_similar_docs = (None, None)

doc_count = len(docTermMatrix)
for i in range(doc_count):
    for j in range(i + 1, doc_count):
        doc1_id, vec1 = docTermMatrix[i]
        doc2_id, vec2 = docTermMatrix[j]
        similarity = cosine_similarity(vec1, vec2)
        if similarity > max_similarity:
            max_similarity = similarity
            most_similar_docs = (doc1_id, doc2_id)

# Print the most similar documents
print(f"The most similar documents are document {most_similar_docs[0]} and document {most_similar_docs[1]} with cosine similarity = {max_similarity:.4f}")
#print(f"Document", most_similar_docs[0], ":", rows[117])
#print(f"Document", most_similar_docs[1], ":", rows[163])