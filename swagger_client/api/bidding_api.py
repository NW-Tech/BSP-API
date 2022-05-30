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


class BiddingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_bid(self, id, **kwargs):  # noqa: E501
        """Deletes a simple, complex bid or a bid component  # noqa: E501

        This operation can be used to delete   * a specific simple bid (with the unique ID of the bid),   * a single component of a complex bid (with the unique ID of the bid component) or   * the entire complex bid with all its components (with the group ID of the complex bid).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bid(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidIdentification id: Bid identification (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_bid_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_bid_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def delete_bid_with_http_info(self, id, **kwargs):  # noqa: E501
        """Deletes a simple, complex bid or a bid component  # noqa: E501

        This operation can be used to delete   * a specific simple bid (with the unique ID of the bid),   * a single component of a complex bid (with the unique ID of the bid component) or   * the entire complex bid with all its components (with the group ID of the complex bid).   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_bid_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidIdentification id: Bid identification (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_bid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `delete_bid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/bids/{id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bid(self, id, **kwargs):  # noqa: E501
        """Get a simple, complex bid or a complex bid component  # noqa: E501

        Returns the single bid with requested ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bid(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidIdentification id: Unique bid identification or group bid id of complex bid (required)
        :return: Bid
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bid_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_bid_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def get_bid_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get a simple, complex bid or a complex bid component  # noqa: E501

        Returns the single bid with requested ID  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bid_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidIdentification id: Unique bid identification or group bid id of complex bid (required)
        :return: Bid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `get_bid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

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
            '/bids/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Bid',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_bids(self, **kwargs):  # noqa: E501
        """List submitted bids (optionally capacity or energy market)  # noqa: E501

        Returns the list of all submitted capacity/energy bids and complex bid components sorted in the following order:   * `productType`,   * `productName`,   * `state`,   * `revisionTimestamp`,   * `id`.  The result list can be reduced as required by specifying combinations of different filter parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bids(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date delivery_date: Only bids for the specified delivery date will be listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only bids for today's delivery day will be listed.
        :param ReserveMarket market: Market filter. If not specified and also no tender ID is specified, then only bids for capacity market will be listed.
        :param TenderIdentification tender: By specifying the tender ID, only bids of this tender will be listed. For details on the tender id format, see the [reference guide.](/docs/guide#tender-id)
        :param ProductType product_type: Product type filter. If this query parameter is not set and also no tender ID is specified, bids for all product types are returned.
        :param ProductName product_name: Product name filter. If this query parameter is not set, bids for all product names are returned.
        :param str state:
        :param EIC zone:
        :param datetime _from:
        :param datetime to:
        :param BidType type: By specifying the type, only bids of this type will be listed.
        :param BidIdentification cid: Filters bids that have the given complex bid ID.
        :param BidIdentification gid: Filters bids that have the given bid group ID.
        :param TechnicalLinkIdentification link: Filters bids that have the given technical link ID.
        :param BidIdentification linked_to: Filters bids that have a conditional link to the given bid ID.
        :param BidTag tag: Filters bids that have the given tag.
        :param bool backups_only:
        :param EIC backup_for: Filters bids which are a backup for the provider with the given EIC
        :param int offset: The number of items to skip before starting to collect the result set.
        :param int limit: The numbers of items to return
        :return: list[Bid]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_bids_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_bids_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_bids_with_http_info(self, **kwargs):  # noqa: E501
        """List submitted bids (optionally capacity or energy market)  # noqa: E501

        Returns the list of all submitted capacity/energy bids and complex bid components sorted in the following order:   * `productType`,   * `productName`,   * `state`,   * `revisionTimestamp`,   * `id`.  The result list can be reduced as required by specifying combinations of different filter parameters.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_bids_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param date delivery_date: Only bids for the specified delivery date will be listed (ISO 8601 format YYYY-MM-DD). If not specified and also no tender ID is specified, then only bids for today's delivery day will be listed.
        :param ReserveMarket market: Market filter. If not specified and also no tender ID is specified, then only bids for capacity market will be listed.
        :param TenderIdentification tender: By specifying the tender ID, only bids of this tender will be listed. For details on the tender id format, see the [reference guide.](/docs/guide#tender-id)
        :param ProductType product_type: Product type filter. If this query parameter is not set and also no tender ID is specified, bids for all product types are returned.
        :param ProductName product_name: Product name filter. If this query parameter is not set, bids for all product names are returned.
        :param str state:
        :param EIC zone:
        :param datetime _from:
        :param datetime to:
        :param BidType type: By specifying the type, only bids of this type will be listed.
        :param BidIdentification cid: Filters bids that have the given complex bid ID.
        :param BidIdentification gid: Filters bids that have the given bid group ID.
        :param TechnicalLinkIdentification link: Filters bids that have the given technical link ID.
        :param BidIdentification linked_to: Filters bids that have a conditional link to the given bid ID.
        :param BidTag tag: Filters bids that have the given tag.
        :param bool backups_only:
        :param EIC backup_for: Filters bids which are a backup for the provider with the given EIC
        :param int offset: The number of items to skip before starting to collect the result set.
        :param int limit: The numbers of items to return
        :return: list[Bid]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['delivery_date', 'market', 'tender', 'product_type', 'product_name', 'state', 'zone', '_from', 'to', 'type', 'cid', 'gid', 'link', 'linked_to', 'tag', 'backups_only', 'backup_for', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_bids" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'delivery_date' in params:
            query_params.append(('delivery-date', params['delivery_date']))  # noqa: E501
        if 'market' in params:
            query_params.append(('market', params['market']))  # noqa: E501
        if 'tender' in params:
            query_params.append(('tender', params['tender']))  # noqa: E501
        if 'product_type' in params:
            query_params.append(('product-type', params['product_type']))  # noqa: E501
        if 'product_name' in params:
            query_params.append(('product-name', params['product_name']))  # noqa: E501
        if 'state' in params:
            query_params.append(('state', params['state']))  # noqa: E501
        if 'zone' in params:
            query_params.append(('zone', params['zone']))  # noqa: E501
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'type' in params:
            query_params.append(('type', params['type']))  # noqa: E501
        if 'cid' in params:
            query_params.append(('cid', params['cid']))  # noqa: E501
        if 'gid' in params:
            query_params.append(('gid', params['gid']))  # noqa: E501
        if 'link' in params:
            query_params.append(('link', params['link']))  # noqa: E501
        if 'linked_to' in params:
            query_params.append(('linked-to', params['linked_to']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
        if 'backups_only' in params:
            query_params.append(('backups-only', params['backups_only']))  # noqa: E501
        if 'backup_for' in params:
            query_params.append(('backup-for', params['backup_for']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/bids', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Bid]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_bid(self, **kwargs):  # noqa: E501
        """Submit a simple, complex bid or a complex bid component  # noqa: E501

        Submission of a simple or complex bid for a open capacity/energy market tender. By specifying the product, delivery date and market, the bid is automatically assigned to the corresponding open tender. The gate closure time of the tender is relevant for the submission.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_bid(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidSubmission body:
        :return: BidSubmissionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.submit_bid_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.submit_bid_with_http_info(**kwargs)  # noqa: E501
            return data

    def submit_bid_with_http_info(self, **kwargs):  # noqa: E501
        """Submit a simple, complex bid or a complex bid component  # noqa: E501

        Submission of a simple or complex bid for a open capacity/energy market tender. By specifying the product, delivery date and market, the bid is automatically assigned to the corresponding open tender. The gate closure time of the tender is relevant for the submission.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_bid_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidSubmission body:
        :return: BidSubmissionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_bid" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/bids', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BidSubmissionResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_bid(self, id, **kwargs):  # noqa: E501
        """Updates a simple, complex bid or a bid component  # noqa: E501

        Connecting zone, volumes and prices can be changed (only applies to simple bids and individual components of a complex bid). Furthermore, linkages can be defined. The validation rules apply as for bid submission. It is possible to only include necessary information (change) in the request body, thus omitting bid attributes which are not to be changed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bid(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidIdentification id: Bid identification (required)
        :param BidModification body:
        :return: Bid
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_bid_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_bid_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def update_bid_with_http_info(self, id, **kwargs):  # noqa: E501
        """Updates a simple, complex bid or a bid component  # noqa: E501

        Connecting zone, volumes and prices can be changed (only applies to simple bids and individual components of a complex bid). Furthermore, linkages can be defined. The validation rules apply as for bid submission. It is possible to only include necessary information (change) in the request body, thus omitting bid attributes which are not to be changed.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_bid_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param BidIdentification id: Bid identification (required)
        :param BidModification body:
        :return: Bid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_bid" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `update_bid`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['OAuth2']  # noqa: E501

        return self.api_client.call_api(
            '/bids/{id}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Bid',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
