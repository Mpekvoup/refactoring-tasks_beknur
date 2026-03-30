from typing import Dict, Any, List


class OrderRepository:
    def __init__(self, db_connection):
        self.db = db_connection
        self.orders: List[Dict[str, Any]] = []

    def save_order(self, order: Dict[str, Any]) -> None:
        self.orders.append(order)
        self.db.execute(
            'INSERT INTO orders (id, user_id, items, total, status) VALUES (?, ?, ?, ?, ?)',
            (order['id'], order['user'], str(order['items']), order['total'], order['status'])
        )

    def get_next_order_id(self) -> int:
        return len(self.orders) + 1
