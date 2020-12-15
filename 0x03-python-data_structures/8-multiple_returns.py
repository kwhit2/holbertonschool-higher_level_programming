#!/usr/bin/python3
def multiple_returns(sentence):
    total = len(sentence)
    first = sentence[0] if total > 0 else "None"
    new = total, first
    return (new)

#  Below also works
#  def multiple_returns(sentence):
#        if sentence == "" or sentence is None:
#           return (0, None)
#        else:
#            return (len(sentence), sentence[0])
