import pytest
from parsing_bytes_ajax import get_data_from_payload

test_data = [("10FA0E00", {'field1': 'Low',
                           'field2': '00',
                           'field3': '01',
                           'field4': '00',
                           'field5': '00',
                           'field6': '01',
                           'field7': '00',
                           'field8': 'Very High',
                           'field9': '00',
                           'field10': '00'}),
             ("10AA0D00", {'field1': 'Low',
                           'field2': '00',
                           'field3': '01',
                           'field4': '00',
                           'field5': '00',
                           'field6': '01',
                           'field7': '00',
                           'field8': 'High',
                           'field9': '01',
                           'field10': '00'}),
             ("10510300", {'field1': 'Low',
                           'field2': '00',
                           'field3': '01',
                           'field4': '00',
                           'field5': '01',
                           'field6': '00',
                           'field7': '00',
                           'field8': 'Low',
                           'field9': '01',
                           'field10': '00'})
             ]


@pytest.mark.parametrize('payload, expected', test_data)
def test_payload_data(payload, expected):
    assert get_data_from_payload(payload) == expected

