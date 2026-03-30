"""
HttpRequest после рефакторинга с паттерном Builder.
"""
from typing import Dict, Any, Optional


class HttpRequest:
    """HTTP-запрос с валидированными параметрами."""

    def __init__(self, url: str, method: str = 'GET', headers: Optional[Dict[str, str]] = None,
                 body: Optional[Any] = None, timeout: int = 30, retries: int = 3,
                 auth_token: Optional[str] = None, proxy: Optional[str] = None,
                 ssl_verify: bool = True, follow_redirects: bool = True,
                 cache_ttl: int = 0, compression: Optional[str] = None):
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

    def __repr__(self) -> str:
        return f"HttpRequest(url={self.url}, method={self.method})"


class HttpRequestBuilder:
    """
    Builder для создания HttpRequest с fluent interface.
    """

    VALID_METHODS = {'GET', 'POST', 'PUT', 'DELETE', 'PATCH', 'HEAD', 'OPTIONS'}

    def __init__(self):
        self._url: Optional[str] = None
        self._method: str = 'GET'
        self._headers: Dict[str, str] = {}
        self._body: Optional[Any] = None
        self._timeout: int = 30
        self._retries: int = 3
        self._auth_token: Optional[str] = None
        self._proxy: Optional[str] = None
        self._ssl_verify: bool = True
        self._follow_redirects: bool = True
        self._cache_ttl: int = 0
        self._compression: Optional[str] = None

    def set_url(self, url: str) -> 'HttpRequestBuilder':
        """Установить URL (обязательно)."""
        self._url = url
        return self

    def set_method(self, method: str) -> 'HttpRequestBuilder':
        """Установить HTTP метод."""
        self._method = method.upper()
        return self

    def with_headers(self, headers: Dict[str, str]) -> 'HttpRequestBuilder':
        """Добавить заголовки."""
        self._headers.update(headers)
        return self

    def with_body(self, body: Any) -> 'HttpRequestBuilder':
        """Установить тело запроса."""
        self._body = body
        return self

    def with_timeout(self, timeout: int) -> 'HttpRequestBuilder':
        """Установить таймаут."""
        self._timeout = timeout
        return self

    def with_retries(self, retries: int) -> 'HttpRequestBuilder':
        """Установить количество повторных попыток."""
        self._retries = retries
        return self

    def with_auth(self, token: str) -> 'HttpRequestBuilder':
        """Добавить токен аутентификации."""
        self._auth_token = token
        return self

    def with_proxy(self, proxy: str) -> 'HttpRequestBuilder':
        """Установить прокси."""
        self._proxy = proxy
        return self

    def with_ssl_verify(self, verify: bool) -> 'HttpRequestBuilder':
        """Установить проверку SSL."""
        self._ssl_verify = verify
        return self

    def with_redirects(self, follow: bool) -> 'HttpRequestBuilder':
        """Следовать ли за редиректами."""
        self._follow_redirects = follow
        return self

    def with_cache(self, ttl: int) -> 'HttpRequestBuilder':
        """Включить кеширование с заданным TTL."""
        self._cache_ttl = ttl
        return self

    def with_compression(self, compression: str) -> 'HttpRequestBuilder':
        """Включить сжатие (gzip, deflate, br)."""
        self._compression = compression
        return self

    def build(self) -> HttpRequest:
        """
        Создать HttpRequest с валидацией.

        Raises:
            ValueError: если параметры невалидны
        """
        self._validate()

        return HttpRequest(
            url=self._url,
            method=self._method,
            headers=self._headers.copy(),
            body=self._body,
            timeout=self._timeout,
            retries=self._retries,
            auth_token=self._auth_token,
            proxy=self._proxy,
            ssl_verify=self._ssl_verify,
            follow_redirects=self._follow_redirects,
            cache_ttl=self._cache_ttl,
            compression=self._compression
        )

    def _validate(self) -> None:
        """Валидация параметров перед созданием объекта."""
        if not self._url:
            raise ValueError("URL is required")

        if self._method not in self.VALID_METHODS:
            raise ValueError(f"Invalid HTTP method: {self._method}. "
                           f"Must be one of {self.VALID_METHODS}")

        if self._timeout <= 0:
            raise ValueError("Timeout must be positive")

        if self._retries < 0:
            raise ValueError("Retries must be non-negative")

        if self._cache_ttl < 0:
            raise ValueError("Cache TTL must be non-negative")
