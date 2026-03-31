from typing import Dict, Any
from user_validator import UserValidator
from inventory_service import InventoryService
from price_calculator import PriceCalculator
from order_repository import OrderRepository
from notification_service import NotificationService
from discount_strategy import PromoCodeResolver


class OrderManager:
    def __init__(
        self,
        user_validator: UserValidator,
        inventory_service: InventoryService,
        price_calculator: PriceCalculator,
        order_repository: OrderRepository,
        notification_service: NotificationService,
        promo_code_resolver: PromoCodeResolver
    ):
        self.user_validator = user_validator
        self.inventory_service = inventory_service
        self.price_calculator = price_calculator
        self.order_repository = order_repository
        self.notification_service = notification_service
        self.promo_code_resolver = promo_code_resolver

    def create_order(self, user_id: str, items: Dict[str, int], promo_code: str = None) -> Dict[str, Any]:
        self.user_validator.validate(user_id)
        self.inventory_service.validate_availability(items)

        item_prices = {item_id: self.inventory_service.get_item_price(item_id) for item_id in items}

        discount_strategy = self.promo_code_resolver.get_discount_strategy(promo_code)
        subtotal = sum(item_prices[item_id] * qty for item_id, qty in items.items())
        discount = discount_strategy.calculate_discount(subtotal)

        total = self.price_calculator.calculate_total(subtotal, discount)

        self.inventory_service.reserve_items(items)

        order = {
            'id': self.order_repository.get_next_order_id(),
            'user': user_id,
            'items': items,
            'total': total,
            'status': 'new'
        }

        self.order_repository.save_order(order)

        user_email = self.user_validator.get_user_email(user_id)
        self.notification_service.send_notification(
            user_email,
            'Order Confirmation',
            f'Order {order["id"]} confirmed. Total: {total}'
        )

        return order
