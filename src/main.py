import socket

test_site = 'www.google.com'
test_port = 80


def service_exists(host, port):
    try:
        host_addr = socket.gethostbyname(host)
        captive_dns_addr = socket.gethostbyname("FalseDomainThatDoesntExist.com")
        if captive_dns_addr == host_addr:
            return False
    except:
        pass

    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        s.close()
    except:
        return False

    return True

print(service_exists(test_site, test_port))
