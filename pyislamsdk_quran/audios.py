from .dbs import config
import os

class AudioConfig:
  def __init__(self, surah_number=1, reciter_ar=None):
    self.surah_number = surah_number
    self.reciter_ar = reciter_ar
    self.db = config.DBConnect(os.path.join(os.path.abspath(os.path.dirname(__file__)), "dbs/quran.db"))
    self.table = "audio"
  
  def get_rewaya(self, lang="en"):
    try: return {"status": True, "data": self.db.fetch(self.table, where=f"reciter_{lang} = '{self.reciter_ar}'")}
    except Exception as e: return {"status": False, "error": e}
  
  class Servers:
    def __init__(self): self.config = self
    
    def get_all_servers(self):
      try: return {"status": True, "data": self.config.db.fetch(self.config.table)}
      except Exception as e: return {"status": False, "error": e}
  
    def get_server(self):
      try: return {"status": True, "data": self.config.db.fetch(self.config.table, columns=f"id,server", where=f"id = {self.config.surah_number}")}
      except Exception as e: return {"status": False, "error": e}
