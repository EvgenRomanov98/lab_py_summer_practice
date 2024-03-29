import json
import requests
from tabulate import *

requests.packages.urllib3.disable_warnings()

def get_ticket():

    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/ticket"
    headers = {
        "content-type": "application/json"
    }
    body_json = {
        "username": "devnetuser",
        "password": "Xj3BDqbU"
    }

    resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)

    print("Ticket request status: ", resp.status_code)

    response_json = resp.json()
    serviceTicket = response_json["response"]["serviceTicket"]

    return serviceTicket


def print_hosts():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/host"
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": get_ticket()
    }

    resp = requests.get(api_url, headers=headers, verify=False)
    response_json = resp.json()
    host_list = []
    i = 0
    print(type(response_json))
    for item in response_json["response"]:
        i += 1
        host = [
            i,
            item["hostType"],
            item["hostIp"]
        ]
        host_list.append(host)
    table_header = ["Number", "Type", "IP"]
    print(tabulate(host_list, table_header))


print_hosts()
