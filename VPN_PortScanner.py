#!/usr/bin/env python
import socket
import time
import os


def port_scan(ip_address, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((ip_address, port))
        if result == 0:
            return True
        else:
            return False
        sock.close()
    except socket.error:
        return False


def main():
    ip_address = input("Enter IP address to scan: ")
    port_range = input("Enter port range to scan (e.g. 1-100): ")
    use_vpn = input("Do you want to use VPN? (y/n): ")

    if use_vpn.lower() == 'y':
        vpn_config_path = input("Enter the path to the VPN configuration file: ")

        # Activate the VPN connection using the specified path
        sudo_command = f"sudo openvpn {vpn_config_path} --daemon"
        os.system(f"{sudo_command}")
        print("Connecting to VPN...")
        print("VPN activated successfully!")
    else:
        print("VPN not activated.")
        # wait for VPN connection to establish
        time.sleep(10)

    start_port, end_port = port_range.split('-')
    start_port, end_port = int(start_port), int(end_port)

    print(f"Scanning {ip_address} for open ports...")

    open_ports = []

    for port in range(start_port, end_port + 1):
        if port_scan(ip_address, port):
            open_ports.append(port)

    if len(open_ports) > 0:
        print("The following ports are open: ")
        for port in open_ports:
            print(port)
    else:
        print("No open ports found.")


if __name__ == "__main__":
    main()
