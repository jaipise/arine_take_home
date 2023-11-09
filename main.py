import datetime
from typing import Optional

# Question 1
def fizzbuzz() -> None:
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i %  3 == 0:
            print("Fizz")
        elif i %  5 == 0:
            print("Buzz")
        else:
            print(i)

# Question 2
def convert_to_float(input_str: str, default: float) -> float:
    try :
        return float(input_str)
    except ValueError:
        return default


# Question 3
def get_antihtn_meds(data_obj: dict) -> list:
    # Write a function that takes a data object as an argument and returns the list of all medications that have “antihtn” in their “drugGroup”. If there are no matching medications, return an empty list.

    result = []
    for med in data_obj["medications"]:
        if med["drugGroup"] and "antihtn" in med["drugGroup"]:
            result.append(med["brandName"])

    return result

# Question 4
def get_tablet_meds(data_obj: dict) -> list:
    result = []
    for med in data_obj["medications"]:
        if med["doseForm"] and "tablet" in med["doseForm"]:
            result.append(med["brandName"])

    return result

# Question 5
def get_latest_med_ndc(data_obj: dict) -> Optional[str]:
    # Write a function that takes a data object (see Sample Data Object below) as an argument and returns the “ndc9” value of the medication that was filled most recently. If there’s a tie, return any of the “ndc9” for medications filled on that day. If there are no medications, return None.
    if not data_obj["medications"]:
        return None

    result = ""
    curr_max = datetime.datetime.strptime("1900-01-01", '%Y-%m-%d')
    for med in data_obj["medications"]:
        if med["fills"]:
            tmp_max = max(med["fills"], key=lambda x: datetime.datetime.strptime(x["fillDate"], '%Y-%m-%d'))
            if datetime.datetime.strptime(tmp_max["fillDate"], '%Y-%m-%d') > curr_max:
                result = med["ndc9"]

    return result


sample = {
  "etlUpdated": "2012-12-21T23:58:00",
  "id": "123",
  "medications": [
    {
      "ndc9": "39017-0147",
      "brandName": "AMLODIPINE BESYLATE",
      "dosageStrength": "5",
      "dosageUnit": "mg",
      "doseForm": "tablet",
      "drugGroup": [
        "ccb",
        "antihtn"
      ],
      "route": "oral",
      "quantity": "90",
      "daysSupply": "90",
      "fills": [
        {
          "fillDate": "2012-02-18",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-05-16",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-08-06",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-11-01",
          "daysSupply": "90",
          "quantity": "90"
        }
      ],
      "display": "AMLODIPINE BESYLATE 5 MG",
      "unitsPerDay": "1",
      "dosePerDay": "5"
    },
    {
      "ndc9": "60505-2671",
      "brandName": "ATORVASTATIN CALCIUM",
      "genericName": "ATORVASTATIN CALCIUM",
      "dosageStrength": "80",
      "dosageUnit": "mg",
      "doseForm": "tablet, film coated",
      "drugGroup": [
        "statin",
        "azoleddi",
        "antilipid",
        "cms_statin",
        "cms_spc_statin"
      ],
      "route": "oral",
      "quantity": "90",
      "daysSupply": "90",
      "fills": [
        {
          "fillDate": "2012-04-10",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-07-09",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-10-09",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-01-03",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-04-01",
          "daysSupply": "90",
          "quantity": "90"
        }
      ],
      "unitsPerDay": "1",
      "dosePerDay": "80"
    },
    {
      "ndc9": "68382-0136",
      "brandName": "LOSARTAN POTASSIUM",
      "genericName": "LOSARTAN POTASSIUM",
      "dosageStrength": "50",
      "dosageUnit": "mg",
      "doseForm": "tablet, film coated",
      "drugGroup": [
        "arb",
        "antihtn",
        "cms_rasa"
      ],
      "route": "oral",
      "quantity": "90",
      "daysSupply": "90",
      "fills": [
        {
          "fillDate": "2012-02-25",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-05-25",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-07-14",
          "daysSupply": "90",
          "quantity": "90"
        },
        {
          "fillDate": "2012-10-15",
          "daysSupply": "90",
          "quantity": "90"
        }
      ],
      "unitsPerDay": "1",
      "dosePerDay": "50"
    },
    {
      "ndc9": "00378-0018",
      "brandName": "METOPROLOL TARTRATE",
      "genericName": "METOPROLOL TARTRATE",
      "dosageStrength": "25",
      "dosageUnit": "mg",
      "doseForm": "tablet, film coated",
      "drugGroup": [
        "antihtn",
        "betablocker"
      ],
      "route": "oral",
      "quantity": "180",
      "daysSupply": "90",
      "fills": [
        {
          "fillDate": "2012-02-06",
          "daysSupply": "90",
          "quantity": "180"
        },
        {
          "fillDate": "2012-05-16",
          "daysSupply": "90",
          "quantity": "180"
        },
        {
          "fillDate": "2012-08-13",
          "daysSupply": "90",
          "quantity": "180"
        },
        {
          "fillDate": "2012-11-12",
          "daysSupply": "90",
          "quantity": "180"
        },
        {
          "fillDate": "2012-02-16",
          "daysSupply": "90",
          "quantity": "180"
        }
      ],
      "unitsPerDay": "2",
      "dosePerDay": "50"
    }
  ],
  "resourceType": "cmr"
}
