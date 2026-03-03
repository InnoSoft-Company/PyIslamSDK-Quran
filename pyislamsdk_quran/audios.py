from .dbs import config
import os

class AudioConfig:
  def __init__(self, surah_number=1, reciter_ar=None):
    self.surah_number = surah_number
    self.reciter_ar = reciter_ar
    self.db = config.DBConnect(os.path.join(os.path.abspath(os.path.dirname(__file__)), "/dbs/quran.db"))
    self.table = "audio"
  
  def get_rewaya(self, lang=ar):
    pass
