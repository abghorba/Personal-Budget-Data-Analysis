# Personal-Budget

<h2>Setting Up</h2>
First, create your virtual environment:

    python3 -m venv env

Then activate your virtual environment and install dependencies:

    pip install --upgrade pip
    pip install -r requirements.txt

Activate your pre-commit hooks:

    pre-commit install

And you're good to go!

<h2>What my Budget Spreadsheet Looks Like:</h2>
In order to use this, you should be keeping track of your spending in a similar spreadsheet:

It is not necessary to follow the way I do my accounting there, but it is recommended to keep columns
B through G similar.

<h3>Link:</h3>
https://docs.google.com/spreadsheets/d/12sQdKVUK1-r6Wx17N34a6Qr6IMCCcL8-Bz_MTL_LS0A/edit?usp=sharing


<h2>Capabilities:</h2>

As of now we can do the following data analyses:

    1. Average over each year and the lifetime of the data
    2. Medians over each year and the lifetime of the data
    3. Variance over each year and the lifetime of the data
    4. Standard Deviations over each year and the lifetime of the data
    5. Linear Regression Analysis over each year and the lifetime of the data

It's completely up to you how you wish to use your own data.


<h2>Performance Measurements</h2>

I wanted to check how fast I can get each piece of the code running. You can check this out by
running:

    python performance.py

This might take several minutes, but will output a log with the time measurements for
a small, medium, large, and extra large data set.
