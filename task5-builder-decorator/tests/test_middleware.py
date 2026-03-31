"""Тесты для middleware."""
from http_request import HttpRequest, HttpRequestBuilder
from middleware import (
    Middleware, NullMiddleware, LoggingMiddleware,
    AuthMiddleware, CacheMiddleware, RetryMiddleware,
    CompressionMiddleware, MiddlewareChain
)


def test_null_middleware():
    """Тест NullMiddleware - ничего не делает."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .build())

    middleware = NullMiddleware()
    result = middleware.handle(request)

    assert result["status"] == 200
    assert result["request"] == request


def test_logging_middleware(capsys):
    """Тест LoggingMiddleware - логирует запрос."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .set_method("POST")
              .build())

    middleware = LoggingMiddleware()
    result = middleware.handle(request)

    captured = capsys.readouterr()
    assert "[LOG] POST https://api.example.com" in captured.out


def test_auth_middleware():
    """Тест AuthMiddleware - добавляет заголовок Authorization."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .with_auth("secret_token")
              .build())

    middleware = AuthMiddleware()
    result = middleware.handle(request)

    assert "Authorization" in request.headers
    assert request.headers["Authorization"] == "Bearer secret_token"


def test_cache_middleware(capsys):
    """Тест CacheMiddleware - логирует кеширование."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .with_cache(60)
              .build())

    middleware = CacheMiddleware()
    result = middleware.handle(request)

    captured = capsys.readouterr()
    assert "[CACHE] Caching for 60 seconds" in captured.out


def test_compression_middleware():
    """Тест CompressionMiddleware - добавляет заголовок Accept-Encoding."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .with_compression("gzip")
              .build())

    middleware = CompressionMiddleware()
    result = middleware.handle(request)

    assert "Accept-Encoding" in request.headers
    assert request.headers["Accept-Encoding"] == "gzip"


def test_middleware_chain_single():
    """Тест цепочки с одним middleware."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .build())

    chain = MiddlewareChain().add(LoggingMiddleware())
    result = chain.execute(request)

    assert result["status"] == 200


def test_middleware_chain_multiple(capsys):
    """Тест цепочки с несколькими middleware."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .with_auth("token")
              .with_cache(60)
              .build())

    chain = (MiddlewareChain()
            .add(LoggingMiddleware())
            .add(AuthMiddleware())
            .add(CacheMiddleware()))

    result = chain.execute(request)

    captured = capsys.readouterr()
    assert "[LOG]" in captured.out
    assert "[CACHE]" in captured.out
    assert "Authorization" in request.headers


def test_middleware_chain_order(capsys):
    """Тест порядка выполнения middleware."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .build())

    chain = (MiddlewareChain()
            .add(LoggingMiddleware())
            .add(CacheMiddleware()))

    chain.execute(request)

    captured = capsys.readouterr()
    log_pos = captured.out.find("[LOG]")
    cache_pos = captured.out.find("[CACHE]")

    assert log_pos < cache_pos


def test_middleware_chain_empty():
    """Тест пустой цепочки - использует NullMiddleware."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .build())

    chain = MiddlewareChain()
    result = chain.execute(request)

    assert result["status"] == 200


def test_middleware_chain_fluent_interface():
    """Тест fluent interface для MiddlewareChain."""
    chain = MiddlewareChain()

    assert chain.add(LoggingMiddleware()) is chain
    assert chain.add(AuthMiddleware()) is chain


def test_middleware_set_next():
    """Тест установки следующего обработчика."""
    first = LoggingMiddleware()
    second = AuthMiddleware()

    result = first.set_next(second)

    assert result is second
    assert first._next_handler is second
