from flask import Flask, render_template, request
from database import Database

app = Flask(__name__)

db=Database('comments.db')

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        name=request.form.get("name")
        comment=request.form.get("comment")
        db.add_comments(name, comment)
    comments = db.get_comments()
    return render_template('comments.html', comments=comments)

if __name__ == "__main__":
    app.run(debug=True)