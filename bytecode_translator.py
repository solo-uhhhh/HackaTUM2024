def main():
    """
    Decodes a binary file containing instructions directly in the main function
    without separate functions for decoding logic.
    """
    try:
        binary_file_path = "compressor.kyb"
        output_file_path = "instr1.txt"

        with open(binary_file_path, "rb") as file, open(output_file_path, "w") as output_file:
            instruction_index = 0
            while (byte := file.read(1)):  # Read one byte at a time
                byte_value = int.from_bytes(byte, byteorder="little")
                instruction = None
                to_add = 0

                try:
                    # Decode the instruction directly
                    opcode = byte_value >> 6
                    arg1 = (byte_value >> 3) & 0b111
                    arg2 = byte_value & 0b111

                    if opcode == 0b00:  # ADD instruction
                        instruction = f"ADD R{arg1}, R{arg2}"
                    elif opcode == 0b01:  # SUB instruction
                        instruction = f"SUB R{arg1}, R{arg2}"
                    elif opcode == 0b10:  # MOV instruction
                        instruction = f"MOV R{arg1}, R{arg2}"
                    elif (byte_value >> 3) == 0b11100:  # GET instruction
                        instruction = f"GET R{arg2}"
                    elif (byte_value >> 3) == 0b11101:  # PRINT instruction
                        instruction = f"PRINT R{arg2}"
                    elif byte_value == 0b11111111:  # EXIT instruction
                        instruction = "EXIT"
                    elif byte_value == 0xFB:  # JL instruction
                        address = int.from_bytes(file.read(2), byteorder="little") - 0x8000
                        to_add += 2
                        instruction = f"JL 0x{address:04X}"
                    elif byte_value == 0xFA:  # JZ instruction
                        address = int.from_bytes(file.read(2), byteorder="little") - 0x8000
                        to_add += 2
                        instruction = f"JZ 0x{address:04X}"
                    elif byte_value == 0xF9:  # JMP instruction
                        address = int.from_bytes(file.read(2), byteorder="little") - 0x8000
                        to_add += 2
                        instruction = f"JMP 0x{address:04X}"
                    elif (byte_value >> 3) == 0b11000:  # LOAD_FROM instruction
                        memory_address = int.from_bytes(file.read(2), byteorder="little")
                        to_add += 2
                        instruction = f"LOAD_FROM R{arg2}, 0x{memory_address:02X}"
                    elif (byte_value >> 3) == 0b11001:  # WRITE_TO instruction
                        memory_address = int.from_bytes(file.read(2), byteorder="little")
                        to_add += 2
                        instruction = f"WRITE_TO R{arg2}, 0x{memory_address:02X}"
                    elif (byte_value >> 3) == 0b11010:  # SHIFT instruction
                        shift_value = int.from_bytes(file.read(1), byteorder="little")
                        to_add += 1
                        instruction = f"SHIFT R{arg2}, {shift_value}"
                    elif byte_value == 0xFC:  # CALL instruction
                        address = int.from_bytes(file.read(2), byteorder="little")
                        to_add += 2
                        instruction = f"CALL 0x{address:04X}"
                    elif byte_value == 0xFD:  # RET instruction
                        instruction = "RET"
                    elif (byte_value >> 3) == 0b11110:  # MULTIPLY instruction
                        register = byte_value & 0b111
                        address = int.from_bytes(file.read(2), byteorder="little")
                        to_add += 2
                        instruction = f"MULTIPLY R{register}, 0x{address:04X}"
                    elif (byte_value >> 3) == 0b11011:  # INDIRECT_LOAD instruction
                        register = byte_value & 0b111
                        instruction = f"INDIRECT_LOAD R{register}"
                    else:
                        instruction = f"UNKNOWN OPCODE: {byte_value:08b}"
                except Exception as e:
                    instruction = f"Error decoding instruction: {e}"

                # Write the instruction to the output file
                output_file.write(f"{instruction_index:04X}: {instruction}\n")
                instruction_index += 1 + to_add

        print(f"Decoding complete. Instructions written to {output_file_path}.")
    except FileNotFoundError:
        print(f"Error: File '{binary_file_path}' not found.")
    except IOError as e:
        print(f"File error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nOperation cancelled by user.")
