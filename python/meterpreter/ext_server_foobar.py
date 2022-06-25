import os
import sys

ERROR_SUCCESS            = 0
TLV_EXTENSIONS           = 20000
TLV_META_TYPE_STRING     = (1 << 16)

TLV_TYPE_FOOBAR_ECHO_MSG = TLV_META_TYPE_STRING | (TLV_EXTENSIONS + 1)

meterpreter.register_extension('foobar')

# Meterpreter register function decorators
register_function = meterpreter.register_function

@register_function
def foobar_echo(request, response):
    message = packet_get_tlv(request, TLV_TYPE_FOOBAR_ECHO_MSG)['value']
    response += tlv_pack(TLV_TYPE_FOOBAR_ECHO_MSG, message)
    return ERROR_SUCCESS, response
