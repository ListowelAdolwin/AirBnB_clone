#!/usr/bin/python3
"""
The entry point of a command line interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import json
import shlex
from models.user import User
# from models.city import City
# from models.state import State
# from models.place import Place
# from models.revier import Review


class HBNBCommand(cmd.Cmd):
    """
    Class to implement the basic commands of
    the interpreter
    """
    classes_list = ['BaseModel', 'User']

    prompt = '(hbnd) '

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Enter Cntrl-D or EOF to quit the interpreter\n")

    def do_quit(self, line):
        " quit to exit the interpreter "
        return True

    def help_quit(self):
        print("quit command to exit the interpreter\n")

    def emptyline(self):
        return False

    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return False

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False

        if len(args) >= 1:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def help_create(self):
        print("Use create to create an instance of a class\n")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return False

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        storage.reload()
        reloaded_json = storage.all()

        key = ".".join(args)
        if key not in reloaded_json.keys():
            print("** instance not found **")
            return False

        else:
            print(reloaded_json[key])
            return False

    def help_show(self):
        print("Use show to display an instance\n")

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return False

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        storage.reload()
        reloaded_json = storage.all()

        key = ".".join(args)
        if key not in reloaded_json:
            print("** instance not found **")
            return False

        else:
            del reloaded_json[key]
            storage.save()

    def help_destroy(self):
        print("Use destroy to destroy an object\n")

    def do_all(self, line):

        new_list = []
        storage.reload()
        reloaded_json = storage.all()

        if not line:
            for key in reloaded_json.keys():
                print(str(reloaded_json[key]))
            return False

        args = shlex.split(line)
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")

        else:
            for key, value in reloaded_json.items():
                if type(value) is eval(args[0]):
                    print(str(reloaded_json[key]))
                else:
                    return False

    def help_all(self):
        print(" Use all with or without arguments to print all attributes")

    def do_update(self, line):

        storage.reload()
        relooaded_json = storage.all()
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")

        elif len(args) < 2:
            print("** instance id is missing **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        elif args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")

        elif (args[0]+"."+args[1]) not in relooaded_json.keys():
            print("** instance doesn't exist")

        elif (args[2]) in ["created_at", "id", "updated_at"]:
            print(f"** can't update {args[2]}")
            return False

        else:
            key = ".".join(args[2:4])
            key = args[0] + "." + args[1]
            setattr((relooaded_json[key]), args[2], args[3])
            storage.all()[key].save()
            return False

    def help_update(self):
        print("Use update to update attributes")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
