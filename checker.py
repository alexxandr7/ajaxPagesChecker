from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
from colorama import init, Fore, Back
from colorama import Style

init(autoreset=True)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', metavar='File', type=str, help="Check pages from file", required=True)
    parser.add_argument('-cl', action="store_true", help="Get page length", required=False)
    parser.add_argument('-ew', metavar='Error-words', help="Filter by Error-words", required=False)    
    args = parser.parse_args()
    return args


def get_page(url):
    driver.get(url)
    rendered_page = str(driver.page_source.encode("utf-8"))
    return rendered_page


def check_page(url):
    renderedPage = get_page(url)
    isErrorPage, pageLength = None, None
    if errorWords != None:
        isErrorPage = errorWords in renderedPage
        text = f"{Fore.RED + '[-]' if isErrorPage else Fore.WHITE + '[+]'} {url}"
    if getContentLength:
        pageLength = len(renderedPage)
        text = f"{url}, Length: {pageLength}"
    if isErrorPage != None and pageLength != None:
        text = f"{Fore.RED + '[-]' if isErrorPage else Fore.WHITE + '[+]'} {url}, Length: {pageLength}"
    return text


if __name__ == "__main__":
    args = get_args()
    urlsFile = args.urls
    getContentLength = args.cl
    errorWords = args.ew

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    
    with open(urlsFile, "r") as file:
        urls_for_scan = list(map(lambda x: x[:-1], file.readlines()))
        for scanned_url in urls_for_scan:
            result = check_page(scanned_url)
            print(result)

    driver.quit()