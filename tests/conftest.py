import selenium.webdriver
import pytest

@pytest.fixture
def browser():
    b = selenium.webdriver.Chrome()
    b.implicitly_wait(10)
    yield b
    b.quit()

