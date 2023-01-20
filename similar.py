from gensim.models import word2vec


def most_similar(load_model_path, positive=None, negative=None):
    model = word2vec.Word2Vec.load(load_model_path)
    print(load_model_path)
    print(positive)

    results = model.wv.most_similar(
        positive=[positive]
    )

    print('ccc')
    return results