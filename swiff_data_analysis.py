import csv
from collections import Counter
from pathlib import Path

DATA_PATH = Path("data/swiff_2023_submissions.csv")
OUTPUT_PATH = Path("outputs/country_submission_counts.txt")


def count_submissions_by_country(csv_path):
    with open(csv_path, mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file)

        countries = [
            row[1].strip()
            for row in reader
            if len(row) > 1 and row[1].strip()
        ]

    return Counter(countries)


def main():
    OUTPUT_PATH.parent.mkdir(exist_ok=True)

    country_counts = count_submissions_by_country(DATA_PATH)

    with open(OUTPUT_PATH, "w", encoding="utf-8") as file:
        for country, count in country_counts.most_common():
            file.write(f"{country}: {count}\n")

    print(f"Saved results to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
