import sys
from datetime import datetime
import socket
import threading


#Function to scan a port

def scan_port(target,port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((target,port)) #error indicator
        if result == 0:
            print(f"Port {port} is open")
        s.close()

    except socket.error as e:
        print(f"Socket errror on port {port}: {e}") 
    except exception as e:
        print(f"Unexpected error on port {port: {e}}")

# main function - argument validation and target definition
def main():
    if len(sys.argv) == 2:
        target = sys.argv[1]
    else:
        print("Invalid number of argument")
        print("Usage: python.exe scanner.py <target>")
        sys.exit(1)

#Resolve the target hostname to the ip address

    try: 
        target_ip = socket.gethostbyname(target)
    except socket.gaierror:
        print(f"Error: Unable to resolve hostname {target}")
        sys.exit(1)

    #add a pretty banner

    print("_"* 50)
    print(f"Scanning target  {target_ip}")
    print(f"Time started: {datetime.now()}")
    print("_"* 50)


    try:
        # Use multithreading to scan ports concurrently
        threads = []
        for port in range(1,65536):
            thread = threading.Thread(target=scan_port, args=(target_ip,port))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
        for thread in threads:
            thread.join()
    except KeyboardInterrupt:
        print("\n Exitting program")
        sys.exit(0)
    
    except socket.error as e:
        print(f"Socket error: {e}")
        sys.exit(1)

    print("\m Scan completed")

if __name__ == "__main__":
    main()


