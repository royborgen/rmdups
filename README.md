# rmdups 1.0 - Remove duplicates 
A Python script that reads a file, removed duplicate lines and outputs results. 

## Usage
The script needs a filename as argument

```
Usage: rmdups [FILENAME]
Reads a file and removes duplicate lines.
Filename must be provided as argument.

Optional arguments:
    -v, --version   Displays version information and exits
        --help      Displays this helptext

Example:
rmdups test.txt         Reads test.txt and removes duplicate lines
```

## Example
Let's say we provide a file with the following content as argument: 
```
Fred
Jeff
Jeff
Jeff
Lisa
Lisa
Bobby
```

Script will output: 
```
Fred
Jeff
Lisa
Bobby
```

## Requirements
- Python 3 
- os library installed (standard with Python 3) 
- sys library installed (standard with Python 3) 
