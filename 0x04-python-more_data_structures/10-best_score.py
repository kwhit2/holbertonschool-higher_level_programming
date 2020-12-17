#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return
    max_key = max(a_dictionary, key=lambda x: a_dictionary[x])
    return (max_key)

#  2 code below are same but diff format. Correct Output/missing 2 checks
#  return (max(a_dictionary) if a_dictionary else None)
#  ----------------------------------------------------
#  if not a_dictionary:
#      return None
#  return (max(a_dictionary))
