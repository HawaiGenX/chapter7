patients = {
    "P001": {
        "full_name": "Maria Rodriguez",
        "age": 48,
        "address": "1245 Coral Way, Miami, FL",
        "phone": "305-555-0142",
        "primary_doctor": "Dr. James Whitfield",
        "blood_type": "O+",
    },
    "P002": {
        "full_name": "David Chen",
        "age": 36,
        "address": "88 Brickell Ave, Miami, FL",
        "phone": "786-555-0198",
        "primary_doctor": "Dr. Priya Natarajan",
        "blood_type": "A-",
    },
    "P003": {
        "full_name": "Angela Thompson",
        "age": 70,
        "address": "4410 NW 7th St, Miami, FL",
        "phone": "305-555-0167",
        "primary_doctor": "Dr. James Whitfield",
        "blood_type": "B+",
    },
    "P004": {
        "full_name": "Jamal Brooks",
        "age": 18,
        "address": "2731 SW 22nd Ter, Miami, FL",
        "phone": "786-555-0121",
        "primary_doctor": "Dr. Sofia Alvarez",
        "blood_type": "AB+",
    },
    "P005": {
        "full_name": "Ethan O'Connor",
        "age": 59,
        "address": "15 Ocean Dr, Miami Beach, FL",
        "phone": "305-555-0186",
        "primary_doctor": "Dr. Priya Natarajan",
        "blood_type": "O-",
    },
}
#Create a list of keys of the main dictionary
id = list(patients.keys())

count = 0
#Printing patient's details
while count < len(id):
    patient_key = id[count]
    patient_details = patients[patient_key] #detail about each key(or dictionary) of the main dictionary
    print(f"\n{patient_key}")
    
    keys = list(patient_details.keys())
    k = 0
    while k < len(keys):
        print(f"{keys[k]}: {patient_details[keys[k]]}")
        
        k = k + 1
        
    count +=1
print()