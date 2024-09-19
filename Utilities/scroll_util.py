class ScrollUtil:

    @staticmethod
    def scrollToTextByAndroidUIAutomator(text, driver):
        """
        Scrolls to an element containing the specified text using Android UI Automator and clicks it.

        Args:
        text (str): The text to scroll to and click.
        driver: The Appium driver used for interacting with the Android app.

        Explanation:
        - `UiScrollable`: Used to make the screen scrollable.
        - `scrollable(true)`: Ensures the UI element is scrollable.
        - `scrollIntoView`: Scrolls until the element with the specified text is found.
        - `textContains`: Searches for elements containing the specified text.
        """
        driver.find_element_by_android_uiautomator("new UiScrollable(new UiSelector().scrollable(true).instance(0))"
                                                   ".scrollIntoView(new UiSelector().textContains(\"" + text + "\").instance(0))").click()

    @staticmethod
    def swipeUp(howManySwipes, driver):
        """
        Performs a swipe up action on the screen a specified number of times.

        Args:
        howManySwipes (int): The number of times to perform the swipe up action.
        driver: The Appium driver used for interacting with the Android app.

        Explanation:
        - `swipe`: Swipes from a starting point to an ending point.
        - Coordinates: (514, 600) is the starting point and (514, 200) is the ending point.
        - The swipe lasts for 1000 milliseconds.
        """
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 600, 514, 200, 1000)

    @staticmethod
    def swipeDown(howManySwipes, driver):
        """
        Performs a swipe down action on the screen a specified number of times.

        Args:
        howManySwipes (int): The number of times to perform the swipe down action.
        driver: The Appium driver used for interacting with the Android app.

        Explanation:
        - Coordinates: (514, 500) is the starting point and (514, 800) is the ending point.
        """
        for i in range(1, howManySwipes + 1):
            driver.swipe(514, 500, 514, 800, 1000)

    @staticmethod
    def swipeLeft(howManySwipes, driver):
        """
        Performs a swipe left action on the screen a specified number of times.

        Args:
        howManySwipes (int): The number of times to perform the swipe left action.
        driver: The Appium driver used for interacting with the Android app.

        Explanation:
        - Coordinates: (900, 600) is the starting point and (200, 600) is the ending point.
        """
        for i in range(1, howManySwipes + 1):
            driver.swipe(900, 600, 200, 600, 1000)

    @staticmethod
    def swipeRight(howManySwipes, driver):
        """
        Performs a swipe right action on the screen a specified number of times.

        Args:
        howManySwipes (int): The number of times to perform the swipe right action.
        driver: The Appium driver used for interacting with the Android app.

        Explanation:
        - Coordinates: (200, 600) is the starting point and (900, 600) is the ending point.
        """
        for i in range(1, howManySwipes + 1):
            driver.swipe(200, 600, 900, 600, 1000)
