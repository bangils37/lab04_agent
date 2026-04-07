# Kết quả test cho Lab 4

## 1. Kiểm tra tool logic trực tiếp

- `search_flights('Hà Nội', 'Đà Nẵng')`
  - Trả về 4 chuyến bay đúng theo dữ liệu mock.
- `search_hotels('Phú Quốc', 900000)`
  - Trả về 2 khách sạn phù hợp, sắp xếp theo rating giảm dần.
- `calculate_budget(5000000, 'vé_máy_bay:1100000,khách_sạn:1600000')`
  - Tính tổng chi phí 2.700.000đ và ngân sách còn lại 2.300.000đ.

## 2. Ghi chú

- `agent.py` đã được biên dịch thành công cùng với `tools.py`.
- Để chạy agent tương tác, cần điền giá trị `OPENAI_API_KEY` trong file `.env`.
