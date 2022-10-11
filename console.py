#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of the 
command interpreter:
"""
import cmd
import sys

class HBNBCommand(cmd.Cmd):
    """ command line processor """
    def __init__(self):
        cmd.Cmd.__init__(self)
        self.prompt = '(hbnb)'

    def do_quit(self, arg):
        """to exit the program"""
        return True

    def do_EOF(self, arg):
        """ to exit the program """
        return True
    
    def emptyline(self):
        """ empty line"""
        # pass, because if we return the program it dies
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()