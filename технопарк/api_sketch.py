import requests
from urllib.parse import urljoin

id = 1391767
csrf_token = "ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8"


class ApiClient:

    csrf_token = None
    session = requests.Session()

    def set_csrf(self, csrf_token):
        self.csrf_token = csrf_token

    def delete_segment(self, segment_id):
        url = urljoin(
            "https://target.my.com/api/v2/remarketing/segments", (str(segment_id) + ".json"))
        headers = {
            'X-CSRFToken': self.csrf_token,
        }
        response = self.session.request("DELETE", url, headers=headers)
        return response

if __name__ == "__main__":
    client = ApiClient()
    client.set_csrf(csrf_token)
    resp = client.delete_segment(id)
    print(resp)
    print(resp.json())
    print(dir(resp))