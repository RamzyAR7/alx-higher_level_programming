#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    names_of_func = dir(hidden_4)
    for n in names_of_func:
        if n[:2] != "__":
            print(n)
