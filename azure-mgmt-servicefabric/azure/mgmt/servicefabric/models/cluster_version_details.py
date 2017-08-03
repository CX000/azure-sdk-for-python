# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator 1.2.2.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ClusterVersionDetails(Model):
    """The detail of the ServiceFabric runtime version result.

    :param code_version: The ServiceFabric runtime version of the cluster
    :type code_version: str
    :param support_expiry_utc: The date of expiry of support of the version
    :type support_expiry_utc: str
    :param environment: Cluster operating system. Possible values include:
     'Windows', 'Linux'
    :type environment: str or :class:`enum
     <azure.mgmt.servicefabric.models.enum>`
    """

    _attribute_map = {
        'code_version': {'key': 'codeVersion', 'type': 'str'},
        'support_expiry_utc': {'key': 'supportExpiryUtc', 'type': 'str'},
        'environment': {'key': 'environment', 'type': 'str'},
    }

    def __init__(self, code_version=None, support_expiry_utc=None, environment=None):
        self.code_version = code_version
        self.support_expiry_utc = support_expiry_utc
        self.environment = environment
