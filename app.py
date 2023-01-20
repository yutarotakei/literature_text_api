from flask import *
from save_word2vec import *
from similar import *
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def index():
    return '''
    <form method="post" action="/upload_text" enctype="multipart/form-data">
      <input type="file" name="file">
      <button>upload</button>
    </form>
    <form method="post" action="/upload_direct">
      <textarea name="name" cols=60" rows="30"></textarea>
          <p>ポジティブな単語</p>
      <textarea name="positive_word"></textarea>
      <button>upload</button>
    </form>
'''

# アップロード機能
@app.route('/upload_text', methods=['POST'])
def upload_text():
    if 'file' not in request.files:
        return 'ファイル未指定'
    fs = request.files['file']

    # 下記のような情報がFileStorageからは取れる
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    #text_file = ''
    #for line in fs:
        #line = line.decode('utf-8')
        #line = line.rstrip('\n')
        #text_file += line
    #print(text_file)
    fs.save('保存するファイルパス')

    word_model = save_word2vec_model()
    return jsonify({"result": word_model})

@app.route('/upload_direct', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form['name']
    word = request.form['positive_word']
    #print(field)
    #print(word)

    #入力されたものをファイルにする
    file = open('/Users/yutarotakei/Program_Python/flask_practice/test.txt', mode='w')
    file.write(field)
    file.close()

    #load_path = 'wakati.txt'
    save_word2vec_model('/Users/yutarotakei/Program_Python/flask_practice/test.txt')
    save_model_path = 'save.model'
    results = most_similar(save_model_path, word)

    return jsonify({"result": results})



 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)