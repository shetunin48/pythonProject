# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import prot_pb2 as prot__pb2


class MyserverStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetKeys = channel.unary_unary(
                '/prot.Myserver/GetKeys',
                request_serializer=prot__pb2.Keys_Request.SerializeToString,
                response_deserializer=prot__pb2.Array_Reply.FromString,
                )
        self.GenerateJson = channel.unary_unary(
                '/prot.Myserver/GenerateJson',
                request_serializer=prot__pb2.Generate_Request.SerializeToString,
                response_deserializer=prot__pb2.Simple_Json_Reply.FromString,
                )
        self.FindValue = channel.unary_unary(
                '/prot.Myserver/FindValue',
                request_serializer=prot__pb2.Find_Request.SerializeToString,
                response_deserializer=prot__pb2.Array_Reply.FromString,
                )
        self.Convert = channel.unary_unary(
                '/prot.Myserver/Convert',
                request_serializer=prot__pb2.Convert_Request.SerializeToString,
                response_deserializer=prot__pb2.Convert_Reply.FromString,
                )


class MyserverServicer(object):
    """Missing associated documentation comment in .proto file."""

    def GetKeys(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GenerateJson(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindValue(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Convert(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MyserverServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetKeys': grpc.unary_unary_rpc_method_handler(
                    servicer.GetKeys,
                    request_deserializer=prot__pb2.Keys_Request.FromString,
                    response_serializer=prot__pb2.Array_Reply.SerializeToString,
            ),
            'GenerateJson': grpc.unary_unary_rpc_method_handler(
                    servicer.GenerateJson,
                    request_deserializer=prot__pb2.Generate_Request.FromString,
                    response_serializer=prot__pb2.Simple_Json_Reply.SerializeToString,
            ),
            'FindValue': grpc.unary_unary_rpc_method_handler(
                    servicer.FindValue,
                    request_deserializer=prot__pb2.Find_Request.FromString,
                    response_serializer=prot__pb2.Array_Reply.SerializeToString,
            ),
            'Convert': grpc.unary_unary_rpc_method_handler(
                    servicer.Convert,
                    request_deserializer=prot__pb2.Convert_Request.FromString,
                    response_serializer=prot__pb2.Convert_Reply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'prot.Myserver', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Myserver(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def GetKeys(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prot.Myserver/GetKeys',
            prot__pb2.Keys_Request.SerializeToString,
            prot__pb2.Array_Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GenerateJson(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prot.Myserver/GenerateJson',
            prot__pb2.Generate_Request.SerializeToString,
            prot__pb2.Simple_Json_Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindValue(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prot.Myserver/FindValue',
            prot__pb2.Find_Request.SerializeToString,
            prot__pb2.Array_Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Convert(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/prot.Myserver/Convert',
            prot__pb2.Convert_Request.SerializeToString,
            prot__pb2.Convert_Reply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
