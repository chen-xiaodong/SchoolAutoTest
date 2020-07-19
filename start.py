#! /usr/bin/env python3

from time import sleep

from case import case
from config import drivers, web_driver_path, target_Url
from pages import Login


def load_case(path):
    return case(path).get_cases()


def load_driver():
    return drivers(web_driver_path, "chrome").set_driver()


def run_cases(case_item, case_obj):
    for k, v in case_item.items():
        label = getattr(case_obj, v['label'])
        action = getattr(label, v['action'])
        if v.get("value"):
            action(v['value'])
        else:
            action()


def start(case_obj):
    for key, value in cases.items():
        if value.get('steps'):
            run_cases(value.get('steps'), case_obj)
        else:
            print("No steps available")
        sleep(5)


if __name__ == '__main__':
    cases = load_case('case.yaml')
    driver = load_driver()
    login = Login(driver)
    login.get_url(target_Url)
    start(login)
    print("success")
