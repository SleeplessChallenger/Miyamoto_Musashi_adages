from abc import ABC, abstractmethod
from typing import List
from .Bone import QuoteModel


class IngestorInterface(ABC):
	"""Overall methods
	part of which will be realized
	in another files"""

	allowed = ['txt', 'csv', 'docx', 'pdf']

	# below we take path, divide by '.'
	# hence file extension will be
	# the last value in the list
	# take that value and see
	# whether it's in allowed extensions
	@classmethod
	def can_ingest(cls, path: str) -> bool:
		x = path.split('.')[-1]
		return x in cls.allowed

	@classmethod
	@abstractmethod
	def parse(cls, path: str) -> List[QuoteModel]:
		pass
