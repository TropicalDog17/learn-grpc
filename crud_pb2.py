# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: crud.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ncrud.proto\"v\n\x0c\x42ookingQuery\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x01(\t\x12\x14\n\x0c\x62ooking_name\x18\x03 \x01(\t\x12\x15\n\rbooking_email\x18\x04 \x01(\t\x12\x10\n\x08location\x18\x05 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x06 \x01(\t\"\xad\x01\n\x0e\x42ookingDetails\x12\n\n\x02id\x18\x01 \x01(\t\x12\r\n\x05movie\x18\x02 \x01(\t\x12\x14\n\x0c\x62ooking_name\x18\x03 \x01(\t\x12\x15\n\rbooking_email\x18\x04 \x01(\t\x12\x0c\n\x04\x64\x61te\x18\x05 \x01(\t\x12\x10\n\x08location\x18\x06 \x01(\t\x12\x0e\n\x06screen\x18\x07 \x01(\t\x12\x13\n\x0bseat_number\x18\x08 \x01(\x05\x12\x0e\n\x06status\x18\t \x01(\t\"\x1f\n\x0bTestRequest\x12\x10\n\x08test_msg\x18\x01 \x01(\t\"\x1f\n\x0cTestResponse\x12\x0f\n\x07message\x18\x01 \x01(\t2\xe4\x02\n\x13MovieBookingService\x12/\n\x0bmakeBooking\x12\r.BookingQuery\x1a\x0f.BookingDetails\"\x00\x12\x35\n\x11getBookingDetails\x12\r.BookingQuery\x1a\x0f.BookingDetails\"\x00\x12>\n\x18getAllBookingsByLocation\x12\r.BookingQuery\x1a\x0f.BookingDetails\"\x00\x30\x01\x12:\n\x14getAllBookingsByName\x12\r.BookingQuery\x1a\x0f.BookingDetails\"\x00\x30\x01\x12;\n\x15getAllBookingsByMovie\x12\r.BookingQuery\x1a\x0f.BookingDetails\"\x00\x30\x01\x12,\n\x0btestService\x12\x0c.TestRequest\x1a\r.TestResponse\"\x00\x62\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'crud_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _BOOKINGQUERY._serialized_start=14
  _BOOKINGQUERY._serialized_end=132
  _BOOKINGDETAILS._serialized_start=135
  _BOOKINGDETAILS._serialized_end=308
  _TESTREQUEST._serialized_start=310
  _TESTREQUEST._serialized_end=341
  _TESTRESPONSE._serialized_start=343
  _TESTRESPONSE._serialized_end=374
  _MOVIEBOOKINGSERVICE._serialized_start=377
  _MOVIEBOOKINGSERVICE._serialized_end=733
# @@protoc_insertion_point(module_scope)
