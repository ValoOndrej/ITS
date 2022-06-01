# -*- coding: utf-8 -*-
# login: xvaloo00
# jmeno: Ondrej Valo
from behave import *
import unittest
import selenium
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


@given("Web browser is at the page of product.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=42")

@when("User click on checkbox for difrent options.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[2]/label/input").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/div[2]/label/input").click()


@then("option wil be set to checkbox.")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[2]/label/input").is_selected() is True
    assert context.driver.find_element(By.XPATH, "//div[2]/div/div[2]/label/input").is_selected() is True


@when("User whrite to textbox.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=42")
    context.driver.find_element(By.XPATH, "//div[3]/input").clear()
    context.driver.find_element(By.XPATH, "//div[3]/input").send_keys("text123123")
    context.driver.find_element(By.XPATH, "//div[5]/textarea").clear()
    context.driver.find_element(By.XPATH, "//div[5]/textarea").send_keys("texttext2314")
    context.driver.find_element(By.XPATH, "//div[7]/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[7]/div/input").send_keys("2020-11-11")
    context.driver.find_element(By.XPATH, "//div[8]/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[8]/div/input").send_keys("12:12")
    context.driver.find_element(By.XPATH, "//div[9]/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[9]/div/input").send_keys("2011-02-20 22:12")
    context.driver.find_element(By.XPATH, "//div[10]/input").send_keys("3")



@then("Text in textbox wil change.")
def step_impl(context):
    value = context.driver.find_element(By.XPATH, "//div[3]/input").get_attribute("value")
    assert value == "text123123"
    value = context.driver.find_element(By.XPATH, "//div[5]/textarea").get_attribute("value")
    assert value == "texttext2314"
    value = context.driver.find_element(By.XPATH, "//div[7]/div/input").get_attribute("value")
    assert value == "2020-11-11"
    value = context.driver.find_element(By.XPATH, "//div[8]/div/input").get_attribute("value")
    assert value == "12:12"
    value = context.driver.find_element(By.XPATH, "//div[9]/div/input").get_attribute("value")
    assert value == "2011-02-20 22:12"
    value = context.driver.find_element(By.XPATH, "//div[10]/input").get_attribute("value")
    assert value == "23"


@when("User click to selectboxes.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//select").click()


@then("Options will apear for selectboxes.")
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//select")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == " --- Please Select --- "

@given("Web browser is at the page of another product.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=42")

@when("User click to options.")
def step_impl(context):
    select = Select(context.driver.find_element(By.XPATH, "//select"))
    select.select_by_value('4')


@then("options will be set as active.")
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//select")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text.splitlines()[0] == "Red                                (+$4.80)"


@given("Web browser is at the page of difrent product.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")


@when("User click on button Add to Cart.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()


@then("product will be added to cart.")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//body/div[2]/div")
    assert len(elements) > 0


@when("User click on button of shopping cart.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[3]/div/button/span").click()


@then("Pop up window with information about shopping cart will apear.")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//p")
    assert len(elements) > 0


@when("User click on button Wiew Cart on pup up of shopping cart.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")


@then("User will be redirect to the page Shopping Cart.")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//td[4]/div/span/button/i")
    assert len(elements) > 0


@given("Web browser is at the page Shopping Cart with somthing in cart.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")

@when("User wil click on option.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/h4/a").click()


@then("Difrent setting will apreat base on option.")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/h4/a")
    assert len(elements) > 0


@given("Web browser is at the page Shopping Cart, with unrolled rollbar Use Coupon Code.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")


@when("User will insert correct cupon code to textbox and click button Apply Coupon.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/div[1]/h4/a").click()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/input").send_keys("1111")
    context.driver.find_element(By.XPATH, "//span/input").click()


@then("Coupon wil be aceptet")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//body/div[2]/div")
    assert len(elements) > 0


@given("Web browser is at the page Shopping Cart, with unrolled rollbar Estimate Shipping & Taxes.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")


@when("User will fill textboxes with correct parameters and click on button Get Quets.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div[1]/div[2]/div[1]/h4/a").click()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "//select").click()
    dropdown = context.driver.find_element(By.XPATH, "//select")
    dropdown.find_element(By.XPATH, "//option[. = 'Slovak Republic']").click()
    context.driver.find_element(By.XPATH, "//select").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/select").click()
    dropdown = context.driver.find_element(By.XPATH, "//div[2]/div/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Banskobystrický']").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/select").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").send_keys("966 03")


@then("Pop up window will apear.")
def step_impl(context):
    element = context.driver.find_element(By.XPATH, "//select")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "Slovak Republic"
    element = context.driver.find_element(By.XPATH, "//div[2]/div/select")
    locator = "option[@value='{}']".format(element.get_attribute("value"))
    selected_text = element.find_element(By.XPATH, locator).text
    assert selected_text == "Banskobystrický"
    value = context.driver.find_element(By.XPATH, "//div[3]/div/input").get_attribute("value")
    assert value == "966 03"


@given("Web browser is at the page Shopping Cart, with pop up window opend.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")
    context.driver.find_element(By.XPATH, "//div[2]/div/h4/a").click()
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "//select").click()
    dropdown = context.driver.find_element(By.XPATH, "//select")
    dropdown.find_element(By.XPATH, "//option[. = 'Slovak Republic']").click()
    context.driver.find_element(By.XPATH, "//select").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/select").click()
    dropdown = context.driver.find_element(By.XPATH, "//div[2]/div/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Banskobystrický']").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/select").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").send_keys("966 03")
    context.driver.find_element(By.XPATH, "//div[2]/div/div/button").click()


@when("User will choose shipping method and click button Apply Shipping.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//label/input").click()
    context.driver.find_element(By.XPATH, "//div[3]/input").click()


@then("Shipping estimate will be applied.")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//body/div[2]/div")
    assert len(elements) > 0


@given("Web browser is at the page Shopping Cart, with unrolled rollbar Use Gift Certificate.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "//div[3]/div/h4/a").click()


@when("User will insert correct gift certificate to textbox and click button Apply Gift Certificate.")
def step_impl(context):
    context.driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/input").click()
    context.driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/input").send_keys("1111")
    context.driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/span/input").click()
    element = context.driver.find_element(By.XPATH, "//div[3]/div[2]/div/div/span/input")
    actions = ActionChains(context.driver)
    actions.move_to_element(element).perform()


@then("Gift Certificate wil be acepted")
def step_impl(context):
    elements = context.driver.find_elements(By.XPATH, "//body/div[2]/div")
    assert len(elements) > 0


@given("Web browser is at the page Shopping Cart, with filed options for Shiping.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/cart")
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "//div[2]/div/h4/a").click()
    context.driver.find_element(By.XPATH, "//select").click()
    dropdown = context.driver.find_element(By.XPATH, "//select")
    dropdown.find_element(By.XPATH, "//option[. = 'Slovak Republic']").click()
    context.driver.find_element(By.XPATH, "//select").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/select").click()
    dropdown = context.driver.find_element(By.XPATH, "//div[2]/div/select")
    dropdown.find_element(By.XPATH, "//option[. = 'Banskobystrický']").click()
    context.driver.find_element(By.XPATH, "//div[2]/div/select").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").clear()
    context.driver.find_element(By.XPATH, "//div[3]/div/input").send_keys("966 03")
    context.driver.find_element(By.XPATH, "//div[2]/div/div/button").click()
    context.driver.find_element(By.XPATH, "//label/input").click()
    context.driver.find_element(By.XPATH, "//div[3]/input").click()


@when("User will click on button Checkout.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/checkout")


@then("User will be redirect to the page Checkout.")
def step_impl(context):
    context.driver.implicitly_wait(30)
    assert context.driver.find_element(By.CSS_SELECTOR, "h1").text == "Shopping Cart  (10.00kg)"


@given("Web browser is at the page Checkout, with unrolled step 1.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/checkout")


@when("User will choose chcekout_option and click on button continue.")
def step_impl(context):
    context.driver.implicitly_wait(10)
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/label/input").click()


@then("Step 2 will unroll with difrent parameter base on chcekout_option.")
def step_impl(context):
    assert context.driver.find_element(By.XPATH, "//div[2]/label/input").is_selected() is True


@given("Web browser is at the page Checkout, with unrolled step 2.")
def step_impl(context):
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=product/product&product_id=40")
    context.driver.find_element(By.XPATH, "//div[2]/div[2]/div/button").click()
    context.driver.find_element(By.XPATH, "//div[3]/div/button").click()
    context.driver.get("http://mat.fit.vutbr.cz:8108/index.php?route=checkout/checkout")
    context.driver.implicitly_wait(5)
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/div[2]/label/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[1]/div[2]/div/div/div[1]/input").click()
    context.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/div[2]/div[1]/h4/a").click()


@when("User will fill all mandatory texboxes and click button continue.")
def step_impl(context):
    context.driver.implicitly_wait(30)
    context.driver.find_element(By.XPATH, "//fieldset/div[2]/input").clear()
    context.driver.find_element(By.XPATH, "//fieldset/div[2]/input").send_keys("Ondrej")
    context.driver.find_element(By.XPATH, "//div[3]/input").send_keys("Valo")
    context.driver.find_element(By.XPATH, "//div[2]/fieldset/div[2]/input").send_keys("Sklene Teplice 205")
    context.driver.find_element(By.XPATH, "//div[2]/fieldset/div[4]/input").send_keys("Sklene Teplice")
    context.driver.find_element(By.XPATH, "//div[2]/fieldset/div[5]/input").send_keys("96603")
    context.driver.find_element(By.XPATH, "//div[4]/input").send_keys("ondrejvalo6@gmail.com")
    context.driver.find_element(By.XPATH, "//div[5]/input").send_keys("0915233290")


@then("Step 3 will unroll")
def step_impl(context):
    value = context.driver.find_element(By.XPATH, "//fieldset/div[2]/input").get_attribute("value")
    assert value == "Ondrej"
    value = context.driver.find_element(By.XPATH, "//div[3]/input").get_attribute("value")
    assert value == "Valo"
    value = context.driver.find_element(By.XPATH, "//div[4]/input").get_attribute("value")
    assert value == "ondrejvalo6@gmail.com"
    value = context.driver.find_element(By.XPATH, "//div[5]/input").get_attribute("value")
    assert value == "0915233290"
    value = context.driver.find_element(By.XPATH, "//div[2]/fieldset/div[2]/input").get_attribute("value")
    assert value == "Sklene Teplice 205"
    value = context.driver.find_element(By.XPATH, "//div[2]/fieldset/div[4]/input").get_attribute("value")
    assert value == "Sklene Teplice"
    value = context.driver.find_element(By.XPATH, "//div[2]/fieldset/div[5]/input").get_attribute("value")
    assert value == "96603"