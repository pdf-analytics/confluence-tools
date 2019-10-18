import configparser
import json

from bs4 import BeautifulSoup
from atlassian import Confluence


class ConfluencePlayground():

    def __init__(self):
        conf = configparser.ConfigParser()
        conf.read('credentials.ini')
        self.site = Confluence(url=conf.get('CONFLUENCE', 'url'),
                                     username=conf.get('CONFLUENCE', 'username'),
                                     password=conf.get('CONFLUENCE', 'password')
                                     )

    def get_rnu_in_page(self, page_id, rnu_id):
        """Get the the data from a ‘QC - Read and Understood’ Macro"""
        # Get context page
        page = self.site.get_page_by_id(page_id, expand='body.export_view')
        page_cnt = page['body']['export_view']['value']

        # Parse the HMTL
        soup = BeautifulSoup(page_cnt, "lxml")

        # Get data from span element
        div_elm = soup.find("div", text="read-and-understood-data-{id}".format(id=rnu_id))
        parent_elm = div_elm.parent
        span_elem = parent_elm.find("span")
        return json.loads(span_elem.get_text())


playground = ConfluencePlayground()
rnu_dictionary = playground.get_rnu_in_page(page_id=775585805, rnu_id=775585805)
print(rnu_dictionary)

