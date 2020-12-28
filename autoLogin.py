import sys
import time
import argparse
import os
import getpass
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

parser = argparse.ArgumentParser(formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog='example:\n'
                                             'autoLogin -f login -u 20180101 \n'
                                             'autoLogin -f logout')
parser.add_argument('-f', '--function', help='login or logout, where login fuction requires username and password', required=True)
parser.add_argument('-u', '--username', type=str,help='username is student id')
args = parser.parse_args()

ff_options = webdriver.FirefoxOptions()
ff_options.headless = True
ff_options.add_argument('--disable-gpu')
browser = webdriver.Firefox(firefox_options=ff_options)
browser.get("http://202.206.1.231/")


def check_login(page_source):
    return "已用时长" in page_source


def login(user):
    time.sleep(2)
    if check_login(browser.page_source):
        print("已经是登录状态")
        browser.quit()
        sys.exit()
    try:
        username = browser.find_element_by_id("username")
        password = browser.find_element_by_id("password")
    except NoSuchElementException :
        print("登录界面加载出错")
        browser.quit()
        sys.exit(1)
    passwd = getpass.getpass()
    print("正在登录.............................................")
    username.send_keys(user)
    password.send_keys(passwd)
    login_button = browser.find_element_by_id("login")
    login_button.click()
    time.sleep(1)
    if not check_login(browser.page_source):
        print("用户名密码错误，请重新登录")
        browser.quit()
        sys.exit(1)
    print('登录成功')
    browser.quit()


def logout():
    time.sleep(2)
    try:
        logout_button = browser.find_element_by_id('logout')
    except NoSuchElementException:
        print('不是登录状态')
        browser.quit()
        sys.exit(1)
    logout_button.click()
    time.sleep(1)
    if not check_login(browser.page_source):
        print("注销成功")
    browser.quit()


if args.function == 'logout':
    logout()
elif args.function == 'login':
    if not args.username:
        print('please input username')
        browser.quit()
        sys.exit(1)
    login(args.username)
