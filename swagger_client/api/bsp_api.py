# coding: utf-8

"""
    IP RL BSP API

    IP RL BSP API for participation in capacity/energy market tenders.  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class BSPApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_backup_contracts(self, **kwargs):  # noqa: E501
        """Returns current backup contracts  # noqa: E501

        Returns valid backup contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_contracts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date valid_date: Contracts for a specified day can be queried. If not specified, contracts for today will be listed.
        :param str product_type: Product type filter for contracts. If not specified, then contracts for all product types are returned.
        :return: list[BackupContract]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_backup_contracts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_backup_contracts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_backup_contracts_with_http_info(self, **kwargs):  # noqa: E501
        """Returns current backup contracts  # noqa: E501

        Returns valid backup contracts.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_backup_contracts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date valid_date: Contracts for a specified day can be queried. If not specified, contracts for today will be listed.
        :param str product_type: Product type filter for contracts. If not specified, then contracts for all product types are returned.
        :return: list[BackupContract]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['valid_date', 'product_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_backup_contracts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'valid_date' in params:
            query_params.append(('valid-date', params['valid_date']))  # noqa: E501
        if 'product_type' in params:
            query_params.append(('product-type', params['product_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/backup-contracts', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[BackupContract]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_framework_contracts(self, **kwargs):  # noqa: E501
        """Current framework agreements  # noqa: E501

        Returns current framework agreements.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_framework_contracts(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_type: Product type filter for framework agreements. If this query parameter is not set, contracts for all product types are returned.
        :return: list[FrameworkAgreement]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_framework_contracts_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_framework_contracts_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_framework_contracts_with_http_info(self, **kwargs):  # noqa: E501
        """Current framework agreements  # noqa: E501

        Returns current framework agreements.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_framework_contracts_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str product_type: Product type filter for framework agreements. If this query parameter is not set, contracts for all product types are returned.
        :return: list[FrameworkAgreement]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['product_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_framework_contracts" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'product_type' in params:
            query_params.append(('product-type', params['product_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/framework-agreements', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[FrameworkAgreement]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_pre_qualified_capacities(self, delivery_date, **kwargs):  # noqa: E501
        """Prequalified capacities.  # noqa: E501

        Returns my pre-qualified capacities in each control area (sum of PTU capacities) valid on specific delivery date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pre_qualified_capacities(delivery_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date delivery_date: Defines the delivery date for which the pre-qualified capacities are to be returned. (required)
        :param str product_type: Product type filter for contracts. If not specified, then contracts for all product types are returned.
        :return: list[PrequalifiedCapacity]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_pre_qualified_capacities_with_http_info(delivery_date, **kwargs)  # noqa: E501
        else:
            (data) = self.get_pre_qualified_capacities_with_http_info(delivery_date, **kwargs)  # noqa: E501
            return data

    def get_pre_qualified_capacities_with_http_info(self, delivery_date, **kwargs):  # noqa: E501
        """Prequalified capacities.  # noqa: E501

        Returns my pre-qualified capacities in each control area (sum of PTU capacities) valid on specific delivery date.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_pre_qualified_capacities_with_http_info(delivery_date, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date delivery_date: Defines the delivery date for which the pre-qualified capacities are to be returned. (required)
        :param str product_type: Product type filter for contracts. If not specified, then contracts for all product types are returned.
        :return: list[PrequalifiedCapacity]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_date', 'product_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_pre_qualified_capacities" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'delivery_date' is set
        if ('delivery_date' not in params or
                params['delivery_date'] is None):
            raise ValueError("Missing the required parameter `delivery_date` when calling `get_pre_qualified_capacities`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'delivery_date' in params:
            path_params['deliveryDate'] = params['delivery_date']  # noqa: E501

        query_params = []
        if 'product_type' in params:
            query_params.append(('product-type', params['product_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/pre-qualified-capacities/{deliveryDate}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[PrequalifiedCapacity]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
