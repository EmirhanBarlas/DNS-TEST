import socket

def check_dns_status(domain_or_ip):
    try:
        result = socket.getaddrinfo(domain_or_ip, None)
        for res in result:
            print(f"Address: {res[4][0]} - Active")
    except socket.gaierror:
        print("DNS not active or invalid domain/ip.")
domain_or_ip = input("Enter a domain name or an IP address: ") 
check_dns_status(domain_or_ip)
