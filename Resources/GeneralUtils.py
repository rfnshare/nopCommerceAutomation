import csv
import glob
import os
from datetime import datetime
import random
import string
from pathlib import Path


# Read current date
def read_date():
    return str(datetime.today().strftime("%Y-%m-%d"))


# function to read current date and time
def read_datetime():
    return str(datetime.today().strftime("%Y-%m-%d-%H-%M-%S"))


# function to read raw time
def get_raw_time():
    return str(datetime.today().strftime("%Y%d%H%M%S"))


def read_time():
    return str(datetime.today().strftime("%I-%M-%S-%p"))


def take_standard_screenshot(driver, file_name):
    driver.save_screenshot(file_name, False)


def generate_email():
    domain = "example.com"  # Change this to your desired domain
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{username}@{domain}"


def get_html_reports(report_type):
    reports = []
    if not report_type == "both":
        try:
            report = os.path.abspath(
                glob.glob(
                    f"../Reports/HTMLReports/{report_type}_report_html/{report_type}_*.html"
                )[-1]
            )
            reports.append(report)
        except Exception as e:
            print("Report not ready, Error", e)
    else:
        try:
            report1 = os.path.abspath(glob.glob(f"reports/api_report_html/*.html")[-1])
            report2 = os.path.abspath(glob.glob(f"reports/ui_report_html/*.html")[-1])
            # logs = os.path.abspath(glob.glob("logs/*.log")) # get logs
            reports.append(report1)
            reports.append(report2)
        except Exception as e:
            print("Reports are not ready, Error", e)
    return reports


# Global flag to track if CSV file has been created for the current run
csv_file_created = False
csv_file_path = None  # Define csv_file_path outside the function


def store_info(category, request_payload, response_payload, additional_info=None):
    global csv_file_created, csv_file_path

    # Check if CSV file has already been created for this run
    if not csv_file_created:
        # Get current date and time
        now = datetime.now()
        year_month_day = now.strftime("%Y_%m_%d")
        hour_minute_second = now.strftime("%H_%M_%S")

        # Create folder structure if it doesn't exist
        data_folder = Path(__file__).parent.parent / "Reports/Logs"
        folder_path = os.path.join(data_folder, year_month_day, "csv_logs")
        os.makedirs(folder_path, exist_ok=True)

        # Define CSV file path with minute and second precision
        csv_file_path = os.path.join(folder_path, f"logs_{hour_minute_second}.csv")

        fieldnames = ["Timestamp", "Category", "Request Payload", "Response Payload"]
        if additional_info:
            fieldnames.append("Additional Info")

        # Write data to CSV file
        with open(csv_file_path, mode='a', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)

            # Write header if file is empty
            if os.path.getsize(csv_file_path) == 0:
                writer.writeheader()

            # Set the flag to indicate that CSV file has been created for this run
            csv_file_created = True

    # Get current date and time
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Construct data to write
    data = {"Timestamp": timestamp, "Category": category, "Request Payload": request_payload,
            "Response Payload": response_payload}
    if additional_info:
        data["Additional Info"] = additional_info

    # Append data to CSV file
    with open(csv_file_path, mode='a', newline='') as file:
        fieldnames = list(data.keys())  # Define fieldnames here
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(data)
