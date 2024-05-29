import time

from selenium.webdriver.common.by import By

from datas.fake import job
from pages.catalog_page import CatalogPage


class TestProductCatalog:

    def test_new_category_displayed(self, browser, authorization):
        catalog = CatalogPage(browser)
        cat_name = job()

        catalog.open_catalog_page()

        catalog.create_category()

        catalog.input_category_name("asdfasd")


        catalog.click_create_category()

        category_name = browser.find_elements(By.CSS_SELECTOR,
                                              'div[class="MuiDataGrid-treeDataGroupingCell MuiBox-root css-61mbqb"]')
        time.sleep(3)
        for name in category_name:
            assert cat_name in name.text
