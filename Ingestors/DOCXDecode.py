from typing import List
import docx
import unicodedata

from Engine import IngestorInterface
from Engine import QuoteModel


class DOCXclass(IngestorInterface):
	allowed = ['docx']

	@classmethod
	def parse(cls, fl: str) -> List[QuoteModel]:
		if not cls.can_ingest(fl):
			raise Exception('Not desired extension!')
		result = []
		doc_ = docx.Document(fl)
		for x in doc_.paragraphs:
			if x.text is not '':
				temp = x.text.split('-')
				temp1 = temp[0].strip()
				temp2 = temp[1]
				res = QuoteModel(temp1, temp2)
				result.append(res)
		return result
