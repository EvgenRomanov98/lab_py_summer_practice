import json

import requests
from tabulate import *

requests.packages.urllib3.disable_warnings()


# ------------------------

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


# ----------------

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


# ------------------------

def print_device():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/network-device"
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
            item["type"],
            item["macAddress"]
        ]
        host_list.append(host)
    table_header = ["Number", "Type", "macAddress"]
    print(tabulate(host_list, table_header))


def path_trace():
    api_url = "https://devnetsbx-netacad-apicem-3.cisco.com/api/v1/flow-analysis"
    headers = {
        "content-type": "application/json",
        "X-Auth-Token": get_ticket()
    }

    print("list hosts")
    print_hosts()
    print("list devices")
    print_device()

    # destIp = str(input("dest Ip: "))
    # sourceIp = str(input("source Ip: "))
    destIp = "8.8.8.8"
    sourceIp = "10.2.1.22"
    body_json = {
        "destIP": destIp,
        "sourceIP": sourceIp
    }
    resp = requests.post(api_url, json.dumps(body_json), headers=headers, verify=False)
    print(resp.json()["response"]["flowAnalysisId"])
    print(resp.json())
    check_url = api_url + "/" + str(resp.json()["response"]["flowAnalysisId"])

    print(check_url)
    response_json = requests.get(check_url, headers=headers, verify=False)
    # print(response_json.json())
    path_source = response_json.json()["response"]["request"]["sourceIP"]
    path_dest = response_json.json()["response"]["request"]["destIP"]
    status = response_json.json()["response"]["request"]["status"]
    print("path_source = " + path_source)
    print("path_dest = " + path_dest)
    print("status = " + status)

    networkElementsInfo = response_json.json()["response"]["networkElementsInfo"]
    print(networkElementsInfo)


path_trace()
