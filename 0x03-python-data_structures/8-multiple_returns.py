#!/usr/bin/python3
def multiple_returns(sentence):
    total = len(sentence)
    first = sentence[0] if total > 0 else "None"
    new = total, first
    return (new)
