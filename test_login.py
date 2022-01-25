import pytest
from selenium import webdriver
from time import sleep
from loginpage import LoginPage
from settings import user, passwd


def test_failed_login(browser):
    page =  LoginPage(browser)
    page.load()
    page.login()
    page.validate_failed_login()


def test_valid_login(browser):
    page =  LoginPage(browser)
    page.load()
    page.login(user,passwd)
    page.validate_login_sucess()

def test_wrong_password_login(browser):
    page =  LoginPage(browser)
    page.load()
    page.login(user)
    page.validate_failed_login()
