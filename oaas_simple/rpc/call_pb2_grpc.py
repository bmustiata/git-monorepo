# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import oaas_simple.rpc.call_pb2 as call__pb2


class ServiceInvokerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.InvokeMethod = channel.unary_unary(
            "/gr.ServiceInvoker/InvokeMethod",
            request_serializer=call__pb2.ServiceCall.SerializeToString,
            response_deserializer=call__pb2.Data.FromString,
        )


class ServiceInvokerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def InvokeMethod(self, request, context):
        """*
        Invoke a single method.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    @staticmethod
    def add_to_server(servicer, server):
        rpc_method_handlers = {
            "InvokeMethod": grpc.unary_unary_rpc_method_handler(
                servicer.InvokeMethod,
                request_deserializer=call__pb2.ServiceCall.FromString,
                response_serializer=call__pb2.Data.SerializeToString,
            ),
        }
        generic_handler = grpc.method_handlers_generic_handler(
            "gr.ServiceInvoker", rpc_method_handlers
        )
        server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class ServiceInvoker(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def InvokeMethod(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/gr.ServiceInvoker/InvokeMethod",
            call__pb2.ServiceCall.SerializeToString,
            call__pb2.Data.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
