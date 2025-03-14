import requests

class ApiGoogleMap:
    # Конструктор
    def __init__(self):
        self.base_url = 'https://rahulshettyacademy.com'
        self.key = '?key=qaclick123'
        self.post_resourse = '/maps/api/place/add/json'
        self.get_resourse = '/maps/api/place/get/json'
        self.put_resourse = '/maps/api/place/update/json'

    # Метод POST
    def create_new_location(self):
        post_url = self.base_url + self.post_resourse + self.key
        print(post_url)
        body = json_location = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            }, "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }
        result = requests.post(post_url, json=body)
        return result

    # Метод PUT
    def update_location(self, place_id, new_address):
        put_url = self.base_url + self.put_resourse + self.key
        print(put_url)
        json_put_location = {
            "place_id" : place_id,
            "address" : new_address,
            "key" : "qaclick123"
        }
        result = requests.put(put_url, json=json_put_location)
        return result

    # Метод GET
    def check_location(self, place_id):
        get_url = self.base_url + self.get_resourse + self.key + '&place_id=' + place_id
        print(get_url)
        result = requests.get(get_url)
        return result