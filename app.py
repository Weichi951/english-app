from flask import Flask, render_template, jsonify
import random
import os

# 自動抓取 app.py 所在資料夾底下的 templates
base_dir = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__, template_folder=os.path.join(base_dir, 'templates'))

# 單字資料庫
WORDS = [
    {"id": 1, "word": "Resilient", "definition": "有彈性的；能迅速恢復的", "example": "She is a resilient person."},
    {"id": 2, "word": "Innovation", "definition": "創新；革新", "example": "Technological innovation improves our lives."},
    {"id": 3, "word": "Persistent", "definition": "堅持不懈的；持續的", "example": "Success comes from persistent effort."},
    {"id": 4, "word": "Eloquent", "definition": "雄辯的；有說服力的", "example": "He gave an eloquent speech."}
]

# 首頁路由
@app.route('/')
def home():
    return render_template('index.html', words=WORDS)

# 隨機單字 API
@app.route('/api/quiz')
def get_quiz():
    target = random.choice(WORDS)
    return jsonify(target)

# ⚠️ 關鍵！這兩行一定要貼在最底部、最左邊（頂格）！
if __name__ == '__main__':
    print("🚀 伺服器正在啟動中...")
    app.run(host='0.0.0.0', port=5000, debug=True)