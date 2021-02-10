from typing import List
import subprocess
from pathlib import Path
import os

from Engine import IngestorInterface
from Engine import QuoteModel
from .TXTDecode import TXTclass


class PDFclass(IngestorInterface):

	allowed = ['pdf']

	@classmethod
	def parse(cls, fl: str) -> List[QuoteModel]:
		if not cls.can_ingest(fl):
			raise Exception('Not desired extension!')
		cont = list()
		temps = f'{Path.cwd()}/temp.txt'
		subprocess.call(['pdftotext', fl, temps], stdout = subprocess.PIPE, stderr = subprocess.PIPE)

		var = open(temps, 'r')
		for x in var.readlines():
			# if len(x) > 0:
			x = x.split('- Miyamoto Musashi')
			x.pop()
			for obj in x:
				obj = obj.strip()
				new_ = QuoteModel(obj, 'Miyamoto Musashi')
				cont.append(new_)
		var.close()
		os.remove(temps)
		return cont
