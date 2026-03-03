from .dbs import config

class SurahsConfig:
  def __init__(self, surah_number=1, reciter_ar=None):
    self.surah_number = surah_number
    self.reciter_ar = reciter_ar
    self.db = config.DBConnect(os.path.join(os.path.abspath(os.path.dirname(__file__)), "/dbs/quran.db"))
    self.table = "audio"
  
  def get_rewaya(self, get_rewaya_lang="en", input_rewaya_lang="ar"):
    try: return {"status": True, "data": self.db.fetch(self.table, columns=f"id,rewaya_{'ar' if get_rewaya_lang == 'ar' else 'en'}", where=f"reciter_{input_rewaya_lang} == {self.reciter_ar}")}
    except Exception as e: return {"status": False, "error": e}
  
  def get_server(self):
    try: return {"status": True, "data": self.db.fetch(self.table, columns=f"id,server")}
    except Exception as e: return {"status": False, "error": e}
  
  def get_server(self, id):
    try: return {"status": True, "data": self.db.fetch(self.table, columns=f"id,server", where=f"id == {id}")}
    except Exception as e: return {"status": False, "error": e}
  
class AyatConfig:
  def __init__(self, surah_number=1, reciter_ar=None):
    self.surah_number = surah_number
    self.reciter_ar = reciter_ar
    self.db = config.DBConnect(os.path.join(os.path.abspath(os.path.dirname(__file__)), "/dbs/quran.db"))
    self.table = "audio"
  
  def get_rewaya(self, get_rewaya_lang="en", input_rewaya_lang="ar"):
    try: return {"status": True, "data": self.db.fetch(self.table, columns=f"id,rewaya_{'ar' if get_rewaya_lang == 'ar' else 'en'}", where=f"reciter_{input_rewaya_lang} == {self.reciter_ar}")}
    except Exception as e: return {"status": False, "error": e}
  
  def get_server(self):
    try: return {"status": True, "data": self.db.fetch(self.table, columns=f"id,server")}
    except Exception as e: return {"status": False, "error": e}
  
  def get_server(self, id):
    try: return {"status": True, "data": self.db.fetch(self.table, columns=f"id,server", where=f"id == {id}")}
    except Exception as e: return {"status": False, "error": e}
