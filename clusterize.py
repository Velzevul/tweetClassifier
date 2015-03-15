from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

def clusterize(vectors, threshold):
    count_vectorizer = CountVectorizer()
    tfidf_transformer = TfidfTransformer()

    frequency_matrix = count_vectorizer.fit_transform(vectors)
    tfidf_matrix = tfidf_transformer.fit_transform(frequency_matrix)
    distances = cosine_similarity(tfidf_matrix, tfidf_matrix)

    clusters = []
    indices = []

    for i in range(tfidf_matrix.shape[0]):
        if i not in indices:
            clusters.append([ vectors[i] ])
            indices.append(i)

            for j in range(i+1, tfidf_matrix.shape[0]):
                if j not in indices:
                    if distances[i][j] > threshold:
                        clusters[-1].append( vectors[j] )
                        indices.append(j)

    return clusters

def print_clusters(clusters):
    for cluster in clusters:
        print('------------------------')
        for item in cluster:
            print(item)