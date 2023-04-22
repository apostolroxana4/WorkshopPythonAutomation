import pytest
from driver.driver import Driver
from actions.actions_text_box import Actions
from pages.elements import StepsElements


@pytest.mark.usefixtures("browser")
class TestAssertCheckboxDownloads:
    actions = Actions()
    steps_elements = StepsElements()

