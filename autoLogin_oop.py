#  Copyright (c) 2021. All Rights Reserved.
#  ProjectName: spiderLearning
#  FileName: autoLogin_oop.py
#  Author: Casuall
#  Date: 2021/1/12 上午11:15
#  LastModified: 2021/1/12 上午11:15
import sys
import time
import getpass
import argparse
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions


parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='example:\n'
                                        'autoLogin -f login -u 20180101 \n'
                                        'autoLogin -f logout')
parser.add_argument('-f', '--function', help='login function requires username and password', choices=['login', 'logout'],
                    required=True)
parser.add_argument('-u', '--username', type=str, help='username is student id')
parser.add_argument('-b', '--browser', type=str, choices=['firefox', 'chrome'],
                    default='chrome', help='select which browser, default chrome')
args = parser.parse_args()


class User:
    def __init__(self, student_id):
        self.id = student_id
        self.password = None
        self.update_password()

    def update_password(self):
        self.password = getpass.getpass('Password:')


class AutoLogin:
    """提供用于自动登录的API"""
    def __init__(self, url, browser='chrome'):
        self.url = url
        self.browser_name = browser
        self.is_login = False
        self.count = 2
        self.drive = WebDriverAuto(self.browser_name)
        self.drive.get_page(self.url)

    def login(self, username):
        self.is_login = self.drive.check_login()
        if self.is_login:
            self.drive.quit_and_clean('已经是登录状态')

        self.drive.position_box_input()

        user = User(username)
        self.drive.login(user)
        self.is_login = self.drive.check_login()
        
        while (not self.is_login) and self.count:
            self.drive.click_button(self.drive.position_button_confirm())
            print(f'用户名密码错误，请重新输入密码，还有{self.count}次机会\n')
            self.count -= 1
            time.sleep(1)
            user.update_password()
            self.drive.login(user)
            self.is_login = self.drive.check_login()

        if self.is_login:
            self.drive.quit_and_clean('登录成功\n')
        else:
            self.drive.quit_and_clean('登录失败\n')

    def logout(self):
        self.drive.check_loaded()
        self.drive.click_button(self.drive.position_button_logout())
        self.drive.click_button(self.drive.position_button_confirm())
        self.drive.browser.refresh()
        if not self.drive.check_login():
            print('注销成功')
        self.drive.quit_and_clean()


class DriverGet:
    """获取浏览器驱动"""
    def __init__(self, name_browser='chrome'):
        """
        :param name_browser: select which browser driver
        """
        self.name_browser = name_browser

    def get_browser_drive(self):
        if self.name_browser == 'chrome':
            browser = self.get_chrome_drive()
        elif self.name_browser == 'firefox':
            browser = self.get_firefox_drive()
        else:
            raise NameError('Browser error, currently only supports chrome and firefox browsers')
        return browser

    @staticmethod
    def get_chrome_drive():
        option = ChromeOptions()
        option.add_argument("--headless")  # 指定无头模式
        browser = webdriver.Chrome(options=option)
        return browser

    @staticmethod
    def get_firefox_drive():
        option = webdriver.FirefoxOptions()
        option.headless = True
        option.add_argument('--disable-gpu')
        browser = webdriver.Firefox(firefox_options=option)
        return browser


class WebDriverAuto:
    """将有关于webdriver的操作进行类封装"""
    def __init__(self, which_browser: str = 'chrome'):
        """
        :param which_browser: 选择哪个浏览器
        :var self.browser: 浏览器驱动
        :var self.username: 用户名输入框
        :var self.password: 密码输入框
        """
        self.name_browser = which_browser.lower()
        self.browser = DriverGet(self.name_browser).get_browser_drive()

        self.input_box_username = None
        self.input_box_password = None

        self.button_login = None
        self.button_confirm = None
        self.button_logout = None

    def check_login(self):
        return "used-flow" in self.browser.page_source

    def get_page(self, url):
        """get url, and check if page is loaded"""
        self.browser.get(url)
        self.check_loaded()
        time.sleep(2)

    def quit_and_clean(self, msg=''):
        print(msg)
        self.browser.quit()
        sys.exit()

    def check_loaded(self):
        try:
            WebDriverWait(self.browser, 5, 1).until(EC.presence_of_element_located((By.ID, 'self-service')))
        except TimeoutException:
            self.quit_and_clean("登录界面加载出错")

    def position_box_input(self):
        try:
            self.input_box_username = WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((By.ID, 'username')))
            self.input_box_password = WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((By.ID, 'password')))
        except TimeoutException:
            self.quit_and_clean('输入框定位失败')

    def position_button_login(self):
        try:
            self.button_login = WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((By.ID, 'login-account')))
        except TimeoutException:
            self.quit_and_clean('login button 定位失败')
        return self.button_login

    def position_button_logout(self):
        try:
            self.button_logout = WebDriverWait(self.browser, 3).until(
                EC.presence_of_element_located((By.ID, 'logout')))
        except TimeoutException:
            self.quit_and_clean('不是登录状态')
        return self.button_logout

    def position_button_confirm(self):
        try:
            self.button_confirm = WebDriverWait(self.browser, 4).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'btn-confirm')))
        except TimeoutException:
            self.quit_and_clean('conform button 定位失败')
        return self.button_confirm

    def click_button(self, button):
        if not button.is_enabled():
            self.quit_and_clean('button is not clickable')
        button.click()
        time.sleep(1)

    def login(self, user: User):
        if not (self.input_box_username or self.input_box_password):
            self.position_box_input()
        print('正在登录........................................\n')
        self.input_box_username.clear()
        self.input_box_username.send_keys(user.id)
        self.input_box_password.clear()
        self.input_box_password.send_keys(user.password)
        self.click_button(self.position_button_login())
        time.sleep(2)


if args.function == 'logout':
    auto_login = AutoLogin('http://202.206.1.231/', args.browser)
    auto_login.logout()
elif args.function == 'login':
    if not args.username:
        print("please input username")
        sys.exit()
    auto_login = AutoLogin('http://202.206.1.231/', args.browser)
    auto_login.login(args.username)