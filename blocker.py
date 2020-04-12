import time
from datetime import datetime

hosts_temp = "hosts"
hosts_path = "/etc/hosts"
redirect = "127.0.0.1"
websites_file = "websites.txt"

while True:
    if datetime(datetime.now().year, datetime.now().month, datetime.now().day, 0) < datetime.now() < datetime(
            datetime.now().year, datetime.now().month, datetime.now().day,2):
        with open(hosts_path, "r+") as hosts_file:
            with open(websites_file, "r") as web_file:
                content1 = hosts_file.read()
                content2 = web_file.readlines()
                for website in content2:
                    if website in content1:
                        pass
                    else:
                        hosts_file.write(redirect + " " + website)

    else:
        with open(hosts_path, "r+") as hosts_file:
            with open(websites_file, "r+") as web_file:
                content1 = hosts_file.readlines()
                content2 = web_file.readlines()
                hosts_file.seek(0)
                for line in content1:
                    if not any(website in line for website in content2):
                        hosts_file.write(line)

                hosts_file.truncate()
    time.sleep(60)
