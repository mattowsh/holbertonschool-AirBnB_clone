#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of the
command interpreter:
"""
import cmd
import sys
from models.base_model import BaseModel
from models import storage

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

    def do_create(self, args):
        """ Creates a new instance of BaseModel """
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            new_instance = eval(args)()
            new_instance.save()
            print(new_instance.id)
        except:
            print("** class doesn't exist **")

    def do_show(self, args):
        """ Prints the string representation of an instance """
        if len(args) == 0:
            print("** class name missing **")
            return
        # devuelve una lista de strings de los args del promt
        prompt_args = args.split()
        # si el len < 2 es xq no tiene id
        if len(prompt_args) < 2:
            print("** instance id missing **")
            return
        # string con la siguiente syntax 'class.id'
        class_plus_id = '.'.join(prompt_args)
        #print(class_plus_id)
        objs = storage.all()
        print(objs[class_plus_id])



if __name__ == '__main__':
    HBNBCommand().cmdloop()
