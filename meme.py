import os
import random
from .QuoteEngine import Ingestor
from .MemeEngine import MemeEngine
from pathlib import Path
import argparse


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "/Users/daniilslobodenuk/Desktop/Udacity/src/_data/photos/samurai/"
        imgs = []
        for root, dirs, files in os.walk(images):
            if '.DS_Store' in files:
                files.remove('.DS_Store')
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['/Users/daniilslobodenuk/Desktop/Udacity/src/_data/MiyamotoMusashiAdages/SamuraiAdages.txt',
                       '/Users/daniilslobodenuk/Desktop/Udacity/src/_data/MiyamotoMusashiAdages/SamuraiAdages.docx',
                       '/Users/daniilslobodenuk/Desktop/Udacity/src/_data/MiyamotoMusashiAdages/SamuraiAdages.csv',
                       '/Users/daniilslobodenuk/Desktop/Udacity/src/_data/MiyamotoMusashiAdages/SamuraiAdages.pdf']
        quotes = []
        for y in quote_files:
            quotes.extend(Ingestor.parse(y))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeEngine("./generated_quote")
    path = meme.make_meme(img, quote.body, quote.author)
    return path


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='This program will output image with adage insripted on it',
                                     proq='Wise adages generator',
                                     epilog='Listen to the master!')
    parser.add_argument('-b', '--body', help='Put quote',
                        type=str, default=None)
    parser.add_argument('-a', '--author', help='Put author',
                        type=str, default=None)
    parser.add_argument('-p', '--path', help='Where to find',
                        type=str, default=None)
    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
