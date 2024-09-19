import allure
import pytest
import os


class BaseTest:
    """Base test class with shared configurations and actions."""

    @pytest.fixture(autouse=True)
    def setup_method(self, request, browser):
        """Run this before every test method."""
        self.browser = browser

        # Automatically capture screenshots after each test step.
        yield
        # Capture screenshot at the end of each test step (you can add this at every step)
        if request.node.rep_call.failed:
            self.capture_screenshot(request.node.nodeid)

    def capture_screenshot(self, step_name):
        """Capture and attach screenshot to Allure report."""
        screenshot_name = f"{step_name.replace('::', '_')}.png"
        screenshot_path = os.path.join("screenshots", screenshot_name)

        self.browser.save_screenshot(screenshot_path)  # Save the screenshot

        with open(screenshot_path, "rb") as image_file:
            allure.attach(image_file.read(), name=step_name, attachment_type=allure.attachment_type.PNG)
