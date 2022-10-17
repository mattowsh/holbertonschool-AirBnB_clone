#!/usr/bin/python3
"""
Write a program called console.py that contains the entry point of the
command interpreter:
"""
import cmd
import sys
import uuid
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ command line processor """
    prompt = '(hbnb) '
    our_classes = [
            "BaseModel", "User", "State", "City", "Amenity", "Place", "Review"
            ]

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
        except Exception:
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
            if (prompt_args[0] in self.our_classes) is True:
                # check if ID is missing
                print("** instance id missing **")
                return
            else:
                # prompt_args[0] is not a valid class name
                print("** class doesn't exist **")
                return

        try:
            if (prompt_args[0] in self.our_classes) is True:
                # string format: 'class.id'
                class_plus_id = '.'.join(prompt_args)
                objs = storage.all()
                # search in JSON file with the key 'class.id'
                print(objs[class_plus_id])
            else:
                print("** class doesn't exist **")
        except Exception:
            print("** no instance found **")

    def do_destroy(self, args):
        """ Deletes an instance based on the class name and id """
        prompt_args = args.split()

        if len(prompt_args) == 0:
            # check if class name is missing
            print("** class name missing **")
            return

        elif len(prompt_args) == 1:
            if (prompt_args[0] in self.our_classes) is True:
                # check if prompt_args[0] is a valid class name
                print("** instance id missing **")
                return
            else:
                # when prompt_args[0] is not a valid class name
                print("** class doesn't exist **")
                return

        try:
            if (prompt_args[0] in self.our_classes) is True:
                # string format: 'class.id'
                class_delete = '.'.join(prompt_args)
                objs = storage.all()
                # update JSON file with the key 'class.id' removed
                del objs[class_delete]
                storage.save()
            else:
                print("** class doesn't exist **")
        except Exception:
            print("** no instance found **")
            return

    def do_all(self, args):
        """ Prints all string representation of all instances based or not
        on the class name """
        prompt_args = args.split()

        if len(args) == 0:
            # check if the class name is valid or not
            objs = storage.all()
            all_objs = []

            for key, value in objs.items():
                string_objs = str(objs[key])
                all_objs.append(string_objs)
            print(all_objs)

        elif (prompt_args[0] in self.our_classes) is True:
            objs = storage.all()
            all_objs = []

            for key, value in objs.items():
                if prompt_args[0] in key:
                    string_objs = str(objs[key])
                    all_objs.append(string_objs)
            print(all_objs)

        else:
            # if prompt_args[0] is a non-valid class name
            print("** class doesn't exist **")
            return

    def do_update(self, args):
        """ Updates an instance based on the class name and id by adding
        or updating attribute"""
        prompt_args = args.split()

        if len(prompt_args) == 0:
            # when input == update, and no more args
            print("** class name missing **")
            return

        if (prompt_args[0] in self.our_classes) is True:
            # check if the class name is a valid value
            if len(prompt_args) < 2:
                print("** instance id missing **")
                return
        else:
            # when class name is not a valid value
            print("** class doesn't exist **")
            return

        key = str(prompt_args[0]) + '.' + str(prompt_args[1])
        objs = storage.all()

        if (key in objs) is False:
            # check if we have the key in our storage dict
            print("** no instance found **")
            return
        elif len(prompt_args) < 3:
            # in this case, the input only contain class name + id but
            # is not contain an attr
            print("** attribute name missing **")
            return
        elif len(prompt_args) < 4:
            # in this case, the input only contain class name + id + attr
            # but is not contain a value to be updated
            print("** value missing **")
            return

        # after all those error "if"s, we can proceed with the class update
        # ignoring all args [4:], in case of they exists
        # we used eval to cast to the correct attribute type
        objs[key].__dict__[prompt_args[2]] = eval(prompt_args[3])


if __name__ == "__main__":
    HBNBCommand().cmdloop()
