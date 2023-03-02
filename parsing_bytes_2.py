device_settings = [{0: [3, 'field1'],
                    3: [1, 'field2'],
                    4: [1, 'field3'],
                    5: [3, 'field4']},
                   {0: [1, 'field5'],
                    1: [1, 'field6'],
                    2: [1, 'field7'],
                    3: [3, 'field8'],
                    },
                   {0: [1, 'field9'],
                    5: [1, 'field10']
                    },
                   {}
                   ]

FIELDS_VARIABLES = dict(
    field1={'0': 'Low',
            '1': 'reserved',
            '2': 'reserved',
            '3': 'reserved',
            '4': 'Medium',
            '5': 'reserved',
            '6': 'reserved',
            '7': 'High',
            },
    field4={'0': '00',
            '1': '10',
            '2': '20',
            '3': '30',
            '4': '40',
            '5': '50',
            '6': '60',
            '7': '70',
            },
    field8={'0': 'Very Low',
            '1': 'reserved',
            '2': 'Low',
            '3': 'reserved',
            '4': 'Medium',
            '5': 'High',
            '6': 'reserved',
            '7': 'Very High',
            }
)


def payload_to_bytes_list(payload: str):
    bytes_list = []
    for i in range(0, len(payload), 2):
        byte_str = payload[i: i + 2]
        bit_str = '{:08b}'.format(int(byte_str, base=16))
        bytes_list.append(bit_str[::-1])
    return bytes_list


def get_data_from_payload(payload: str):
    payload_bytes_list = payload_to_bytes_list(payload)
    parsed_data = {}
    # for each byte in the payload find the corresponding values in device_settings
    for sett_byte, specific_byte in zip(device_settings, payload_bytes_list):
        for bias, (size, field_name) in sett_byte.items():
            # determine the value for each parameter
            bits_parameter = specific_byte[bias: bias + size]
            # get the value from fields variables
            if size == 3:
                variable = FIELDS_VARIABLES[field_name]
                parsed_data[field_name] = variable[str(int(bits_parameter, 2))]
            else:
                # format the parameter to the look we need
                parsed_data[field_name] = '{:02x}'.format(int(bits_parameter, 2))

    return parsed_data


print(get_data_from_payload("10FA0E00"))
