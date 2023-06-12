# import tensorflow as tf
# from sklearn.metrics.pairwise import cosine_similarity
# import tensorflow_hub as hub

# embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3")
# # embed = hub.load("https://tfhub.dev/google/universal-sentence-encoder-multilingual/3", tags=['tf2'])

# def mode_predict(data, answer):
#     embeddings_data = embed([data])
#     embeddings_answer = embed([answer])
#     similarity_scores = tf.reduce_sum(tf.multiply(tf.nn.l2_normalize(embeddings_data, axis=1), tf.nn.l2_normalize(embeddings_answer, axis=1)), axis=1)
#     similarity = cosine_similarity([embeddings_data[0]], [embeddings_answer[0]])
#     result_similarity = 0
#     if(similarity_scores.numpy()[0] >= similarity[0][0]):
#         result_similarity = similarity_scores.numpy()[0]
#     else:
#         result_similarity = similarity[0][0]
#     return result_similarity

# sentences1 = 'Pantun adalah salah satu jenis puisi lama yang sangat luas dikenal di Asia tenggara. Pantun memiliki sajak ABAB. Dalam bahasa Sunda pantun disebut paparikan dan dalam bahasa Batak, pantun dikenal dengan sebutan umpasa.'
# sentences2 = 'Pantun merupakan salah satu jenis puisi lama'

# result = mode_predict(sentences1, sentences2)
# print(result)

