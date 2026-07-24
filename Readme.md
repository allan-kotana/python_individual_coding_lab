# Lab 1: Grade Evaluator & Archiver

This project calculates a student's final grade from `grades.csv` and archives the CSV file with a Bash script.

## Files

- `grade-evaluator.py`
- `grades.csv`
- `organizer.sh`
- `Readme.md`

## Run the Grade Evaluator

```bash
python3 grade-evaluator.py
```

When asked for the filename, enter:

```bash
grades.csv
```

## Run the Organizer

```bash
bash organizer.sh
```

The script moves `grades.csv` into the `archive` folder with a timestamped name, creates a new empty `grades.csv`, and adds a record to `organizer.log`.
