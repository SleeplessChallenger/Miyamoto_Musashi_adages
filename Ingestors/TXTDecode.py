from typing import List

from Engine import IngestorInterface
from Engine import QuoteModel


class TXTclass(IngestorInterface):
	allowed = ['txt']

	@classmethod
	def parse(cls, fl: str) -> List[QuoteModel]:
		if not cls.can_ingest(fl):
			raise Exception('Not desired extension!')
		file = open(fl, "r", encoding="utf-8")
		temp = file.readlines()
		file.close()
		bucket = list()
		for x in temp:
			x = x.strip()
			if len(x) > 0:
				data = x.split('-')
				new_ = QuoteModel(data[0], data[1])
				bucket.append(new_)
		return bucket
