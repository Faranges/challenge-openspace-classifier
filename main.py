"""
main.py
Main script that loads data, creates the OpenSpace, and runs the organizer.
"""

import csv
from utils.openspace import OpenSpace


def load_names_from_csv(filename: str) -> list[str]:
    """Load a list of names from a CSV file with a column called 'Name'."""
    names = []
    with open(filename, newline="", encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if "Name" in row and row["Name"].strip():
                names.append(row["Name"].strip())
    return names


def main() -> None:
    # 1️⃣ Load names from the CSV file
    names = load_names_from_csv("new_colleagues.csv")
    print(f"Loaded {len(names)} names from CSV file.")

    # 2️⃣ Create the OpenSpace
    workspace = OpenSpace(number_of_tables=6)

    # 3️⃣ Organize and display seating
    workspace.organize(names)
    workspace.display()

    # 4️⃣ Save seating plan to a text file
    workspace.store("seating_plan.txt")




