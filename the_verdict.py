
import os


path = os.path.join(os.path.expanduser("~"), os.getcwd(), "the_verdict.txt")
with open(path, "r", encoding="utf-8") as f:
    raw_text = f.read()
    print("Total number of character:", len(raw_text))
    print(raw_text[:99])