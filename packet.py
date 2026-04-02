def create_packet(address, content):
    packet = []

    # Start byte ':'
    packet.append(ord(':'))

    # Length (2 bytes)
    length = len(content)
    packet.append((length >> 8) & 0xFF)  # MSB
    packet.append(length & 0xFF)         # LSB

    # Address (2 bytes)
    packet.append((address >> 8) & 0xFF)
    packet.append(address & 0xFF)

    # Type
    packet.append(0x00)

    # Content
    packet.extend(content)

    # Checksum (pa ':')
    checksum_data = packet[1:]
    total = sum(checksum_data)
    checksum = (256 - (total % 256)) % 256

    packet.append(checksum)

    return packet


# TEST
p = create_packet(1, [5, 6])
print(p)
