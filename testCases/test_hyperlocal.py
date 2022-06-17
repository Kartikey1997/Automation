import time

from pageObjects.hyperlocal_pages import Hyperlocal

class Test_nearby:

    def test_nearby_popular_area(self,setup):
        self.driver=setup
        hype = Hyperlocal(self.driver)
        hype.get_cityPage_url()
        hype.get_nearby_section()
