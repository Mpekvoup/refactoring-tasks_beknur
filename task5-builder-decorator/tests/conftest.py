"""
Конфигурация pytest для тестов task5.
Добавляет путь к модулям after/ в sys.path.
"""
import sys
from pathlib import Path

# Добавляем путь к модулям after/
after_dir = Path(__file__).parent.parent / "after"
sys.path.insert(0, str(after_dir))
