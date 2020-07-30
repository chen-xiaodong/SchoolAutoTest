from selenium import webdriver


class config:
    """
    config类
    用于配置webDriver、case文件、默认Url进行配置
    """
    def __init__(self):
        # webDriver路径
        self.__web_driver_path = "./src/chromedriver"
        # 默认打开的URL
        self.__target_url = "https://www.maxluck.top/dist/"
        # case路径
        self.__case_path = "./case/case.yaml"

    @property
    def get_web_driver_path(self):
        return self.__web_driver_path

    @property
    def get_target_url(self):
        return self.__target_url

    @property
    def get_case_path(self):
        return self.__case_path


class drivers:
    def __init__(self, target="chrome"):
        self.path = config().get_web_driver_path
        self.url = config().get_target_url
        self.target = target
        self.driver = None

    def set_driver(self):
        """
        :desc: 配置Chrome的webDriver
        :return: WebDriver
        """
        if self.target == "chrome":
            driver = webdriver.Chrome(executable_path=self.path, options=self.set_options())
            self.driver = driver
            return driver

    def set_options(self):
        """
        :desc: 用于设置Chrome浏览器options
        :return: options
        """
        if self.target == 'chrome':
            options = webdriver.ChromeOptions()
            # options.add_argument('--headless')
            options.add_argument('windows-size=1920x1080')
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            return options

    def set_url(self):
        """
        :desc: 用于打开默认Url
        :return:
        """
        self.driver.get(self.url)
