from typing import Dict, Any


class UserValidator:
    def __init__(self, users: Dict[str, Dict[str, Any]]):
        self.users = users

    def validate(self, user_id: str) -> None:
        if user_id not in self.users:
            raise ValueError(f'User {user_id} not found')

        if self.users[user_id].get('banned', False):
            raise ValueError(f'User {user_id} is banned')

    def get_user_email(self, user_id: str) -> str:
        return self.users[user_id]['email']
