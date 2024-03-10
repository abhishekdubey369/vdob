def get_ip_details(ip_address):
    # Split the IP address by '.'
    octets = ip_address.split('.')

    # Convert each octet to an integer
    octet1 = int(octets[0])
    
    # Initialize variables for network bits and class bits
    network_bits = 0
    class_bits = 0

    # Check the class of the IP address and set network bits and class bits
    if octet1 >= 1 and octet1 <= 126:
        ip_class = 'A'
        network_bits = 8
        class_bits = 7
        subnet_mask = '255.0.0.0'
        num_hosts = 2 ** 24 - 2  # -2 for network and broadcast addresses
        num_networks = 2 ** 7 - 2  # -2 for reserved networks
        host_bits = 24
        reserved_addresses = 2
        multicast_addresses = 0  # No multicast addresses in Class A
        fixed_class_bits = 8
        network_id = octets[0]
        host_id = '.'.join(octets[1:])
        ip_range = f'{network_id}.0.0.1 - {network_id}.255.255.254'
    elif octet1 >= 128 and octet1 <= 191:
        ip_class = 'B'
        network_bits = 16
        class_bits = 14
        subnet_mask = '255.255.0.0'
        num_hosts = 2 ** 16 - 2  # -2 for network and broadcast addresses
        num_networks = 2 ** 14 - 2  # -2 for reserved networks
        host_bits = 16
        reserved_addresses = 2
        multicast_addresses = 0  # No multicast addresses in Class B
        fixed_class_bits = 16
        network_id = '.'.join(octets[:2])
        host_id = '.'.join(octets[2:])
        ip_range = f'{network_id}.0.1 - {network_id}.255.254'
    elif octet1 >= 192 and octet1 <= 223:
        ip_class = 'C'
        network_bits = 24
        class_bits = 21
        subnet_mask = '255.255.255.0'
        num_hosts = 2 ** 8 - 2  # -2 for network and broadcast addresses
        num_networks = 2 ** 21 - 2  # -2 for reserved networks
        host_bits = 8
        reserved_addresses = 2
        multicast_addresses = 0  # No multicast addresses in Class C
        fixed_class_bits = 24
        network_id = '.'.join(octets[:3])
        host_id = octets[3]
        ip_range = f'{network_id}.1 - {network_id}.254'
    elif octet1 >= 224 and octet1 <= 239:
        ip_class = 'D (Multicast)'
        subnet_mask = 'N/A'
        num_hosts = 'N/A'
        num_networks = 'N/A'
        network_bits = 'N/A'
        class_bits = 'N/A'
        host_bits = 'N/A'
        reserved_addresses = 'N/A'
        multicast_addresses = 'N/A'
        fixed_class_bits = 'N/A'
        network_id = 'N/A'
        host_id = 'N/A'
        ip_range = 'N/A'
    elif octet1 >= 240 and octet1 <= 255:
        ip_class = 'E (Reserved)'
        subnet_mask = 'N/A'
        num_hosts = 'N/A'
        num_networks = 'N/A'
        network_bits = 'N/A'
        class_bits = 'N/A'
        host_bits = 'N/A'
        reserved_addresses = 'N/A'
        multicast_addresses = 'N/A'
        fixed_class_bits = 'N/A'
        network_id = 'N/A'
        host_id = 'N/A'
        ip_range = 'N/A'
    else:
        ip_class = 'Invalid'
        subnet_mask = 'N/A'
        num_hosts = 'N/A'
        num_networks = 'N/A'
        network_bits = 'N/A'
        class_bits = 'N/A'
        host_bits = 'N/A'
        reserved_addresses = 'N/A'
        multicast_addresses = 'N/A'
        fixed_class_bits = 'N/A'
        network_id = 'N/A'
        host_id = 'N/A'
        ip_range = 'N/A'

    # Calculate network address
    network_address = '.'.join([str(int(octets[i]) & int(subnet_mask.split('.')[i])) for i in range(4)])

    # Calculate broadcast address
    broadcast_address = '.'.join([str(int(octets[i]) | (255 - int(subnet_mask.split('.')[i]))) for i in range(4)])

    # Calculate first usable host address
    first_host_address = '.'.join([str(int(octets[i]) & int(subnet_mask.split('.')[i])) for i in range(4)])
    first_host_address = first_host_address.rsplit('.', 1)[0] + '.' + str(int(first_host_address.rsplit('.', 1)[1]) + 1)

    # Calculate last usable host address
    last_host_address = broadcast_address.rsplit('.', 1)[0] + '.' + str(int(broadcast_address.rsplit('.', 1)[1]) - 1)

    return ip_class, network_id, host_id, subnet_mask, network_address, broadcast_address, first_host_address, last_host_address, num_hosts, ip_range, network_bits, class_bits, num_networks, host_bits, reserved_addresses, multicast_addresses, fixed_class_bits

# Accept user input for IP address
ip_address = input("Enter an IP address: ")

# Get details of the IP address
(ip_class, network_id, host_id, subnet_mask, network_address, broadcast_address, first_host_address,
 last_host_address, num_hosts, ip_range, network_bits, class_bits, num_networks, host_bits,
 reserved_addresses, multicast_addresses, fixed_class_bits) = get_ip_details(ip_address)

# Display the details
print("IP Class:", ip_class)
print("Network ID:", network_id)
print("Host ID:", host_id)
print("Subnet Mask:", subnet_mask)
print("Network Address:", network_address)
print("Broadcast Address:", broadcast_address)
print("First Usable Host Address:", first_host_address)
print("Last Usable Host Address:", last_host_address)
print("Number of Hosts:", num_hosts)
print("IP Range:", ip_range)
print("Network Bits:", network_bits)
print("Class Bits:", class_bits)
print("Total Number of Networks:", num_networks)
print("Number of Host Bits:", host_bits)
print("Reserved Addresses:", reserved_addresses)
# print("Multicast Addresses:", multicast_addresses)
print("Total Number of Fixed Class Bits:", fixed_class_bits)