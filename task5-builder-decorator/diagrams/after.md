# UML-диаграмма классов ПОСЛЕ рефакторинга

```mermaid
classDiagram
    class HttpRequest {
        +url: str
        +method: str
        +headers: dict
        +body: Any
        +timeout: int
        +retries: int
        +auth_token: str
        +proxy: str
        +ssl_verify: bool
        +follow_redirects: bool
        +cache_ttl: int
        +compression: str
        +__init__(...)
    }

    class HttpRequestBuilder {
        -_url: str
        -_method: str
        -_headers: dict
        -_body: Any
        -_timeout: int
        -_retries: int
        -_auth_token: str
        -_proxy: str
        -_ssl_verify: bool
        -_follow_redirects: bool
        -_cache_ttl: int
        -_compression: str
        +VALID_METHODS: Set
        +set_url(url): HttpRequestBuilder
        +set_method(method): HttpRequestBuilder
        +with_headers(headers): HttpRequestBuilder
        +with_body(body): HttpRequestBuilder
        +with_timeout(timeout): HttpRequestBuilder
        +with_retries(retries): HttpRequestBuilder
        +with_auth(token): HttpRequestBuilder
        +with_proxy(proxy): HttpRequestBuilder
        +with_ssl_verify(verify): HttpRequestBuilder
        +with_redirects(follow): HttpRequestBuilder
        +with_cache(ttl): HttpRequestBuilder
        +with_compression(compression): HttpRequestBuilder
        +build(): HttpRequest
        -_validate(): void
    }

    class Middleware {
        <<abstract>>
        #_next_handler: Middleware
        +set_next(handler): Middleware
        +handle(request): dict
        #_process(request)*: dict
    }

    class NullMiddleware {
        +_process(request): dict
    }

    class LoggingMiddleware {
        +_process(request): dict
    }

    class AuthMiddleware {
        +_process(request): dict
    }

    class CacheMiddleware {
        +_process(request): dict
    }

    class RetryMiddleware {
        +_process(request): dict
    }

    class CompressionMiddleware {
        +_process(request): dict
    }

    class MiddlewareChain {
        -_head: Middleware
        -_tail: Middleware
        +add(middleware): MiddlewareChain
        +execute(request): dict
    }

    HttpRequestBuilder --> HttpRequest: creates
    Middleware <|-- NullMiddleware
    Middleware <|-- LoggingMiddleware
    Middleware <|-- AuthMiddleware
    Middleware <|-- CacheMiddleware
    Middleware <|-- RetryMiddleware
    Middleware <|-- CompressionMiddleware
    MiddlewareChain --> Middleware: uses
    Middleware --> Middleware: _next_handler

    note for HttpRequestBuilder "Fluent interface\nВалидация в build()\nЧитаемый код\nОпциональные параметры"

    note for Middleware "Паттерн Decorator\nЛюбой порядок\nОткрыт для расширения (OCP)\nТестируемость"

    note for MiddlewareChain "Динамическая композиция\nПереиспользование\nFluent interface"
```
