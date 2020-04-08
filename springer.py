from selenium import webdriver
import unittest

class Testuser_journey_search(unittest.TestCase):
    driver = webdriver.Chrome(
        executable_path="./chromedriver")  # Opens the Browser in a new window - Cleared Cache !


    def setUp(self):

        self.driver.get("https://link.springer.com")
        self.driver.maximize_window()

    def test_searchbox_alpha_num(self):
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys("A Classified Bibliography of the History of Dutch Medicine 1900–1974")
        self.driver.find_element_by_id("search").click()
        webelement_result = self.driver.find_element_by_xpath(".//*[@class='title']").text
        self.assertEqual(webelement_result,"A Classified Bibliography of the History of Dutch Medicine 1900–1974")
        self.assertGreaterEqual(int("".join(
            str(self.driver.find_element_by_id("number-of-search-results-and-search-terms").text).split(" ")[0].split(
                ",")[0:])), 0)

    def test_searchbox_alpha(self):
        self.driver.find_element_by_id("query").clear()
        self.driver.find_element_by_id("query").send_keys("Indian Journal of Microbiology")
        self.driver.find_element_by_id("search").click()
        webelement_result = self.driver.find_element_by_xpath(".//*[@class='title']").text
        self.assertEqual(webelement_result,"Indian Journal of Microbiology")
        self.assertGreaterEqual(int("".join(
            str(self.driver.find_element_by_id("number-of-search-results-and-search-terms").text).split(" ")[0].split(
                ",")[0:])), 0)



    def test_searchbox_alpha_num_special(self):
        self.driver.find_element_by_id("query").send_keys("19%")
        self.driver.find_element_by_id("search").click()
        webelement_result = self.driver.find_element_by_xpath(".//*[@class='title']").text
        self.assertEqual(webelement_result,"19%")
        self.assertGreaterEqual(int("".join(
            str(self.driver.find_element_by_id("number-of-search-results-and-search-terms").text).split(" ")[0].split(
                ",")[0:])), 0)

    def test_searchbox_space(self):
        self.driver.find_element_by_id("query").send_keys("     ") #Entering Space
        self.driver.find_element_by_id("search").click()
        webelement_result = self.driver.find_element_by_xpath(".//*[@class='title']").text
        self.assertGreaterEqual(int("".join(
            str(self.driver.find_element_by_id("number-of-search-results-and-search-terms").text).split(" ")[0].split(
                ",")[0:])), 0)




unittest.main()
