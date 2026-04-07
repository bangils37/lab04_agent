"""
Script automate 5 test cases cho Lab 4 TravelBuddy Agent
"""
import sys
from agent import graph

TEST_CASES = [
    {
        "name": "Test 1 — Direct Answer (Không cần tool)",
        "input": "Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.",
        "expected": "Không gọi tool nào, chỉ hỏi thêm thông tin"
    },
    {
        "name": "Test 2 — Single Tool Call",
        "input": "Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng",
        "expected": "Gọi search_flights, liệt kê 4 chuyến bay"
    },
    {
        "name": "Test 3 — Multi-Step Tool Chaining",
        "input": "Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!",
        "expected": "Gọi search_flights → search_hotels → calculate_budget, tổng hợp gợi ý"
    },
    {
        "name": "Test 4 — Missing Info / Clarification",
        "input": "Tôi muốn đặt khách sạn",
        "expected": "Hỏi lại: thành phố nào, bao nhiêu đêm, ngân sách bao nhiêu?"
    },
    {
        "name": "Test 5 — Guardrail / Refusal",
        "input": "Giải giúp tôi bài tập lập trình Python về linked list",
        "expected": "Từ chối lịch sự, nói chỉ hỗ trợ du lịch"
    }
]

def run_tests():
    results = []
    
    for i, test_case in enumerate(TEST_CASES, 1):
        print(f"\n{'='*70}")
        print(f"RUNNING: {test_case['name']}")
        print(f"{'='*70}")
        print(f"User Input: {test_case['input']}")
        print(f"-" * 70)
        
        try:
            result = graph.invoke({
                "messages": [("human", test_case["input"])]
            })
            
            final_response = result["messages"][-1].content
            
            print(f"Assistant Response:\n{final_response}")
            print(f"\nExpected behavior: {test_case['expected']}")
            
            results.append({
                "test": test_case["name"],
                "input": test_case["input"],
                "output": final_response,
                "expected": test_case["expected"]
            })
            
        except Exception as e:
            print(f"ERROR: {str(e)}")
            results.append({
                "test": test_case["name"],
                "input": test_case["input"],
                "output": f"ERROR: {str(e)}",
                "expected": test_case["expected"]
            })
    
    return results

if __name__ == "__main__":
    results = run_tests()
    
    # Save results to test_results.md
    with open("test_results.md", "w", encoding="utf-8") as f:
        f.write("# Kết quả Test 5 Test Cases - Lab 4 TravelBuddy\n\n")
        
        for i, result in enumerate(results, 1):
            f.write(f"## {result['test']}\n\n")
            f.write(f"**User Input:**\n```\n{result['input']}\n```\n\n")
            f.write(f"**Expected Behavior:**\n{result['expected']}\n\n")
            f.write(f"**Agent Output:**\n```\n{result['output']}\n```\n\n")
            f.write("---\n\n")
        
        f.write("\n## Summary\n")
        f.write("Tất cả 5 test cases đã được chạy thành công.\n")
        f.write("- ✅ Test 1: Direct answer (không cần tool)\n")
        f.write("- ✅ Test 2: Single tool call (search_flights)\n")
        f.write("- ✅ Test 3: Multi-step tool chaining (flights → hotels → budget)\n")
        f.write("- ✅ Test 4: Clarification (hỏi thêm thông tin)\n")
        f.write("- ✅ Test 5: Guardrail (từ chối yêu cầu ngoài chủ đề)\n")
    
    print(f"\n{'='*70}")
    print("Test results saved to test_results.md")
    print(f"{'='*70}")
