import sys
import time
import argparse
import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver import ChromeOptions

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='example:\n'
                                        'autoLogin -f login -u 20180101 \n'
                                        'autoLogin -f logout')
parser.add_argument('-f', '--function', help='login or logout, where login function requires username and password',
                    required=True)
parser.add_argument('-u', '--username', type=str, help='username is student id')
args = parser.parse_args()

option = ChromeOptions()
option.add_argument("--headless")#指定无头模式
#browser = webdriver.Chrome(options=option)
browser = webdriver.Chrome()
# ff_options = webdriver.FirefoxOptions()
# ff_options.headless = True
# ff_options.add_argument('--disable-gpu')
# browser = webdriver.Firefox(firefox_options=ff_options)
browser.get("http://202.206.1.231/")


def quit_and_clean(drive, msg):
    """exit entire browser and print error message
    :param drive: selenium.webdriver
    :param msg:error message
    """
    print(msg)
    drive.quit()
    sys.exit()


def check_login(page_source):
    """Check whether it is already logged in"""
    return "已用时长" in page_source


def check_loaded():
    """Check whether the page has been loaded"""
    time.sleep(1)
    locator = (By.ID, 'self-service')
    try:
        WebDriverWait(browser, 10, 1).until(EC.presence_of_element_located(locator))
    except TimeoutException:
        quit_and_clean(browser, "登录界面加载出错")


def login(user):
    check_loaded()
    if check_login(browser.page_source):
        quit_and_clean(browser, "已经是登录状态")
    try:
        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")
    except NoSuchElementException:
        quit_and_clean(browser, "输入框定位错误")

    passwd = getpass.getpass()
    print("正在登录.............................................")
    username.send_keys(user)
    password.send_keys(passwd)
    login_button = browser.find_element_by_id("login-account")
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, "login-account")))
    login_button.click()
    time.sleep(2)
    if not check_login(browser.page_source):
        quit_and_clean(browser, "用户名密码错误，请重新登录")
    quit_and_clean(browser, "登录成功")


def logout():
    """Click the logout button and confirm logout"""
    check_loaded()
    time.sleep(2)
    try:
        logout_button = browser.find_element_by_id('logout')
    except NoSuchElementException:
        quit_and_clean(browser, "不是登录状态")
    logout_button.click()
    time.sleep(1)
    confirm = browser.find_element_by_class_name("btn-confirm")
    confirm.click()
    time.sleep(1)
    browser.refresh()
    if not check_login(browser.page_source):
        print("注销成功")
    browser.quit()


if args.function == 'logout':
    logout()
elif args.function == 'login':
    if not args.username:
        quit_and_clean(browser, "please input username")
    login(args.username)
