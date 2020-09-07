#!/usr/bin/python3
"""
Get information from o.s.d Maintenance: Test Repo specific for SAP & HA
"""

import argparse
import sys

from concurrent.futures import ThreadPoolExecutor
from urllib.request import urlopen
from time import strftime

from bs4 import BeautifulSoup

__version__ = "0.1.0"

GROUP_ID = {
    '12-SP2': 54, '12-SP3': 108, '12-SP4': 218, '12-SP5': 280,
    '15': 165, '15-SP1': 232, '15-SP2': 308
}
FLAVORS = ('SAP-DVD-Updates', 'Server-DVD-HA-Updates')
BASE_URL = 'https://openqa.suse.de/tests/'
URL = BASE_URL + 'overview?distri=sle&version=%s&build=%s-1&groupid=%s'

info = {}


def parse_args():
    """
    Parse options and arguments
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--all', action='store_true',
                        help="Also show passed tests")
    parser.add_argument('-V', '--version', action='store_true',
                        help="Show version and exit")
    return parser.parse_args()


def get_info(version):
    """
    Get the information for a particular SLE version
    """
    url = URL % (version, strftime("%Y%m%d"), GROUP_ID[version])
    with urlopen(url) as conn:
        soup = BeautifulSoup(conn.read(), 'html.parser')
    info[version] = {}
    for flavor in FLAVORS:
        table = soup.find('table', id="results_%s" % flavor)
        rows = table.find_all('tr')[1:]
        info[version][flavor] = {}
        for row in rows:
            job = row.find('td', {'class': "name"}).span.text
            status = row.find('i', {'class': "status"})['class']
            if status[3].startswith("result_"):
                status = status[3][len("result_"):]
            elif status[1].startswith("state_"):
                status = status[1][len("state_"):]
            if not args.all and status in {'passed', 'softfailed'}:
                continue
            url = row.find('a', href=True)['href'][len("/tests/"):]
            info[version][flavor][job] = {'url': url, 'status': status}
        if not info[version][flavor]:
            del info[version][flavor]
    if not info[version]:
        del info[version]


def print_info():
    """
    Print information
    """
    for version in info:
        print(version)
        for flavor in info[version]:
            print(flavor)
            for job, data in info[version][flavor].items():
                print("%s\t%s\t%s" % (job, data['status'], data['url']))
            print()
        print()


if __name__ == "__main__":
    args = parse_args()
    if args.version:
        print(__version__)
        sys.exit(0)
    with ThreadPoolExecutor() as executor:
        executor.map(get_info, GROUP_ID)
    print_info()
