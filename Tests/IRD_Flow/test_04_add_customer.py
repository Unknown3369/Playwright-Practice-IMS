from pathlib import Path
import os
import random
import uuid
import csv
import time
from Pages.Login import login
from Pages.Masters.add_customer import AddCustomer

BASE_DIR = Path(__file__).resolve().parents[2]
CUSTOMER_CSV = BASE_DIR / "customers.csv"

def random_name():
    return "IRD_Customer" # + uuid.uuid4().hex[:2]

def random_phone():
    return "98" + str(random.randint(10000000, 99999999))

def clear_csv(filename=CUSTOMER_CSV):
    filename = Path(filename)
    filename.parent.mkdir(parents=True, exist_ok=True)
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
            "Contact",
            "Email"
        ])
    print(f"CSV reset complete: {filename}")

def write_customer_to_csv(data, file_name=CUSTOMER_CSV):
    file_name = Path(file_name)
    file_name.parent.mkdir(parents=True, exist_ok=True)
    file_exists = file_name.exists()
    with file_name.open(
        mode="a",
        newline="",
        encoding="utf-8"
    ) as file:
        writer = csv.DictWriter(
            file,
            fieldnames=data.keys()
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(data)

    print(f"Customer data written to CSV: {file_name}")

def test_add_customer(page, config_data):
    username = config_data["username"]
    password = config_data["password"]

    try:
        login_page = login(page)
        login_page.perform_login(username, password)
    except Exception:
        print("Already Logged In")

    add_customer = AddCustomer(page)
    clear_csv(CUSTOMER_CSV)
    page.wait_for_load_state("networkidle")
    add_customer.open_add_customer()
    customer_name = random_name()
    customer_address = config_data["customer_address"]
    customer_contact = random_phone()

    add_customer.add_customer(
        customer_name,
        customer_address,
        customer_contact
    )

    customer_data = {
        "MainGroup": "SUPPLIER",
        "ACNAME": customer_name,
        "Address": customer_address,
        "Contact": customer_contact,
        "Email": ""
    }

    write_customer_to_csv(customer_data,CUSTOMER_CSV)

    print(f"CSV absolute path: {CUSTOMER_CSV}")
    print(f"CSV exists: {CUSTOMER_CSV.exists()}")
    print(f"CSV size: {CUSTOMER_CSV.stat().st_size} bytes")
    time.sleep(3)
    print(f"Customer '{customer_name}' added successfully!")