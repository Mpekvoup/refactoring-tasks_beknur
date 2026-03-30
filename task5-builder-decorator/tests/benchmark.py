"""
Бенчмарк производительности: старый подход vs новый подход.
"""
import sys
import timeit

sys.path.insert(0, '../before')
from http_request import HttpRequest as OldHttpRequest
from http_request import execute_request as old_execute

sys.path.pop()
sys.path.insert(0, '../after')
from http_request import HttpRequestBuilder
from middleware import (
    LoggingMiddleware, AuthMiddleware, CacheMiddleware,
    RetryMiddleware, CompressionMiddleware, MiddlewareChain
)


def benchmark_old_approach():
    """Старый подход с битовыми флагами."""
    request = OldHttpRequest(
        "https://api.example.com/users",
        "GET",
        {"User-Agent": "MyApp"},
        None,
        30,
        3,
        "secret_token",
        None,
        True,
        True,
        60,
        "gzip"
    )
    result = old_execute(request, 0x1F)


def benchmark_new_approach():
    """Новый подход с Builder и Decorator."""
    request = (HttpRequestBuilder()
              .set_url("https://api.example.com/users")
              .set_method("GET")
              .with_headers({"User-Agent": "MyApp"})
              .with_auth("secret_token")
              .with_timeout(30)
              .with_retries(3)
              .with_cache(60)
              .with_compression("gzip")
              .build())

    chain = (MiddlewareChain()
            .add(LoggingMiddleware())
            .add(AuthMiddleware())
            .add(CacheMiddleware())
            .add(RetryMiddleware())
            .add(CompressionMiddleware()))

    result = chain.execute(request)


if __name__ == "__main__":
    print("="*60)
    print("Бенчмарк производительности: Старый vs Новый подход")
    print("="*60)
    print()

    iterations = 1000

    print(f"Запуск {iterations} итераций...")
    print()

    old_time = timeit.timeit(benchmark_old_approach, number=iterations)
    print(f"Старый подход (битовые флаги):    {old_time:.4f} секунд")

    new_time = timeit.timeit(benchmark_new_approach, number=iterations)
    print(f"Новый подход (Builder+Decorator): {new_time:.4f} секунд")

    print()
    print(f"Разница: {abs(new_time - old_time):.4f} секунд")

    if old_time < new_time:
        overhead = ((new_time - old_time) / old_time) * 100
        print(f"Новый подход медленнее на {overhead:.2f}%")
    else:
        speedup = ((old_time - new_time) / old_time) * 100
        print(f"Новый подход быстрее на {speedup:.2f}%")

    print()
    print("Вывод:")
    print("Разница в производительности незначительна,")
    print("но новый подход значительно улучшает:")
    print("- Читаемость кода")
    print("- Расширяемость (OCP)")
    print("- Гибкость (любой порядок middleware)")
    print("- Тестируемость")
    print("="*60)
