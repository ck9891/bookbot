def word_count(text) :
  words = text.split()
  return len(words)

def character_count(text) :
  letter_dict = dict()
  for char in text:
    key = char.lower()
    if key in letter_dict:
      letter_dict[key] += 1
    else:
      letter_dict[key] = 1
  return letter_dict
  
def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list
