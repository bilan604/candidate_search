import re
import os
import sys
import time
import json
import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

import pickle


def get_env(file_path=".env"):
    env = {}
    with open(file_path, "r", encoding='UTF-8') as f:
        for line in f.readlines():
            line = line.strip()
            if not line:
                continue
            if line[0] == "#":
                continue
            lst = line.split("=")
            env[lst[0].strip()] = lst[1].strip()
    return env



class SeleniumHelper(object):
    # parent. no camel case.
    # keep name. use child 'webhelper' and run convert code from camel case
    def __init__(self):
        self.driver = None
        self.headless = False
    
    def load_driver(self):
        env = get_env()
        if "MAC" in env and env["MAC"] == "TRUE":
            self.driver = webdriver.Firefox()
            print("driver set for mac")
            return

        path = os.getcwd() + "\geckodriver_windows.exe"
        print("path:", path)
        self.driver = webdriver.Firefox(
            #executable_path=path
        )
        print("driver set for windows")


    def load_cookies(self):
        try:    
            # Load cookies from the saved file
            with open('logs/cookies.pkl', 'rb') as cookie_file:
                cookies = pickle.load(cookie_file)

            # Add each cookie to the WebDriver
            for cookie in cookies:
                # Ensure the cookie is valid (contains necessary keys)
                if 'expiry' in cookie:  # Some cookies might not have an expiry attribute
                    del cookie['expiry']  # Remove expiry to avoid issues with cookie format
                self.driver.add_cookie(cookie)

            # Refresh the page to apply the cookies and maintain the session
            self.driver.refresh()
        except Exception as e:
            print("Error loading cookies:", e)

    def save_cookies(self):
        # After logging in, get all the cookies
        cookies = self.driver.get_cookies()

        # Save cookies to a file (e.g., cookies.pkl)
        with open('logs/cookies.pkl', 'wb') as cookie_file:
            pickle.dump(cookies, cookie_file)

    def load_script(self, fn):
        with open(fn, 'r') as f:
            return "".join(f.readlines())

    def execute_script_with_params(self, script, params):
        res = self.driver.execute_script(script, params)
        return res

    def execute_script_with_params_by_name(self, name, params):
        script = self.load_script(name) # name is local path to script
        res = self.driver.execute_script(script, params)
        return res

    def switch_to(self, i: int):
        self.driver.switch_to.window(self.driver.window_handles[i])





