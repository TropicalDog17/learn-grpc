# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the GRPC helloworld.Greeter server."""

from concurrent import futures
import logging

import grpc
import crud_pb2
import crud_pb2_grpc


class MovieBookingService(crud_pb2_grpc.MovieBookingServiceServicer):
    def __init__(self):
        self.count = 1

    def makeBooking(self, request, context):
        return crud_pb2.makeBooking(request, context)

    def getBookingDetails(self, request, context):
        return crud_pb2.getBookingDetails(request, context)

    def getAllBookingsByLocation(self, request, context):
        return crud_pb2.getAllBookingsByLocation(request, context)

    def getAllBookingsByName(self, request, context):
        return crud_pb2.getAllBookingsByName(request, context)

    def getAllBookingsByMovie(self, request, context):
        return crud_pb2.getAllBookingsByMovie(request, context)

    def testService(self, request, context):
        message = f'hello my friend {request.test_msg}. you have greeted me {self.count} times already'
        self.count += 1
        return crud_pb2.TestResponse(message=message)


def serve():
    port = '50051'
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    crud_pb2_grpc.add_MovieBookingServiceServicer_to_server(
        MovieBookingService(), server)
    server.add_insecure_port('[::]:' + port)
    server.start()
    print("Server started, listening on " + port)
    server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig()
    serve()
