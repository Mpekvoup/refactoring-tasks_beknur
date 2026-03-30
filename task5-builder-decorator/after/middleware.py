"""
Middleware с паттерном Decorator (Chain of Responsibility).
"""
from abc import ABC, abstractmethod
from typing import Dict, Any, Optional
from http_request import HttpRequest


class Middleware(ABC):
    """
    Абстрактный базовый класс для middleware.
    Использует паттерн Chain of Responsibility.
    """

    def __init__(self):
        self._next_handler: Optional[Middleware] = None

    def set_next(self, handler: 'Middleware') -> 'Middleware':
        """Установить следующий обработчик в цепочке."""
        self._next_handler = handler
        return handler

    def handle(self, request: HttpRequest) -> Dict[str, Any]:
        """
        Обработать запрос и передать следующему обработчику.

        Args:
            request: HTTP-запрос

        Returns:
            Результат выполнения цепочки
        """
        result = self._process(request)

        if self._next_handler:
            return self._next_handler.handle(request)

        return result

    @abstractmethod
    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        """Обработать запрос (реализуется в подклассах)."""
        pass


class NullMiddleware(Middleware):
    """Null Object - пустой middleware, ничего не делает."""

    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        return {"status": 200, "body": "response", "request": request}


class LoggingMiddleware(Middleware):
    """Middleware для логирования запросов."""

    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        print(f"[LOG] {request.method} {request.url}")
        if self._next_handler:
            return self._next_handler.handle(request)
        return {"status": 200, "body": "response", "request": request}


class AuthMiddleware(Middleware):
    """Middleware для добавления аутентификации."""

    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        if request.auth_token:
            print(f"[AUTH] Adding auth token")
            request.headers['Authorization'] = f"Bearer {request.auth_token}"

        if self._next_handler:
            return self._next_handler.handle(request)
        return {"status": 200, "body": "response", "request": request}


class CacheMiddleware(Middleware):
    """Middleware для кеширования ответов."""

    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        if request.cache_ttl > 0:
            print(f"[CACHE] Caching for {request.cache_ttl} seconds")

        if self._next_handler:
            return self._next_handler.handle(request)
        return {"status": 200, "body": "response", "request": request}


class RetryMiddleware(Middleware):
    """Middleware для повторных попыток."""

    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        if request.retries > 0:
            print(f"[RETRY] Max retries: {request.retries}")

        if self._next_handler:
            return self._next_handler.handle(request)
        return {"status": 200, "body": "response", "request": request}


class CompressionMiddleware(Middleware):
    """Middleware для сжатия данных."""

    def _process(self, request: HttpRequest) -> Dict[str, Any]:
        if request.compression:
            print(f"[COMPRESS] Using {request.compression}")
            request.headers['Accept-Encoding'] = request.compression

        if self._next_handler:
            return self._next_handler.handle(request)
        return {"status": 200, "body": "response", "request": request}


class MiddlewareChain:
    """
    Цепочка middleware для динамической композиции.
    Позволяет создавать различные комбинации middleware.
    """

    def __init__(self):
        self._head: Optional[Middleware] = None
        self._tail: Optional[Middleware] = None

    def add(self, middleware: Middleware) -> 'MiddlewareChain':
        """
        Добавить middleware в цепочку.

        Args:
            middleware: Middleware для добавления

        Returns:
            self для fluent interface
        """
        if not self._head:
            self._head = middleware
            self._tail = middleware
        else:
            self._tail.set_next(middleware)
            self._tail = middleware

        return self

    def execute(self, request: HttpRequest) -> Dict[str, Any]:
        """
        Выполнить цепочку middleware.

        Args:
            request: HTTP-запрос

        Returns:
            Результат выполнения
        """
        if not self._head:
            null_middleware = NullMiddleware()
            return null_middleware.handle(request)

        return self._head.handle(request)
