import tensorflow as tf
from sentence_transformers import SentenceTransformer, util
from sklearn.metrics.pairwise import cosine_similarity

# Memuat pre-trained Universal Sentence Encoder
# embedder = SentenceTransformer('all-mpnet-base-v2')
embedder = SentenceTransformer('paraphrase-albert-small-v2')

def model_predict(embedder, data, answer):
    sentences1, sentences2 = [data, data, data, data, data],  [answer, answer, answer, answer, answer]
    embeddings1 = embedder.encode(sentences1, convert_to_tensor=True)
    embeddings2 = embedder.encode(sentences2, convert_to_tensor=True)
    # Menghitung kemiripan antara embedding kalimat menggunakan cosine similarity
    cosine_scores = util.pytorch_cos_sim(embeddings1, embeddings2)
    similarity_scores = tf.reduce_sum(tf.multiply(tf.nn.l2_normalize(embeddings1, axis=1),
                                                tf.nn.l2_normalize(embeddings2, axis=1)),
                                                axis=1)
    similarity = cosine_similarity(embeddings1.numpy(), embeddings2.numpy())
    result = [cosine_scores[0][0].item(), similarity_scores[0].numpy(), similarity[0][0]]
    return max(result)