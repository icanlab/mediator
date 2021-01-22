# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.test import BaseTestCase


class TestAdaptorController(BaseTestCase):
    """AdaptorController integration test stubs"""

    def test_translate_msg(self):
        """Test case for translate_msg

        translate msg
        """
        query_string = [('protocol', 'netconf'),
                        ('neid', 'neid_example'),
                        ('xml_msg', 'xml_msg_example')]
        response = self.client.open(
            '/v1/adaptor/translate_msg',
            method='GET',
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
