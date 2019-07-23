from fuzzywuzzy import fuzz
from fuzzywuzzy import process

r = fuzz.ratio("this is a test", "this is a test!")
print(r)

r = fuzz.ratio("fuzzy wuzzy was a bear", "wuzzy fuzzy was a bear")
print(r)
