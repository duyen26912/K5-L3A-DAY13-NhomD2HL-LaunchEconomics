# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

Tính bằng khối "Nhiệm vụ E1" trong `src/lab13.py`, trên 1.200 yêu cầu của đợt chạy thử.

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83%** (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12%** (48/177: 41 sửa + 7 bỏ) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25%** (51/1.200); trong phạm vi `noi_dia` + `hang_nang`: 3,97% |
| Dùng | Nhóm tự đề xuất: **% yêu cầu của nhóm can thiệp được mở bằng trợ lý** | Số `refund_request_created` của nhân viên nhóm trợ lý có `agent_suggestion_shown` cùng `trace_id`, chia tổng yêu cầu của nhóm trợ lý; theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: **% đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần** (bắt lỗi ngầm như ca 5, 17) | Số `audit_sample_checked` có `so_tien_da_hoan ≠ so_tien_dung`, chia 100 đơn mẫu mỗi tuần; cảnh báo khi ≥ 1% | Không cần tính |

Chỉ số trong đợt chạy thử là 82,83%. Đợt chạy thử không có nhóm đối chứng nên **không** kết luận được tác động của trợ lý so với baseline 0,70; pilot có đối chứng (`pilot_plan.yaml`) mới trả lời được câu này. Chỉ số chính chênh lệch lớn theo loại: `noi_dia` 95,3% · `hang_nang` 76,6% · `doi_tac` 58,8% · `quoc_te` 32,0%.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent (`logix_runs.csv`).

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien_vnd, depot, staff_id, arm (tro_ly / doi_chung), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | request_id, attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện cho nhân viên |
| `staff_review_decision` | Nhân viên | staff_id, quyet_dinh (giu / sua / bo), phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi / sửa / bỏ |
| `staff_rework_completed` | Nhân viên | staff_id, phut_lam_lai (đo thật), ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua (ok / loi), trace_id | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | reason (thieu_du_lieu / ngoai_pham_vi / het_lan_chay), tom_tat, trace_id | Khi chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | request_id, closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | request_id, reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | request_id, so_tien_da_hoan, so_tien_dung, phien_ban_bang_gia, trace_id | Hằng tuần, 100 đơn mẫu |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- **Chính** (đóng 24 giờ, không mở lại 7 ngày): `refund_request_created` (mốc bắt đầu) + `ticket_closed` (closed_at − created ≤ 24 giờ) + `ticket_reopened` (không có trong 7 ngày sau closed_at). Đo được.
- **Dùng** (bỏ qua gợi ý): `staff_review_decision` với quyet_dinh ∈ {sua, bo}, chia số `staff_review_decision`. Đo được.
- **An toàn** (mở lại 7 ngày): `ticket_reopened` trong 7 ngày sau `ticket_closed`, chia số `ticket_closed`. Đo được.
- **Dùng tự đề xuất** (% yêu cầu mở bằng trợ lý): `agent_suggestion_shown` nối với `refund_request_created` qua `trace_id`, lọc arm = tro_ly. Đo được.
- **An toàn tự đề xuất** (% đơn hoàn sai tiền): `audit_sample_checked`. Đo được.
- **Chi phí mỗi việc thành công** (dùng trong luật dừng chi phí): `agent_run_completed` (token, tool) + `staff_review_decision.phut_xem_lai` + `staff_rework_completed.phut_lam_lai`, chia số yêu cầu thành công. Đo được; thay phút simulated bằng phút đo thật sau tuần 1.
- **Lỗi mất tiền** (ca 7, 20 trong `bang_loi.md`): `refund_ledger_write` trùng `idempotency_key`, hoặc tin nhắn "đã hoàn" không có `refund_ledger_write` ok cùng `trace_id`. Đo được, ngưỡng 0 ca.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy và A4 (`bang_chi_phi.md`). Mọi tác động là **simulated**.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%: 4.472 đ → **6.787 đ** [simulated] | Tỉ lệ làm lại trong phạm vi theo tuần > 7% (đợt chạy thử: 4,9%), từ `staff_rework_completed` | Thu hẹp về `noi_dia`, giới hạn 2 lần chạy; rà 20 trace làm lại gần nhất | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** (9 phút làm lại); **12.415 đ = 1,03×** (15,3 phút làm lại như dữ liệu) [simulated]: gần như không tiết kiệm | % yêu cầu được xem lại còn > 50% cuối bước rollout 0.25; phút xem lại trung bình > 5,1 phút (hoà vốn) | Giảm xem lại theo bậc khi tỉ lệ sửa + bỏ < 15%; rút gọn màn hình xem lại | Trưởng nhóm CSKH |
| Tỉ lệ xem lại tăng gấp đôi | +40,7%: 4.472 đ → **6.292 đ** [simulated] | Số `staff_review_decision` / số yêu cầu nhóm trợ lý, theo tuần | Không mở rộng rollout cho tới khi tỉ lệ xem lại quay về mức đợt chạy thử | PM trợ lý hoàn phí |
| Khối lượng thấp hơn dự kiến | Cố định 40 triệu/tháng: +1.185 đ/việc ở 45.000 yc/tháng, **+2.370 đ/việc** khi còn một nửa (tổng 5.784 đ = 0,48×) [simulated] | Số việc thành công theo tuần < 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
