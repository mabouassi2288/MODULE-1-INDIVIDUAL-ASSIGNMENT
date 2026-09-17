import csv

with open("/Users/monaabouassi/Library/Mobile Documents/com~apple~CloudDocs/BME 2315/MODULE 1 INDIVIDUAL ASSIGNMENT/MODULE-1-INDIVIDUAL-ASSIGNMENT/Metadata and Protein Data for Module 1.csv", newline="") as f:
        reader = csv.reader(f)
        headers = next(reader) # Get the first row
        for h in headers:
            print(h)

class Patient:  #STEP 1: Define a Class of "patient objects".

    all_patients = [] 

    #STEP 2: Make a "constructor" (__init__) that lists the different attributes that your want your patient objects to have.
    def __init__(self, patient_ID: int, age_at_death: int, highest_education: str, ABeta42: float, pTAU: str = "n/a", cognitive_status: str = "n/a"): 
        self.patient_ID = patient_ID
        self.age_at_death = age_at_death
        self.highest_education = highest_education
        self.ABeta42 = ABeta42
        self.pTAU = pTAU
        self.cognitive_status = cognitive_status

        # Append each new dog to the list upon initialization
        Patient.all_patients.append(self)

    #STEP 3: Make a "representer" (__repr__) that defines what is shown when you print a patient object.
    def __repr__(self):  
        return f"Patient ID {self.patient_ID}: ({self.age_at_death} | {self.highest_education} | ABeta42: {self.ABeta42} | pTAU: {self.pTAU} | {self.cognitive_status})" 

    def get_age_at_death(self): 
        return self.age_at_death

    @classmethod
    def sum_ages(cls):
        total = 0
        for patient in Patient.all_patients:
            total += patient.age_at_death
        return total

    @classmethod
    def get_patient(cls, patient_ID):
        for patient in Patient.all_patients:
            if patient_ID == patient.patient_ID: 
                return patient

    @classmethod
    def print_sorted_by(cls, attribute_name: str, reverse: bool = False):
        sorted_list = sorted(
            cls.all_patients,
            key=lambda patient: getattr(patient, attribute_name),
            reverse=reverse,
        )
        print(f"\n--- Patients sorted by '{attribute_name}' ---")
        for patient in sorted_list:
            print(patient)

    @classmethod
    def instantiate_from_csv(cls, filename: str):
        # your CSV loading code...
        pass

    #STEP 5: Sort and print the patients in order based on a specific attribute (e.g., age at diagnosis, highest education level, Thal score, etc.)
    @classmethod
    def filter(cls, list, patient_ID:str ="any", age_at_death:int ="any", highest_education:str ="any", ABeta42:float ="any", pTAU:str ="any", cognitive_status:str ="any"):
            all_patients = list
            remove_list = []
            attr_list = (
                        patient_ID,
                        age_at_death,
                        highest_education,
                        ABeta42,
                        pTAU,
                        cognitive_status
                        )
            attr_name = (
                        "patient_ID",
                        "age_at_death",
                        "highest_education",
                        "ABeta42",
                        "pTAU",
                        "cognitive_status"
                        )
            for attr in range(len(attr_list)):
                if attr_list[attr] != "any":
                    for patient in all_patients:
                        if getattr(patient,attr_name[attr]) != attr_list[attr]:
                            remove_list.append(patient)
                    all_patients = [patient for patient in all_patients if patient not in remove_list]
                    remove_list.clear()

            return all_patients

    #STEP 6: Make a class method to filter and print a sub-set of patients based on at least two specific attributes 
    @classmethod
    def print_patients_in_80s_low_abeta(cls, max_abeta: float = 50.0):
        filtered_patients = [
            patient for patient in cls.all_patients
            if 80 <= patient.age_at_death < 90 and patient.ABeta42 < max_abeta
        ]
        print(f"\n--- Patients who died in 80s with ABeta42 < {max_abeta} ---")
        for patient in filtered_patients:
            print(patient)
        return filtered_patients


