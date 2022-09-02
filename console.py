#!/usr/bin/python3
"""
The entry point of a command line interpreter
"""

import cmd
from models.base_model import BaseModel
from models import storage
import json


class HBNBCommand(cmd.Cmd):
    """
    Class to implement the basic commands of
    the interpreter
    """
    classes_list = ['BaseModel']

    prompt = '(hbnd) '

    def do_EOF(self, line):
        return True

    def help_EOF(self):
        print("Enter Cntrl-D or EOF to quit the interpreter\n")

    def do_quit(self, line):
        return True
    
    def help_quit(self):
        print("quit command to exit the interpreter\n")

    def emptyline(self):
        pass
    
    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) == 1:
            obj = eval(args[0])()
            obj.save()
            print(obj.id)

    def help_create(self):
        print("Use create with a class name to create an instance of the class\n")

    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()
        
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return
        
        reloaded_json = storage.reload()
        print(reloaded_json)
        
        key = ".".join(args)
        if key not in reloaded_json.keys():
            print("** instance not found **")
            return
        else:
            print(reloaded_json[key])
            return
    
    def help_show(self):
        print("Use show with a class name and instance id to display the instance\n")
    
    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("*** class doesn't exist ***")
            return

        if len(args) < 2:
            print("*** instance id missing ***")
            return

        reloaded_json = storage.reload()
        key = ".".join(args)
        if key not in reloaded_json:
            print("*** instance not found ***")
            return

        else:
            del reloaded_json[key]
            storage.save()
            
    def help_destroy(self):
        print("Use destroy with a class name and instance id to delete the instance\n")

    def do_all(self, line):
        reloaded_json = storage.reload()

        if not line:
            for key in reloaded_json.keys():
                print(reloaded_json[key])
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
        else:
            for key in reloaded_json.keys():
                print(reloaded_json[key])
                
    def help_all(self):
        print(" Use help with or without arguments to print all attributes")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
