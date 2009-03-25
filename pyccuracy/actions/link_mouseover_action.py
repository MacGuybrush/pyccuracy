import os
import sys
sys.path.insert(0,os.path.abspath(__file__+"/../../../"))
from pyccuracy.page import Page
from pyccuracy.actions.action_base import ActionBase
from pyccuracy.actions.element_is_visible_base import *

class LinkMouseoverAction(ActionBase):
    def __init__(self, browser_driver, language):
        super(LinkMouseoverAction, self).__init__(browser_driver, language)

    def matches(self, line):
        reg = self.language["link_mouseover_regex"]
        self.last_match = reg.search(line)
        return self.last_match

    def values_for(self, line):
        return self.last_match and (self.last_match.groups()[1],) or tuple([])

    def execute(self, values, context):
        link_name = values[0]
        link = self.resolve_element_key(context, Page.Link, link_name)
        self.assert_element_is_visible(link, self.language["link_is_visible_failure"] % link_name)
        self.browser_driver.mouseover_element(link)
        