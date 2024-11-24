def add(arg1, arg2):
    """
    Generates an opcode for the ADD instruction.
    The first 2 bits are 00, the next 3 bits are arg1, 
    and the final 3 bits are arg2.

    Args:
        arg1 (int): The first argument (0-7).
        arg2 (int): The second argument (0-7).

    Returns:
        int: The generated opcode as an 8-bit integer.

    Raises:
        ValueError: If arguments are not in the range 0-7.
    """
    # Validate the arguments
    if not (0 <= arg1 <= 7):
        raise ValueError(f"arg1 must be between 0 and 7. Received: {arg1}")
    if not (0 <= arg2 <= 7):
        raise ValueError(f"arg2 must be between 0 and 7. Received: {arg2}")
    
    # Construct the opcode: 00 | arg1 (3 bits) | arg2 (3 bits)
    opcode = (0b00 << 6) | (arg1 << 3) | arg2

    return opcode

def sub(arg1, arg2):
    """
    Generates an opcode for the ADD instruction.
    The first 2 bits are 00, the next 3 bits are arg1, 
    and the final 3 bits are arg2.

    Args:
        arg1 (int): The first argument (0-7).
        arg2 (int): The second argument (0-7).

    Returns:
        int: The generated opcode as an 8-bit integer.

    Raises:
        ValueError: If arguments are not in the range 0-7.
    """
    # Validate the arguments
    if not (0 <= arg1 <= 7):
        raise ValueError(f"arg1 must be between 0 and 7. Received: {arg1}")
    if not (0 <= arg2 <= 7):
        raise ValueError(f"arg2 must be between 0 and 7. Received: {arg2}")
    
    # Construct the opcode: 00 | arg1 (3 bits) | arg2 (3 bits)
    opcode = (0b01 << 6) | (arg1 << 3) | arg2

    return opcode

def mov(arg1, arg2):
    """
    Generates an opcode for the ADD instruction.
    The first 2 bits are 00, the next 3 bits are arg1, 
    and the final 3 bits are arg2.

    Args:
        arg1 (int): The first argument (0-7).
        arg2 (int): The second argument (0-7).

    Returns:
        int: The generated opcode as an 8-bit integer.

    Raises:
        ValueError: If arguments are not in the range 0-7.
    """
    # Validate the arguments
    if not (0 <= arg1 <= 7):
        raise ValueError(f"arg1 must be between 0 and 7. Received: {arg1}")
    if not (0 <= arg2 <= 7):
        raise ValueError(f"arg2 must be between 0 and 7. Received: {arg2}")
    
    # Construct the opcode: 00 | arg1 (3 bits) | arg2 (3 bits)
    opcode = (0b10 << 6) | (arg1 << 3) | arg2

    return opcode

def get(register):
    """
    Generates an opcode for the GET instruction.
    The first 5 bits are 11100, and the next 3 bits are the register.

    Args:
        register (int): The target register (0-7).

    Returns:
        int: The generated opcode as an 8-bit integer.

    Raises:
        ValueError: If the register is not in the range 0-7.
    """
    # Validate the register
    if not (0 <= register <= 7):
        raise ValueError(f"Register must be between 0 and 7. Received: {register}")
    
    # Construct the opcode: 11100 | register (3 bits)
    opcode = (0b11100 << 3) | register

    return opcode


def print(register):
    """
    Generates an opcode for the PRINT instruction.
    The first 5 bits are 11101, and the next 3 bits are the register.

    Args:
        register (int): The target register (0-7).

    Returns:
        int: The generated opcode as an 8-bit integer.

    Raises:
        ValueError: If the register is not in the range 0-7.
    """
    # Validate the register
    # if not (0 <= register <= 7):
    #     raise ValueError(f"Register must be between 0 and 7. Received: {register}")
    
    # Construct the opcode: 11101 | register (3 bits)
    opcode = (0b11101 << 3) | register

    return opcode

def exit():
    """
    Generates the opcode for the EXIT instruction.
    The opcode is always 11111111.

    Returns:
        int: The generated opcode as an 8-bit integer (255).
    """
    # The EXIT opcode is fixed: 11111111
    return 0b11111111

def jl():
    return 0xfb

def jz():
    return 0xfa

def jmp():
    return 0xf9



def shift(register):
    # Validate register argument
    if not (0 <= register <= 7):
        raise ValueError(f"Register must be between 0 and 7. Received: {register}")
    
    # Construct the opcode: 11101 | register (3 bits)
    opcode = (0b11010 << 3) | register

    return opcode

def load_from(register):
    opcode = (0b11000 << 3) | register

    return opcode

def write_to(register):
    opcode = (0b11001 << 3) | register

    return opcode

def shift(register):
    opcode = (0b11010 << 3) | register

    return opcode

def call():
    return 0xfc

def ret():
    return 0xfd

def write_bytes_to_file(byte_list, filename):
    """
    Write a list of bytes to a file in binary format.

    Args:
        byte_list (list): A list of integers (bytes) to be written to the file.
        filename (str): The name of the file to write the binary data to.
    """
    with open(filename, 'wb') as f:
        for byte in byte_list:
            # Ensure that the byte is within the valid range (0-255)
            # if not (0 <= byte <= 255):
            #     raise ValueError(f"Invalid byte value: {byte}. It must be between 0 and 255.")
            # Write the byte to the file in binary format
            f.write(byte.to_bytes(1, byteorder='big'))  # 1 byte in big-endian order

    # print(f"Bytes written to {filename} successfully!")

# zero filled buffer of 64 bytes

data_map = {
    '0': 0,
    'a': 2,
    '\n': 4,
    '39': 6,
}


# '0', 'a', '\n', '39'
data = [0x30, 0x00, 0x61, 0x00, 0x0a, 0x00, 39, 0x00]

print_digit_off = 200
parse_digit_off = print_digit_off + 22
data_off = parse_digit_off + 23

main_code = [
    get(0),
    call(),
    parse_digit_off,
    0x80,
    mov(7, 0),
    add(0, 1),
    get(0),
    mov(0, 2),
    load_from(3),
    data_off + data_map['\n'],
    0x80,
    sub(3, 0),
    jz(),
    21,
    0x80,
    mov(2, 0),
    shift(1),
    4,
    jmp(),
    1,
    0x80,
    shift(2),
    16,
    get(0),
    call(),
    parse_digit_off,
    0x80,
    mov(7, 0),
    add(0, 2),
    get(0),
    mov(0, 3),
    load_from(4),
    data_off + data_map['\n'],
    0x80,
    sub(4, 0),
    jz(),
    44,
    0x80,
    mov(3, 0),
    shift(2),
    4,
    jmp(),
    24,
    0x80,
    add(1, 2),
    shift(4),
    16,
    mov(2, 0),
    shift(0),
    0xff - 12 + 1,
    shift(2),
    4,
    shift(1),
    16,
    sub(0, 1),
    jz(),
    65,
    0x80,
    load_from(4),
    data_off + data_map['39'],
    0x80,
    call(),
    print_digit_off,
    0x80,
    print(7),
    mov(2, 0),
    shift(0),
    0xff - 12 + 1,
    shift(2),
    4,
    shift(1),
    16,
    mov(4, 5),
    add(0, 5),
    jz(),
    84,
    0x80,
    load_from(4),
    data_off + data_map['39'],
    0x80,
    call(),
    print_digit_off,
    0x80,
    print(7),
    mov(2, 0),
    shift(0),
    0xff - 12 + 1,
    shift(2),
    4,
    shift(1),
    16,
    mov(4, 5),
    add(0, 5),
    jz(),
    84 + 19,
    0x80,
    load_from(4),
    data_off + data_map['39'],
    0x80,
    call(),
    print_digit_off,
    0x80,
    print(7),
    mov(2, 0),
    shift(0),
    0xff - 12 + 1,
    shift(2),
    4,
    shift(1),
    16,
    mov(4, 5),
    add(0, 5),
    jz(),
    84 + 19 + 19,
    0x80,
    load_from(4),
    data_off + data_map['39'],
    0x80,
    call(),
    print_digit_off,
    0x80,
    print(7),
    load_from(2),
    data_off + data_map['0'],
    0x80,
    load_from(0),
    data_off + data_map['39'],
    0x80,
    sub(0, 4),
    jz(),
    84 + 19 + 19 + 11,
    0x80,
    print(2),
    load_from(4),
    data_off + data_map['\n'],
    0x80,
    print(4),
    exit(),
]

print_digit_code = [
    mov(0, 2),
    load_from(1),
    data_off + data_map['\n'],
    0x80,
    sub(1, 0),
    jl(),
    14 + print_digit_off,
    0x80,
    load_from(1),
    data_off + data_map['a'],
    0x80,
    add(0, 1),
    mov(1, 7),
    ret(),
    load_from(1),
    data_off + data_map['0'],
    0x80,
    add(2, 1),
    mov(1, 7),
    ret(),
]

parse_digit_code = [
    load_from(1),
    data_off + data_map['0'],
    0x80,
    sub(1, 0),
    load_from(1),
    data_off + data_map['39'],
    0x80,
    mov(0, 2),
    sub(1, 2),
    jl(),
    parse_digit_off + 13,
    0x80,
    mov(2, 0),
    mov(0, 7),
    ret(),
]

program = main_code + (200 - len(main_code)) * [0] + print_digit_code + (22 - len(print_digit_code)) * [0] + parse_digit_code + (23 - len(parse_digit_code)) * [0] + data

write_bytes_to_file(program, "muie_fcsb.kyb")