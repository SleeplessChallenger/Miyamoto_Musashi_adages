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
  
  
