import requests
from HW28.test_data.env import url


def create_booking(payload):
    return requests.post(f"{url}/booking", json=payload)


def get_booking(booking_id):
    return requests.get(f"{url}/booking/{booking_id}")


def delete_booking(booking_id, token):
    headers = {"Cookie": f"token={token}"}
    return requests.delete(f"{url}/booking/{booking_id}", headers=headers)
