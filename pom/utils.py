from selenium.common.exceptions import WebDriverException
from time import sleep
from time import perf_counter as now
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

timeout = 30
poll_time = 0.1


def wait_until_element_is_visible(context, method, value, timeout=timeout) -> WebElement:
    return WebDriverWait(context.driver, timeout, poll_time).until(EC.visibility_of_element_located((method, value)), \
           f"Element '{value}' not visible after timeout of '{timeout}'seconds")


def wait_loop(*, condition, timeout_seconds: float = 60.0, poll_freq: float = 0.01, exit_exception=False):
    end_time = now() + timeout_seconds

    while True:
        result = None
        try:
            result = condition()
        except WebDriverException:
            pass

        if result:
            return result

        if now() > end_time:
            if exit_exception:
                condition()
            break
        sleep(poll_freq)
    return result
