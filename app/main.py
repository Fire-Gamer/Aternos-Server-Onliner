from selenium import webdriver
from argparse import ArgumentParser

PATH = "./libs/chromedriver.exe"
SERVER_ADDRESS = "https://aternos.org/servers/"

driver = webdriver.Chrome(PATH)


def check_login() -> bool:
    """Checks if logged in

    Returns:
        bool: logged or not
    """
    driver.get(SERVER_ADDRESS)
    title = str(driver.title())
    if title.find("Login") != -1:
        return False
    return True


def args():
    parser = ArgumentParser(help="An app to start aternos server")
    subparsers = parser.add_subparsers(dest="cmd")

    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("name", help="The server name")

    return parser.parse_args()


def main():
    try:
        if check_login():
            pass
        else:
            raise Exception("Not logged in")
    except Exception as e:
        print(f"Error {e} has occurred")
