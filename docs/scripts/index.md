# Scripting in SeaTable

## Supported scripting languages and requirements

Scripts are used to interact with the data in a base. SeaTable supports scripts written in Python and JavaScript (JS).

JS code is executed directly in the user's browser, requires no authentication, and is used for simple data operations.

Python scripts, by contrast, are executed on a server or locally. As a consequence, Python scripts must authenticate against SeaTable Server. They are also suitable for more complex data processing scenarios.

JS and Python scripts can be composed and executed directly in a SeaTable base. 
![Screenshot of script icon in SeaTable](https://seatable.io/wp-content/uploads/2023/03/Anlegen-eines-Skriptes.jpg)

The execution of JS scripts in SeaTable has no requirements. 

To run Python scripts in SeaTable, the so-called [Python Pipeline](https://admin.seatable.io/installation/components/python-pipeline/) must be installed. You can also choose to run scripts [locally](https://developer.seatable.io/scripts/python/common_questions/#how-to-make-the-script-support-both-local-and-cloud-run). Local execution is convenient for development and debugging purposes. Scripts can also be easily integrated into larger projects.

## How to start?

Each chapter provides you with explanations about the available objects and methods. Multiple examples should help you to start immediately and get a feeling about the possibilities.

Here are some additional help articles from the [user manual](https://docs.seatable.io/?lang=auto) explaining how to create, execute and monitor a script in SeaTable:

- [Creating and deleting a script](https://seatable.io/docs/javascript-python/anlegen-und-loeschen-eines-skriptes/?lang=auto)
- [Run script manually, by button or by automation](https://seatable.io/en/docs/javascript-python/skript-manuell-per-schaltflaeche-oder-automation-ausfuehren/?lang=auto)
- [The execution log of scripts](https://seatable.io/en/docs/javascript-python/das-ausfuehrungslog-von-skripten/?lang=auto)
