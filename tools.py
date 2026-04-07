from typing import Dict, List, Optional

from langchain_core.tools import tool

FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1_450_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2_800_000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1_200_000, "class": "economy"},
    ],
    ("Hà Nội", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1_350_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1_100_000, "class": "economy"},
    ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1_600_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950_000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1_300_000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3_200_000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1_300_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780_000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1_100_000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650_000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1_800_000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1_200_000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650_000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250_000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350_000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3_500_000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1_500_000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800_000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200_000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2_800_000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1_400_000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550_000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 180_000, "area": "Quận 1", "rating": 4.6},
    ],
}


def format_currency(amount: int) -> str:
    return f"{amount:,}".replace(",", ".") + "đ"


def find_flights(origin: str, destination: str) -> Optional[List[Dict]]:
    if (origin, destination) in FLIGHTS_DB:
        return FLIGHTS_DB[(origin, destination)]
    if (destination, origin) in FLIGHTS_DB:
        return FLIGHTS_DB[(destination, origin)]
    return None


def format_flight(flight: Dict) -> str:
    return (
        f"- {flight['airline']} | {flight['departure']} - {flight['arrival']} | "
        f"{format_currency(flight['price'])} | hạng {flight['class']}"
    )

@tool
def search_flights(origin: str, destination: str) -> str:
    """Tìm kiếm và format các chuyến bay giữa origin và destination."""
    origin = origin.strip()
    destination = destination.strip()
    flights = find_flights(origin, destination)

    if not flights:
        return f"Không tìm thấy chuyến bay từ {origin} đến {destination}."

    sorted_flights = sorted(flights, key=lambda x: x["price"])
    lines = [f"Tìm thấy {len(sorted_flights)} chuyến bay từ {origin} đến {destination}:"]
    for flight in sorted_flights:
        lines.append(format_flight(flight))

    return "\n".join(lines)

@tool
def search_hotels(city: str, max_price_per_night: int = 99_999_999) -> str:
    """Tìm kiếm khách sạn tại city và lọc theo giá tối đa mỗi đêm."""
    city = city.strip()
    if city not in HOTELS_DB:
        return f"Không tìm thấy dữ liệu khách sạn cho thành phố {city}."

    hotels = [hotel for hotel in HOTELS_DB[city] if hotel["price_per_night"] <= max_price_per_night]
    if not hotels:
        return (
            f"Không tìm thấy khách sạn tại {city} với giá dưới {format_currency(max_price_per_night)}/đêm. "
            "Hãy thử tăng ngân sách."
        )

    hotels.sort(key=lambda item: item["rating"], reverse=True)
    lines = [f"Khách sạn phù hợp tại {city} (tối đa {format_currency(max_price_per_night)}/đêm):"]
    for hotel in hotels:
        lines.append(
            f"- {hotel['name']} | {hotel['stars']} sao | {format_currency(hotel['price_per_night'])}/đêm | "
            f"Khu vực: {hotel['area']} | Rating: {hotel['rating']}"
        )

    return "\n".join(lines)

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """Tính toán ngân sách còn lại dựa trên tổng ngân sách và chuỗi expenses."""
    total_budget = int(total_budget)
    if not expenses:
        return "Không có khoản chi nào để tính."

    expense_items: Dict[str, int] = {}
    invalid_entries: List[str] = []
    for pair in expenses.split(","):
        if ":" not in pair:
            invalid_entries.append(pair)
            continue
        key, value = pair.split(":", 1)
        key = key.strip()
        value = value.strip().replace(".", "").replace("đ", "")
        if not key or not value.isdigit():
            invalid_entries.append(pair)
            continue
        expense_items[key] = int(value)

    if invalid_entries:
        return (
            "Định dạng expenses không hợp lệ. "
            f"Vui lòng dùng 'tên_khoản:số_tiền' cách nhau bằng dấu phẩy. "
            f"Các mục sai: {', '.join(invalid_entries)}"
        )

    total_expense = sum(expense_items.values())
    remaining = total_budget - total_expense
    lines = ["Bảng chi phí:"]
    for name, amount in expense_items.items():
        readable_name = name.replace("_", " ").capitalize()
        lines.append(f"- {readable_name}: {format_currency(amount)}")

    lines.append("---")
    lines.append(f"Tổng chi: {format_currency(total_expense)}")
    lines.append(f"Ngân sách: {format_currency(total_budget)}")
    if remaining >= 0:
        lines.append(f"Còn lại: {format_currency(remaining)}")
    else:
        lines.append(f"Vượt ngân sách {-remaining}đ! Cần điều chỉnh.")

    return "\n".join(lines)
