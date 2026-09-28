import socket
import sys
from urllib.parse import urlparse


def resolve_host(target: str) -> None:
    parsed = urlparse(target if "://" in target else f"//{target}")
    host = parsed.hostname
    if not host:
        raise ValueError("Could not determine a hostname.")

    print(f"Host: {host}")
    print(f"IPv4: {socket.gethostbyname(host)}")

    infos = socket.getaddrinfo(host, None, socket.AF_UNSPEC, socket.SOCK_STREAM)
    addresses = sorted({info[4][0] for info in infos})
    print("Resolved addresses:")
    for address in addresses:
        print(f"  - {address}")


def check_port(host: str, port: int, timeout: float = 1.0) -> bool:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.settimeout(timeout)
        return sock.connect_ex((host, port)) == 0


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python network_tool.py example.com [port ...]")
        raise SystemExit(1)

    target = sys.argv[1]
    resolve_host(target)

    parsed = urlparse(target if "://" in target else f"//{target}")
    host = parsed.hostname
    ports = [int(value) for value in sys.argv[2:]]

    if ports:
        print("\nTCP checks:")
        for port in ports:
            state = "OPEN" if check_port(host, port) else "closed/unreachable"
            print(f"  {port:>5}: {state}")


if __name__ == "__main__":
    main()
