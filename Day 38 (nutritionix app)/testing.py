import requests
from get_stuff import get_stuff


USER_NAME = "c3cacb5163317a3fc90abc43cfd73795"
PROJ_NAME = "myWorkouts"
SHEET_NAME = "workouts"
SHEETY_EP = f"https://api.sheety.co/{USER_NAME}/{PROJ_NAME}/{SHEET_NAME}"


def sheety_get_row(row=1):
    credentials = get_stuff('sheety')
    header = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {credentials['token']}"
    }
    row_url = f"{SHEETY_EP}/{row}"

    return (requests.get(url=row_url, headers=header))


if __name__ == "__main__":

    r = sheety_get_row(2)
    print(r.json())
    print(r.text)
