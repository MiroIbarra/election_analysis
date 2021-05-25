# Election Analysis

## Project Overview

Seth, a Colorado Board of elections employee, has assigned the tasks below for completing the election audit of a recent local congressional election:

1. Calculate the total number of votes cast. 
2. Compile a complete list of candidates who received votes. 
3. Calculate the total number of votes each candidate received. 
4. Determine the winner of the election based on popular vote.

Additionally, the election commission requested further data to complete the audit:

1. Voter turnout for each county
2. Percentage of votes from each county out of the total count
3. The county with the highest voter turnout


## Resources
* Data source: election_results.csv
* Software: Python 3.8.8, Visual Code 1.55.2

## Summary
The analysis of the election indicate the following:

* There were 369,711 total votes in the election

![Screen Shot 2021-05-25 at 2 24 05 AM](https://user-images.githubusercontent.com/82562823/119474887-788c2700-bd01-11eb-872a-95c6d225a89c.png)

### County Results

* The county votes were:
	* Jefferson: 10.5% (38,855)
	* Denver: 82.8% (306,055)
	* Arapahoe: 6.7% (24,801)
* The largest county turnout:
	* Denver 

### Candidate Results

* The candidates were:
	* Casper Stockham 
	* Diana DeGette 
	* Raymon Anthony Doane
* The candidate results were:
	* Casper Stockham received 23% of the vote and 85,213 number of votes
	* Diana DeGette received 73.8% of the vote and 272,892 number of votes
	* Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes
* The winner of the election was:
	* Candidate Diana DeGette, who received 73.8% of the vote and 272,892 number of votes

## Election Audit Summary

Election committee, please consider how this script can be used for any election by using different text files and seeing how the function of this script remains the same. Please see snippets of the script attached to each task. Please note that it would be best practice to analyze the entire script to see how it all connects.  

**1. Calculating the total number of votes cast.**

After opening the csv file and allowing python to read the headers and rows, add function to count total votes. 

![Screen Shot 2021-05-25 at 3 46 31 AM](https://user-images.githubusercontent.com/82562823/119485345-cc037280-bd0b-11eb-804c-39190994c45d.png)

**2. Compile a complete list of candidates who received votes.**

An if statement can be used to identify candidates that received votes. 

![Screen Shot 2021-05-25 at 3 36 26 AM](https://user-images.githubusercontent.com/82562823/119483962-65ca2000-bd0a-11eb-8785-b610377b023c.png)

**3. Calculate the total number of votes each candidate received.**

First, vote count and percentage is retrieved from the csv file before determing the winning vote count, percentage and candidate, per images below. 

![Screen Shot 2021-05-25 at 3 12 36 AM](https://user-images.githubusercontent.com/82562823/119480995-10d8da80-bd07-11eb-975d-925a0dbb007d.png)

![Screen Shot 2021-05-25 at 3 13 17 AM](https://user-images.githubusercontent.com/82562823/119481074-2a7a2200-bd07-11eb-9bd4-147a863fa175.png)

**4. Determine the winner of the election based on popular vote.**

An if statement can be used to determine the winning coute count, winning percentage, and winning candidate.

![Screen Shot 2021-05-25 at 3 08 05 AM](https://user-images.githubusercontent.com/82562823/119480361-6eb8f280-bd06-11eb-8d3b-04142441032c.png)

Additional tasks assigned:

**1. Voter turnout for each county**

An if statement can be used to determine the winning county and the vote counts for each county.

![Screen Shot 2021-05-25 at 3 29 45 AM](https://user-images.githubusercontent.com/82562823/119483085-7928bb80-bd09-11eb-86c4-e27683729ec5.png)

**2. Percentage of votes from each county out of the total count**

A for loop was used  to retrieve the county from the county dictionary.

![Screen Shot 2021-05-25 at 3 23 15 AM](https://user-images.githubusercontent.com/82562823/119482286-8beec080-bd08-11eb-837d-f7aee12ae28c.png)

**3. The county with the highest voter turnout**

f"-------------------------\n" creates a line break that make the results look cleaner.

![Screen Shot 2021-05-25 at 3 17 10 AM](https://user-images.githubusercontent.com/82562823/119481549-b2602c00-bd07-11eb-83cb-627e46e489c2.png)

Please consider the following suggestions to modify the script:

* Besides having the largest voter turnout, also adding a function for determining lowest county turnover so that the election committee can spend more resources in the concerned county to encourage a higher voter turnout for the next election. 
	* Suggestion: add two new variables - lowest county turnout and lowest county count.
		* psuedocode: 3: track the smallest county and county voter turnout
		* lowest _ county_turnout = ""
		* lowest _ county_count = {}
* You may also consider sorting the county votes by descending order, per image below. 

![Screen Shot 2021-05-25 at 4 24 19 AM](https://user-images.githubusercontent.com/82562823/119489943-163b2280-bd11-11eb-9d9b-297f11ac6fdd.png)
