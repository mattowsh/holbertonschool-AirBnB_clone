#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of the
command interpreter:
"""
import cmd
import sys
import uuid
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    """ command line processor """
    prompt = '(hbnb)'
    our_classes = [BaseModel]

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
        # to create a list of strings that contain the input
        prompt_args = args.split()
        
        if len(prompt_args) == 0:
            print("** class name missing **")
            return

        elif len(prompt_args) == 1: 
            # if len(prompt_args) <= 2 means that input is incomplete,
            if (prompt_args[0] in self.our_classes) is False:
                # check if ID is missing
                print("** instance id missing **")
                return
            else:
                # prompt_args[0] is not a valid class name
                print("** class doesn't exist **")
                return

        elif len(prompt_args) == 2:
            # the correct quantity of args
            try:
                # string format: 'class.id'
                class_plus_id = '.'.join(prompt_args)
                objs = storage.all()
                # search in JSON file with the key 'class.id'
                print(objs[class_plus_id])
            except:
                print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        prompt_args = args.split()

        if len(prompt_args) == 0:
            # check if class name is missing
            print("** class name missing **")
            return

        elif len(prompt_args) == 1:
            if (prompt_args[0] in self.our_classes) is False:
                # check if prompt_args[0] is a valid class name
                print("** instance id missing **")
                return
            else:
                # when prompt_args[0] is not a valid class name
                print("** class doesn't exist **")
                return

        elif len(prompt_args) == 2:
            try:
                # string format: 'class.id'
                class_delete = '.'.join(prompt_args)
                objs = storage.all()
                # update JSON file with the key 'class.id' removed
                del objs[class_delete]
                storage.save()
            except:
                print("** no instance found **")
                return


if __name__ == "__main__":
    HBNBCommand().cmdloop()
