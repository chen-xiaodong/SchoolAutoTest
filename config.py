from selenium import webdriver

web_driver_path = "/Users/chenxiaodong/Downloads/chromedriver"
target_Url = "https://www.maxluck.top/dist/"


class drivers:
    def __init__(self, path, target):
        self.path = path
        self.target = target

    def set_driver(self):
        if self.target == "chrome":
            driver = webdriver.Chrome(executable_path=self.path)
            return driver
