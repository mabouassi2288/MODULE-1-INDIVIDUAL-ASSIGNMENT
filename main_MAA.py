from patient_Mona import *

#STEP 7: Make a bar graph that compares the mean (+/- standard deviation) of an attribute that you are interested in between female and male patients 
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np
import statistics 

#STEP 4:  Create patient objects using the .csv fileDownload .csv file you were provided of patient demographic data and Luminex protein (amyloid beta and Tau) data. 
patient1 = Patient(1933004, 80, "Bachelors", 0.97, 1.90, "No dementia")
patient2 = Patient(2033020, 81, "High School", 45.73, 3.87, "Dementia")
patient3 = Patient(2033001, 82, "Bachelors", 2.74, 2.74, "No dementia")
patient4 = Patient(2033002, 97, "High School", 0.15, 2.62, "No dementia")
patient5 = Patient(2033004, 86, "Trade School/Tech School", 80.27, 7.41, "Dementia")
patient6 = Patient(2033005, 99, "High School", 16.16, 1.33, "No dementia")
patient7 = Patient(2033008, 92, "Graduate(PhD/Masters)", 101.83, 2.57, "No dementia")
patient8 = Patient(2033011, 93, "Bachelors", 60.51, 9.54, "Dementia")
patient9 = Patient(2033012, 91, "Graduate(PhD/Masters)", 47.71, 4.55, "No dementia")
patient10 = Patient(2033013, 94, "Trade School/Tech School", 24.78, 3.11, "No dementia")
patient11 = Patient(2033014, 82, "Graduate(PhD/Masters)", 16.14, 3.40, "No dementia")
patient12 = Patient(2033015, 88, "Graduate(PhD/Masters)", 27.61, 1.83, "Dementia")
patient13 = Patient(2033016, 93, "Trade School/Tech School", 21.27, 2.82, "Dementia")
patient14 = Patient(2033017, 69, "Trade School/Tech School", 209.43, 5.88, "Dementia")
patient15 = Patient(2033018, 81, "Graduate(PhD/Masters)", 1412.57, 5.11, "Dementia")


"""
dementia_patients = range(len(Patient.filter(Patient.all_patients, cognitive_status = "Dementia")))

print(f'Number of Dementia patients = {len(dementia_patients)}')

no_dementia_patients = range(
len(Patient.filter(Patient.all_patients, cognitive_status="No dementia"))
)

print(f"Number of No dementia patients = {len(no_dementia_patients)}")
"""

#STEP 5: Sort and print the patients in order based on a specific attribute (e.g., age at diagnosis, highest education level, Thal score, etc.)
Patient.print_sorted_by("age_at_death")
Patient.print_sorted_by("highest_education")
Patient.print_sorted_by("ABeta42") # Optional reverse sorting
Patient.print_sorted_by("pTAU")
Patient.print_sorted_by("cognitive_status")

#STEP 6: Make a class method to filter and print a sub-set of patients based on at least two specific attributes 
Patient.print_patients_in_80s_low_abeta(50.0) 

#STEP 7: Make a bar graph that compares the mean (+/- standard deviation) of an attribute that you are interested in between female and male patients 
    
    #to be sure that you're still creating your patient objects from the .csv data file. 
Patient.instantiate_from_csv("/Users/monaabouassi/Library/" \
"Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1 INDIVIDUAL ASSIGNMENT/MODULE-1-INDIVIDUAL-ASSIGNMENT/Metadata and Protein Data for Module 1.csv")

    #makes two empty lists that will be populated by the dementia versus no dementia patients, respectively
abeta_Dementia_patients = []
abeta_NoDementia_patients = []

    #populates these two lists with the ABeta42 values in each dementia vs no dementia group that you want to filter:
for patient in Patient.filter(Patient.all_patients, cognitive_status="Dementia"):
    abeta_Dementia_patients.append(patient.ABeta42)
for patient in Patient.filter(Patient.all_patients, cognitive_status="No dementia"):
    abeta_NoDementia_patients.append(patient.ABeta42)

    #defines the bars for the bar graph as the means of the ABeta42 values of dementia versus no dementia patients:
x_Dementia_patient_bar = statistics.mean(abeta_Dementia_patients)
x_NoDementia_patient_bar = statistics.mean(abeta_NoDementia_patients)

abeta_Dementia_patient_stdev = statistics.stdev(abeta_Dementia_patients)
abeta_NoDementia_patient_stdev = statistics.stdev(abeta_NoDementia_patients)

    #defines the standard deviations for the bar graph as the standard deviations of the ABeta42 values of the dementia versus no dementia patients
print(
    f"x_Dementia_patient_bar = {x_Dementia_patient_bar}, abeta_Dementia_patient_stdev {abeta_Dementia_patient_stdev}"
)
print(
    f"x_NoDementia_patient_bar = {x_NoDementia_patient_bar}, abeta_NoDementia_patient_stdev {abeta_NoDementia_patient_stdev}"
)

    #makes the bar graph (which will have two bars) and the standard deviation will be shown
Patient_cognitive_cols = ["Dementia", "No Dementia"]
mean_cognitive = [x_Dementia_patient_bar, x_NoDementia_patient_bar]
stdev_cognitive = [
    abeta_Dementia_patient_stdev,
    abeta_NoDementia_patient_stdev,
]
yerr = [np.zeros(len(mean_cognitive)), stdev_cognitive]

plt.bar(
    Patient_cognitive_cols,
    mean_cognitive,
    yerr=yerr,
    capsize=10,
    color=["blue", "orange"],
)

    #Labels the title and axes
plt.title("Average ABeta42 Levels by Cognitive Status")
plt.xlabel("Cognitive Status")
plt.ylabel("Average ABeta42 Level")
plt.show()