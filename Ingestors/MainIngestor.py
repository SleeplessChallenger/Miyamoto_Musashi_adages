from typing import List

from .CSVDecode import CSVclass
from .DOCXDecode import DOCXclass
from .PDFDecode import PDFclass
from .TXTDecode import TXTclass

from Engine import IngestorInterface
from Engine import QuoteModel


class Ingestor(IngestorInterface):
	types = [CSVclass, DOCXclass, TXTclass, PDFclass]

	@classmethod
	def parse(cls, fl: str) -> List[QuoteModel]:
		for obj in cls.types:
			if obj.can_ingest(fl):
				return obj.parse(fl)
