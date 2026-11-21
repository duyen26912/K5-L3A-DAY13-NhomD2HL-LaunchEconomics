# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: D2HL · Lớp: L3A

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | Toàn bộ: **4.472 đ/việc TC** [simulated] (gấp 16,3× hoá đơn 274,7 đ/yc; làm lại 51,8%, xem lại 40,7%). Phạm vi `noi_dia` + `hang_nang`: **3.414 đ** (chưa cố định); cộng cố định 40 tr/tháng: **4.599 đ** ở 45.000 yc/tháng, **5.784 đ** ở nửa khối lượng [simulated] | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | 1. Số ca làm lại (×2: +51,8%) · 2. Tỉ lệ xem lại (×2: +40,7%) · 3. Lương nhân viên (+25%: +23,1%); giá token ×2 chỉ +5,6% [simulated]. Giới hạn 2 lần chạy rẻ nhất cho cả hệ thống (6.901.220 đ / 1.200 yêu cầu); xem lại 100% = 11.743 đ (0,98×) đến 12.415 đ (1,03×) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Cả hệ thống (1.200 yc, đã cộng 222 ca nhân viên làm thay): **5.865 đ/yc = 0,49×** của 12.000 đ [simulated]. Theo loại: `noi_dia` 0,22×, `hang_nang` 0,69×, `doi_tac` 0,85×, `quoc_te` **1,88×** (loại `quoc_te`, `doi_tac` khỏi pilot). Phạm vi pilot + cố định: **0,38×** (45.000 yc/tháng) – **0,48×** (nửa khối lượng) [simulated] | Giả lập | PM trợ lý hoàn phí |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử (chưa có đối chứng, chưa kết luận tác động): chính **82,83%** (994/1.200 đóng 24 giờ, không mở lại 7 ngày) · dùng: bỏ qua gợi ý **27,12%** (48/177) · an toàn: mở lại 7 ngày **4,25%** (51/1.200; 3,97% trong phạm vi). Thêm 2 chỉ số tự đề xuất; 10 event đều có `trace_id`, mọi chỉ số tính được từ event | Xong, có bằng chứng (`chi_so.md`, `lab13.py`) | Chủ nhiệm vụ E (Linh) |
| 5 · Bảng lỗi và cách khắc phục | Đồng thuận 19/20 = 95% (≥ 80%); 20 ca: 4 do người dùng · 5 hệ thống · 4 ngữ cảnh · 4 giới hạn · 3 ngầm (nhãn thống nhất); 5 cách khắc phục đủ 5 loại (ca 9, 7, 18, 4, 17), mỗi cách có event + ngưỡng + tần suất và một vai trò | Xong, có bằng chứng (`bang_loi.md`) | Kỹ sư trưởng agent |
| 6 · Pilot plan | Chia theo nhân viên 20 + 20 trên cả 12 depot, 40 nhân viên (ngẫu nhiên, phân tầng theo depot, cùng tuần, ≥ 20 cụm mỗi nhóm; 6 depot chạy thử chỉ có 20 người nên không đủ), phạm vi `noi_dia` + `hang_nang`. Cỡ mẫu: 1.251 yc/nhóm nếu chia theo yêu cầu; theo nhân viên chỉ đủ mức chênh **6 điểm** (859/nhóm, mỗi người ≥ 299 yc, DE 6,96), nếu tác động thật là 5 điểm thì power chỉ **0,64**. Tỉ lệ mở lại hiện tại 4,25% (3,97% trong phạm vi) nên luật an toàn so với đối chứng (≥ 2 điểm) kèm trần 6%, không dùng trần 3%. 3 luật dừng (an toàn, chi phí > 8.000 đ [simulated], bỏ qua gợi ý > 40%); `decision_date` 2027-01-05 | Xong, có bằng chứng (`pilot_plan.yaml`; ngưỡng chi phí dựa trên số simulated) | Giám đốc vận hành |
| 7 · Rủi ro kinh tế | Làm lại ×2: **6.787 đ (+51,8%)** · xem lại 100%: **11.743 đ = 0,98×** đến **12.415 đ = 1,03×** · xem lại ×2: 6.292 đ (+40,7%) · khối lượng còn một nửa: +2.370 đ/việc cố định (5.784 đ = 0,48×) [simulated]; mỗi rủi ro có dấu hiệu theo dõi, hành động và một vai trò | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện** cho pilot trợ lý hoàn phí, chỉ trong phạm vi `noi_dia` + `hang_nang`, cả 12 depot, chia theo nhân viên 20 + 20 (`pilot_plan.yaml`).

Lý do bằng số: trong phạm vi, chi phí mỗi việc thành công cộng cố định là 4.599 đ = **0,38×** nhân viên tự làm (0,48× khi khối lượng còn một nửa) [simulated]; `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×) đã loại. **Con số bất lợi:** xem lại 100% đẩy chi phí lên **0,98× – 1,03×** [simulated], gần như hết tiết kiệm; 40 nhân viên chỉ đủ mẫu cho mức chênh 6 điểm, tác động thật 5 điểm thì power chỉ **0,64**; còn hai lỗi mất tiền (ca 7, 20) chưa sửa. Vì vậy không Go thẳng mà Go kèm điều kiện:

| # | Điều kiện | Người phụ trách | Ngày kiểm tra |
| --: | --- | --- | --- |
| 1 | Có khoá chống trùng (`idempotency_key`) và đối soát sổ cái mỗi giờ; chỉ báo "đã hoàn" khi sổ cái trả ok (ca 7, 20); kiểm thử 0 ca hoàn trùng | Kỹ sư trưởng agent | 2026-12-01 (trước ngày bắt đầu) |
| 2 | Ký chấp nhận mức chênh 6 điểm (power 0,64 nếu tác động thật là 5 điểm) và chốt seed bốc thăm 20 + 20 | Giám đốc vận hành | 2026-12-01 |
| 3 | Bật đủ 10 event có `trace_id`; thay phút xem lại / làm lại simulated bằng phút đo thật và tính lại chi phí mỗi việc thành công | PM trợ lý hoàn phí | 2026-12-15 (sau tuần 1) |
| 4 | Kế hoạch giảm xem lại theo bậc: hạ khỏi 100% khi tỉ lệ sửa + bỏ < 15%; phút xem lại trung bình ≤ 5,1 phút (hoà vốn B4) | Trưởng nhóm CSKH | 2026-12-22 (cuối bước rollout 0.25) |

Chưa đạt điều kiện 1 và 2 thì không bắt đầu pilot; chưa đạt điều kiện 3 và 4 thì không sang bước rollout 0.50. Quyết định mở rộng chỉ đọc chỉ số chính vào `decision_date` 2027-01-05.
