class QuoteModel:
	"""Class that depicts
	body and author"""

	def __init__(self, body, author):
		self.body = body
		self.author = author

	def __repr__(self):
		return f"Main model: {self.body} by {self.author}"
