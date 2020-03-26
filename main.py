from selenium import webdriver
from multiprocessing import Process
import sys

procs = []
file , url ,count = sys.argv

def openWeb(index):
    browser = webdriver.Firefox(executable_path=r'./geckodriver')
    browser.get(url)
    browser.quit()

    print("url : %s #%s Complete"%(url, index))


if __name__ == "__main__":
    print("arguments : ")
    print(sys.argv)
    for i in range(int(count)):
        proc = Process(target=openWeb, args=(i,))
        procs.append(proc)
        proc.start()
    for proc in procs:
        proc.join()
