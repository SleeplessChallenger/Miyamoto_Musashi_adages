from PIL import Image, ImageDraw, ImageFont
import pathlib
import os
import random


class MemeEngine:
	"""Class that will create
	meme itself"""

	def __init__(self, place):
		"""will put meme
		into provided folder"""
		self.place = place
		if not pathlib.Path(place).exists():
			pathlib.Path(place).mkdir()
		self.counter = 10

	def make_meme(self, image, body, author, width=500):
		font = ImageFont.truetype("./_data/Lato-Regular.ttf", 32, encoding='UTF-8')
		self.counter = random.randint(1, 100)
		img = Image.open(image)
		output = os.path.join(self.place, f"Quote: {self.counter}.jpeg")
		x_width, x_height = img.size
		ratio = width/ x_width
		height = int(x_height * ratio)
		img.thumbnail((width, height))
		fill = 'white'
		stroke_fill = 'black'
		draw = ImageDraw.Draw(img)
		rand_pos = random.choice(range(20, height-40))
		draw.text((50, rand_pos), body, fill, font, 
                    stroke_fill=stroke_fill, stroke_width=2)
		draw.text((50, rand_pos+30), f" - {author}", fill,
                    font=font, stroke_fill=stroke_fill, stroke_width=2)
		img.save(output, 'jpeg')
		return output
