import math
import random
import json

# This script generates dummy data for the development of the Lumiad dashboard. it is not real data and should not be treated as such

# List of departments and drugs
departments = [
    "Spoedeisende Hulp", "Chirurgie", "Geriatrie", "Kardiochirurgie",
    "Verloskunde", "Oncologie", "Pediatrie", "Psychiatrie"
]

drugs = [
    "morphine", "fentanyl", "ketamine", "propofol", "midazolam",
    "lorazepam", "dexmedetomidine", "naloxone", "pentobarbital", "remifentanil", "hydromorphone"
]

# Function to generate a random dataset
def generate_data(num_entries):
    data = []
    unique_ids = set()  # This set will keep track of all generated IDs to avoid duplicates

    while len(data) < num_entries:
        department = random.choice(departments)
        ward = f"ward {random.randint(1, 6)}"
        tempbed = random.randint(1, 16)
        if tempbed < 10:
            bed =  f'bed 0{tempbed}'
        else:
            bed = f'bed {tempbed}'
        pumpdrugname = random.choice(drugs)
        status = random.choice(["green", "orange", "red"])
        total_ml = random.randint(100, 600)
        remaining_ml = random.randint(0, total_ml)
        actRate = random.randint(0, 25)
        if actRate == 0:
            PumpCumTime = "Infusion not running"
            PumpRemTime = "Infusion not running"
        else:
            PumpCumTimeMinutesTotal = math.trunc(((total_ml - remaining_ml) / actRate) * 60)
            PumpCumHours = math.trunc(PumpCumTimeMinutesTotal / 60)
            if PumpCumTimeMinutesTotal % 60 == 0:
                CumMinutes = "00"
                PumpCumTime = f"{PumpCumHours}"  + ":" + f"{CumMinutes}"
            elif PumpCumTimeMinutesTotal % 60 < 10:
                pumpTempCumMinutes = math.trunc(PumpCumTimeMinutesTotal % 60)
                CumMinutes = "0" +f"{pumpTempCumMinutes}"
                PumpCumTime = f"{PumpCumHours}"  + ":" + f"{CumMinutes}"
            else:
                CumMinutes = math.trunc(PumpCumTimeMinutesTotal % 60)
                PumpCumTime = f"{PumpCumHours}"  + ":" + f"{CumMinutes}"


            PumpRemTimeMinutesTotal = math.trunc((remaining_ml / actRate) * 60)
            PumpRemHours = math.trunc(PumpRemTimeMinutesTotal / 60)
            if PumpRemTimeMinutesTotal % 60 == 0:
                Minutes = "00"
                PumpRemTime = f"{PumpRemHours}"  + ":" + f"{Minutes}"
            elif PumpRemTimeMinutesTotal % 60 < 10:
                pumpTempMinutes = math.trunc(PumpRemTimeMinutesTotal % 60)
                Minutes = "0" +f"{pumpTempMinutes}"
                PumpRemTime = f"{PumpRemHours}"  + ":" + f"{Minutes}"
            else:
                Minutes = math.trunc(PumpRemTimeMinutesTotal % 60)
                PumpRemTime = f"{PumpRemHours}"  + ":" + f"{Minutes}"




        id_number = random.randint(10000000, 99999999)
        Swversion = "3.154"
        Mversion = "1.3"

        # Ensure that the ID is unique
        if id_number not in unique_ids:
            unique_ids.add(id_number)
            data.append({
                "department": department,
                "ward": ward,
                "bed": bed,
                "drug": pumpdrugname,
                "status": status,
                "totalMl": total_ml,
                "remainingMl": remaining_ml,
                "mlPerHour": actRate,
                "timeRunning": PumpCumTime,
                "timeRemaining": PumpRemTime,
                "id": str(id_number),
                "softwareVersion": Swversion,
                "medicalLibraryVersion": Mversion
            })

    return data

# Generate 500 entries
generated_data = generate_data(500)

# Convert to JSON format
json_data = json.dumps(generated_data, indent=2)

# Print or save to a file
with open("generated_data_unique_with_time.json", "w") as file:
    file.write(json_data)

print("500 unique entries generated and saved to 'generated_data_unique_with_time.json'.")
