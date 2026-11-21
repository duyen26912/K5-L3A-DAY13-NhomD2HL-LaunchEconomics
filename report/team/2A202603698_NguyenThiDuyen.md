# Báo cáo cá nhân — NguyenThiDuyen-2A202603698

## 1. Thông tin thành viên

- Họ tên: Nguyễn Thị Duyên
- MSSV: 2A202603698
- Email: nguyenduyen.260903@gmail.com
- GitHub: duyen26912
- Vai trong nhóm: chủ nhiệm vụ **C** (CP3) rồi **B** (CP2); người gắn nhãn 1 ở nhiệm vụ C; giữ bút `TEAM.md`. Nhóm chia việc theo 2 đợt, mỗi người ôm trọn một nhiệm vụ (tự code, tự chạy, tự tính tay đối chiếu, tự điền hồ sơ); tôi thuộc đợt 1 cùng Huyền và viết bàn giao cho Huân, Linh.

## 2. Phần việc phụ trách

- `TEAM.md`: thông tin nhóm, thành viên, cách chia việc, người giữ bút từng file.
- Nhiệm vụ C: người gắn nhãn 1, `report/team/bang_loi.md` (hai bộ nhãn, đồng thuận, quy tắc ca không trùng, bảng khắc phục 5 ca).
- Nhiệm vụ B (B1–B4): khối "Nhiệm vụ B" trong `src/lab13.py` và phần B của `report/team/bang_chi_phi.md`.
- Mục 2 (ba yếu tố nhạy nhất) và mục 5 (bảng lỗi) của `report/team/ho_so_launch_v0.md`.
- `BAN_GIAO.md` phần B, C.

## 3. Đóng góp cụ thể

- **B1 · Đổi từng yếu tố:** gọi lại `mo_hinh` cho 9 kịch bản (giá token ×2 / ÷2, xem lại ×2 / ÷2, làm lại ×2 / ÷2, lương +25%, giới hạn 2 lần, giới hạn 1 lần) so với gốc 4.472 đ [simulated]. Thêm `assert` tự kiểm "giảm một nửa = nửa mức tăng gấp đôi": 5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9 (%), in ĐẠT.
- **B2 · Đổi một cặp và xếp hạng:** token ×2 + xem lại ×2 = **6.543 đ (+46,3%)** [simulated], đúng bằng 5,6% + 40,7% vì mô hình cộng tuyến tính. Xếp hạng: 1. số ca làm lại (+51,8%) · 2. tỉ lệ xem lại (+40,7%) · 3. lương nhân viên (+23,1%); giá token ×2 chỉ +5,6% nên pilot phải theo dõi làm lại và xem lại, không phải giá token.
- **B3 · Giới hạn chạy lại:** tính chi phí cả hệ thống = chi phí trợ lý + 12.000 đ × số yêu cầu không thành công. Giới hạn **2 lần** rẻ nhất (6.901.220 đ), so với 1 lần 7.449.781 đ và 3 lần 7.037.585 đ [simulated]. Giới hạn 1 lần cho chi phí mỗi việc thành công thấp nhất (4.111 đ) nhưng đẩy thêm 85 yêu cầu sang nhân viên, cả hệ thống đắt hơn 548.561 đ.
- **B4 · Xem lại 100%:** phạm vi `noi_dia` + `hang_nang`: (948 × 5 + 48 × 9) × 2.000 + 224.513 = 10.568.513 đ ÷ 900 = **11.743 đ = 0,98×** [simulated]; nếu dùng phút làm lại trung bình trong dữ liệu (15,3 phút) thì **12.415 đ = 1,03×**. Hoà vốn: mỗi lần xem lại ≤ 5,1 phút (hoặc ≤ 4,8 phút).
- **Nhiệm vụ C · Gắn nhãn:** gắn độc lập cả 20 ca trong 8 phút, không trao đổi với Huyền. Đồng thuận **19/20 = 95%**; ca lệch duy nhất là ca 16 (tôi gắn Hệ thống, Huyền gắn Ngữ cảnh), thống nhất **Ngữ cảnh** với quy tắc: chỉ gắn Hệ thống khi trợ lý làm trái thiết kế hoặc chính sách.
- **Nhiệm vụ C · Bảng khắc phục:** chọn 5 ca đủ 5 loại (9, 7, 18, 4, 17); mỗi dòng có event đo được, ngưỡng, tần suất và một vai trò (PM trợ lý hoàn phí, Kỹ sư trưởng agent, Trưởng nhóm CSKH, Kế toán trưởng). Đồng bộ tên event với danh sách 10 event trong `chi_so.md` (`refund_ledger_write`, `ticket_reopened`, `handoff_to_staff`, `audit_sample_checked`).
- **Hồ sơ và bàn giao:** điền mục 2 và mục 5 của hồ sơ launch v0 (người phụ trách là vai trò có quyền quyết định); viết `BAN_GIAO.md` phần B, C gồm số chính, gợi ý dùng cho `chi_so.md` và luật dừng trong `pilot_plan.yaml`, câu hội đồng hay hỏi.

## 4. Bằng chứng

| Commit | Nội dung |
| --- | --- |
| `8ab5cee` | `TEAM.md`: thông tin nhóm và phân công |
| `5ef541d` | CP2-B1..B4: khối Nhiệm vụ B trong `src/lab13.py`, bảng B1–B4 trong `bang_chi_phi.md` |
| `f0a4517` | CP2-CP3: bảng khắc phục 5 ca trong `bang_loi.md`, mục 2 + 5 hồ sơ, `BAN_GIAO.md` phần B, C |

Con số tự kiểm tay: B1 làm lại ×2 = 4.472 + 2.264.000 / 978 = 6.787 đ; B2 = 4.472 + 245.585 / 978 (token ×2) + 1.780.000 / 978 (xem lại ×2) = 4.472 + 251 + 1.820 ≈ 6.543 đ; B4 như trên. Mọi số từ cột `_simulated` có nhãn [simulated].

## 5. Công cụ AI đã dùng

- **Claude (Claude Code):** hỗ trợ viết khung vòng lặp kịch bản B1–B3 trong `src/lab13.py`, soát định dạng bảng và câu chữ trong `bang_chi_phi.md`, `bang_loi.md`, `BAN_GIAO.md`, tổng hợp báo cáo cá nhân từ lịch sử commit.
- **Cách tự kiểm tra:** không dùng thẳng số AI đưa ra. Kiểm tính tuyến tính bằng `assert` trong code và tính tay lại B2, B4; đối chiếu số trong hồ sơ với output `lab13.py`. Nhãn nhiệm vụ C do tôi tự gắn, không dùng AI gắn nhãn (theo `RULES.md`).

## 6. Tự đánh giá

- **Làm tốt:** B1–B4 đủ số và có tự kiểm; xếp hạng ba yếu tố cho nhóm biết pilot cần theo dõi làm lại và xem lại; B4 chỉ ra con số bất lợi (xem lại 100% gần hết tiết kiệm) để đề xuất Go có điều kiện. Nhiệm vụ C đạt đồng thuận 95%, bàn giao có số rõ để đợt 2 dùng lại.
- **Cần cải thiện:** B4 có hai mức phút làm lại (9 và 15,3 phút) nên con số kết luận chưa thống nhất một giá trị; tên event ở bảng khắc phục ban đầu chưa khớp với `chi_so.md`, phải sửa lại sau. Lần sau thống nhất danh sách event với người làm E ngay từ đầu.
