<p align="center">
<img src="https://camo.githubusercontent.com/a0c52a69dc410e983b8c63fa4aa57e83cb4157cd/68747470733a2f2f73332e616d617a6f6e6177732e636f6d2f696e7472616e65742d70726f6a656374732d66696c65732f686f6c626572746f6e7363686f6f6c2d6869676865722d6c6576656c5f70726f6772616d6d696e672b2f3236332f4842544e2d68626e622d46696e616c2e706e67" alt="hbnb" width=40% heigth=40% >
</p>

# AirBnB clone v1: the console
The **hbhn** is a project of Foundations: second trimester, of the career Software Engineering at Holberton School.The general objetive is create a full-stack clone of the recognized web application [AirBnB](https://www.airbnb.com/). 

The objetive of this first phase is **create our data model** to:
- manage correcly Python objects
- store and persist objects to a JSON file

The console is a tool to **manipulate and validate the powerful storage system** that we created. This storage engine will give us an abstraction between *My object* and *How they are stored and persisted*.

![HBNH_v1](https://user-images.githubusercontent.com/103126719/194949080-d2131133-6a4d-46d0-b008-bfda593a01da.png)
## Requirements
- All the files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- `README.md` file must exist
- All the files use the `pycodestyle (version 2.7.)` standard guidelines, including class and functions documentation
- All tests are execute using the `unittest` module

## The console main file
- **`console.py`** : contains the entry point of the command interpreter and specific methods to handle the input. **These are the commands you must use to work in the console**:

	| Function | Description | Usage example |
	| -- | -- | -- |
	| `do_quit` | To exit the progrmm | `quit` |
	| `do_EOF` | To exit the program handling End of File (ctrl + D) | ctrl + D |
	| `emptyline` | Do anything | empty line + enter |
	| `do_create` | Creates a new instance of BaseModel | `create BaseModel` |
	| `do_show` | Prints the string representation of an instance | `show Place` |
	| `do_destroy` | Deletes an instance based on the class name and id | `destroy User a1c42567-c2b9-43bc-9825-9b2edffb483f` |
	| `do_all` | Prints all string representation of all instances | `all` or `all Review`|
	| `do_update` | Updates an instance based on the class name and id by adding or updating attribute | `update User a1c42567-c2b9-43bc-9825-9b2edffb483f email "aibnb@mail.com"`|
	
#### Supported Classes:
The main class is `BaseModel` that defines all common attributes/methods to be inherited by other classes.

| Class name | Attributes |
| -- | -- |
| `BaseModel` | <ul><li>id (by UUID)</li><li>created_at (datetime when an instance is created)</li><li>updated_at (when an instance is created or updated)</li></ul> |
| `User` | <ul><li>email</li><li>password</li><li>first_name</li><li>last_name</li></ul> |
| `State` | <ul><li>name</li></ul> |
| `City` | <ul><li>state_id</li><li>name</li></ul> |
| `Amenity` | <ul><li>name</li></ul> |
| `Place` | <ul><li>city_id</li><li>user_id</li><li>name</li><li>description</li><li>number_rooms</li><li>number_bathrooms</li><li>max_guest</li><li>price_by_night</li><li>latitude</li><li>longitude</li><li>amenity_ids</li></ul> |
| `Review` | <ul><li>place_id</li><li>user_id</li><li>text</li></ul> |

## The storage system file
- **`file_storage.py`** : is the responsable to keep functional and safe all the data in the system via serializations of instances to a JSON file and deserializations of JSON file to instances. The file is found in *models* folder > *engine* folder. The methods of the class FileStorage are for internal use only. 
 
	| Function | Description |
	| -- | -- |
	| `all` | Return the dictionary of attributes of the instance |
	| `new` | To create a new instance |
	| `save` | Serializes the dictionary of attributes of an instance to the JSON file |
	| `reload` | Deserializes the JSON file to the dictionary of attributes of an instance |
	

## Execute the console [UPDATE]
Clone this repository:

    git clone https://github.com/mattowsh/holbertonschool-AirBnB_clone.git

Execute the console in interactive mode:

    $ ./console.py

Execute the console in non-interactive mode: [UPDATE IMAGE]

    $ echo "the_command_you_want" | ./console.py

Unit testing:

    python3 -m unittest discover tests

## Usage examples
### Non-interactive mode
```
$ echo "help" | ./console.py
(hbnb)
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
$
$ cat test_create
create BaseModel
$
$ cat test_create | ./console.py
(hbnb)cac68aef-e8eb-4379-8981-b6809ba01b72
$
```

### Interactive mode

```
$ ./console.py
(hbnb) help
Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
(hbnb)
(hbnb) create BaseModel
c384e626-0924-4fd7-910c-2b87af45215c
(hbnb) 
(hbnb) all
["[BaseModel] (c384e626-0924-4fd7-910c-2b87af45215c) {'id': 'c384e626-0924-4fd7-910c-2b87af45215c', 'created_at': datetime.datetime(2022, 10, 15, 15, 12, 22, 529850), 'updated_at': datetime.datetime(2022, 10, 15, 15, 12, 22, 529862)}"]
(hbnb)
(hbnb) destroy BaseModel c384e626-0924-4fd7-910c-2b87af45215c
(hbnb) show BaseModel c384e626-0924-4fd7-910c-2b87af45215c
** no instance found **
(hbnb)
(hbnb) quit
$
```

## Authors
[Luis Baute](https://www.linkedin.com/in/luis-baute-99305b188/)  
[Belén Matto](https://www.linkedin.com/in/mattobelen/) 

Montevideo, Uruguay.
