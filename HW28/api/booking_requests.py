import requests
from HW28.test_data.env import url


def get_booking(booking_id):
    response = requests.get(f"{url}/booking/{booking_id}")
    return response


def delete_booking(booking_id, token):
    headers = {"Cookie": f"token={token}"}
    response = requests.delete(f"{url}/booking/{booking_id}", headers=headers)
    return response


def create_booking_invalid_payload():
    response = requests.post(f"{url}/booking", json={"invalid": "data"})
    return response
