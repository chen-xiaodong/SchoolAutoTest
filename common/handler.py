import queue

import yaml

from config.config import config


class handle_case:
    """
    :Desc: 处理case
    """
    def __init__(self):
        self.path = config().get_case_path

    def get_cases(self):
        """
        :Desc: 将yaml类型的用例文件转成dict
        :return: cases
        """
        with open(self.path, 'r+') as f:
            cases = yaml.safe_load(f)
        return cases

    def put_case_to_queue(self):
        """
        :Desc: 获取用例，将用例依次放入队列中
        :return: queue
        """
        cases = self.get_cases()
        case_queue = MyQueue().get_queue()
        for key, value in cases.items():
            case_queue.put(cases.get(key))
        return case_queue


class MyQueue:
    """
    :desc: 自定义的queue类，用于生成一个队列
    :return： queue
    """
    def __init__(self):
        self.queue = queue.Queue()

    def get_queue(self):
        return self.queue
