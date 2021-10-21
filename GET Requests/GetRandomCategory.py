import time
import uuid
import requests
import threading
import csv
import random
from Tools.Utility import Utility as Uti
import logging

url = "http://sk-cat-stg.safekiddo.net/api/v1/categorize-url"
auth_input = ('test', '123')


def request_for_test(index, list_of_url, array):

    print("Request: " + str(index))
    logging.info("Request: " + str(index))

    start_time = time.time()
    cathegorized_url = random.choice(list_of_url)
    hash_code = "36c71541-89b0-4636-81d2-5ee8bc47d55f"

    print(cathegorized_url)

    params = {"url": cathegorized_url}
    headers = {"AuthHash": Uti.generate_hash(cathegorized_url, hash_code),
               "Idempotency-Key": str(uuid.uuid1())}

    response = requests.post(url, auth=auth_input,
                             params=params,
                             headers=headers,
                             verify=False,
                             allow_redirects=False)

    status_code_msg = "Response status code: " + str(response.status_code)
    print(status_code_msg)
    logging.info(status_code_msg)

    content_msg = "Content of the request no. " + str(index) + ": " + str(response.content)
    print(content_msg)
    logging.info(content_msg)

    end_time = time.time()

    duration = end_time - start_time
    time_elapsed_msg = "Request executed in :" + "%.3f" % duration + "\n"
    print(time_elapsed_msg)
    logging.info(time_elapsed_msg)

    array.append(duration)


if __name__ == "__main__":
    websites = []
    array = []

    logging.basicConfig(filename='timelog.log',
                        filemode='a',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.INFO)

    with open('URLS.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=' ')
        for row in reader:
            websites.append(row[0])
    threads =[]
    for x in range(1):
        t1 = threading.Thread(target=request_for_test(x, websites, array))
        if x != 0:
            time.sleep(1/x)
        t1.start()

    duration = 0.0
    for element in array:
        duration +=element

    # all threads completely executed
    print("Done!")
    print("Total time for execution "+str(duration))
    logging.info("Total time for execution "+str(duration))
