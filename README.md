#  Text Replacement Based on Configuration File

### Description
This project involves reading a configuration file containing unique key-value pairs and using those pairs to replace occurrences of the keys with their corresponding values in a specified text file. 
The program will output the modified lines to the console, sorted by the total number of characters replaced.

#### Goals
* Read a configuration file containing key-value pairs
* Read a text file where replacements will be made
* Replace all non-overlapping occurrences of the keys with their corresponding values
* Sort the modified lines by the total number of characters replaced, from most to least
* Output the resulting text to the console

To run the program, use the following command:
> python replace_text.py config.txt text.txt