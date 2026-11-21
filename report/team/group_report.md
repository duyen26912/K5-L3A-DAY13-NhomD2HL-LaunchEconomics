# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính.

## 1. Thông tin nhóm

- Tên nhóm: D2HL
- Lớp: L3A
- Thành viên: xem `TEAM.md` (Võ Thị Kim Huyền, Nguyễn Thị Duyên, Nguyễn Đức Huân, Vũ Gia Linh)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để hội đồng Gate 2a quyết định có duyệt kế hoạch pilot hay không. Hồ sơ trả lời bốn câu: có đáng chạy không (chi phí mỗi việc thành công), nhân viên có dùng không (chỉ số, event), khi hỏng thì sao (bảng lỗi), pilot có ra được quyết định không (đối chứng, cỡ mẫu, luật dừng).

Nhóm chia 2 đợt, mỗi người ôm trọn một nhiệm vụ (tự code, tự chạy, tự tính tay đối chiếu, tự điền hồ sơ, tự commit): đợt 1 Huyền (A) + Duyên (B, C); đợt 2 Huân (D) + Linh (E). `src/lab13.py` chỉ một người sửa tại mỗi thời điểm; bàn giao giữa hai đợt qua `BAN_GIAO.md`.

## 3. Giải pháp

- **A · Chi phí** (`bang_chi_phi.md`): ba phép thử A1 ĐẠT (1,20 · 1,25 · 1,25); `mo_hinh` tính tử số trên mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm việc thành công; tách theo `loai`; cộng chi phí cố định 40 triệu/tháng.
- **B · Độ nhạy** (`bang_chi_phi.md`): 9 kịch bản đổi từng yếu tố, một cặp, giới hạn 1/2/3 lần chạy theo chi phí cả hệ thống, xem lại 100%.
- **C · Bảng lỗi** (`bang_loi.md`): hai người gắn nhãn độc lập 20 ca theo 5 loại Google PAIR, so nhãn, viết quy tắc cho ca lệch, bảng khắc phục 5 ca đủ 5 loại.
- **D · Pilot** (`pilot_plan.yaml`): cỡ mẫu theo ba cách chia, chọn chia theo nhân viên 20 + 20, mức chênh 6 điểm, 3 luật dừng NẾU – TRONG – THÌ – KHÔNG THÌ.
- **E · Chỉ số, rủi ro, hồ sơ** (`chi_so.md`, `ho_so_launch_v0.md`): 3 chỉ số tính thử + 2 tự đề xuất, 10 event có `trace_id`, 4 rủi ro kinh tế, hồ sơ 7 mục và đề xuất.

## 4. Kết quả

- Chi phí mỗi việc thành công: **4.472 đ** = 16,3× hoá đơn token/yêu cầu [simulated]; giờ nhân viên chiếm 92,5%.
- Phạm vi `noi_dia` + `hang_nang` cộng cố định: **4.599 đ = 0,38×** của 12.000 đ (0,48× khi khối lượng còn một nửa) [simulated]; loại `quoc_te` (1,88×) và `doi_tac` (0,85×).
- Ba yếu tố nhạy nhất: làm lại (+51,8%), xem lại (+40,7%), lương (+23,1%); giá token ×2 chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống. Xem lại 100%: **0,98× – 1,03×** [simulated].
- Bảng lỗi: đồng thuận **19/20 = 95%**.
- Pilot: chia theo nhân viên 20 + 20, chỉ đủ mẫu cho mức chênh 6 điểm (power 0,64 ở 5 điểm).
- Chỉ số trong đợt chạy thử: chính 82,83% · bỏ qua gợi ý 27,12% · mở lại 7 ngày 4,25%.
- **Đề xuất:** Go có điều kiện (4 điều kiện, mỗi điều kiện có vai trò phụ trách và ngày kiểm tra).
- Kết quả duyệt chéo nhóm nhận được từ hội đồng: ... (điền sau buổi duyệt chéo: điểm / 30, quyết định của hội đồng, câu hỏi và câu trả lời)
- Nhận xét của giảng viên: ...

## 5. Khó khăn và cách xử lý

- Chia 2 đợt nên dễ xung đột git ở `src/lab13.py`: quy ước một người giữ file tại mỗi thời điểm, `git pull` trước khi sửa, commit + push ngay sau khi chạy được.
- Người đợt 2 cần hiểu số của đợt 1 để trả lời hội đồng: viết `BAN_GIAO.md` (số chính, số simulated, câu hội đồng hay hỏi).
- Bản phân công ghi `run_00001` = 263,7 đ; dữ liệu cho 262,7 đ (123,7 + 64,0 + 75). Nhóm dùng số tính từ dữ liệu.
- ...

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

- Phút xem lại và làm lại là số giả lập; chi phí thật có thể lệch, đặc biệt B4 (0,98× hay 1,03× tuỳ phút làm lại). Cần đo phút thật ngay tuần 1 pilot.
- 40 nhân viên không đủ mẫu cho mức chênh 5 điểm; nếu tác động thật nhỏ, pilot có thể không kết luận được (power 0,64).
- Đợt chạy thử không có đối chứng nên 82,83% chưa nói được gì về tác động của trợ lý.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, arxiv.org/abs/2504.13359
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", pair.withgoogle.com
- Tài liệu statsmodels, `NormalIndPower` (`stats.power`)
- Đề bài và hướng dẫn Lab 13 (`docs/`)
