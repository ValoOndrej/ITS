from selenium import webdriver
from behave import fixture
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def selenium_browser_chrome(context):
    context.driver = webdriver.Chrome('C:/WebDriver/bin/chromedriver')
    webdriver.Remote(command_executor='http://mys01.fit.vutbr.cz:4444/wd/hub', desired_capabilities=DesiredCapabilities.CHROME)
    context.driver.implicitly_wait(30)
    context.base_url = "http://mat.fit.vutbr.cz:8108/"
    webdriver.DesiredCapabilities.CHROME["unexpectedAlertBehaviour"] = "accept"


def after_all(context):
    context.driver.quit()
    context.assertEqual([], context.verificationErrors)


def before_scenario(context, scenario):
    context.driver =  webdriver.Remote(command_executor="http://mys01.fit.vutbr.cz:4444/wd/hub", desired_capabilities=DesiredCapabilities.CHROME)
    context.driver.set_page_load_timeout(30)
    context.base_url = "http://mat.fit.vutbr.cz:8108/"
    webdriver.DesiredCapabilities.CHROME["unexpectedAlertBehaviour"] = "accept"


def after_scenario(context, scenario):
    context.driver.quit()
