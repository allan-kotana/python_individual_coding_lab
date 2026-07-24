#!/bin/bash

if [ ! -f "grades.csv" ]; then
    echo "grades.csv was not found."
    exit 1
fi

if [ ! -d "archive" ]; then
    mkdir archive
fi

timestamp=$(date +"%Y%m%d-%H%M%S")
new_file="grades_$timestamp.csv"

mv grades.csv "archive/$new_file"
touch grades.csv

echo "$timestamp | grades.csv | archive/$new_file" >> organizer.log
echo "Archived grades.csv as archive/$new_file"
