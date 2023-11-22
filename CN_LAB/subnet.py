def calculate_subnet_mask(prefix_length):
    subnet_mask = (0xFFFFFFFF << (32 - prefix_length)) & 0xFFFFFFFF
    subnet_mask_str = ".".join(str((subnet_mask >> i) & 0xFF) for i in [24, 16, 8, 0])
    return subnet_mask_str

def demonstrate_subnetting(base_ip_address, prefix_length):
    subnet_mask = calculate_subnet_mask(prefix_length)
    print("Base IP Address: " + base_ip_address)
    print("Prefix Length: /" + str(prefix_length))
    print("Subnet Mask: " + subnet_mask)

# Example usage
if __name__ == "__main__":
    base_ip_address = "192.168.1.0"
    network_prefix_length = 24  # For example, use a /24 network

    demonstrate_subnetting(base_ip_address, network_prefix_length)

Absolutely! Subnetting is a technique used in computer networking to divide a single large
network into smaller networks, called subnets. This practice helps efficiently utilize IP 
addresses and manage network traffic more effectively.

The basic idea behind subnetting involves manipulating the subnet mask, which is typically 
represented in dotted-decimal notation (e.g., 255.255.255.0 for a /24 subnet).

Let's discuss the core concepts:

Understanding IP Addresses and Subnet Masks
IP addresses are composed of two parts: the network part and the host part. The subnet mask 
determines the boundary between these two parts.

For example, in an IPv4 address like 192.168.1.0/24:

192.168.1 is the network part.
0 is the host part.
CIDR Notation
CIDR (Classless Inter-Domain Routing) notation is a compact representation of an IP address 
and its associated network prefix length. For instance:

192.168.1.0/24 means the first 24 bits of the IP address are used for network identification,
and the remaining 8 bits are used for hosts.
/24 indicates that the first 24 bits of the address are the network address, represented by 
the subnet mask 255.255.255.0.
Calculating the Subnet Mask
To calculate the subnet mask in Python, you can use bitwise operations:

python
Copy code
def calculate_subnet_mask(prefix_length):
    subnet_mask = (1 << 32 - prefix_length) - 1
    subnet_mask_str = ".".join(str((subnet_mask >> i) & 0xFF) for i in [24, 16, 8, 0])
    return subnet_mask_str
Let's break down the function calculate_subnet_mask():

(1 << 32 - prefix_length) - 1: This creates a mask by left-shifting 1 by 32 - prefix_length 
positions and subtracting 1. This generates a binary number representing the subnet mask with 
prefix_length 1s followed by 32 - prefix_length 0s.
The subsequent line formats this binary number into a dotted-decimal notation.
Demonstration
The demonstrate_subnetting() function displays the base IP address, prefix length, and calculated 
subnet mask using the calculate_subnet_mask() function.

Practical Example
Let's say you have an IP address 192.168.1.0 and want to create a subnet with a prefix length of
/24. By calling calculate_subnet_mask(24), you'd obtain the subnet mask 255.255.255.0.

Understanding subnetting is crucial in networking, especially when designing network architectures
or troubleshooting network-related issues. Practice with different IP addresses and prefix lengths to 
get a better grasp of subnetting concepts and their applications in networking scenarios.

IP Addresses:
An IP (Internet Protocol) address is a numerical label assigned to devices (computers, printers,
etc.) connected to a network. It enables communication and identification within a network.

Subnetting:
Subnetting is the process of dividing a large IP network into smaller sub-networks (subnets). It 
enables efficient utilization of IP addresses, better organization of network traffic, and
improved security by logically partitioning a network.

Subnet Mask:
A subnet mask is a 32-bit number that divides an IP address into network and host portions. 
It determines the boundaries between the network and host parts by using 1s and 0s. A subnet 
mask consists of consecutive 1s followed by consecutive 0s. For example:

A subnet mask of 255.255.255.0 (or /24 in CIDR notation) means the first 24 bits are the network 
part, and the last 8 bits are for hosts.
A subnet mask of 255.255.255.192 (or /26 in CIDR notation) indicates the first 26 bits for the
network and the remaining 6 bits for hosts.
IP Address Classes:
IP addresses are classified into different classes based on their leading bits. There are five
IP address classes: A, B, C, D, and E. However, classes A, B, and C are primarily used.

Class A: Addresses start with a 0 in the first bit (0.0.0.0 to 127.255.255.255). Class A networks 
are large and suitable for big organizations. Example: 10.0.0.0/8 (or 10.0.0.0 with subnet mask 255.0.0.0).

Class B: Addresses start with binary 10 (128.0.0.0 to 191.255.255.255). Class B networks are 
medium-sized and fit for mid-sized companies. Example: 172.16.0.0/16 (or 172.16.0.0 with subnet
mask 255.255.0.0).

Class C: Addresses start with binary 110 (192.0.0.0 to 223.255.255.255). Class C networks are 
small and commonly used for small businesses. Example: 192.168.0.0/24 (or 192.168.0.0 with subnet 
mask 255.255.255.0).

Example:
Let's consider an IP address 192.168.1.0 with a subnet mask of 255.255.255.0 (or /24). 
It belongs to the Class C range and provides 254 usable IP addresses for hosts (192.168.1.1
to 192.168.1.254). The remaining addresses (192.168.1.0 and 192.168.1.255) are reserved for 
network address and broadcast address respectively.

This understanding helps in designing networks, allocating IP addresses, and creating subnets
efficiently. Remembering examples like 192.168.1.0/24 and associating them with specific network 
sizes (Class C with 254 hosts) aids in recalling subnetting concepts.





