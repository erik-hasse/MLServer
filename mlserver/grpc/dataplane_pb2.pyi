"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.internal.containers
import google.protobuf.message
import typing
import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor = ...

class ServerLiveRequest(google.protobuf.message.Message):
    """
    ServerLive messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

global___ServerLiveRequest = ServerLiveRequest

class ServerLiveResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    LIVE_FIELD_NUMBER: builtins.int
    live: builtins.bool = ...
    """True if the inference server is live, false if not live."""
    def __init__(
        self,
        *,
        live: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["live", b"live"]
    ) -> None: ...

global___ServerLiveResponse = ServerLiveResponse

class ServerReadyRequest(google.protobuf.message.Message):
    """
    ServerReady messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

global___ServerReadyRequest = ServerReadyRequest

class ServerReadyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    READY_FIELD_NUMBER: builtins.int
    ready: builtins.bool = ...
    """True if the inference server is ready, false if not ready."""
    def __init__(
        self,
        *,
        ready: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["ready", b"ready"]
    ) -> None: ...

global___ServerReadyResponse = ServerReadyResponse

class ModelReadyRequest(google.protobuf.message.Message):
    """
    ModelReady messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the model to check for readiness."""

    version: typing.Text = ...
    """The version of the model to check for readiness. If not given the
    server will choose a version based on the model and internal policy.
    """
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        version: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["name", b"name", "version", b"version"],
    ) -> None: ...

global___ModelReadyRequest = ModelReadyRequest

class ModelReadyResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    READY_FIELD_NUMBER: builtins.int
    ready: builtins.bool = ...
    """True if the model is ready, false if not ready."""
    def __init__(
        self,
        *,
        ready: builtins.bool = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: typing_extensions.Literal["ready", b"ready"]
    ) -> None: ...

global___ModelReadyResponse = ModelReadyResponse

class ServerMetadataRequest(google.protobuf.message.Message):
    """
    ServerMetadata messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    def __init__(
        self,
    ) -> None: ...

global___ServerMetadataRequest = ServerMetadataRequest

class ServerMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    EXTENSIONS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The server name."""

    version: typing.Text = ...
    """The server version."""
    @property
    def extensions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The extensions supported by the server."""
        pass
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        version: typing.Text = ...,
        extensions: typing.Optional[typing.Iterable[typing.Text]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "extensions", b"extensions", "name", b"name", "version", b"version"
        ],
    ) -> None: ...

global___ServerMetadataResponse = ServerMetadataResponse

class ModelMetadataRequest(google.protobuf.message.Message):
    """
    ModelMetadata messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    NAME_FIELD_NUMBER: builtins.int
    VERSION_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The name of the model."""

    version: typing.Text = ...
    """The version of the model to check for readiness. If not given the
    server will choose a version based on the model and internal policy.
    """
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        version: typing.Text = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal["name", b"name", "version", b"version"],
    ) -> None: ...

global___ModelMetadataRequest = ModelMetadataRequest

class ModelMetadataResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class TensorMetadata(google.protobuf.message.Message):
        """Metadata for a tensor."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___InferParameter] = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["value", b"value"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        NAME_FIELD_NUMBER: builtins.int
        DATATYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        """The tensor name."""

        datatype: typing.Text = ...
        """The tensor data type."""
        @property
        def shape(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            builtins.int
        ]:
            """The tensor shape. A variable-size dimension is represented
            by a -1 value.
            """
            pass
        @property
        def parameters(
            self,
        ) -> google.protobuf.internal.containers.MessageMap[
            typing.Text, global___InferParameter
        ]:
            """Optional default parameters for input.
            NOTE: This is an extension to the standard
            """
            pass
        def __init__(
            self,
            *,
            name: typing.Text = ...,
            datatype: typing.Text = ...,
            shape: typing.Optional[typing.Iterable[builtins.int]] = ...,
            parameters: typing.Optional[
                typing.Mapping[typing.Text, global___InferParameter]
            ] = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "datatype",
                b"datatype",
                "name",
                b"name",
                "parameters",
                b"parameters",
                "shape",
                b"shape",
            ],
        ) -> None: ...
    class ParametersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___InferParameter: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___InferParameter] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    NAME_FIELD_NUMBER: builtins.int
    VERSIONS_FIELD_NUMBER: builtins.int
    PLATFORM_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    name: typing.Text = ...
    """The model name."""
    @property
    def versions(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[typing.Text]:
        """The versions of the model available on the server."""
        pass
    platform: typing.Text = ...
    """The model's platform. See Platforms."""
    @property
    def inputs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ModelMetadataResponse.TensorMetadata
    ]:
        """The model's inputs."""
        pass
    @property
    def outputs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ModelMetadataResponse.TensorMetadata
    ]:
        """The model's outputs."""
        pass
    @property
    def parameters(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, global___InferParameter
    ]:
        """Optional default parameters for the request / response.
        NOTE: This is an extension to the standard
        """
        pass
    def __init__(
        self,
        *,
        name: typing.Text = ...,
        versions: typing.Optional[typing.Iterable[typing.Text]] = ...,
        platform: typing.Text = ...,
        inputs: typing.Optional[
            typing.Iterable[global___ModelMetadataResponse.TensorMetadata]
        ] = ...,
        outputs: typing.Optional[
            typing.Iterable[global___ModelMetadataResponse.TensorMetadata]
        ] = ...,
        parameters: typing.Optional[
            typing.Mapping[typing.Text, global___InferParameter]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "inputs",
            b"inputs",
            "name",
            b"name",
            "outputs",
            b"outputs",
            "parameters",
            b"parameters",
            "platform",
            b"platform",
            "versions",
            b"versions",
        ],
    ) -> None: ...

global___ModelMetadataResponse = ModelMetadataResponse

class ModelInferRequest(google.protobuf.message.Message):
    """
    ModelInfer messages.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class InferInputTensor(google.protobuf.message.Message):
        """An input tensor for an inference request."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___InferParameter] = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["value", b"value"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        NAME_FIELD_NUMBER: builtins.int
        DATATYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        CONTENTS_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        """The tensor name."""

        datatype: typing.Text = ...
        """The tensor data type."""
        @property
        def shape(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            builtins.int
        ]:
            """The tensor shape."""
            pass
        @property
        def parameters(
            self,
        ) -> google.protobuf.internal.containers.MessageMap[
            typing.Text, global___InferParameter
        ]:
            """Optional inference input tensor parameters."""
            pass
        @property
        def contents(self) -> global___InferTensorContents:
            """The input tensor data."""
            pass
        def __init__(
            self,
            *,
            name: typing.Text = ...,
            datatype: typing.Text = ...,
            shape: typing.Optional[typing.Iterable[builtins.int]] = ...,
            parameters: typing.Optional[
                typing.Mapping[typing.Text, global___InferParameter]
            ] = ...,
            contents: typing.Optional[global___InferTensorContents] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["contents", b"contents"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "contents",
                b"contents",
                "datatype",
                b"datatype",
                "name",
                b"name",
                "parameters",
                b"parameters",
                "shape",
                b"shape",
            ],
        ) -> None: ...
    class InferRequestedOutputTensor(google.protobuf.message.Message):
        """An output tensor requested for an inference request."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___InferParameter] = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["value", b"value"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        NAME_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        """The tensor name."""
        @property
        def parameters(
            self,
        ) -> google.protobuf.internal.containers.MessageMap[
            typing.Text, global___InferParameter
        ]:
            """Optional requested output tensor parameters."""
            pass
        def __init__(
            self,
            *,
            name: typing.Text = ...,
            parameters: typing.Optional[
                typing.Mapping[typing.Text, global___InferParameter]
            ] = ...,
        ) -> None: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "name", b"name", "parameters", b"parameters"
            ],
        ) -> None: ...
    class ParametersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___InferParameter: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___InferParameter] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    MODEL_NAME_FIELD_NUMBER: builtins.int
    MODEL_VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    INPUTS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    model_name: typing.Text = ...
    """The name of the model to use for inferencing."""

    model_version: typing.Text = ...
    """The version of the model to use for inference. If not given the
    server will choose a version based on the model and internal policy.
    """

    id: typing.Text = ...
    """Optional identifier for the request. If specified will be
    returned in the response.
    """
    @property
    def parameters(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, global___InferParameter
    ]:
        """Optional inference parameters."""
        pass
    @property
    def inputs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ModelInferRequest.InferInputTensor
    ]:
        """The input tensors for the inference."""
        pass
    @property
    def outputs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ModelInferRequest.InferRequestedOutputTensor
    ]:
        """The requested output tensors for the inference. Optional, if not
        specified all outputs produced by the model will be returned.
        """
        pass
    def __init__(
        self,
        *,
        model_name: typing.Text = ...,
        model_version: typing.Text = ...,
        id: typing.Text = ...,
        parameters: typing.Optional[
            typing.Mapping[typing.Text, global___InferParameter]
        ] = ...,
        inputs: typing.Optional[
            typing.Iterable[global___ModelInferRequest.InferInputTensor]
        ] = ...,
        outputs: typing.Optional[
            typing.Iterable[global___ModelInferRequest.InferRequestedOutputTensor]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "inputs",
            b"inputs",
            "model_name",
            b"model_name",
            "model_version",
            b"model_version",
            "outputs",
            b"outputs",
            "parameters",
            b"parameters",
        ],
    ) -> None: ...

global___ModelInferRequest = ModelInferRequest

class ModelInferResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    class InferOutputTensor(google.protobuf.message.Message):
        """An output tensor returned for an inference request."""

        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        class ParametersEntry(google.protobuf.message.Message):
            DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
            KEY_FIELD_NUMBER: builtins.int
            VALUE_FIELD_NUMBER: builtins.int
            key: typing.Text = ...
            @property
            def value(self) -> global___InferParameter: ...
            def __init__(
                self,
                *,
                key: typing.Text = ...,
                value: typing.Optional[global___InferParameter] = ...,
            ) -> None: ...
            def HasField(
                self, field_name: typing_extensions.Literal["value", b"value"]
            ) -> builtins.bool: ...
            def ClearField(
                self,
                field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
            ) -> None: ...
        NAME_FIELD_NUMBER: builtins.int
        DATATYPE_FIELD_NUMBER: builtins.int
        SHAPE_FIELD_NUMBER: builtins.int
        PARAMETERS_FIELD_NUMBER: builtins.int
        CONTENTS_FIELD_NUMBER: builtins.int
        name: typing.Text = ...
        """The tensor name."""

        datatype: typing.Text = ...
        """The tensor data type."""
        @property
        def shape(
            self,
        ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
            builtins.int
        ]:
            """The tensor shape."""
            pass
        @property
        def parameters(
            self,
        ) -> google.protobuf.internal.containers.MessageMap[
            typing.Text, global___InferParameter
        ]:
            """Optional output tensor parameters."""
            pass
        @property
        def contents(self) -> global___InferTensorContents:
            """The output tensor data."""
            pass
        def __init__(
            self,
            *,
            name: typing.Text = ...,
            datatype: typing.Text = ...,
            shape: typing.Optional[typing.Iterable[builtins.int]] = ...,
            parameters: typing.Optional[
                typing.Mapping[typing.Text, global___InferParameter]
            ] = ...,
            contents: typing.Optional[global___InferTensorContents] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["contents", b"contents"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal[
                "contents",
                b"contents",
                "datatype",
                b"datatype",
                "name",
                b"name",
                "parameters",
                b"parameters",
                "shape",
                b"shape",
            ],
        ) -> None: ...
    class ParametersEntry(google.protobuf.message.Message):
        DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
        KEY_FIELD_NUMBER: builtins.int
        VALUE_FIELD_NUMBER: builtins.int
        key: typing.Text = ...
        @property
        def value(self) -> global___InferParameter: ...
        def __init__(
            self,
            *,
            key: typing.Text = ...,
            value: typing.Optional[global___InferParameter] = ...,
        ) -> None: ...
        def HasField(
            self, field_name: typing_extensions.Literal["value", b"value"]
        ) -> builtins.bool: ...
        def ClearField(
            self,
            field_name: typing_extensions.Literal["key", b"key", "value", b"value"],
        ) -> None: ...
    MODEL_NAME_FIELD_NUMBER: builtins.int
    MODEL_VERSION_FIELD_NUMBER: builtins.int
    ID_FIELD_NUMBER: builtins.int
    PARAMETERS_FIELD_NUMBER: builtins.int
    OUTPUTS_FIELD_NUMBER: builtins.int
    model_name: typing.Text = ...
    """The name of the model used for inference."""

    model_version: typing.Text = ...
    """The version of the model used for inference."""

    id: typing.Text = ...
    """The id of the inference request if one was specified."""
    @property
    def parameters(
        self,
    ) -> google.protobuf.internal.containers.MessageMap[
        typing.Text, global___InferParameter
    ]:
        """Optional inference response parameters."""
        pass
    @property
    def outputs(
        self,
    ) -> google.protobuf.internal.containers.RepeatedCompositeFieldContainer[
        global___ModelInferResponse.InferOutputTensor
    ]:
        """The output tensors holding inference results."""
        pass
    def __init__(
        self,
        *,
        model_name: typing.Text = ...,
        model_version: typing.Text = ...,
        id: typing.Text = ...,
        parameters: typing.Optional[
            typing.Mapping[typing.Text, global___InferParameter]
        ] = ...,
        outputs: typing.Optional[
            typing.Iterable[global___ModelInferResponse.InferOutputTensor]
        ] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "id",
            b"id",
            "model_name",
            b"model_name",
            "model_version",
            b"model_version",
            "outputs",
            b"outputs",
            "parameters",
            b"parameters",
        ],
    ) -> None: ...

global___ModelInferResponse = ModelInferResponse

class InferParameter(google.protobuf.message.Message):
    """
    An inference parameter value.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOOL_PARAM_FIELD_NUMBER: builtins.int
    INT64_PARAM_FIELD_NUMBER: builtins.int
    STRING_PARAM_FIELD_NUMBER: builtins.int
    bool_param: builtins.bool = ...
    """A boolean parameter value."""

    int64_param: builtins.int = ...
    """An int64 parameter value."""

    string_param: typing.Text = ...
    """A string parameter value."""
    def __init__(
        self,
        *,
        bool_param: builtins.bool = ...,
        int64_param: builtins.int = ...,
        string_param: typing.Text = ...,
    ) -> None: ...
    def HasField(
        self,
        field_name: typing_extensions.Literal[
            "bool_param",
            b"bool_param",
            "int64_param",
            b"int64_param",
            "parameter_choice",
            b"parameter_choice",
            "string_param",
            b"string_param",
        ],
    ) -> builtins.bool: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bool_param",
            b"bool_param",
            "int64_param",
            b"int64_param",
            "parameter_choice",
            b"parameter_choice",
            "string_param",
            b"string_param",
        ],
    ) -> None: ...
    def WhichOneof(
        self,
        oneof_group: typing_extensions.Literal["parameter_choice", b"parameter_choice"],
    ) -> typing.Optional[
        typing_extensions.Literal["bool_param", "int64_param", "string_param"]
    ]: ...

global___InferParameter = InferParameter

class InferTensorContents(google.protobuf.message.Message):
    """
    The data contained in a tensor. For a given data type the
    tensor contents can be represented in "raw" bytes form or in
    the repeated type that matches the tensor's data type. Protobuf
    oneof is not used because oneofs cannot contain repeated fields.
    """

    DESCRIPTOR: google.protobuf.descriptor.Descriptor = ...
    BOOL_CONTENTS_FIELD_NUMBER: builtins.int
    INT_CONTENTS_FIELD_NUMBER: builtins.int
    INT64_CONTENTS_FIELD_NUMBER: builtins.int
    UINT_CONTENTS_FIELD_NUMBER: builtins.int
    UINT64_CONTENTS_FIELD_NUMBER: builtins.int
    FP32_CONTENTS_FIELD_NUMBER: builtins.int
    FP64_CONTENTS_FIELD_NUMBER: builtins.int
    BYTES_CONTENTS_FIELD_NUMBER: builtins.int
    @property
    def bool_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.bool
    ]:
        """Representation for BOOL data type. The size must match what is
        expected by the tensor's shape. The contents must be the flattened,
        one-dimensional, row-major order of the tensor elements.
        """
        pass
    @property
    def int_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Representation for INT8, INT16, and INT32 data types. The size
        must match what is expected by the tensor's shape. The contents
        must be the flattened, one-dimensional, row-major order of the
        tensor elements.
        """
        pass
    @property
    def int64_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Representation for INT64 data types. The size must match what
        is expected by the tensor's shape. The contents must be the
        flattened, one-dimensional, row-major order of the tensor elements.
        """
        pass
    @property
    def uint_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Representation for UINT8, UINT16, and UINT32 data types. The size
        must match what is expected by the tensor's shape. The contents
        must be the flattened, one-dimensional, row-major order of the
        tensor elements.
        """
        pass
    @property
    def uint64_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[builtins.int]:
        """Representation for UINT64 data types. The size must match what
        is expected by the tensor's shape. The contents must be the
        flattened, one-dimensional, row-major order of the tensor elements.
        """
        pass
    @property
    def fp32_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.float
    ]:
        """Representation for FP32 data type. The size must match what is
        expected by the tensor's shape. The contents must be the flattened,
        one-dimensional, row-major order of the tensor elements.
        """
        pass
    @property
    def fp64_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.float
    ]:
        """Representation for FP64 data type. The size must match what is
        expected by the tensor's shape. The contents must be the flattened,
        one-dimensional, row-major order of the tensor elements.
        """
        pass
    @property
    def bytes_contents(
        self,
    ) -> google.protobuf.internal.containers.RepeatedScalarFieldContainer[
        builtins.bytes
    ]:
        """Representation for BYTES data type. The size must match what is
        expected by the tensor's shape. The contents must be the flattened,
        one-dimensional, row-major order of the tensor elements.
        """
        pass
    def __init__(
        self,
        *,
        bool_contents: typing.Optional[typing.Iterable[builtins.bool]] = ...,
        int_contents: typing.Optional[typing.Iterable[builtins.int]] = ...,
        int64_contents: typing.Optional[typing.Iterable[builtins.int]] = ...,
        uint_contents: typing.Optional[typing.Iterable[builtins.int]] = ...,
        uint64_contents: typing.Optional[typing.Iterable[builtins.int]] = ...,
        fp32_contents: typing.Optional[typing.Iterable[builtins.float]] = ...,
        fp64_contents: typing.Optional[typing.Iterable[builtins.float]] = ...,
        bytes_contents: typing.Optional[typing.Iterable[builtins.bytes]] = ...,
    ) -> None: ...
    def ClearField(
        self,
        field_name: typing_extensions.Literal[
            "bool_contents",
            b"bool_contents",
            "bytes_contents",
            b"bytes_contents",
            "fp32_contents",
            b"fp32_contents",
            "fp64_contents",
            b"fp64_contents",
            "int64_contents",
            b"int64_contents",
            "int_contents",
            b"int_contents",
            "uint64_contents",
            b"uint64_contents",
            "uint_contents",
            b"uint_contents",
        ],
    ) -> None: ...

global___InferTensorContents = InferTensorContents
