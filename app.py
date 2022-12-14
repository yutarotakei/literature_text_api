from flask import *
 
app = Flask(__name__)
 
@app.route('/', methods=['GET'])
def index():
    return '''
    <form method="post" action="/upload" enctype="multipart/form-data">
      <input type="file" name="file">
      <button>upload</button>
    </form>
'''

# アップロード機能
@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return 'ファイル未指定'

    # fileの取得（FileStorage型で取れる）
    # https://tedboy.github.io/flask/generated/generated/werkzeug.FileStorage.html
    fs = request.files['file']

    # 下記のような情報がFileStorageからは取れる
    app.logger.info('file_name={}'.format(fs.filename))
    app.logger.info('content_type={} content_length={}, mimetype={}, mimetype_params={}'.format(
        fs.content_type, fs.content_length, fs.mimetype, fs.mimetype_params))

    # ファイルを保存
    for line in fs:
        print(line)


 
if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8888, debug=True)