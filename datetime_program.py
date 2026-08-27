from datetime import datetime

DOB_string = input("Enter your date of birth (dd/mm/yyyy): ")
DOB = datetime.strptime(DOB_string, "%d/%m/%Y")
today = datetime.now()
diff = today - DOB
days = diff.days
hours = diff.total_seconds() // 3600
minutes = diff.total_seconds() // 60
weeks = days // 7
print(f"\nYour age is: {days // 365} years")
print(f"You have lived for:")
print(f"  {days} days")
print(f"  {weeks} weeks")
print(f"  {int(hours):,} hours")
print(f"  {int(minutes):,} minutes")
