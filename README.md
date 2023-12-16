# Read Cookies.Sqlite

## Introduction

This is a basic program that outputs cookies data of firefox browser's cookies.sqlite based on website input from user.

## Requirements

- Python 3.6 or above
- Sqlite3
- Firefox Browser

## Usage

- Clone the repository
- Install the requirements using `pip install -r requirements.txt`
- Run the program
- Enter the website name
- Output will be displayed

### Note

The program will read from all the cookies.sqlite files present in the profiles folder of firefox in Windows.

## Current Status

~~- Right now, the current idea for the program has been decided. The code for the program will be written in python and will be available soon.~~ [Update: Code is available now]

## Structure of the program

- The program requires the user to input the website name.
- The program will then search for the website name in the database.
- If the website name is found, the program will output the cookies data of the website.
- The program will also save the output in a json file.

## Future Scope

- [x] Make the code more efficient by using functions.
- [x] Add a loop so that the user can input multiple website names.
- [x] Make it so that the cookies.sqlite file is automatically detected and the user doesn't have to input the path of the file.
- [ ] Give the user option whether to save the output in a json file or not.
- [ ] Following the above point, if the user wants to save the output of each website or update the json file, then the program should be able to do that.
- [ ] Maybe add the option to decode the cookies data.
- [ ] Give the user the option to choose which profile's cookies data to read.
