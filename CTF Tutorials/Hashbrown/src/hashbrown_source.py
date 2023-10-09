import hashlib
import sys

# pyinstaller -w -F hashbrown.py

def read_files(key1, key2):
  try:
    with open(key1, 'rb') as f1, open(key2, 'rb') as f2:
      content1 = f1.read()
      content2 = f2.read()
      if content1 != content2:
        hash1 = hashlib.md5(content1).hexdigest()
        hash2 = hashlib.md5(content2).hexdigest()
        if hash1 == hash2:
          print("\n  You have successfully logged in!")
          print("\n  Flag: 0x4067{HASHBROWN_HASH_COLLIDED}\n")
          return
        else:
          print("\n  Access denied! File hashes are different!\n")
      else:
        print("\n  Access denied! File contents are the same!\n")
  except Exception as e:
    print(f"\n Access denied! {e}")


def main():
  print("""\n ____ ____ ____ ____ ____ ____ ____ ____ ____\n||h |||4 |||5 |||h |||b |||r |||0 |||w |||n ||\n||__|||__|||__|||__|||__|||__|||__|||__|||__||\n|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|/__\|
    """)
  if len(sys.argv) < 3:
    print("\n Usage: ./hashbrown <path_to_file_1> <path_to_file_2>\n")
  else:
    read_files(sys.argv[1], sys.argv[2])


if __name__ == "__main__":
  main()