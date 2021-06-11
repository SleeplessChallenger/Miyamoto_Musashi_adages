import random
import os
import requests
from flask import Flask, render_template, abort, request
from Ingestors import Ingestor
from Engine import MemeEngine
import requests
import pathlib

app = Flask(__name__)

meme = MemeEngine('./static')
# 1) gives MemeEngine class self.place
# 2) 'meme' is a class instance which
#    will be used for meme.make_mem(...)


class UnableParsing(Exception):
    pass


def setup():
    """ Load all resources """

    quote_files = ['./_data/MiyamotoMusashiAdages/SamuraiAdages.txt',
                   './_data/MiyamotoMusashiAdages/SamuraiAdages.docx',
                   './_data/MiyamotoMusashiAdages/SamuraiAdages.csv'
                   ]

    quotes = []
    for x in quote_files:
        try:
            quotes.extend(Ingestor.parse(x))
        # except UnableParsing as err:
        #     print(err)
        except ValueError as err:
            print(err)

    imgs = []
    # images_path = "/Users/daniilslobodenuk/Desktop/Udacity/src/_data/photos/samurai"
    images_path = "./_data/photos/samurai"
    for root, dir, files in os.walk(images_path):
        if '.DS_Store' in files:
            files.remove('.DS_Store')
        imgs = [os.path.join(root, y) for y in files]

    return quotes, imgs


# quotes, imgs = setup()


@app.route('/')
def meme_rand():
    """ Generate a random meme """
    global imgs, quotes
    img = random.choice(imgs)
    quote = random.choice(quotes)
    path = meme.make_meme(img, quote.body, quote.author)
    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """ User input for meme information """
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """ Create a user defined meme """

    img = f"{pathlib.Path.cwd()}/new_masterpiece.jpg"
    img_url = request.form.get('image_url')
    response = requests.get(img_url, stream=True)
    img_cont = response.content
    with open(img, 'wb') as file1:
        file1.write(img_cont)
    body = request.form.get('body', "")
    author = request.form.get('author', 'Unnamed')
    path = meme.make_meme(img, body, author)
    os.remove(img)
    # line above manages to delete files from
    # '/src' folder and only keep newly 
    # created meme in '/static'

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    quotes, imgs = setup()
    app.run(host='0.0.0.0', port=5000)
