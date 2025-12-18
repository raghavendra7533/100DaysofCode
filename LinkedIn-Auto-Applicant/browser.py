"""
Browser automation module using Selenium
"""
import time
import logging
from typing import Optional
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException,
    ElementClickInterceptedException, StaleElementReferenceException
)
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from config import Config

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class BrowserManager:
    """Manages browser instance and provides utility methods"""

    def __init__(self, headless: bool = None, browser_type: str = None):
        self.headless = headless if headless is not None else Config.HEADLESS_MODE
        self.browser_type = browser_type or Config.BROWSER_TYPE
        self.driver: Optional[webdriver.Chrome | webdriver.Firefox] = None
        self.wait: Optional[WebDriverWait] = None

    def start(self):
        """Initialize and start the browser"""
        if self.browser_type.lower() == 'firefox':
            self._start_firefox()
        else:
            self._start_chrome()

        self.wait = WebDriverWait(self.driver, 10)
        self.driver.maximize_window()
        logger.info(f"Browser started: {self.browser_type}")

    def _start_chrome(self):
        """Start Chrome browser"""
        options = ChromeOptions()

        if self.headless:
            options.add_argument('--headless=new')

        # Common options
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument('--disable-infobars')
        options.add_experimental_option('excludeSwitches', ['enable-automation'])
        options.add_experimental_option('useAutomationExtension', False)

        # User agent to appear more human-like
        options.add_argument(
            'user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
            'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
        )

        try:
            # Try using webdriver-manager
            driver_path = ChromeDriverManager().install()
            # Fix path if it points to wrong file
            if 'THIRD_PARTY' in driver_path:
                import os
                driver_dir = os.path.dirname(driver_path)
                for f in os.listdir(driver_dir):
                    if f == 'chromedriver' or f == 'chromedriver.exe':
                        driver_path = os.path.join(driver_dir, f)
                        break
            service = ChromeService(driver_path)
            self.driver = webdriver.Chrome(service=service, options=options)
        except Exception as e:
            logger.error(f"Error with webdriver-manager: {e}")
            # Fallback: try without specifying service (uses system chromedriver)
            self.driver = webdriver.Chrome(options=options)

        # Remove webdriver flag
        self.driver.execute_script(
            "Object.defineProperty(navigator, 'webdriver', {get: () => undefined})"
        )

    def _start_firefox(self):
        """Start Firefox browser"""
        options = FirefoxOptions()

        if self.headless:
            options.add_argument('--headless')

        options.set_preference('dom.webdriver.enabled', False)
        options.set_preference('useAutomationExtension', False)

        service = FirefoxService(GeckoDriverManager().install())
        self.driver = webdriver.Firefox(service=service, options=options)

    def quit(self):
        """Close the browser"""
        if self.driver:
            self.driver.quit()
            self.driver = None
            logger.info("Browser closed")

    def get(self, url: str):
        """Navigate to URL"""
        self.driver.get(url)
        time.sleep(1)  # Allow page to start loading

    def find_element(self, by: By, value: str, timeout: int = 10):
        """Find element with wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            return None

    def find_elements(self, by: By, value: str, timeout: int = 10):
        """Find multiple elements with wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.presence_of_element_located((by, value)))
            return self.driver.find_elements(by, value)
        except TimeoutException:
            return []

    def find_clickable(self, by: By, value: str, timeout: int = 10):
        """Find clickable element with wait"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.element_to_be_clickable((by, value)))
        except TimeoutException:
            return None

    def click_element(self, element, retry: int = 3):
        """Click element with retry logic"""
        for attempt in range(retry):
            try:
                element.click()
                return True
            except ElementClickInterceptedException:
                time.sleep(0.5)
                try:
                    self.driver.execute_script("arguments[0].click();", element)
                    return True
                except Exception:
                    pass
            except StaleElementReferenceException:
                time.sleep(0.5)
        return False

    def safe_send_keys(self, element, text: str, clear_first: bool = True):
        """Safely send keys to element"""
        try:
            if clear_first:
                element.clear()
                time.sleep(0.1)
            element.send_keys(text)
            return True
        except Exception as e:
            logger.error(f"Error sending keys: {e}")
            return False

    def scroll_to_element(self, element):
        """Scroll element into view"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",
            element
        )
        time.sleep(0.5)

    def scroll_page(self, pixels: int = 300):
        """Scroll page by pixels"""
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")
        time.sleep(0.3)

    def is_element_visible(self, by: By, value: str, timeout: int = 3) -> bool:
        """Check if element is visible"""
        try:
            wait = WebDriverWait(self.driver, timeout)
            wait.until(EC.visibility_of_element_located((by, value)))
            return True
        except TimeoutException:
            return False

    def get_current_url(self) -> str:
        """Get current page URL"""
        return self.driver.current_url

    def get_page_source(self) -> str:
        """Get page source"""
        return self.driver.page_source

    def take_screenshot(self, filename: str):
        """Take screenshot of current page"""
        import os
        filepath = os.path.join(Config.LOGS_DIR, filename)
        os.makedirs(Config.LOGS_DIR, exist_ok=True)
        self.driver.save_screenshot(filepath)
        logger.info(f"Screenshot saved: {filepath}")
        return filepath

    def wait_for_page_load(self, timeout: int = 30):
        """Wait for page to fully load"""
        try:
            WebDriverWait(self.driver, timeout).until(
                lambda d: d.execute_script('return document.readyState') == 'complete'
            )
        except TimeoutException:
            logger.warning("Page load timeout")

    def human_delay(self, min_seconds: float = 0.5, max_seconds: float = 2.0):
        """Add human-like delay"""
        import random
        delay = random.uniform(min_seconds, max_seconds)
        time.sleep(delay)
