# Synopsis

The Airbnb clone project is all about creating a clone of the [Airbnb](https://www.airbnb.com/) Web Application.
Note: not all of the features of the Web App is included here.

### Usage
First, clone this repository to your local machine.
To launch the console application in interactive mode simply run:

```console.py ```
```
$ ./console.py 
(hbnb)
```

or to use the non-interactive mode run:

```echo "your-command-goes-here" | ./console.py ```

```
echo "help" | ./console.py
(hbnb) 
Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update
```

To exit the interpreter, input the EOF signal(`Ctrl-D`) or simple
type `quit`

```
$ ./console.py 
(hbnb) quit
$
```

# Features

## Command Interpreter

### Description


The Command Interpreter, for administrative purposes is used to manage the entire application from the command line. 
#### Objects
The objects implemented are;
+ ###### User
The user has attributes such as name, password, first name and last name, all managed by the interpreter.
+ ###### State
The state keeps the state names of users
+ ###### City
City keeps the name and state ids of users
+ ###### Amenity
This is where names of available amenities are managed
+ ###### Place
Place manges the name, City id, user id, description, number of rooms, number of bathrooms, price per night and location of various available places
+ ###### Review
Here is where reviewing is managed.
It keeps the place id, user id and the rewiew

#### Commands
The implemmented commands includes;
+ * **create**
  * Usage: `create <class>` 
  to create an instance of the class and save it to a json file, `file.json`.

```
$ ./console.py 
(hbnb) create User
6697cf9c-0812-446a-958f-d79fa6be7890
(hbnb) 
```
+ **show**
  * Usage: `show <class> <id>` or `<class>.show(<id>)`
to print an object using its name and id

```
(hbnb) show User 6697cf9c-0812-446a-958f-d79fa6be7890
[User] (6697cf9c-0812-446a-958f-d79fa6be7890) {'id': '6697cf9c-0812-446a-958f-d79fa6be7890', 'created_at': datetime.datetime(2022, 9, 4, 15, 55, 2, 233636), 'updated_at': datetime.datetime(2022, 9, 4, 15, 55, 2, 233674)}
(hbnb) 
```
+ **destroy**
  * Usage: `destroy <class> <id>` or `<class>.destroy(<id>)`
to delete/destroy the object

```
(hbnb) destroy User 6697cf9c-0812-446a-958f-d79fa6be7890
(hbnb) show User 6697cf9c-0812-446a-958f-d79fa6be7890
** no instance found **
(hbnb)
```
+ **all**
  * Usage: `all` or `all <class>` or `<class>.all()`
to display all instances of the class. If no class name is provided,it displays instances of all classes

```
(hbnb) all User
[User] (f7ae0637-e57d-4dab-963c-023504dc61dd) {'id': 'f7ae0637-e57d-4dab-963c-023504dc61dd', 'created_at': datetime.datetime(2022, 9, 4, 14, 38, 4, 819510), 'updated_at': datetime.datetime(2022, 9, 4, 14, 38, 4, 819554)}
[User] (a84f085c-257c-42ef-9ab2-e1311de6b7c2) {'id': 'a84f085c-257c-42ef-9ab2-e1311de6b7c2', 'created_at': datetime.datetime(2022, 9, 4, 15, 20, 57, 406036), 'updated_at': datetime.datetime(2022, 9, 4, 15, 20, 57, 406098)}
(hbnb) 

(hbnb) all
[BaseModel] (61bbf693-e4b9-4049-8502-3804c6aae141) {'id': '61bbf693-e4b9-4049-8502-3804c6aae141', 'created_at': datetime.datetime(2022, 9, 4, 13, 6, 53, 225816), 'updated_at': datetime.datetime(2022, 9, 4, 13, 6, 53, 225828)}
[City] (5fae427c-5e5f-4f00-86ae-4434152cd5f2) {'id': '5fae427c-5e5f-4f00-86ae-4434152cd5f2', 'created_at': datetime.datetime(2022, 9, 4, 13, 10, 53, 388473), 'updated_at': datetime.datetime(2022, 9, 4, 13, 10, 53, 388518)}
[User] (f7ae0637-e57d-4dab-963c-023504dc61dd) {'id': 'f7ae0637-e57d-4dab-963c-023504dc61dd', 'created_at': datetime.datetime(2022, 9, 4, 14, 38, 4, 819510), 'updated_at': datetime.datetime(2022, 9, 4, 14, 38, 4, 819554)}
[User] (a84f085c-257c-42ef-9ab2-e1311de6b7c2) {'id': 'a84f085c-257c-42ef-9ab2-e1311de6b7c2', 'created_at': datetime.datetime(2022, 9, 4, 15, 20, 57, 406036), 'updated_at': datetime.datetime(2022, 9, 4, 15, 20, 57, 406098)}
[City] (9e095ba9-67e1-4756-962f-4bb49ca7a370) {'id': '9e095ba9-67e1-4756-962f-4bb49ca7a370', 'created_at': datetime.datetime(2022, 9, 4, 15, 21, 21, 194449), 'updated_at': datetime.datetime(2022, 9, 4, 15, 21, 21, 194499)}
(hbnb) 


```
+ **count**
  * Usage: `count <class>` or `<class>.count()`
to count all instances of a class

```
(hbnb) User.count
2
(hbnb) 

```
+  **update**
  * Usage: `update <class> <id> <attribute name> "<attribute value>"` or
`<class>.update(<id>, <attribute name>, <attribute value>)` or `<class>.update(
<id>, <attribute dictionary>)`.
to update the an object.

```
(hbnb) update User f7ae0637-e57d-4dab-963c-023504dc61dd Name "Listowel"
(hbnb) show User f7ae0637-e57d-4dab-963c-023504dc61dd
[User] (f7ae0637-e57d-4dab-963c-023504dc61dd) {'id': 'f7ae0637-e57d-4dab-963c-023504dc61dd', 'created_at': datetime.datetime(2022, 9, 4, 14, 38, 4, 819510), 'updated_at': datetime.datetime(2022, 9, 4, 16, 8, 3, 602073), 'Name': 'Listowel'}
(hbnb) 
```

## Tests

The application was tested with Unittest which can be found in
the [tests](./tests) folder.

Use 
```
python3 -m unittest discover tests
 ```
to run all tests or use
```
python -m unittest tests/test_user.py
```
to run a specific test
