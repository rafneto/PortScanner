from socket import *
import time

start_time=time.time()

if __name__ == '__main__':
    target = input("Enter the host IP adrress to be scanned: ")
    print("Starting scan host: ", target)
    
    for i in range(1, 10000):
        sock = socket(AF_INET, SOCK_STREAM)
        sock.settimeout(.3)
        connection = sock.connect_ex((target, i))
        if (connection == 0):
            print("Port %d: OPEN" % (i,))
        sock.close()
print("Time:", time.time() - start_time)