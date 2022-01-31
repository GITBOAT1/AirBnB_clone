from models import storage
from models.base_model import BaseModel


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

