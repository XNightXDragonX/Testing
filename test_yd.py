import unittest
import requests
import time


TOKEN = ""
BASE_URL = "https://cloud-api.yandex.net/v1/disk/resources"
HEADERS = {
    "Authorization": f"OAuth {TOKEN}",
    "Accept": "application/json"
}

class TestYandexDiskAPI(unittest.TestCase):
    def setUp(self):
        test_folder = "disk:/test_folder"
        requests.delete(BASE_URL, headers=HEADERS, params={"path": test_folder, "permanently": True})
        time.sleep(1)

    def tearDown(self):
        test_folder = "disk:/test_folder"
        requests.delete(BASE_URL, headers=HEADERS, params={"path": test_folder, "permanently": True})

    def test_create_folder_success(self):
        folder_path = "disk:/test_folder"
        response = requests.put(BASE_URL, headers=HEADERS, params={"path": folder_path})
        self.assertEqual(response.status_code, 201, f"Ожидался статус 201, получен - {response.status_code}")
        check_response = requests.get(BASE_URL, headers=HEADERS, params={"path": "disk:/"})
        self.assertEqual(check_response.status_code, 200)
        resources = check_response.json().get("_embedded", {}).get("items", [])
        folder_names = [item["name"] for item in resources]
        self.assertIn("test_folder", folder_names, "Папка не было создана.")

    def test_create_existing_folder(self):
        folder_path = "disk:/test_folder"
        requests.put(BASE_URL, headers=HEADERS, params={"path": folder_path})
        time.sleep(1)
        response = requests.put(BASE_URL, headers=HEADERS, params={"path": folder_path})
        self.assertEqual(response.status_code, 409, f"Ожидался статус 409, получен - {response.status_code}")
        error_data = response.json()
        self.assertIn(error_data.get("error"), ["DiskResourceAlreadyExistsError", "DiskPathPointsToExistentDirectoryError"], "Ожидалась ошибка существования")

    def test_create_folder_no_auth(self):
        folder_path = "disk:/test_folder"
        no_auth_headers = {"Accept": "application/json"}
        response = requests.put(BASE_URL, headers=no_auth_headers, params={"path": folder_path})
        self.assertEqual(response.status_code, 401, f"Ожидался статус 401, получен - {response.status_code}")
        error_data = response.json()
        self.assertEqual(error_data.get("error"), "UnauthorizedError", "Ожидалась ошибка UnauthorizedError")


if __name__ == "__main__":
    unittest.main()