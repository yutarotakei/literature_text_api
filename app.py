from flask import *
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def index():
    return '''
    <form method="post" action="/upload_text" enctype="multipart/form-data">
      <input type="file" name="file">
      <button>upload</button>
    </form>
    <form method="post" action="/upload_direct">
      <textarea name="name"></textarea>
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
    text_file = ''
    for line in fs:
        line = line.decode('utf-8')
        line = line.rstrip('\n')
        text_file += line
    print(text_file)

@app.route('/upload_direct', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form['name']
    #print(field)



 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)