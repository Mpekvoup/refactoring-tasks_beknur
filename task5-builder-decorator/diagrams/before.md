# UML-диаграмма классов ДО рефакторинга

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
        +__init__(url, method, headers, body, timeout, retries, auth_token, proxy, ssl_verify, follow_redirects, cache_ttl, compression)
    }

    class execute_request {
        <<function>>
        +execute_request(req, middleware_flags)
    }

    class log_middleware {
        <<function>>
        +log_middleware(result)
    }

    class auth_middleware {
        <<function>>
        +auth_middleware(result)
    }

    class cache_middleware {
        <<function>>
        +cache_middleware(result)
    }

    class retry_middleware {
        <<function>>
        +retry_middleware(result)
    }

    class compress_middleware {
        <<function>>
        +compress_middleware(result)
    }

    execute_request --> log_middleware: calls if 0x01
    execute_request --> auth_middleware: calls if 0x02
    execute_request --> cache_middleware: calls if 0x04
    execute_request --> retry_middleware: calls if 0x08
    execute_request --> compress_middleware: calls if 0x10

    note for HttpRequest "Телескопический конструктор\n12 параметров\nНет валидации\nСложно использовать"

    note for execute_request "Битовые флаги: 0x01, 0x02, 0x04, 0x08, 0x10\nФиксированный порядок\nНарушение OCP\nMagic numbers"
```
