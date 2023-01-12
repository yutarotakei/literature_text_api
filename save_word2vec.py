from gensim.models import word2vec

def save_word2vec_model(load_path):
   save_model_path = 'save.model'
   # 分かち書きしたテキストデータからコーパスを作成
   sentences = word2vec.LineSentence(load_path)

   # ベクトル化
   model = word2vec.Word2Vec(
       sentences,
       sg=1,  # Skip-Gram Modelを使用
       size=200,  # ベクトルの次元数
       min_count=4,  # 単語の出現回数によるフィルタリング
       window=5,  # 対象単語からの学習範囲,
       iter=40,
       hs=1
   )
   # 階層化ソフトマックスを使用

   model.save(save_model_path)
   # 作成したモデルをファイルに保存
