{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "55b99232-0248-4f18-add2-1c0be20481c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Your task is to create a Python script that analyzes the records to calculate each of the following:\n",
    "\n",
    "# Import the necessary libraries for reading csv files\n",
    "import pandas as pd\n",
    "\n",
    "\n",
    "# Set the path for the csv file\n",
    "pb = pd.read_csv (r\"/Users/NACA_MAC/Desktop/python-homework/PyBank.csv\")\n",
    "print(pb)\n",
    "\n",
    "# The total number of months included in the dataset.\n",
    "sum1 = df['Date'].sum()\n",
    "        \n",
    "\n",
    "# The net total amount of Profit/Losses over the entire period.\n",
    "add [1] - [-1]/2\n",
    "\n",
    "# The average of the changes in Profit/Losses over the entire period.\n",
    "\n",
    "\n",
    "# The greatest increase in profits (date and amount) over the entire period.\n",
    "\n",
    "\n",
    "# The greatest decrease in losses (date and amount) over the entire period.\n",
    "\n",
    "\n",
    "# Your resulting analysis should look similar to the following:\n",
    "\n",
    "Financial Analysis\n",
    "----------------------------\n",
    "Total Months: 86\n",
    "Total: $38382578\n",
    "Average  Change: $-2315.12\n",
    "Greatest Increase in Profits: Feb-2012 ($1926159)\n",
    "Greatest Decrease in Profits: Sep-2013 ($-2196167)\n",
    "\n",
    "Your final script should print the analysis to the terminal and export a text file with the results.\n",
    "\n",
    "\n",
    "import csv\n",
    "with open('/Users/NACA_MAC/Desktop/python-homework/PyBank.csv', 'r') as f:\n",
    "  next(f) \n",
    "\n",
    "#skips the first row\n",
    "  for row in csv.reader(f):\n",
    "    total = sum(int(row[1]))\n",
    "  print('The total is {}'.format(total))\n",
    "\n",
    "this is an update to PyBank Scrap"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
