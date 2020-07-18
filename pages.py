# encoding:utf-8
from selenium.webdriver.support.select import Select


class BasePage:
    """
    基础页面
    """

    def __init__(self, driver):
        self.driver = driver

    def get_url(self, url):
        self.driver.get(url)

    def find_id(self, elementId):
        return self.driver.find_element_by_id(elementId)

    def find_name(self, elementName):
        return self.driver.find_element_by_name(elementName)

    def find_classname(self, elementClassName):
        return self.driver.find_element_by_class_name(elementClassName)

    def find_xpath(self, element_xpath):
        return self.driver.find_element_by_xpath(element_xpath)


class Login(BasePage):

    @property
    def username(self):
        return self.find_name("username")

    @property
    def password(self):
        return self.find_name("password")

    @property
    def submit(self):
        return self.find_classname("el-button")


class CourseIndex(BasePage):

    @property
    def entry(self):
        print("点击课程大厅")
        return self.find_classname("el-menu-item")

    @property
    def creatButton(self):
        print("点击新建课程")
        return self.find_classname("createBtn")

    @property
    def course_name(self):
        print("输入课程名称")
        return self.find_xpath("/html/body/div[1]/div/div[2]/section/div/div/div/div/form/div[7]/div/div/div["
                               "1]/div/div/div[2]/div/div/input")

    @property
    def submit(self):
        print("提交课程")
        return self.find_classname("submitBtn")

    @property
    def grade(self):
        print("点击选择框")
        grade_select = self.find_classname("el-input__inner")
        return grade_select

    @property
    def select_li(self):
        print("选择年级")
        grade_li = self.find_xpath("/html/body/div[3]/div[1]/div[1]/ul/li[2]")
        return grade_li
