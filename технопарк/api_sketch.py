import requests
from urllib.parse import urljoin
import json
import urllib.parse

from requests.api import request
from templates.jsons import CampagnJsons
from requests.cookies import cookiejar_from_dict

id = 1401571
csrf_token = "ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8"
# cookie = "tmr_lvid=97eb38a6b9b3da5caa5eb1138bd057aa; tmr_lvidTS=1635089481459; _ga=GA1.3.760277518.1635089482; z=xzml6o34u0l1xxydaq430gdg9lkskfcs; _ga=GA1.2.760277518.1635089482; mrcu=327F61757C5331593AF21C11C851; p=ZAAAAEnzFAAA; s=rt=1|dpr=1.25; __utma=144340137.760277518.1635089482.1635089493.1635089493.1; __utmz=144340137.1635089493.1.1.utmcsr=target.my.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gid=GA1.3.735643551.1635841274; _gid=GA1.2.735643551.1635841274; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; mc=a79c9b0ab4ad7dae9f16238df3403402b265d13134383632; sdc=FUE7lcj4tRKsGOxY; _gac_UA-54874995-1=1.1635841276.EAIaIQobChMIq4Coz5_58wIVD2YYCh1i1g13EAAYASAAEgKEhvD_BwE; _gcl_au=1.1.98288910.1635841303; _fbp=fb.1.1635841303613.1674862734; csrftoken=ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8; tmr_detect=0%7C1635841477183; tmr_reqNum=44"
cookie = "tmr_lvid=97eb38a6b9b3da5caa5eb1138bd057aa; tmr_lvidTS=1635089481459; _ga=GA1.3.760277518.1635089482; _ga=GA1.2.760277518.1635089482; mrcu=327F61757C5331593AF21C11C851; p=ZAAAAEnzFAAA; s=rt=1|dpr=1.25; __utma=144340137.760277518.1635089482.1635089493.1635089493.1; __utmz=144340137.1635089493.1.1.utmcsr=target.my.com|utmccn=(referral)|utmcmd=referral|utmcct=/; _gcl_au=1.1.98288910.1635841303; _fbp=fb.1.1635841303613.1674862734; csrftoken=ut3qTnrRuyuaPXIsosd2EGMntCxRj9tP9CRbA7IXOtnZrgkHDvaUMnzmZyKsbEN8; _gid=GA1.3.809879900.1636105958; _gac_UA-54874995-1=1.1636105958.EAIaIQobChMIgseu0fmA9AIVCrwYCh3hTAGgEAAYASAAEgIvK_D_BwE; z=2tkxarhzybi6327ro1ovf0gid007j3zn; _gid=GA1.2.809879900.1636105958; _gac_UA-54874995-1=1.1636105958.EAIaIQobChMIgseu0fmA9AIVCrwYCh3hTAGgEAAYASAAEgIvK_D_BwE; _gat_UA-54874995-1=1; mc=6aed28cb93397ebfb0fbc5dbcc5ec684b265d13134383632; sdc=HR0PsMYz9la3Op5U; tmr_reqNum=236; tmr_detect=0%7C1636115468172"


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
        print("Campaings list response: ")
        print(response)
        print(response.headers)
        return response

    def check_campaign_presence(self, name):
        campaigns = self.get_campaigns().json()
        for x in campaigns['items']:
            if x['name'] == name:
                return True
        return False

    # .json() returns id
    def create_campaign(self, name):
        payload = CampagnJsons.DEFAULT
        payload['name'] = name
        payload = json.dumps(payload)
        url = "https://target.my.com/api/v2/campaigns.json"
        headers = {
            'X-CSRFToken': self.csrf_token,
            'Cookie': self.cookie,
            'Content-Type': 'application/json'
        }
        response = self.session.request(
            "POST", url, headers=headers, data=payload)
        return response

    def get_token(self, resp):
        headers = resp.headers['Set-Cookie'].split(';')
        token_header = [h for h in headers if 'csrftoken' in h]
        if not token_header:
            raise Exception('No csrftoken header found in main page headers')

        token_header = token_header[0]
        token = token_header.split('=')[-1]
        return token

    def login2(self, username, passw):
        params = "?lang=ru&nosavelogin=0"
        url = "https://auth-ac.my.com/auth" + params
        headers = {
            'Content-Type': 'application/json',   
            'Referer': 'https://target.my.com/'
        }
        username = urllib.parse.quote(username.encode('utf-8'))
        passw = urllib.parse.quote(passw.encode('utf-8'))
        payload = f"email={username}&password={passw}&continue=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1%23email&failure=https%3A%2F%2Faccount.my.com%2Flogin%2F"
        payload = payload.encode('utf-8')
        response = self.session.request(
            "POST", url, headers=headers, data=payload, allow_redirects=False)
        cookie = response.headers['Set-Cookie']
        self.cookie += "; " + cookie
        while 'Location' in response.headers:
            url = response.headers['Location']
            response = self.session.request(
            "GET", url, allow_redirects=False)
            if 'Set-Cookie' in response.headers:
                cookie = response.headers['Set-Cookie']
                self.cookie += "; " + cookie

        responseCSRF = self.session.request(
            "GET", "https://target.my.com/csrf")

        cookieCSRF = responseCSRF.headers['Set-Cookie']
        self.cookie += "; " + cookieCSRF
        self.csrf_token = cookieCSRF.split("=")[1].split(";")[0]
        return response
            


    def login(self, username, passw):
        params = "?lang=ru&nosavelogin=0"
        url = "https://auth-ac.my.com/auth" + params
        headers = {
            'Content-Type': 'application/json', #'application/x-www-form-urlencoded',  
            'Referer': 'https://target.my.com/'
        }
        username = urllib.parse.quote(username.encode('utf-8'))
        passw = urllib.parse.quote(passw.encode('utf-8'))
        payload = f"email={username}&password={passw}&continue=https%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1%23email&failure=https%3A%2F%2Faccount.my.com%2Flogin%2F"
        payload = payload.encode('utf-8')
        # print(payload)
        response = self.session.request(
            "POST", url, headers=headers, data=payload, allow_redirects=False)

        print(dir(response.request))

        cookie1 = response.headers['Set-Cookie']
        self.cookie += "; " + cookie1

        # params1 = "?state=target_login%3D1%26ignore_opener%3D1"
        # url1 = "https://target.my.com/auth/mycom" + params1
        url1 = response.headers['Location']

        response1 = self.session.request(
            "GET", url1, allow_redirects=False)

        # params2 = "?from=http%3A%2F%2Ftarget.my.com%2Fauth%2Fmycom%3Fstate%3Dtarget_login%253D1%2526ignore_opener%253D1"
        # url2 = "https://auth-ac.my.com/sdc" + params2
        url2 = response1.headers['Location']

        response2 = self.session.request(
            "GET", url2, allow_redirects=False)

        cookie2 = response2.headers['Set-Cookie']
        print("")
        # print(cookie2)
        self.cookie += "; " + cookie2

        url3 = response2.headers['Location']
        response3 = self.session.request(
            "GET", url3, allow_redirects=False)

        # cookie3 = response3.headers['Set-Cookie']
        # print("")
        # # print(cookie2)
        # self.cookie += "; " + cookie3

        url4 = response3.headers['Location']
        response4 = self.session.request(
            "GET", url4, allow_redirects=False)

        cookie4 = response4.headers['Set-Cookie']
        print("")
        # print(cookie2)
        self.cookie += "; " + cookie4

        url5 = response4.headers['Location']
        response5 = self.session.request(
            "GET", url5, allow_redirects=False)

        url6 = response5.headers['Location']
        response6 = self.session.request(
            "GET", url6, allow_redirects=False)

        cookie6 = response6.headers['Set-Cookie']
        print("")
        # print(cookie2)
        self.cookie += "; " + cookie6

        responseCSRF = self.session.request(
            "GET", "https://target.my.com/csrf")

        cookieCSRF = responseCSRF.headers['Set-Cookie']
        self.cookie += "; " + cookieCSRF
        self.csrf_token = cookieCSRF.split("=")[1].split(";")[0]
        # print(cookieCSRF.split("=")[1].split(";")[0])
        # print(responseCSRF.headers)
        print("\n ============================== \n")

        response = response6
        return response


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
    # client.csrf_token = csrf_token
    # client.cookie = ""
    client.cookie = "_gcl_au=1.1.927225171.1635860281"
    client.login()
    resp = client.get_campaigns()
    print(client.cookie.count("csrf"))
    # print(resp.json())
    assert client.check_campaign_presence("MY NEW CAMP")


def test6():
    client = ApiClient()
    client.csrf_token = csrf_token
    # client.cookie = cookie
    client.cookie = "_gcl_au=1.1.927225171.1635860281"
    client.login2("tttshelby6@gmail.com", "S3leniumpass")
    # print(client.)
    resp = client.create_campaign("My camp")
    print(resp)
    print(resp.json())
    # print(resp.json()['id'])


def test7():
    client = ApiClient()
    # client.cookie = "_gcl_au=1.1.927225171.1635860223"
    client.cookie = "_gcl_au=1.1.927225171.1635860281"
    # client.cookie = ''
    # client.cookie = "tmr_lvid=62eb5ba99f745ac0674cf6bb5b1496bd; tmr_lvidTS=1635860005219; _gcl_au=1.1.1477758274.1635860005; _fbp=fb.1.1635860005638.434159890; _ga=GA1.2.774654065.1635860006; _gid=GA1.2.2109926772.1635860006; tmr_reqNum=5"
    resp = client.login("tttshelby6@gmail.com", "S3leniumpass")
    print(resp.status_code)
    print(resp.url)
    print('')
    print(resp.headers)


if __name__ == "__main__":
    test6()
    # client = ApiClient()
    # client.cookie = "_gcl_au=1.1.927225171.1635860281"
    # client.login()
