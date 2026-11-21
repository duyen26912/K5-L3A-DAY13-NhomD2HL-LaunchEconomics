# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: D2HL · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn bộ: **4.472 đ/việc TC** [simulated] (gấp 16,3× hoá đơn 274,7 đ/yc; làm lại 51,8%, xem lại 40,7%). Phạm vi `noi_dia` + `hang_nang`: **3.414 đ** (chưa cố định); cộng cố định 40 tr/tháng: **4.599 đ** ở 45.000 yc/tháng, **5.784 đ** ở nửa khối lượng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (×2: +51,8%) · 2. Tỉ lệ xem lại (×2: +40,7%) · 3. Lương nhân viên (+25%: +23,1%); giá token ×2 chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ / 1.200 yêu cầu); xem lại 100% = 11.743 đ (0,98×) đến 12.415 đ (1,03×) [simulated] | Giả lập | Chủ nhiệm vụ B (Duyên) |
| 3 · So với nhân viên tự làm | Cả hệ thống (1.200 yc, đã cộng 222 ca nhân viên làm thay): **5.865 đ/yc = 0,49×** của 12.000 đ [simulated]. Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` **1,88×** (loại `quoc_te`, `doi_tac` khỏi pilot). Phạm vi pilot + cố định: **0,38×** (45.000 yc/tháng) – **0,48×** (nửa khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | ... | ... | ... |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 19/20 = 95% (≥ 80%); 20 ca: 4 do người dùng · 5 hệ thống · 4 ngữ cảnh · 4 giới hạn · 3 ngầm (nhãn thống nhất); 5 cách khắc phục đủ 5 loại (ca 9, 7, 18, 4, 17), mỗi cách có event + ngưỡng + tần suất và một vai trò | Xong, có bằng chứng (`bang_loi.md`) | Người gắn nhãn 1 (Duyên) |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20 (ngẫu nhiên, cùng tuần, ≥ 20 cụm mỗi nhóm), phạm vi `noi_dia` + `hang_nang`. Cỡ mẫu: 1.251 yc/nhóm nếu chia theo yêu cầu; theo nhân viên chỉ đủ mức chênh **6 điểm** (859/nhóm, mỗi người ≥ 299 yc, DE 6,96), nếu tác động thật là 5 điểm thì power chỉ **0,64**. Tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi) nên luật an toàn so với đối chứng (≥ 2 điểm) kèm trần 6%, không dùng trần 3%. 3 luật dừng (an toàn, chi phí > 8.000 đ [simulated], bỏ qua gợi ý > 40%); `decision_date` 2027-01-05 | Xong, có bằng chứng (`pilot_plan.yaml`; ngưỡng chi phí dựa trên số simulated) | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | ... | ... | ... |

**Đề xuất:** Go · Go có điều kiện · No-go (giữ một). Go có điều kiện: ghi từng điều kiện, người phụ trách, ngày kiểm tra. No-go: ghi việc phải làm để quay lại cổng.

- ...
