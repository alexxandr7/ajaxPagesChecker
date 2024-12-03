from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import argparse
from colorama import init, Fore, Back
from colorama import Style
import os

init(autoreset=True)

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-u', '--urls', metavar='File', type=str, help="Check pages from file", required=True)
    parser.add_argument('-cl', action="store_true", help="Get page length", required=False)
    parser.add_argument('-ew', metavar='Error-words', help="Filter by Error-words", required=False)
    parser.add_argument('-sp', action="store_true", help="Take a screenshot of pages", required=False)  
    args = parser.parse_args()
    return args


def get_page(url):
    driver.get(url)
    rendered_page = str(driver.page_source.encode("utf-8"))
    return rendered_page


def take_screenshot(url):
    if not os.path.isdir("checker_screenshots"):
        os.mkdir("checker_screenshots")
    filename = f"checker_screenshots/{''.join(url.split('/'[-1]))}.png"
    driver.save_screenshot(filename)


def check_page(renderedPage, url):
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
    getScreenshot = args.sp

    chrome_options = Options()
    chrome_options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=chrome_options)
    
    with open(urlsFile, "r") as file:
        urls_for_scan = list(map(lambda x: x[:-1], file.readlines()))
        for scanned_url in urls_for_scan:
            page = get_page(scanned_url)
            if errorWords != None or getContentLength:
                result = check_page(page, scanned_url)
                print(result)
            if getScreenshot:
                take_screenshot(scanned_url) 
            

    driver.quit()