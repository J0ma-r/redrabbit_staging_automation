
import time
from selenium.common.exceptions import NoSuchElementException
from browser import Browser
import locate
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


def scenario1():
    browser = Browser()

    try:

        url = "https://redrabbit.rebaseventures.com/qa-automation/maintenance"
        driver = browser.go_to(url)
        driver.delete_all_cookies()
        title = driver.title
        assert "RedRabbit Staging" in title

        driver.implicitly_wait(2)
        browser.click(locate.RESIDENTIAL)
        browser.click(locate.BLOCKED_DRAIN)
        browser.click(locate.WINDOW_BROKEN)

        driver.implicitly_wait(2)
        browser.fill("Kitchen", locate.WHERE_1)
        browser.upload(locate.PHOTO_1, "/resources/img.png")
        browser.fill("Bathroom", locate.WHERE_2)
        browser.upload(locate.PHOTO_2, "/resources/img_1.png")

        browser.fill_by_id("TEST1234", "property_reference")
        browser.fill_by_id("222 No Man's land, Nowhere", "address")
        browser.fill_by_id("test_name", "name")
        browser.fill_by_id("test@email.com", "reporter_email")
        browser.fill_by_id("0829999999", "mobile")
        browser.fill_by_id("Please fix it asap", "comments")

        driver.implicitly_wait(2)
        time.sleep(2)
        browser.click(locate.SUBMIT_1)

        time.sleep(4)
        message = driver.find_element(By.TAG_NAME, 'h1')
        assert message.text == "Thank you for logging your request. We will respond to your request within 24hrs"
        driver.save_screenshot("/resources/test_log/scenario1.png")

        return True

    except AssertionError and NoSuchElementException:
        return False

    finally:
        time.sleep(5)
        browser.close()


def scenario2():

    browser = Browser()
    try:

        url = "https://redrabbit.rebaseventures.com/qa-automation/maintenance"
        driver = browser.go_to(url)
        driver.delete_all_cookies()
        title = driver.title
        assert "RedRabbit Staging" in title

        driver.implicitly_wait(2)
        browser.click(locate.COMMERCIAL)
        browser.click(locate.NOT_LISTED)
        browser.fill("Bedroom", locate.WHERE_1)
        browser.fill("Floor", locate.ISSUE_ITEM_1)
        s = "How long does a string have to be for a string to be too long\n"
        for num in range(4):
            browser.fill(s, locate.DESCRIPTION_1)
        browser.fill_by_id("TEST1234", "property_reference")
        browser.fill_by_id("222 No Man's land, Nowhere", "address")
        browser.fill_by_id("test_name", "name")
        browser.fill_by_id("test@email.com", "reporter_email")
        browser.fill_by_id("0829999999", "mobile")
        browser.fill_by_id("Please fix it asap", "comments")

        time.sleep(2)
        browser.click(locate.SUBMIT_2)
        element = browser.find_by_xpath(locate.DESCRIPTION_1)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        message = browser.find_by_xpath(locate.ERROR_1)
        assert message.text == "The description must not be greater than 200 characters."

        return True

    except AssertionError and NoSuchElementException:
        return False

    finally:
        time.sleep(5)
        browser.close()


def scenario3():

    browser = Browser()
    try:

        url = "https://redrabbit.rebaseventures.com/qa-automation/maintenance"
        driver = browser.go_to(url)
        driver.delete_all_cookies()
        title = driver.title
        assert "RedRabbit Staging" in title

        driver.implicitly_wait(2)
        browser.click(locate.BODY_CORPORATE)
        browser.click(locate.IRRIGATION)
        browser.clear(locate.DESCRIPTION_1)
        browser.fill("Leaking water", locate.DESCRIPTION_1)
        browser.fill_by_id("TEST1234", "property_reference")
        browser.fill_by_id("222 No Man's land, Nowhere", "address")
        browser.fill_by_id("test_name", "name")
        browser.fill_by_id("123", "reporter_email")
        browser.fill_by_id("0829999999", "mobile")
        browser.fill_by_id("Please fix it asap", "comments")

        time.sleep(2)
        browser.click(locate.SUBMIT_2)
        driver.find_element(By.ID, "reporter_email")
        element = driver.find_element(By.ID, "reporter_email")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        message = browser.find_by_xpath(locate.ERROR_2)
        assert message.text == "The email must be a valid email address."
        return True

    except AssertionError and NoSuchElementException:
        return False

    finally:
        time.sleep(5)
        browser.close()
        pass


def scenario4():

    browser = Browser()
    try:

        url = "https://redrabbit.rebaseventures.com/qa-automation/maintenance"
        driver = browser.go_to(url)
        driver.delete_all_cookies()
        title = driver.title
        assert "RedRabbit Staging" in title

        driver.implicitly_wait(2)
        browser.click(locate.RESIDENTIAL)
        browser.click(locate.GARAGE)
        browser.click(locate.OVEN)
        browser.click(locate.TAP)
        browser.fill("Garage", locate.WHERE_1)
        browser.fill("Kitchen", locate.WHERE_2)
        browser.fill("Outside", locate.WHERE_3)

        time.sleep(2)
        browser.click(locate.ROOF)

        while not driver.find_element(By.XPATH, locate.POPUP).is_displayed():
            driver.implicitly_wait(2)
            browser.click(locate.ROOF)
        message = browser.find_by_xpath(locate.POPUP)
        assert message.text == "Maximum issues reached"
        return True

    except AssertionError and NoSuchElementException:
        return False

    finally:
        time.sleep(5)
        browser.close()
