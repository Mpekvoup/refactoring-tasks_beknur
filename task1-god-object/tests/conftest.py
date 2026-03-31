"""
Конфигурация pytest для тестов task1.
"""

import sys
from pathlib import Path

after_dir = Path(__file__).parent.parent / "after"
sys.path.insert(0, str(after_dir))
