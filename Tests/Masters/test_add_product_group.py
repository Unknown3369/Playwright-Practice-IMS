import random
import uuid
import pytest

from Pages.Login import login
from Pages.Masters.add_product_group import (AddProductGroupMasterPage)


def random_group_name():
   return f"Group_{uuid.uuid4().hex[:6]}"


def test_add_product_group_master(page):

   login_page = login(page)

   try:
      login_page.perform_login("Testuser","Test@1234")

      add_group = AddProductGroupMasterPage(page)
      add_group.navigate_to_add_product()
      add_group.select_item_group()

      add_group.fill_group_details_and_save(
         group_name=random_group_name(),
         recommended_margin=random.randint(5, 20),
         shelf_life=random.randint(15, 90)
      )
      print("Product Group Added Successfully")

   except Exception as e:
      pytest.fail(
         f"Test failed due to: {str(e)}"
      )