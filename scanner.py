import time
from concurrent.futures import ThreadPoolExecutor
from socket import AF_INET, SOCK_STREAM, socket


def scan_port(target, port):
    """
    Scan a single port on the target host.
    Args:
        target (str): The IP address of the target host.
        port (int): The port number to scan.
    """
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(0.3)
    connection = sock.connect_ex((target, port))
    if connection == 0:
        print("Port %d: OPEN" % (port,))
    sock.close()


def main():
    """
    Main function to initiate port scanning.
    This function prompts the user to enter the IP address of the target host and starts scanning ports.
    It utilizes ThreadPoolExecutor to concurrently scan ports for faster execution.
    """
    target = input("Enter the host IP adrress to be scanned: ")
    print("Starting scan host: ", target)

    with ThreadPoolExecutor(max_workers=1000) as executor:
        futures = [executor.submit(scan_port, target, port) for port in range(1, 10000)]


if __name__ == "__main__":
    start_time = time.time()
    main()
    print(f"Time: {round(time.time() - start_time, 2)} secs")
