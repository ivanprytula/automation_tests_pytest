from pytest import mark


@mark.skip
@mark.env
# @mark.skip(reason="broken by deploy sha:xxxxx")
@mark.xfail(reason="Env just like this....")
def test_environment_is_qa(app_config):
    # assert env == "qa"
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://mydev-qa.com"
    assert port == 80


@mark.skip
@mark.env
def test_environment_is_dev(app_config):
    # assert env == "dev"
    base_url = app_config.base_url
    port = app_config.app_port
    assert base_url == "https://mydev-dev.com"
    assert port == 8080
