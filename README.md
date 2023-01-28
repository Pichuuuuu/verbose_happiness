# Bac Search

A Python script that uses the requests library to make HTTP requests to the website search-candidate.linternaute.com and extract information about a target individual.

## Usage

`vbh [target] [date (optional)]` 

**target** - The name of the target individual. The format should be 'nom' or 'nom prenom'.

**date** - The year of the target individual's bac exam. The format should be YYYY. If no date is provided, the script will search for the target's information from 2007 to 2021.

## Requirements

-   Python 3
-   requests
-   prettytable
-   json

## Installation

```
sudo python3 setup.py install

```

## Note

The oldest date available is 2007, so please keep that in mind when providing a date.

## Example


`vbh "John Doe" 2010` 

This will search for John Doe's bac information from 2010

## Output

```
+-------+-------+------+------------+----------+
|  Nom  | Ville | Date |  Diplome   | Académie |
+-------+-------+------+------------+----------+
| John  | Paris | 2010 | Scientific |    75    |
| Doe   |       |      |            |          |
+-------+-------+------+------------+----------+
```

## Disclaimer

This script is for educational purposes only and should not be used for any illegal activities. The author of this script is not responsible for any misuse of this script.
