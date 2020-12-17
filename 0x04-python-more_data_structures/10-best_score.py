#!/usr/bin/python3
def best_score(a_dictionary):
    return (max(a_dictionary) if a_dictionary else None)

#  Same as above, diff format. Correct Output/missing 2 checks
#  if not a_dictionary:
#      return None
#  return (max(a_dictionary))
