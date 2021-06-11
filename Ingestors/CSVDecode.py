from typing import List
import pandas as pd

from Engine import IngestorInterface
from Engine import QuoteModel


class CSVclass(IngestorInterface):
	allowed = ['csv']

	@classmethod
	def parse(cls, fl: str) -> List[QuoteModel]:
    	if not cls.can_ingest(fl):
        	raise Exception('Not desired extension!')
        result = []
        file = pd.read_csv(fl, header=0, encoding="latin-1")
        for x, y in file.iterrows():
            new_obj = QuoteModel(y['Quote'], y['Master'])
            result.append(new_obj)
            return result
