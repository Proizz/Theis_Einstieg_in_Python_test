import time, threading

def thread_ablauf():
    print("Start Thread")
    for i in range(5):
        print(i, time.time())
        time.sleep(1.5)
    print("Ende Thread")

print("Start Hauptprogramm")
t = threading.Thread(target=thread_ablauf)
t.start()
time.sleep(10)
print("Ende Hauptprogramm")
