#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

total_person = len(enron_data)
print "How many person? ", (total_person) # lenth of dict
print "How many features in each KEY? ", enron_data["SKILLING JEFFREY K"]
print "How many features in each KEY? ",len(enron_data["SKILLING JEFFREY K"])

POI = 0
for key in enron_data:
	if enron_data[key]["poi"] == 1:
		POI = POI + 1
print "How many POIs?", POI

# print enron_data.keys()  # PRINT ALL KEYS

print "What is the total value of the stock belonging to James Prentice? ", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "How many email messages do we have from Wesley Colwell to persons of interest? ", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "What is the value of stock options exercised by Jeffrey K Skilling? ", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

most_money = 0.0
name = ""
for key in enron_data:
	#print key, val
	if enron_data[key]["total_payments"] > most_money and enron_data[key]["total_payments"] != 'NaN' and key != "TOTAL":
		most_money = enron_data[key]["total_payments"]
		name = key
		# print key, enron_data[key]["total_payments"]
print "How much money did that person get? ", name, most_money

quantified_salary = 0
known_email_address = 0
for key in enron_data:
	if enron_data[key]["salary"] != "NaN":
		quantified_salary = quantified_salary + 1
	if enron_data[key]["email_address"] != "NaN":
		known_email_address = known_email_address + 1
print "How many folks in this dataset have a quantified salary? What about a known email address? ",quantified_salary,known_email_address

nan_total_payments = 0.0
for key in enron_data:
	if enron_data[key]["total_payments"] == 'NaN':
		nan_total_payments = nan_total_payments +1
print "How many people in the E+F dataset (as it currently exists) have "'NaN'" for their total payments? ", nan_total_payments, nan_total_payments/total_person

POI_nan_total_payments = 0.0
for key in enron_data:
	if enron_data[key]["poi"] == 1 and enron_data[key]["total_payments"] == 'NaN':
		POI_nan_total_payments += 1
print "How many POIs in the E+F dataset have NaN for their total payments? What percentage of POIs as a whole is this?", POI_nan_total_payments, POI_nan_total_payments/total_person


