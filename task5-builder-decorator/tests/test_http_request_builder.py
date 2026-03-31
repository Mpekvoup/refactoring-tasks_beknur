"""Тесты для HttpRequestBuilder."""
import pytest
from http_request import HttpRequest, HttpRequestBuilder


def test_builder_minimal():
    """Тест создания запроса с минимальными параметрами."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .build())

    assert request.url == "https://api.example.com"
    assert request.method == "GET"
    assert request.timeout == 30


def test_builder_full():
    """Тест создания запроса со всеми параметрами."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com/users")
              .set_method("POST")
              .with_headers({"User-Agent": "MyApp"})
              .with_body({"name": "John"})
              .with_timeout(60)
              .with_retries(5)
              .with_auth("secret_token")
              .with_cache(120)
              .with_compression("gzip")
              .build())

    assert request.url == "https://api.example.com/users"
    assert request.method == "POST"
    assert request.headers["User-Agent"] == "MyApp"
    assert request.body == {"name": "John"}
    assert request.timeout == 60
    assert request.retries == 5
    assert request.auth_token == "secret_token"
    assert request.cache_ttl == 120
    assert request.compression == "gzip"


def test_builder_validation_no_url():
    """Тест валидации: URL обязателен."""
    with pytest.raises(ValueError, match="URL is required"):
        (HttpRequestBuilder()
         .set_method("GET")
         .build())


def test_builder_validation_invalid_method():
    """Тест валидации: недопустимый HTTP метод."""
    with pytest.raises(ValueError, match="Invalid HTTP method"):
        (HttpRequestBuilder()
         .set_url("https://api.example.com")
         .set_method("INVALID")
         .build())


def test_builder_validation_negative_timeout():
    """Тест валидации: таймаут должен быть положительным."""
    with pytest.raises(ValueError, match="Timeout must be positive"):
        (HttpRequestBuilder()
         .set_url("https://api.example.com")
         .with_timeout(-10)
         .build())


def test_builder_validation_negative_retries():
    """Тест валидации: retries не может быть отрицательным."""
    with pytest.raises(ValueError, match="Retries must be non-negative"):
        (HttpRequestBuilder()
         .set_url("https://api.example.com")
         .with_retries(-1)
         .build())


def test_builder_fluent_interface():
    """Тест fluent interface - все методы возвращают builder."""
    builder = HttpRequestBuilder()

    assert builder.set_url("https://api.example.com") is builder
    assert builder.set_method("POST") is builder
    assert builder.with_timeout(60) is builder


def test_builder_method_case_insensitive():
    """Тест: метод преобразуется в верхний регистр."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .set_method("post")
              .build())

    assert request.method == "POST"


def test_builder_headers_merge():
    """Тест: заголовки объединяются."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com")
              .with_headers({"User-Agent": "MyApp"})
              .with_headers({"Accept": "application/json"})
              .build())

    assert len(request.headers) == 2
    assert request.headers["User-Agent"] == "MyApp"
    assert request.headers["Accept"] == "application/json"
