import threading

def run():
    print("thread")

t=threading.Thread(target=run)
t.start()
t.join()