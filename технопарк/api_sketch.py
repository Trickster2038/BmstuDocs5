import requests
from urllib.parse import urljoin

id = 1401571
csrf_token = "ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8"
cookie = "tmr_lvid=97eb38a6b9b3da5caa5eb1138bd057aa; tmr_lvidTS=1635089481459; _ga=GA1.3.760277518.1635089482; z=xzml6o34u0l1xxydaq430gdg9lkskfcs; _ga=GA1.2.760277518.1635089482; mrcu=327F61757C5331593AF21C11C851; p=ZAAAAEnzFAAA; s=rt=1|dpr=1.25; __utma=144340137.760277518.1635089482.1635089493.1635089493.1; __utmz=144340137.1635089493.1.1.utmcsr=target.my.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gid=GA1.3.735643551.1635841274; _gid=GA1.2.735643551.1635841274; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; mc=a79c9b0ab4ad7dae9f16238df3403402b265d13134383632; sdc=FUE7lcj4tRKsGOxY; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; _gcl_au=1.1.98288910.1635841303; _fbp=fb.1.1635841303613.1674862734; csrftoken=ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8; tmr_detect=0%7C1635841477183; tmr_reqNum=27"


class ApiClient:

    csrf_token = None
    session = requests.Session()
    cookie = None

    def delete_segment(self, segment_id):
        # url = urljoin(
            # "https://target.my.com/api/v2/remarketing/segments", (str(segment_id) + ".json"))
        url = "https://target.my.com/api/v2/remarketing/segments/" + str(segment_id) + ".json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Cookie': self.cookie
        }
        response = self.session.request("DELETE", url, headers=headers)
        return response


if __name__ == "__main__":
    client = ApiClient()
    client.csrf_token = csrf_token
    client.cookie = cookie
    resp = client.delete_segment(id)
    print(resp)
    print(resp.headers)
    print(dir(resp))
    assert resp.status_code == 204
