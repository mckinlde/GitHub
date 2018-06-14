## Gets the created_at date for a repo using it's URL
import string
from time import sleep
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from random import randint
import re
import requests
import mysql.connector


def retrieve(url: str):
    """retrieves content at the specified url"""
    print("*", url)
    header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'}
    r=requests.get(url, headers=header, verify=False, timeout=5)
    sleep(1)
    soup = BeautifulSoup(r.text, "lxml")

    return soup

def spy_retrieve(url: str, header: str, sleep: int):
    return soup


def auto_rotator()