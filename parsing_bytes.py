import test_payload


def hex_to_bit(input_hex_str: str) -> bytes:
    """Return a string with a binary number from a string with a hex value"""
    return bytes.fromhex(input_hex_str)


def get_normalized_bit(value: int, bit_index: int) -> int:
    """Get 1-bit field value"""
    return (value >> bit_index) & 1


def reversed_3bit(value: int) -> int:
    """Return a number after flipping it in bit type"""
    return int('{:03b}'.format(value)[::-1], 2)


def get_normalized_3bit(value: int, bit_index: int) -> int:
    """Get 3-bit field value"""
    val3 = (value >> bit_index) & 7
    return reversed_3bit(val3)


def get_data_from_payload(payload: str) -> dict:
    """Main parser"""
    input_data = hex_to_bit(payload)
    parsed_data = {}

    for _id, seq in enumerate(configuration.device_settings):
        for offset, field in seq.items():
            size, name = field
            field_data = None
            if size == 1:
                read_bit = get_normalized_bit(input_data[_id], offset)
                field_data = f'{read_bit:02d}'
            elif size == 3:
                read_3bit = get_normalized_3bit(input_data[_id], offset)
                if name == 'field1':
                    field_data = configuration.field1.get(str(read_3bit))
                elif name == 'field4':
                    field_data = configuration.field4.get(str(read_3bit))
                elif name == 'field8':
                    field_data = configuration.field8.get(str(read_3bit))

            parsed_data[name] = field_data
    return parsed_data



print(get_data_from_payload(''))
