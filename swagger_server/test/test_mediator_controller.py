# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestMediatorController(BaseTestCase):
    """MediatorController integration test stubs"""

    def test_translate_msg_from_adaptor(self):
        """Test case for translate_msg_from_adaptor

        translte msg from adaptor
        """
        query_string = [('neid', 'neid_example'),
                        ('msg_type', 'msg_type_example'),
                        ('opdata', 'opdata_example')]
        response = self.client.open(
            '/v1/mediator/translate_msg_from_adaptor',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()