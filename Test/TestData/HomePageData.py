from Config.ApplicationSettings import ApplicationSettings
from Resources.ExcelUtils import *
import random
import string


def generate_email():
    domain = "example.com"  # Change this to your desired domain
    username = ''.join(random.choices(string.ascii_lowercase, k=8))
    return f"{username}@{domain}"


def read_test_data_from_excel(file, sheet_name, start_row, end_row, start_col, end_col):
    df = pd.read_excel(file, sheet_name, header=None)
    df = df.iloc[start_row-1:end_row, start_col-1:end_col]
    df.columns = ["dynamicemail", "password", "type", "dob", "companyName", "status", "msg"]
    if "dynamicemail" in df.columns:
        df["dynamicemail"] = df["dynamicemail"].apply(lambda x: generate_email())
    test_data = df.to_dict(orient="records")
    return test_data


class HomePageData:
    application_settings = ApplicationSettings()
    data = read_test_data_from_excel(
        application_settings.get_test_data_file_path(), sheet_name="login_reg", start_row=9, end_row=13, start_col=2, end_col=8
    )
    reg_data = data