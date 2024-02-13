#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle
from models.square import Square

if __name__ == "__main__":

    Square.save_to_file_csv([])
    output = Square.load_from_file_csv()


    output = Square.load_from_file_csv()
