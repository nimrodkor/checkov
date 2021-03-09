from enum import Enum


class CustomAttributes(Enum):
    BLOCK_NAME = "block_name_"
    BLOCK_TYPE = "block_type_"
    FILE_PATH = "file_path_"
    CONFIG = "config_"
    LABEL = "label_"
    ID = "id_"
    HASH = "hash"
    RENDERING_BREADCRUMBS = "rendering_breadcrumbs_"
    SOURCE_MODULE = "source_module_"
    SOURCE = "source_"
    RESOURCE_TYPE = "resource_type"
    RESOURCE_ID = "resource_id"
    ENCRYPTION = "encryption_"
    ENCRYPTION_DETAILS = "encryption_details_"


reserved_attribute_names = [attribute_name.value for attribute_name in CustomAttributes]


class EncryptionValues(Enum):
    ENCRYPTED = "ENCRYPTED"
    UNENCRYPTED = "UNENCRYPTED"


class EncryptionTypes(Enum):
    KMS_VALUE = "KMS"
    NODE_TO_NODE = "node-to-node"
    DEFAULT_KMS = "Default KMS"
    AES256 = "AES256"
    AWS_KMS_VALUE = "aws:kms"
