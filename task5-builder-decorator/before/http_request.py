class HttpRequest:
    def __init__(self, url, method='GET', headers=None, body=None,
                 timeout=30, retries=3, auth_token=None,
                 proxy=None, ssl_verify=True, follow_redirects=True,
                 cache_ttl=0, compression=None):
        self.url = url
        self.method = method
        self.headers = headers or {}
        self.body = body
        self.timeout = timeout
        self.retries = retries
        self.auth_token = auth_token
        self.proxy = proxy
        self.ssl_verify = ssl_verify
        self.follow_redirects = follow_redirects
        self.cache_ttl = cache_ttl
        self.compression = compression


def send_http(req):
    return {"status": 200, "body": "response", "request": req}


def log_middleware(result):
    print(f"[LOG] {result['request'].url}")
    return result


def auth_middleware(result):
    if result['request'].auth_token:
        result['request'].headers['Authorization'] = f"Bearer {result['request'].auth_token}"
    return result


def cache_middleware(result):
    if result['request'].cache_ttl > 0:
        print(f"[CACHE] TTL: {result['request'].cache_ttl}")
    return result


def retry_middleware(result):
    print(f"[RETRY] Max: {result['request'].retries}")
    return result


def compress_middleware(result):
    if result['request'].compression:
        result['request'].headers['Accept-Encoding'] = result['request'].compression
    return result


def execute_request(req, middleware_flags):
    result = send_http(req)
    if middleware_flags & 0x01: result = log_middleware(result)
    if middleware_flags & 0x02: result = auth_middleware(result)
    if middleware_flags & 0x04: result = cache_middleware(result)
    if middleware_flags & 0x08: result = retry_middleware(result)
    if middleware_flags & 0x10: result = compress_middleware(result)
    return result
