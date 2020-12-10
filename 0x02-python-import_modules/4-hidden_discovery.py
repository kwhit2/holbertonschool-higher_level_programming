#!/usr/bin/python3
if __name__ == '__main__':
    import hidden_4
    for name in dir(hidden_4):  # will print all names
        if name[:2] != "__":  # if index 0-2 is not __
            print("{}".format(str(name)))
    #  this works as well: print("{:s}".format(name))
