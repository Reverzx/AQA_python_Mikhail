create_booking_payload = {
        "firstname": "Misha",
        "lastname": "Zakhodin",
        "totalprice": 100,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2013-02-23",
            "checkout": "2014-10-23"
        },
        "additionalneeds": "Breakfast"
    }

create_booking_payload_negative = {
        "totalprice": 0,
        "depositpaid": True,
        "bookingdates": {
            "checkout": "20ропо-10-23"
        },
        "additionalneeds": ""
    }

invalid_booking_id = 9999999
