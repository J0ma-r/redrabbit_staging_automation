
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
        browser.click(locate.residential)
        browser.click(locate.blocked_drain)
        browser.click(locate.window_broken)

        driver.implicitly_wait(2)
        browser.fill("Kitchen", locate.where_is_your_problem_1)
        browser.upload(locate.photo_1, "/resources/img.png")
        browser.fill("Bathroom", locate.where_is_your_problem_2)
        browser.upload(locate.photo_2, "/resources/img_1.png")

        browser.fill_by_id("TEST1234", "property_reference")
        browser.fill_by_id("222 No Man's land, Nowhere", "address")
        browser.fill_by_id("test_name", "name")
        browser.fill_by_id("test@email.com", "reporter_email")
        browser.fill_by_id("0829999999", "mobile")
        browser.fill_by_id("Please fix it asap", "comments")

        driver.implicitly_wait(2)
        time.sleep(2)
        browser.click(locate.submit)

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
        browser.click(locate.commercial)
        browser.click(locate.not_listed)
        browser.fill("Bedroom", locate.where_is_your_problem_1)
        browser.fill("Floor", locate.issue_item_1)
        s = "How long does a string have to be for a string to be too long\n"
        for num in range(4):
            browser.fill(s, locate.description_1)
        browser.fill_by_id("TEST1234", "property_reference")
        browser.fill_by_id("222 No Man's land, Nowhere", "address")
        browser.fill_by_id("test_name", "name")
        browser.fill_by_id("test@email.com", "reporter_email")
        browser.fill_by_id("0829999999", "mobile")
        browser.fill_by_id("Please fix it asap", "comments")

        time.sleep(2)
        browser.click(locate.submit_2)
        element = browser.find_by_xpath(locate.description_1)
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        message = browser.find_by_xpath(locate.error_1)
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
        browser.click(locate.body_corporate)
        browser.click(locate.irrigation)
        browser.clear(locate.description_1)
        browser.fill("Leaking water", locate.description_1)
        browser.fill_by_id("TEST1234", "property_reference")
        browser.fill_by_id("222 No Man's land, Nowhere", "address")
        browser.fill_by_id("test_name", "name")
        browser.fill_by_id("123", "reporter_email")
        browser.fill_by_id("0829999999", "mobile")
        browser.fill_by_id("Please fix it asap", "comments")

        time.sleep(2)
        browser.click(locate.submit_2)
        driver.find_element(By.ID, "reporter_email")
        element = driver.find_element(By.ID, "reporter_email")
        actions = ActionChains(driver)
        actions.move_to_element(element).perform()
        time.sleep(2)
        message = browser.find_by_xpath(locate.error_2)
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
        browser.click(locate.residential)
        browser.click(locate.garage)
        browser.click(locate.oven)
        browser.click(locate.tap)
        browser.fill("Garage", locate.where_is_your_problem_1)
        browser.fill("Kitchen", locate.where_is_your_problem_2)
        browser.fill("Outside", locate.where_is_your_problem_3)

        time.sleep(2)
        browser.click(locate.roof)

        while not driver.find_element(By.XPATH, locate.popup).is_displayed():
            driver.implicitly_wait(2)
            browser.click(locate.roof)
        message = browser.find_by_xpath(locate.popup)
        assert message.text == "Maximum issues reached"
        return True

    except AssertionError and NoSuchElementException:
        return False

    finally:
        time.sleep(5)
        browser.close()
