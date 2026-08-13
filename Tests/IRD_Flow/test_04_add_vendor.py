from pathlib import Path
import csv
import random
import uuid

from Pages.Login import login
from Pages.Masters.add_vendor import AddVendor

BASE_DIR = Path(__file__).resolve().parents[2]
VENDOR_CSV = BASE_DIR / "vendors.csv"

def random_name():
    return "IRD_VENDOR_" + uuid.uuid4().hex[:2]

def random_vat_no():
    return str(random.randint(100000000, 999999999))

def random_email():
    return "Vend_" + uuid.uuid4().hex[:8] + "@test.com"

def random_mobile():
    return "98" + str(random.randint(10000000, 99999999))

def clear_csv(filename=VENDOR_CSV):
    filename = Path(filename)
    with filename.open(
        mode="w",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.writer(file)
        writer.writerow([
            "MainGroup",
            "ACNAME",
            "Address",
            "VATNO",
            "PARTYTYPE"
        ])
    print(f"CSV reset complete: {filename}")

def write_vendor_to_csv(data, file_name=VENDOR_CSV):

    file_name = Path(file_name)
    with file_name.open(
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "MainGroup",
                "ACNAME",
                "Address",
                "VATNO",
                "PARTYTYPE"
            ]
        )
        writer.writerow(data)
    print(f"Vendor data written to: {file_name}")

def test_create_vendor(page, config_data):

    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except Exception:
        print("Already logged in")

    clear_csv(VENDOR_CSV)
    vendor_page = AddVendor(page)
    vendor_page.open_add_vendor()
    vendor_name = random_name()
    vendor_address = config_data["vender_address"]
    vendor_vat = random_vat_no()
    vendor_email = random_email()
    vendor_mobile = random_mobile()

    vendor_page.add_vendor(
        vendor_name=vendor_name,
        vendor_address=vendor_address,
        vendor_vat_no=vendor_vat,
        vendor_email=vendor_email,
        vendor_mobile=vendor_mobile
    )

    vendor_data = {
        "MainGroup": "SUPPLIER",
        "ACNAME": vendor_name,
        "Address": vendor_address,
        "VATNO": vendor_vat,
        "PARTYTYPE": "Supplier"
    }

    write_vendor_to_csv(vendor_data,VENDOR_CSV)

    print(f"CSV path: {VENDOR_CSV}")
    print(f"CSV exists: {VENDOR_CSV.exists()}")
    print(f"CSV size: {VENDOR_CSV.stat().st_size} bytes")
    print(f"Vendor '{vendor_name}' created successfully!")