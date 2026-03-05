import sys, subprocess, argparse
from . import __version__

def main():
  parser = argparse.ArgumentParser(prog="pyislamsdk_quran", description="IslamSDK Quran module with Quranic texts, utilities, and local database.")
  parser.add_argument("--version", action="version", version=f"PyIslamSDK-Quran (pyislamsdk_quran) Version: {__version__}", help="Show the current version")
  parser.add_argument("--upgrade", action="store_true", help="Upgrade PyIslamSDK-Quran to the latest version")
  args = parser.parse_args()
  if args.upgrade:
    print("Upgrading PyIslamSDK-Quran...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "--upgrade", "PyIslamSDK-Quran"], shell=True)
    print("Upgrade completed!")
