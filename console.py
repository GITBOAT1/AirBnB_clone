#!/usr/bin/python3
import cmd
from models import storage
from models.base_model import BaseModel

"""
This console contains the entry point of the command interpreter:onsole 0.1
"""


class HBNBCommand(cmd.Cmd):
    """ class definition """
    # intro = "hbnb"
    prompt = "(hbnb) "

    def do_quit(self, line):
        """ Quit command to exit the program"""
        return(True)

    def do_EOF(self, line):
        """ close with ctr+d """
        print("")
        return(True)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
