#!/usr/bin/python3
"""
This is a simple module and it \
contains the entry point of the command interpreter
"""
import cmd
from models import storage
from models.app_classes import appClasses


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command line interpreter
    """
    prompt = '(hbnb) '

    def do_create(self, args):
        """create [ClassName]
Creates a new instance of [ClassName], saves it and prints the id.
        """
        model = args.split()
        if len(model) < 1:
            print('** class name missing **')
            return
        if model[0] in appClasses:
            instance = appClasses[model[0]]()
            instance.save()
            print(instance.id)
            return
        else:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        """show [ClassName] [id]
Prints the string representation of an instance based on the class name and id.
        """
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return

        model = args[0]
        id = args[1]
        if appClasses.get(model) is not None:
            print("** class doesn't exist **")
            return

        instances = storage.all()
        try:
            print(instances[f'{model}.{id}'])
        except KeyError:
            print('** no instance found **')
            return

    def do_destroy(self, args):
        """destroy [ClassName] [id]
Deletes an instance based on the class name and id
        """
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return

        model = args[0]
        id = args[1]
        if appClasses.get(model) is not None:
            print("** class doesn't exist **")
            return

        instances = storage.all()
        try:
            del instances[f'{model}.{id}']
            storage.save()

        except KeyError:
            print('** no instance found **')
            return

    def do_update(self, args):
        """update [ClassName] [id] [attribute_name] [\"attribute value\"]
Updates an instance based on the class name \
and id by adding or updating attribute
        """
        args = args.split()
        if len(args) == 0:
            print('** class name missing **')
            return
        elif len(args) == 1:
            print('** instance id missing **')
            return
        elif len(args) == 2:
            print('** attribute name missing **')
            return
        elif len(args) == 3:
            print('** value missing **')
            return

        model = args[0]
        id = args[1]
        attr = args[2]
        value = args[3].replace('"', '')
        if appClasses.get(model) is not None:
            print("** class doesn't exist **")
            return

        instances = storage.all()
        try:
            instance = instances[f'{model}.{id}']
            attrType = type(getattr(instance, attr))

            setattr(instance, attr, attrType(value))
            storage.save()

        except KeyError:
            print('** no instance found **')
            return

    def do_all(self, args):
        """all [ClassName]
Prints all string representation of all instances \
based or not on the class name.
        """
        args = args.split()
        instances = storage.all()
        if len(args) == 0:
            for k, v in instances.items():
                print(v)
            return
        elif not args[0] in appClasses:
            print("** class doesn't exist **")
            return
        model = args[0]
        for k, v in instances.items():
            if k.split('.')[0] == model:
                print(v)

    def default(self, args):
        args = args.split('.')
        model = args[0]
        method = args[1]
        instances = storage.all()

        if method == 'all()':
            classInstances = []
            for k, v in instances.items():
                if k.split('.')[0] == model:
                    classInstances.append(str(v))
            print(classInstances)
        elif method == 'count()':
            countInstances = 0
            for k, v in instances.items():
                if k.split('.')[0] == model:
                    countInstances = countInstances + 1
            print(countInstances)
        elif 'show' in method:
            id = method.split('\"')[1]
            try:
                print(instances[f'{model}.{id}'])
            except KeyError:
                print('** no instance found **')
                return
        elif 'destroy' in method:
            id = method.split('\"')[1]
            try:
                del instances[f'{model}.{id}']
            except KeyError:
                print('** no instance found **')
                return
        elif 'update' in method:
            attrs = method.split('(')[1]
            attrs = attrs.split(')')[0]
            attrs = attrs.split(',')

            id = attrs[0].replace('"', '').replace(' ', '', 1).replace("'", '')
            # attr = attrs[1].replace('"', '').replace(
            #     ' ', '', 1).replace("'", '')
            # value = attrs[2].replace('"', '').replace(
            #     ' ', '', 1).replace("'", '')
            attrs = attrs[1:]
            attrs = [attr.replace('"', '').replace(
                ' ', '', 1).replace("'", '') for attr in attrs]

            kwargs = {}
            # Check if is a dict or not
            if '{' in attrs[0] and '}' in attrs[-1]:
                for attr in attrs:
                    key, value = attr.split(':')
                    key = key.replace(' ', '', 1).replace(
                        "{", '').replace("}", '')
                    value = value.replace(' ', '', 1).replace(
                        "{", '').replace("}", '')
                    kwargs[key] = value
            else:
                key = attrs[0].replace('"', '').replace(
                    ' ', '', 1).replace("'", '')
                value = attrs[1].replace('"', '').replace(
                    ' ', '', 1).replace("'", '')
                kwargs[key] = value

            try:
                instance = instances[f'{model}.{id}']

                for k, v in kwargs.items():
                    attrType = type(getattr(instance, k))
                    setattr(instance, k, attrType(value))
                    storage.save()

            except KeyError:
                print('** no instance found **')
                return

    def emptyline(self):
        pass

    def do_quit(self, line):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, line):
        """Quit command to exit the program
        """

        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
