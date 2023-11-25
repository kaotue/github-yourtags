import awsgi
import create_tags
import create_wordcloud
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/users/<user>', methods=['GET'])
def get_tags(user):
    print(f'{user=}')
    tags = create_tags.run(user)
    if not tags:
        return 'not found'
    return create_wordcloud.run(tags)

def lambda_handler(event, context):
    return awsgi.response(app, event, context)

if __name__ == '__main__':
    app.run(debug=True)