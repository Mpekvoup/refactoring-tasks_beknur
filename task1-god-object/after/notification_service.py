from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, recipient: str, subject: str, message: str) -> None:
        pass


class EmailNotificationService(NotificationService):
    def __init__(self, smtp_host: str, smtp_port: int, sender_email: str):
        self.smtp_host = smtp_host
        
        self.smtp_port = smtp_port
        self.sender_email = sender_email

    def send_notification(self, recipient: str, subject: str, message: str) -> None:
        import smtplib
        server = smtplib.SMTP(self.smtp_host, self.smtp_port)
        server.sendmail(self.sender_email, recipient, f'Subject: {subject}\n\n{message}')
        server.quit()
