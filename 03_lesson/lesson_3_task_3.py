from address import Address
from mailing import Mailing

to_addr = Address(
    "123456",
    "Москва",
    "Ленина",
    "10",
    "15"
)

from_addr = Address(
    "654321",
    "Санкт-Петербург",
    "Пушкина",
    "5",
    "7"
)

mailing = Mailing(
    to_address=to_addr,
    from_address=from_addr,
    cost=150.50,
    track="TRACK123456"
)

print(
    f"Отправление {mailing.track} из "
    f"{mailing.from_address.index}, {mailing.from_address.city}, "
    f"{mailing.from_address.street}, {mailing.from_address.house} - "
    f"{mailing.from_address.apartment} в "
    f"{mailing.to_address.index}, {mailing.to_address.city}, "
    f"{mailing.to_address.street}, {mailing.to_address.house} - "
    f"{mailing.to_address.apartment}. Стоимость {mailing.cost} рублей."
)
