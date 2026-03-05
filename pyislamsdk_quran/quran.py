import importlib.resources as pkg
from .dbs import config

class SurahsConfig:
  def __init__(self):
    self.db = config.DBConnect(str(pkg.files(dbs).joinpath("quran.db")))
    self.table = "surahs"

  def get_all_surahs(self):
    try: return {"status": True, "data": self.db.fetch(self.table)}
    except Exception as e: return {"status": False, "error": str(e)}
  
  def get_surah(self, name="الفاتحة"):
    try: return {"status": True, "data": self.db.fetch(self.table, where=f"name_ar LIKE '%{name}%'")}
    except Exception as e: return {"status": False, "error": str(e)}
  
  def get_surah_verses(self, id=1):
    try: return {"status": True, "data": self.db.fetch(self.table, where=f"id = {int(id)}")}
    except Exception as e: return {"status": False, "error": str(e)}
  
  def get_revelation_place(self, place="مكية"):
    try: return {"status": True, "data": self.db.fetch(self.table, where=f"revelation_place_ar = '{place}'")}
    except Exception as e: return {"status": False, "error": str(e)}
