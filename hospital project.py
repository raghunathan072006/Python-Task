from pymongo import MongoClient
from pymongo.errors import DuplicateKeyError, ConnectionFailure

# MongoDB Connection

try:
    client = MongoClient("mongodb+srv://raghu07:raghu07@cluster0.kvvxso6.mongodb.net/?appName=Cluster0") 

    # Test connection
    client.admin.command("ping")

    db = client["HospitalDB"]

    patients = db["patients"]
    doctors = db["doctors"]

    # Prevent duplicate Patient IDs and Doctor IDs
    patients.create_index("patient_id", unique=True)
    doctors.create_index("doctor_id", unique=True)

    print("MongoDB connected successfully!")

except ConnectionFailure:
    print("MongoDB connection failed!")
    print("Please start MongoDB Server.")
    exit()


#~~~~~~~~~~~~~~~~~~~~~~~~~
# PATIENT MANAGEMENT
# ************************


# 1. Add Patient
def add_patient():

    print("\n----- Add New Patient -----")

    patient_id = input("Enter Patient ID: ").strip()
    patient_name = input("Enter Patient Name: ").strip()
    age_input = input("Enter Age: ").strip()
    gender = input("Enter Gender: ").strip()
    phone = input("Enter Phone Number: ").strip()
    address = input("Enter Address: ").strip()
    disease = input("Enter Disease/Health Issue: ").strip()

    # Validate empty fields
    if not patient_id or not patient_name:
        print("Patient ID and Name cannot be empty!")
        return

    # Validate age
    try:
        age = int(age_input)

        if age <= 0 or age > 120:
            print("Please enter a valid age!")
            return

    except ValueError:
        print("Age must be a number!")
        return

    patient = {
        "patient_id": patient_id,
        "patient_name": patient_name,
        "age": age,
        "gender": gender,
        "phone": phone,
        "address": address,
        "disease": disease
    }

    try:
        patients.insert_one(patient)
        print("Patient added successfully!")

    except DuplicateKeyError:
        print("Patient ID already exists!")


# 2. View All Patients
def view_patients():

    print("\n----- All Patients -----")

    patient_list = patients.find()

    found = False

    for patient in patient_list:

        found = True

        print("\nPatient ID:", patient["patient_id"])
        print("Patient Name:", patient["patient_name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Phone:", patient["phone"])
        print("Address:", patient["address"])
        print("Disease:", patient["disease"])
        print("-" * 35)

    if not found:
        print("No patient records found!")


# 3. Search Patient
def search_patient():

    print("\n----- Search Patient -----")

    patient_id = input("Enter Patient ID: ").strip()

    patient = patients.find_one({
        "patient_id": patient_id
    })

    if patient:

        print("\nPatient Found!")
        print("Patient ID:", patient["patient_id"])
        print("Patient Name:", patient["patient_name"])
        print("Age:", patient["age"])
        print("Gender:", patient["gender"])
        print("Phone:", patient["phone"])
        print("Address:", patient["address"])
        print("Disease:", patient["disease"])

    else:
        print("Patient record not found!")


# 4. Update Patient
def update_patient():

    print("\n----- Update Patient -----")

    patient_id = input("Enter Patient ID to update: ").strip()

    patient = patients.find_one({
        "patient_id": patient_id
    })

    if not patient:
        print("Patient record not found!")
        return

    print("Press Enter to keep the existing value.")

    name = input(
        f"Patient Name [{patient['patient_name']}]: "
    ).strip()

    age_input = input(
        f"Age [{patient['age']}]: "
    ).strip()

    gender = input(
        f"Gender [{patient['gender']}]: "
    ).strip()

    phone = input(
        f"Phone [{patient['phone']}]: "
    ).strip()

    address = input(
        f"Address [{patient['address']}]: "
    ).strip()

    disease = input(
        f"Disease [{patient['disease']}]: "
    ).strip()

    update_data = {}

    if name:
        update_data["patient_name"] = name

    if age_input:
        try:
            age = int(age_input)

            if age <= 0 or age > 120:
                print("Invalid age!")
                return

            update_data["age"] = age

        except ValueError:
            print("Age must be a number!")
            return

    if gender:
        update_data["gender"] = gender

    if phone:
        update_data["phone"] = phone

    if address:
        update_data["address"] = address

    if disease:
        update_data["disease"] = disease

    if update_data:

        patients.update_one(
            {"patient_id": patient_id},
            {"$set": update_data}
        )

        print("Patient details updated successfully!")

    else:
        print("No changes made.")


# 5. Delete Patient
def delete_patient():

    print("\n----- Delete Patient -----")

    patient_id = input("Enter Patient ID to delete: ").strip()

    patient = patients.find_one({
        "patient_id": patient_id
    })

    if not patient:
        print("Patient record not found!")
        return

    confirm = input(
        "Are you sure you want to delete this patient? (yes/no): "
    ).lower()

    if confirm == "yes":

        patients.delete_one({
            "patient_id": patient_id
        })

        print("Patient deleted successfully!")

    else:
        print("Delete operation cancelled.")



# DOCTOR MANAGEMENT


# 1. Add Doctor
def add_doctor():

    print("\n----- Add New Doctor -----")

    doctor_id = input("Enter Doctor ID: ").strip()
    doctor_name = input("Enter Doctor Name: ").strip()
    specialization = input("Enter Specialization: ").strip()
    phone = input("Enter Phone Number: ").strip()
    fee_input = input("Enter Consultation Fee: ").strip()

    if not doctor_id or not doctor_name:
        print("Doctor ID and Name cannot be empty!")
        return

    # Validate consultation fee
    try:
        consultation_fee = float(fee_input)

        if consultation_fee < 0:
            print("Fee cannot be negative!")
            return

    except ValueError:
        print("Consultation fee must be a number!")
        return

    doctor = {
        "doctor_id": doctor_id,
        "doctor_name": doctor_name,
        "specialization": specialization,
        "phone": phone,
        "consultation_fee": consultation_fee
    }

    try:
        doctors.insert_one(doctor)
        print("Doctor added successfully!")

    except DuplicateKeyError:
        print("Doctor ID already exists!")


# 2. View All Doctors
def view_doctors():

    print("\n----- All Doctors -----")

    doctor_list = doctors.find()

    found = False

    for doctor in doctor_list:

        found = True

        print("\nDoctor ID:", doctor["doctor_id"])
        print("Doctor Name:", doctor["doctor_name"])
        print("Specialization:", doctor["specialization"])
        print("Phone:", doctor["phone"])
        print("Consultation Fee:", doctor["consultation_fee"])
        print("-" * 35)

    if not found:
        print("No doctor records found!")


# 3. Search Doctor
def search_doctor():

    print("\n----- Search Doctor -----")

    doctor_id = input("Enter Doctor ID: ").strip()

    doctor = doctors.find_one({
        "doctor_id": doctor_id
    })

    if doctor:

        print("\nDoctor Found!")
        print("Doctor ID:", doctor["doctor_id"])
        print("Doctor Name:", doctor["doctor_name"])
        print("Specialization:", doctor["specialization"])
        print("Phone:", doctor["phone"])
        print("Consultation Fee:", doctor["consultation_fee"])

    else:
        print("Doctor record not found!")


# 4. Update Doctor
def update_doctor():

    print("\n----- Update Doctor -----")

    doctor_id = input("Enter Doctor ID to update: ").strip()

    doctor = doctors.find_one({
        "doctor_id": doctor_id
    })

    if not doctor:
        print("Doctor record not found!")
        return

    print("Press Enter to keep the existing value.")

    name = input(
        f"Doctor Name [{doctor['doctor_name']}]: "
    ).strip()

    specialization = input(
        f"Specialization [{doctor['specialization']}]: "
    ).strip()

    phone = input(
        f"Phone [{doctor['phone']}]: "
    ).strip()

    fee_input = input(
        f"Consultation Fee [{doctor['consultation_fee']}]: "
    ).strip()

    update_data = {}

    if name:
        update_data["doctor_name"] = name

    if specialization:
        update_data["specialization"] = specialization

    if phone:
        update_data["phone"] = phone

    if fee_input:

        try:
            fee = float(fee_input)

            if fee < 0:
                print("Fee cannot be negative!")
                return

            update_data["consultation_fee"] = fee

        except ValueError:
            print("Consultation fee must be a number!")
            return

    if update_data:

        doctors.update_one(
            {"doctor_id": doctor_id},
            {"$set": update_data}
        )

        print("Doctor details updated successfully!")

    else:
        print("No changes made.")


# 5. Delete Doctor
def delete_doctor():

    print("\n----- Delete Doctor -----")

    doctor_id = input("Enter Doctor ID to delete: ").strip()

    doctor = doctors.find_one({
        "doctor_id": doctor_id
    })

    if not doctor:
        print("Doctor record not found!")
        return

    confirm = input(
        "Are you sure you want to delete this doctor? (yes/no): "
    ).lower()

    if confirm == "yes":

        doctors.delete_one({
            "doctor_id": doctor_id
        })

        print("Doctor deleted successfully!")

    else:
        print("Delete operation cancelled.")


# PATIENT MENU

def patient_menu():

    while True:

        print("\n========== PATIENT MANAGEMENT ==========")
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Search Patient")
        print("4. Update Patient")
        print("5. Delete Patient")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_patient()

        elif choice == "2":
            view_patients()

        elif choice == "3":
            search_patient()

        elif choice == "4":
            update_patient()

        elif choice == "5":
            delete_patient()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Try again.")


# DOCTOR MENU

def doctor_menu():

    while True:

        print("\n========== DOCTOR MANAGEMENT ==========")
        print("1. Add Doctor")
        print("2. View All Doctors")
        print("3. Search Doctor")
        print("4. Update Doctor")
        print("5. Delete Doctor")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_doctor()

        elif choice == "2":
            view_doctors()

        elif choice == "3":
            search_doctor()

        elif choice == "4":
            update_doctor()

        elif choice == "5":
            delete_doctor()

        elif choice == "6":
            break

        else:
            print("Invalid choice! Try again.")


# MAIN MENU

def main():

    while True:

        print("\n========================================")
        print("       HOSPITAL MANAGEMENT SYSTEM")
        print("========================================")

        print("1. Patient Management")
        print("2. Doctor Management")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            patient_menu()

        elif choice == "2":
            doctor_menu()

        elif choice == "3":
            print("Thank you for using Hospital Management System!")
            client.close()
            break

        else:
            print("Invalid choice! Try again.")


# Program starts here
if __name__ == "__main__":
    main()