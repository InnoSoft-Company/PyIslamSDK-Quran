from . import __version__
import sys

def main():
  arg = sys.argv
  if "--version" in arg: print(f"InnoCaptcha Version: {__version__}") 
