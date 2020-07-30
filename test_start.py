#! /usr/bin/env python3

import allure

from common.handler import handle_case, MyQueue
from config.config import drivers
from pages.pages import Login


# def load_driver():
#     return drivers(web_driver_path, "chrome").set_driver()
#
#
# def run_cases(case_item, case_obj):
#     for k, v in case_item.items():
#         label = getattr(case_obj, v['label'])
#         action = getattr(label, v['action'])
#         print(v['label'] + '  ' + v['action'])
#         if v.get("value"):
#             action(v['value'])
#         else:
#             action()
#
#
# def start(case_obj):
#     for key, value in cases.items():
#         print(value.get('url'))
#         if value.get('steps'):
#             run_cases(value.get('steps'), case_obj)
#         else:
#             print("No steps available")
#         sleep(5)
#
#
# def check():
#     url = driver.current_url
#     print(url)

@allure.step("生成case")
def start(page_obj, webDriver):
    """
     从队列中取出一条用例，并调用run_step方法进行用例步骤的执行
    :param page_obj:
    :param webDriver:
    :return:
    """
    case_queue = handle_case().put_case_to_queue()
    step_queue = MyQueue().get_queue()
    while not case_queue.empty():
        case = case_queue.get()
        run_step(case, step_queue, page_obj, webDriver)


@allure.step("处理step")
def deal_step(step, page_obj):
    """
    将用例转为对应page对象的属性，进行执行。有value值则传入进方法中，没有value值则直接执行方法
    :param step:
    :param page_obj:
    :return:
    """
    label = step.get("label")
    value = step.get("value")
    action = step.get('action')
    element = getattr(page_obj, label)
    actions = getattr(element, action)
    with allure.step("执行方法"):
        if value is None:
            actions()
        else:
            actions(value)


def check_result(checks, webDriver):
    """
    验证结果，通过checks中的方法和内容进行验证
    :param checks:
    :param webDriver:
    :return:
    """
    if checks.get("url"):
        factUrl = webDriver.current_url
        exceptUrl = checks.get("url")
        assert factUrl == exceptUrl


def run_step(case, step_queue, page_obj, webDriver):
    """
    从队列中依次存入steps、checks后while循环step队列，依次取出一个case和一个checks，转入处理步骤func
    :param case:
    :param step_queue:
    :param page_obj:
    :param webDriver:
    :return:
    """
    step_queue.put(case.get("steps"))
    step_queue.put(case.get("checks"))
    while not step_queue.empty():
        steps = step_queue.get()
        checks = step_queue.get()
        # print(steps)
        for key, value in steps.items():
            deal_step(value, page_obj)
        check_result(checks, webDriver)


# if __name__ == '__main__':
@allure.story("测试入口")
def test_main():
    driver_obj = drivers()
    driver = driver_obj.set_driver()
    driver_obj.set_url()
    # sleep(5)
    driver.implicitly_wait(5)
    login = Login(driver)
    start(login, driver)
    driver.quit()
