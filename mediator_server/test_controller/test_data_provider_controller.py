# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from mediator_server.test_controller import BaseTestCase


class TestDataProviderController(BaseTestCase):
    """DataProviderController integration test_controller stubs"""

    def test_get_controller_configuration(self):
        """Test case for get_controller_configuration

        get controller configuration
        """
        query_string = [('neid', 'neid_example'),
                        ('tp_path', 'tp_path_example')]
        response = self.client.open(
            '/v1/dataprovider/get_controller_configuration',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_device_configuration(self):
        """Test case for get_device_configuration

        get device configuration
        """
        query_string = [('neid', 'neid_example'),
                        ('top_path', 'top_path_example')]
        response = self.client.open(
            '/v1/dataprovider/get_device_configuration',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
