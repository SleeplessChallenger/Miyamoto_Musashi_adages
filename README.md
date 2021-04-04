# Miyamoto_Musashi_adages
**Wise samurai quotes** is a project where user can observe 
random photos in hand with inscripted phrases either in
the browser or via CLI.

**Conceptual overview**

1) OOP was highle leveraged with myraid features like
@classmethods, inheritance, abstract classes. Also I managed
to stick to the DRY principle.

2) Virtual environment was also implemented

3) __init__.py for absolute and relative imports

4) multiple external libraries like PIL, subprocess,
argparse were also taken into account

**How to deploy**

1) run `pip install -r requirements.txt` to install
all the required packages

2) Then `export FLASK_APP=app.py` should be run

3) Last step: `flask run --host localhost --port 3000 --reload`

4) Open: localhost:3000

**Two ways to create images** 

a) Web one:
  1) Steps were deleneated above
  2) Images will be stored in static folder
  3) Also, user can input link with photo + author and text
 
b) CLI one
  1) run python3 meme.py in command line
  2) result can be found in output folder
  3) there a couple of customizations: 
  _shortcuts: -a for --author, -b for --body and -p fof --path_
  
**A little bit about inheritance stuff**

IngestorInterface is a superclass to CSVDecode, PDFDecode,
DOCXDecode, TXTDecode. IngestorInterface is an abstractclass which is realized 
by Ingestor class in MainIngestor
  
 
**Tips for deployment**

a. Use virtual environment. Open terminal
  1.python3[.figure if you like] -m venv [venv] - name of the environment 
  2.source venv/bin/activate -> it will activate our virtual environment. To exit it use: deactivate 
  3.pip install -r requirements.txt
 
b. For MacOS you'll need *brew*
  1. /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  2. $ brew install wget
  3. brew install --cask pdftotext
+ update: `pip install -U setuptools`

<h3>Some additional explanation of the structure and inner-workings</h3>
<hr>
<h5>How does the overall flow happen?</h5>
1. the app is launched via <i>app.py</i> or <i>meme.py</i>. The former is for web created memes and the latter
   one is for CLI created ones. <br>

**Firstly, let's look at web created ones**

2. meme is an instance of MemeEngine with provided self.place as './static'. Then, quotes, img triggers setup() which will       
   attach photos & quotes to those two variables

3. At first the home page is generated by meme_rand(). From this page we can either generate new random meme that will once again 
   return to meme_rand() or create new custom meme by clicking on 'create' -> leads by url_for() to meme_form -> meme_post() ->
   new meme appears and is saved to './static'

- meme_post() will at first save photo from `create` button in project home directory and after the subsriptions have been added
  `os` module will delete it.

**Secondly, let's look at CLI creted ones**
2. run <i>python3 meme.py</i> + user can add either of the options: -a='Some author' -b='Some body' -p='Some path'.

3. In the function depending on the provided above parameters there will be either default quotes & author taken
   or provided by the user. If <i>body</i> is not None: the code will use <i>QuoteModel</i> class to store there
   self.author & self.body

4. new path [in our case it'll be "./generated_quote"] is created if hasn't existed before. Here <i>meme</i> is also an 
   instance of MemeEngine class. And in that folder new meme will appear.

<h6>Now let's dive deeper into how <i>quotes</i> are taken from preloaded files.</h6>

1. `quotes.extend(Ingestor.parse(y))` is in both aforewritten files. It goes straight to `Ingestors/MainIngestor.py -> class Ingestor'
2. There code loops over provided `types` which comprises imported classes: `CSVclass, DOCXclass, TXTclass, PDFclass`.
3. Program checks if either of those classes can parse file with such an extension.<br>

   **Notice**
  Those classes themselves don't have `can_ingest()` function, but super class `IngestorInterface` in `Ingestors/QuoteEngine` has. 
  If provided extension is in `allowed` -> returns to `MainIngestor.py` -> goes into one of those classes and parse the file ->
  comes back to `MainIngestor.py` and it returns quotes to either <i>app.py</i> or <i>meme.py</i> in list format.
  
```bash
.
├── Engine
│   ├── Bone.py
│   ├── MemeEngine.py
│   ├── QuoteEngine.py
│   ├── __init__.py
├── Ingestors
│   ├── CSVDecode.py
│   ├── DOCXDecode.py
│   ├── MainIngestor.py
│   ├── PDFDecode.py
│   ├── TXTDecode.py
│   ├── __init__.py
├── _data
│   ├── MiyamotoMusashiAdages
│   │   ├── SamuraiAdages.csv
│   │   ├── SamuraiAdages.docx
│   │   ├── SamuraiAdages.pdf
│   │   └── SamuraiAdages.txt
│   ├── SimpleLines
│   │   ├── SimpleLines.csv
│   │   ├── SimpleLines.docx
│   │   ├── SimpleLines.pdf
│   │   └── SimpleLines.txt
│   └── photos
│       └── samurai
│           ├── Samurai1.jpg
│           ├── Samurai2.jpg
│           ├── Samurai3.jpg
│           ├── Samurai4.jpg
│           ├── Samurai5.jpg
│           ├── Samurai6.jpg
│           ├── Samurai7.jpg
│           ├── Samurai8.jpg
│           └── Samurai9.jpg
├── app.py
├── generated_quote
│   ├── Quote:\ 11.jpeg
│   └── Quote:\ 42.jpeg
├── meme.py
├── requirements.txt
├── static
│   ├── Quote:\ 1.jpeg
│   ├── Quote:\ 11.jpeg
└── templates
    ├── base.html
    ├── meme.html
    └── meme_form.html

```
