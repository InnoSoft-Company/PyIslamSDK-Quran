import importlib.resources as pkg
from .dbs import config

class AudioConfig:
  def __init__(self, surah_number=1, reciter_ar=None):
    self.surah_number = surah_number
    self.reciter_ar = reciter_ar
    self.db = config.DBConnect(str(pkg.files(dbs).joinpath("quran.db")))
    self.table = "audio"
    self.servers = self.Servers(self)

  def get_rewaya(self, lang="en"):
    if not self.reciter_ar: return {"status": False, "error": "reciter_ar not set"}
    try: return {"status": True, "data": self.db.fetch(self.table, where=f"reciter_{lang} = '{self.reciter_ar}'")}
    except Exception as e: return {"status": False, "error": str(e)}

  class Servers:
    def __init__(self, outer_instance): self._outer = outer_instance

    def get_all_servers(self):
      try: return {"status": True, "data": self._outer.db.fetch(self._outer.table)}
      except Exception as e: return {"status": False, "error": str(e)}

    def get_server(self):
      try: return {"status": True, "data": self._outer.db.fetch(self._outer.table, columns="id, server", where=f"id = {self._outer.surah_number}")}
      except Exception as e: return {"status": False, "error": str(e)}
  