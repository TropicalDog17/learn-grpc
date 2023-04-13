"""The Python implementation of the GRPC helloworld.Greeter client."""

from __future__ import print_function

import logging

import grpc
import crud_pb2
import crud_pb2_grpc


def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    print("Will try to test world ...")
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = crud_pb2_grpc.MovieBookingServiceStub(channel)
        response = stub.testService(crud_pb2.TestRequest(test_msg='you'))
    print("Greeter client received: " + response.message)


if __name__ == '__main__':
    logging.basicConfig()
    run()
