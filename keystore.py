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

def deref(register):
    return (0b11011 << 3) | register



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


code = [
    load_from(0),
    0x13,
    0x80,
    load_from(1),
    0x15,
    0x80,
    write_to(0),
    0x00,
    0xf0,
    exit(),
    load_from(1),
    0x00,
    0xf0,
    load_from(0),
    0x00,
    0x90,
    call(),
    0x17,
    0x80,
    0x48,
    0xfd,
    0x40,
    0xfd,
    mov (0, 2),
    mov(2, 0),
    load_from(1),
    38,
    0x80,
    deref(0),
    jz(),
    37,
    0x80,
    print(0),
    add(1, 2),
    jmp(),
    24,
    0x80,
    ret(),
    0x01,
    0x00
]

write_bytes_to_file(code, 'muie_rapid.kyb')