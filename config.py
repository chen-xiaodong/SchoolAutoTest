from selenium import webdriver

web_driver_path = "src/chromedriver"
target_Url = "https://www.maxluck.top/dist/"


def set_options():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('windows-size=1920x1080')
    return options


class drivers:
    def __init__(self, path, target):
        self.path = path
        self.target = target

    def set_driver(self):
        if self.target == "chrome":
            driver = webdriver.Chrome(executable_path=self.path, chrome_options=set_options())
            return driver
