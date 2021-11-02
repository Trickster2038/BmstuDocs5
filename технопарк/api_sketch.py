import requests
from urllib.parse import urljoin
import json

id = 1401571
csrf_token = "ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8"
# cookie = "tmr_lvid=97eb38a6b9b3da5caa5eb1138bd057aa; tmr_lvidTS=1635089481459; _ga=GA1.3.760277518.1635089482; z=xzml6o34u0l1xxydaq430gdg9lkskfcs; _ga=GA1.2.760277518.1635089482; mrcu=327F61757C5331593AF21C11C851; p=ZAAAAEnzFAAA; s=rt=1|dpr=1.25; __utma=144340137.760277518.1635089482.1635089493.1635089493.1; __utmz=144340137.1635089493.1.1.utmcsr=target.my.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gid=GA1.3.735643551.1635841274; _gid=GA1.2.735643551.1635841274; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; mc=a79c9b0ab4ad7dae9f16238df3403402b265d13134383632; sdc=FUE7lcj4tRKsGOxY; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; _gcl_au=1.1.98288910.1635841303; _fbp=fb.1.1635841303613.1674862734; csrftoken=ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8; tmr_detect=0%7C1635841477183; tmr_reqNum=44"
cookie = "tmr_lvid=97eb38a6b9b3da5caa5eb1138bd057aa; tmr_lvidTS=1635089481459; _ga=GA1.3.760277518.1635089482; z=xzml6o34u0l1xxydaq430gdg9lkskfcs; _ga=GA1.2.760277518.1635089482; mrcu=327F61757C5331593AF21C11C851; p=ZAAAAEnzFAAA; s=rt=1|dpr=1.25; __utma=144340137.760277518.1635089482.1635089493.1635089493.1; __utmz=144340137.1635089493.1.1.utmcsr=target.my.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gid=GA1.3.735643551.1635841274; _gid=GA1.2.735643551.1635841274; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; mc=a79c9b0ab4ad7dae9f16238df3403402b265d13134383632; sdc=FUE7lcj4tRKsGOxY; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; _gcl_au=1.1.98288910.1635841303; _fbp=fb.1.1635841303613.1674862734; csrftoken=ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8; tmr_detect=0%7C1635846825207; tmr_reqNum=58; _gat_UA-54874995-1=1"


class ApiClient:

    csrf_token = None
    session = requests.Session()
    cookie = None

    def delete_segment(self, segment_id):
        # url = urljoin(
        # "https://target.my.com/api/v2/remarketing/segments", (str(segment_id) + ".json"))
        url = "https://target.my.com/api/v2/remarketing/segments/" + \
            str(segment_id) + ".json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Cookie': self.cookie
        }
        response = self.session.request("DELETE", url, headers=headers)
        return response

    def create_segment(self, name):
        params = "?fields=relations__object_type,relations__object_id,relations__params,relations__params__score,relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags"
        url = "https://target.my.com/api/v2/remarketing/segments.json" + params
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Cookie': self.cookie,
            'Content-Type': 'application/json'
        }
        payload = {
            "name": name,
            "pass_condition": 1,
            "relations": [
                {
                    "object_type": "remarketing_player",
                    "params": {
                        "type": "positive",
                        "left": 365,
                        "right": 0
                    }
                }
            ],
            "logicType": "or"
        }
        payload = json.dumps(payload)
        # print(payload)
        response = self.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    # def get_segments(self):
    #     url = "https://target.my.com/segments/segments_list"
    #     headers = {
    #         'Cookie': self.cookie
    #     }
    #     response = self.session.request("GET", url)
    #     return response

    # def get_segments(self):
    #     params = "?fields=id,created,name,campaigns_ids,users&limit=50&_=1635847108548"
    #     url = "https://target.my.com/api/v2/remarketing/campaign_lists.json" + params
    #     headers = {
    #         'Cookie': self.cookie
    #     }
    #     response = self.session.request("GET", url, headers=headers)
    #     return response

    def get_segments(self):
        params = "?fields=relations__object_type,relations__object_id,relations__params,relations__params__score,relations__id,relations_count,id,name,pass_condition,created,campaign_ids,users,flags&limit=500&_=1635848016171"
        url = "https://target.my.com/api/v2/remarketing/segments.json" + params
        headers = {
            'Cookie': self.cookie
        }
        response = self.session.request("GET", url, headers=headers)
        return response

    def check_segment_presence(self, name):
        segments = self.get_segments().json()
        for x in segments['items']:
            # print(x)
            if x['name'] == name:
                # print(x)
                return True
        return False

    # 204 code
    def delete_campaign(self, id):
        url = "https://target.my.com/api/v2/campaigns/mass_action.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Cookie': self.cookie,
            'Content-Type': 'application/json'
        }
        payload = [
            {
                "id": id,
                "status": "deleted"
            }
        ]
        payload = json.dumps(payload)
        response = self.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def get_campaigns(self):
        params = "?fields=id%2Cname%2Cdelivery%2Cprice%2Cbudget_limit%2Cbudget_limit_day%2Cpads_ots_limits%2Ccreated%2Cissues%2Cprices%2Cstatus%2Cpackage_id%2Cinterface_read_only%2Cread_only%2Cobjective%2Cuser_id%2Ctargetings__split_audience%2Ctargetings__pads%2Cenable_utm%2Cutm%2Cage_restrictions%2Cpackage_priced_event_type%2Cautobidding_mode&sorting=-id&limit=10&offset=0&_status__in=active&_user_id__in=11727528&_=1635850432320"
        url = "https://target.my.com/api/v2/campaigns.json" + params
        headers = {
            'Cookie': self.cookie
        }
        response = self.session.request("GET", url, headers=headers)
        return response

    def check_campaign_presence(self, name):
        campaigns = self.get_campaigns().json()
        for x in campaigns['items']:
            if x['name'] == name:
                return True
        return False



def test1():
    client = ApiClient()
    client.csrf_token = csrf_token
    client.cookie = cookie
    resp = client.delete_segment(id)
    print(resp)
    print(resp.headers)
    print(dir(resp))
    assert resp.status_code == 204


def test2():
    client = ApiClient()
    client.csrf_token = csrf_token
    client.cookie = cookie
    resp = client.create_segment("room 50541e3")
    print(resp)
    print(resp.json())
    # print(resp.headers)
    # print(dir(resp))
    assert resp.status_code == 200


def test3():
    client = ApiClient()
    client.csrf_token = csrf_token
    client.cookie = cookie
    resp = client.get_segments()
    # print(resp)
    # print(dir(resp))
    # print(resp.text)
    # print(resp.text.count("room 50541e3"))
    assert(client.check_segment_presence("room 50541e3"))

def test4():
    client = ApiClient()
    client.csrf_token = csrf_token
    client.cookie = cookie
    resp = client.delete_campaign(46498588)
    # print(resp.json())
    assert resp.status_code == 204

def test5():
    client = ApiClient()
    client.csrf_token = csrf_token
    client.cookie = cookie
    resp = client.get_campaigns()
    # print(resp.json())
    assert client.check_campaign_presence("Новая кампания 02.11.2021 13:30:20")

if __name__ == "__main__":
    test5()
