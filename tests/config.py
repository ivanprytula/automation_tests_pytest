# Customizing Test Runs with the Command Line and Configuration Files
class Config:
    def __init__(self, env: str) -> None:
        # SUPPORTED_ENVS = ["dev", "qa"]
        # if env.lower() not in SUPPORTED_ENVS:
        #     raise Exception(f"{env} is not supported env...")

        self.base_url = {
            "dev": "https://mydev-dev.com",
            "qa": "https://mydev-qa.com",
        }[env]

        self.app_port = {
            "dev": 8080,
            "qa": 80
        }[env]
