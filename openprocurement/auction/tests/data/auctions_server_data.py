from mock import sentinel

AUCTION_DOC_ID = 'some_id'

proxy_data_proxy_path = \
    {'server_config_redis': sentinel.REDIS,
     'connection_limit': sentinel.connection_limit,
     'proxy_connection_pool': sentinel.proxy_pool,
     'get_mapping': sentinel.get_mapping,
     'proxy_path': sentinel.proxy_path,
     'stream_proxy': sentinel.stream_proxy,
     'event_sources_pool': sentinel.event_sources_pool}

# there is no '/login' in request_url
# there is 'X-Forwarded-For' in headers
proxy_data_no_proxy_path_forwarded_header_1 = \
    {'server_config_redis': sentinel.REDIS,
     'get_mapping': sentinel.get_mapping,
     'proxy_path': None,
     'db': ['some_id0', AUCTION_DOC_ID, 'some_id1'],
     'request_headers': {
         'h0': 'h0',
         'X-Forwarded-For': 'hx',
         'h1': 'h1',
         'Host': 'new_host'
     },
     'request_url': 'http://netloc/path;params?query=argument#fragment',
     'transformed_url': 'http://new_host/path;params?query=argument#fragment',
     'redirect_url': sentinel.redirect_url}

# there is '/login' in request_url
# there is 'X-Forwarded-For' in headers
proxy_data_no_proxy_path_forwarded_header_2 = \
    {'server_config_redis': sentinel.REDIS,
     'get_mapping': sentinel.get_mapping,
     'proxy_path': None,
     'db': ['some_id0', AUCTION_DOC_ID, 'some_id1'],
     'request_headers': {
         'h0': 'h0',
         'X-Forwarded-For': 'hx',
         'h1': 'h1',
         'Host': 'new_host'
     },
     'request_url': 'http://netloc/login/path;params?query=argument#fragment',
     'transformed_url': 'http://new_host/path;params?query=argument#fragment',
     'redirect_url': sentinel.redirect_url}

# there is no 'X-Forwarded-For' in headers
proxy_data_no_proxy_path_no_forwarded_header = \
    {'server_config_redis': sentinel.REDIS,
     'get_mapping': sentinel.get_mapping,
     'proxy_path': None,
     'db': ['some_id0', AUCTION_DOC_ID, 'some_id1'],
     'request_headers': {'h0': 'h0',
                         'h1': 'h1',
                         'Host': 'new_host'},
     'abort': sentinel.abort}

proxy_data_no_proxy_path = \
    {'server_config_redis': sentinel.REDIS,
     'get_mapping': sentinel.get_mapping,
     'proxy_path': None,
     'pysse': sentinel.pysse,
     'abort': sentinel.abort}
