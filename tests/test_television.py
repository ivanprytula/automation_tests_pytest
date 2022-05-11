from pytest import mark


# @mark.skip
# @mark.parametrize("tv_brand", [
#     ("Samsung", 1),
#     ("Sony", 2),
#     ("Vizio", 3),
# ])
@mark.skip
@mark.tv_test
def test_television_turns_on(tv_brand):
    print(f"{tv_brand} turns on as expected")


#     assert ...
# @mark.tv_test
@mark.skip
def test_browser_can_navigate_to_training_ground(browser):
    browser.get("https://techacademy.com/training-ground")
