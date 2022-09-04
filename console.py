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
from models.city import City
from models.state import State
from models.place import Place
from models.review import Review
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):
    """
    Class to implement the basic commands of
    the interpreter
    """
    classes_list = ['BaseModel', 'User', 'State',
                    'Place', 'City', 'Amenity', 'Review']

    prompt = '(hbnb) '

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
            print("** no instance found **")
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
            print("** no instance found **")
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

        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")

        else:
            for key, value in reloaded_json.items():
                if key.split(".")[0] == args[0]:
                    print(reloaded_json[key])

            return False

    def help_all(self):
        print(" Use all with or without arguments to print all attributes")

    def do_update(self, line):

        storage.reload()
        relooaded_json = storage.all()
        args = shlex.split(line)
        if len(args) < 1:
            print("** class name missing **")

        elif args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")

        elif len(args) < 2:
            print("** instance id missing **")

        elif (args[0]+"."+args[1]) not in relooaded_json.keys():
            print("** no instance found **")

        elif len(args) < 3:
            print("** attribute name missing **")

        elif len(args) < 4:
            print("** value missing **")

        elif (args[2]) in ["created_at", "id", "updated_at"]:
            print(f"** can't update {args[2]}")
            return False

        else:
            key = ".".join(args[2:4])
            key = args[0] + "." + args[1]
            if type(args[3]) in [int, float, str]:

                if type(args[3]) == int:
                    args[3] = int(args[3])

                elif type(args[0]) == float:
                    args[3] = float(args[3])

                elif type(args[3]) == str:
                    args[3] = str(args[3])

                setattr((relooaded_json[key]), args[2], args[3])
                storage.all()[key].save()
                return False
            else:
                print("** invalid value type **")
                return False

    def help_update(self):
        print("Use update to update attributes")

    def do_count(self, line):
        args = line.split()
        storage.reload()
        reloaded_json = storage.all()
        instance_count = 0

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return False

        for key in reloaded_json.keys():
            if line in key:
                instance_count += 1
        print(instance_count)
        instance_count = 0

    def help_count(self):
        print("Use count to print an instance count")

    def default(self, line):

        args = line.split(".")

        if args[0] in HBNBCommand.classes_list:
            eval(args[0])
            if len(args) > 1:
                if "show" in args[1]:
                    obj_id = args[1].split('"')[1]
                    msg = args[0] + " " + obj_id
                    self.do_show(msg)

                elif "destroy" in args[1]:
                    obj_id = args[1].split('"')[1]
                    msg = args[0] + " " + obj_id
                    self.do_destroy(msg)

                elif "all" in args[1]:
                    msg = args[0]
                    self.do_all(msg)

                elif "count" in args[1]:
                    msg = args[0]
                    self.do_count(msg)

                elif "update" in args[1]:
                    obj_id = args[1].split('"')[1]
                    tt = args[0] + " " + obj_id
                    if '{' in args[1]:
                        tmp = args[1].split('{')[1]
                        tmp = tmp.replace("})", "")
                        tmp = tmp.replace('"', "")
                        tmp = tmp.replace("'", "")
                        tmp = tmp.replace(",", "")
                        tmp = tmp.replace(":", "")
                        tmps = tmp.split()

                        key = []
                        value = []
                        for index in range(len(tmps)):
                            if index % 2 == 0:
                                key.append(tmps[index])
                            else:
                                value.append(tmps[index])

                        for index in range(len(key)):
                            msg = tt + " " + key[index] + ' "' +\
                                    value[index] + '"'
                            self.do_update(msg)
                    else:
                        attr_nm = args[1].split('"')[3]
                        attrval = args[1].split('"')[5]

                        self.do_update(tt + " " + attr_nm + " \"" +
                                       attrval + "\"")
        else:
            print("** class doesn't exist **")
            # print(f"*** Unknown syntax: {args[0]}")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
