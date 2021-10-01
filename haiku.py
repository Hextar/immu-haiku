import re

DEBUG = True

def clean_haiku(haiku):
    lines = haiku.split("\n")
    lines = [line.lower()
                 .replace("[^a-z]","")
                 .strip() for line in lines]
    return lines

def count_syllables(line):
  words = line.split(" ")
  count = 0
  for word in words:
    matches = re.findall("[aeiouy]+", word)
    if word.endswith("e") and len(matches) > 1:
        count -= 1
    count += len(matches)
  return count

def validate_haiku(haiku):
    lines = clean_haiku(haiku)
    if len(lines) != 3:
        return False
    counts = [count_syllables(line) for line in lines]
    if DEBUG:
        print(counts)
    if counts != [5, 7, 5]:
        return False
    return True