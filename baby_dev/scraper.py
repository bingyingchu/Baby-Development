import selectorlib
import time
import pickle
import zmq
import requests

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5557")

HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/107.0.0.0 Safari/537.36"}


# receive a list of strings and sends back a list of strings
def scrape(url, option):
    """
    scrape info from a webpage(use python to grab HTML) and store it into sqlite database
    """
    response = requests.get(url, headers=HEADERS)
    source = response.text
    extractor = selectorlib.Extractor.from_yaml_file("extract.yaml")
    size = extractor.extract(source)["size"]
    glance = extractor.extract(source)["glance"]
    if option == 1:
        return size
    if option == 2:
        return glance
    return size + glance


if __name__ == "__main__":
    while True:
        data = pickle.loads(socket.recv())
        week, choice = data[0], data[1]
        time.sleep(1)
        if week == 1 or week == 2:
            URL = "https://www.whattoexpect.com/pregnancy/week-by-week/weeks-1-and-2.aspx"
        else:
            URL = f"https://www.whattoexpect.com/pregnancy/week-by-week/week-{data[0]}.aspx"

        extracted = pickle.dumps(scrape(URL, choice))
        socket.send(extracted)

