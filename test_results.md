# Kết quả Test Lab 4: TravelBuddy Agent

## Tóm tắt kết quả
✅ **Tất cả 6 test cases PASS**
- Test 1: Direct Answer (Không cần tool) ✅
- Test 2: Single Tool Call (search_flights) ✅
- Test 3: Multi-Step Tool Chaining ✅
- Test 4: Missing Info / Clarification ✅
- Test 5: Guardrail / Refusal ✅
- Test 6: Thêm test Direct Answer khác ✅

---

## Chi tiết Console Log

```
============================================================
2026-04-07 17:02:57,435 - TEST #1
2026-04-07 17:02:57,435 - ============================================================
2026-04-07 17:02:57,435 - User Input: Xin chào
2026-04-07 17:02:57,436 - ⏳ Agent processing request...
2026-04-07 17:03:02,416 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:03:02,419 - ✅ Agent response generated
2026-04-07 17:03:02,420 - Agent Response:
Chào bạn! Rất vui được gặp bạn. Mình là TravelBuddy, người bạn đồng hành cùng bạn lên kế hoạch cho những chuyến đi tuyệt vời tại Việt Nam đây! ✈️

Bạn đang ấp ủ dự định đi đâu hay cần mình hỗ trợ tìm vé máy bay, khách sạn hay tính toán ngân sách cho chuyến đi sắp tới không? Cứ chia sẻ với mình nhé, mình sẵn sàng giúp bạn ngay! 😊
2026-04-07 17:03:02,420 - ============================================================

2026-04-07 17:03:10,197 - 
============================================================
2026-04-07 17:03:10,198 - TEST #2
2026-04-07 17:03:10,198 - ============================================================
2026-04-07 17:03:10,198 - User Input: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
2026-04-07 17:03:10,199 - ⏳ Agent processing request...
2026-04-07 17:03:17,585 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:03:17,589 - 🔍 Searching flights from 'Hà Nội' to 'Đà Nẵng'
2026-04-07 17:03:17,589 - ✈️ Found 4 flights
2026-04-07 17:03:40,612 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:03:40,614 - ✅ Agent response generated
2026-04-07 17:03:40,615 - Agent Response:
Chào bạn! Rất vui được hỗ trợ bạn lên kế hoạch cho chuyến đi Đà Nẵng sắp tới. Dưới đây là các lựa chọn chuyến bay từ Hà Nội đi Đà Nẵng hiện có:

✈️ **CHUYẾN BAY:**
*   **VietJet Air:** 08:30 - 09:50 | 890.000đ (Hạng Economy)
*   **Bamboo Airways:** 11:00 - 12:20 | 1.200.000đ (Hạng Economy)
*   **Vietnam Airlines:** 06:00 - 07:20 | 1.450.000đ (Hạng Economy)
*   **Vietnam Airlines:** 14:00 - 15:20 | 2.800.000đ (Hạng Business)

Bạn đã chọn được chuyến bay nào ưng ý chưa? Nếu bạn cần tìm khách sạn tại Đà Nẵng, hãy cho mình biết **ngân sách dự kiến mỗi đêm** của bạn là bao nhiêu nhé, mình sẽ tìm những lựa chọn phù hợp nhất cho bạn!
2026-04-07 17:03:40,615 - ============================================================

2026-04-07 17:03:52,856 - 
============================================================
2026-04-07 17:03:52,857 - TEST #3
2026-04-07 17:03:52,857 - ============================================================
2026-04-07 17:03:52,857 - User Input: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
2026-04-07 17:03:52,858 - ⏳ Agent processing request...
2026-04-07 17:03:59,998 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:04:00,001 - 🔍 Searching flights from 'Hà Nội' to 'Phú Quốc'
2026-04-07 17:04:00,001 - ✈️ Found 3 flights
2026-04-07 17:04:02,741 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:04:02,745 - 🏨 Searching hotels in 'Phú Quốc' (max price: 1.000.000đ/night)
2026-04-07 17:04:02,745 - 🔑 Found 2 hotels matching criteria
2026-04-07 17:04:04,685 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:04:04,741 - 💰 Calculating budget - Total: 5.000.000đ
2026-04-07 17:04:04,744 - 📈 Expense items parsed: 2 items
2026-04-07 17:04:04,744 - Total expense: 2.700.000đ | Remaining: 2.300.000đ
2026-04-07 17:04:04,744 - ✅ Budget OK - 2.300.000đ remaining
2026-04-07 17:04:09,208 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:04:09,210 - ✅ Agent response generated
2026-04-07 17:04:09,211 - Agent Response:
Chào bạn! Rất vui được đồng hành cùng bạn lên kế hoạch cho chuyến đi Phú Quốc sắp tới. Với ngân sách 5 triệu đồng cho 2 đêm, mình đã tìm kiếm các lựa chọn tối ưu nhất để bạn có một chuyến đi thoải mái mà vẫn tiết kiệm đây:

✈️ **CHUYẾN BAY:**
Mình gợi ý bạn chọn chuyến của **VietJet Air** lúc **16:00 - 18:15** với giá **1.100.000đ**. Đây là mức giá tốt nhất hiện tại, giúp bạn tiết kiệm chi phí để dành cho các trải nghiệm khác tại đảo.

🏨 **KHÁCH SẠN:**
Với ngân sách 2 đêm, mình gợi ý **Lahana Resort** (3 sao) tại khu vực Dương Đông với giá **800.000đ/đêm** (tổng 1.600.000đ). Resort này có không gian xanh mát, rất phù hợp để nghỉ dưỡng. Nếu bạn muốn tiết kiệm hơn nữa để dành tiền ăn uống, **9Station Hostel** cũng là một lựa chọn rất thú vị và trẻ trung.

💰 **TỔNG CHI PHÍ DỰ KIẾN:**
*   **Vé máy bay:** 1.100.000đ
*   **Khách sạn (2 đêm):** 1.600.000đ
*   **Tổng chi phí cơ bản:** 2.700.000đ
*   **Ngân sách còn lại:** **2.300.000đ** (Số tiền này rất thoải mái để bạn chi tiêu ăn uống, thuê xe máy khám phá đảo và tham quan các điểm du lịch trong 3 ngày 2 đêm).

💡 **GỢI Ý THÊM:**
*   Với 2.3 triệu còn lại, bạn có thể thuê xe máy (khoảng 150k/ngày) để tự do đi lại.
*   Đừng quên ghé chợ đêm Dương Đông để thưởng thức hải sản tươi sống nhé!
*   Bạn có muốn mình hỗ trợ đặt thêm dịch vụ nào khác hoặc cần tư vấn thêm về lịch trình tham quan không?
2026-04-07 17:04:09,211 - ============================================================

2026-04-07 17:04:36,877 - 
============================================================
2026-04-07 17:04:36,877 - TEST #4
2026-04-07 17:04:36,877 - ============================================================
2026-04-07 17:04:36,878 - User Input: Tôi muốn đặt khách sạn
2026-04-07 17:04:36,878 - ⏳ Agent processing request...
2026-04-07 17:04:39,352 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:04:39,354 - ✅ Agent response generated
2026-04-07 17:04:39,354 - Agent Response:
Chào bạn! Rất vui được đồng hành cùng bạn trong chuyến đi sắp tới. Để mình tìm được những khách sạn ưng ý nhất cho bạn, bạn cho mình biết một vài thông tin nhé:

1. Bạn dự định đi **thành phố nào**?
2. **Ngân sách** tối đa bạn muốn chi cho mỗi đêm là bao nhiêu?

Chỉ cần có thông tin này, mình sẽ lọc ngay những lựa chọn tốt nhất cho bạn!
2026-04-07 17:04:39,355 - ============================================================

2026-04-07 17:04:56,662 - 
============================================================
2026-04-07 17:04:56,662 - TEST #5
2026-04-07 17:04:56,663 - ============================================================
2026-04-07 17:04:56,663 - User Input: Giải giúp tôi bài tập lập trình Python về linked list
2026-04-07 17:04:56,663 - ⏳ Agent processing request...
2026-04-07 17:04:58,852 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:04:58,853 - ✅ Agent response generated
2026-04-07 17:04:58,854 - Agent Response:
Xin lỗi, như tôi đã chia sẻ, tôi chỉ hỗ trợ về du lịch. Yêu cầu này ngoài khả năng của tôi. Bạn có thể tìm một chuyên gia khác cho vấn đề này.

Nếu bạn đang lên kế hoạch cho một chuyến đi, tôi rất sẵn lòng giúp bạn tìm vé máy bay, khách sạn hoặc tính toán ngân sách cho chuyến đi đó! Bạn có dự định đi đâu không?
2026-04-07 17:04:58,854 - ============================================================

2026-04-07 17:05:32,203 - 
============================================================
2026-04-07 17:05:32,204 - TEST #6
2026-04-07 17:05:32,204 - ============================================================
2026-04-07 17:05:32,204 - User Input: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
2026-04-07 17:05:32,204 - ⏳ Agent processing request...
2026-04-07 17:05:50,146 - HTTP Request: POST https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite-preview:generateContent "HTTP/1.1 200 OK"
2026-04-07 17:05:50,148 - ✅ Agent response generated
2026-04-07 17:05:50,148 - Agent Response:
Chào bạn! Rất vui được làm quen với bạn. Mình là TravelBuddy, người bạn đồng hành lý tưởng để cùng bạn lên kế hoạch cho những chuyến đi tuyệt vời tại Việt Nam đây! ✈️

Việt Nam mình có rất nhiều điểm đến thú vị, tùy vào sở thích của bạn mà mình có thể gợi ý nhé:

*   **Nếu bạn thích biển xanh, cát trắng:** Đà Nẵng, Nha Trang, Phú Quốc hay Quy Nhơn là những lựa chọn tuyệt vời.
*   **Nếu bạn muốn tận hưởng không khí se lạnh, núi rừng hùng vĩ:** Đà Lạt, Sapa hay Hà Giang sẽ khiến bạn mê mẩn.
*   **Nếu bạn muốn khám phá văn hóa, lịch sử:** Huế, Hội An hay Hà Nội luôn là những điểm đến không bao giờ cũ.

Bạn đang nghiêng về phong cách nào? Hoặc bạn có dự định đi từ đâu không? Hãy chia sẻ với mình, mình sẽ giúp bạn tìm chuyến bay và khách sạn phù hợp nhất với ngân sách của bạn ngay! 😊
2026-04-07 17:05:50,149 - ============================================================

2026-04-07 17:06:48,624 - === Session Ended ===
```

---

## Phân tích kết quả

### ✅ Test 1 - Direct Answer (Không cần tool)
- **Input:** "Xin chào"
- **Output:** Agent chào hỏi và hỏi về intention của user
- **Kết quả:** PASS - Không gọi tool, trả lời trực tiếp

### ✅ Test 2 - Single Tool Call
- **Input:** "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"
- **Tool calls:** `search_flights("Hà Nội", "Đà Nẵng")` → 4 flights found
- **Output:** Liệt kê 4 chuyến bay với giá sắp xếp từ rẻ đến đắt
- **Kết quả:** PASS ✈️ Found 4 flights

### ✅ Test 3 - Multi-Step Tool Chaining (CHÍNH YẾU)
- **Input:** "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"
- **Tool chain:**
  1. `search_flights("Hà Nội", "Phú Quốc")` → 3 flights, recommended 1.100.000đ
  2. `search_hotels("Phú Quốc", max_price: 1.000.000đ)` → 2 hotels
  3. `calculate_budget(5000000, "vé_bay:1100000,khách_sạn:1600000")` → OK, remaining 2.300.000đ
- **Output:** Tư vấn hoàn chỉnh với bảng chi phí và gợi ý
- **Kết quả:** PASS ✅ Tool chaining thành công!

### ✅ Test 4 - Missing Info / Clarification
- **Input:** "Tôi muốn đặt khách sạn"
- **Tool calls:** NONE (không gọi tool)
- **Output:** Hỏi lại thành phố & ngân sách
- **Kết quả:** PASS - Agent hỏi lại thông tin thiếu

### ✅ Test 5 - Guardrail / Refusal
- **Input:** "Giải giúp tôi bài tập lập trình Python về linked list"
- **Tool calls:** NONE
- **Output:** Từ chối lịch sự, giải thích chỉ hỗ trợ du lịch
- **Kết quả:** PASS 🛡️ Guardrail hoạt động

### ✅ Test 6 - Direct Answer (Test thêm)
- **Input:** "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."
- **Tool calls:** NONE
- **Output:** Agent gợi ý các điểm đến theo phong cách
- **Kết quả:** PASS - Trả lời thân thiện, hữu ích

---

## Kết luận

| Tiêu chí | Điểm | Ghi chú |
| --- | --- | --- |
| Setup LangGraph + Tools | ✅ | Graph chạy được, agents gọi tool đúng |
| Tool implementations | ✅ | Tất cả 3 tools hoạt động, logging rõ |
| System Prompt | ✅ | Agent từ chối yêu cầu ngoài scope |
| Multi-step chaining | ✅ | Test 3 pass, chuỗi 3 tools liên tiếp |
| Code quality + logging | ✅ | Logging chi tiết, format rõ ràng |

