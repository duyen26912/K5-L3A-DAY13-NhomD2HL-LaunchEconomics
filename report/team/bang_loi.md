# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Duyên · Người gắn nhãn 2: Huyền (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Hệ thống | Ngữ cảnh | Không | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 19 / 20 = 95%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Ca 16 (Hệ thống hay Ngữ cảnh): trợ lý gửi tin lúc 2:14 sáng đúng thiết kế "gửi ngay khi xong", không vi phạm thiết kế hay chính sách nào; sai nằm ở giả định khách sẵn sàng nhận tin mọi giờ, nên là Ngữ cảnh. Chỉ gắn Hệ thống khi trợ lý làm trái thiết kế hoặc chính sách.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed` (kèm `trace_id`, lý do `ma_khong_hop_le`); đếm theo ngày, cảnh báo khi > 2% số yêu cầu trong ngày | Nhận diện mẫu mã đơn sàn TMĐT và tự tra sang mã vận đơn; không tra được thì chỉ khách chỗ tìm mã vận đơn (kèm ảnh mẫu) thay vì dừng | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát tự động mỗi giờ: tin nhắn "đã hoàn tiền" không có event `refund_ledger_write` với `ket_qua = ok` cùng `trace_id`; ngưỡng 0 ca, có 1 ca là cảnh báo ngay | Chỉ gửi "đã hoàn tiền" khi API sổ cái trả `ok`; lỗi 503 sau 3 lần thử thì báo "đang xử lý", tạo việc cho nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` có `reason` "số tiền" mà nhân viên kiểm tra thấy đúng chính sách; theo dõi tỉ lệ hằng tuần, ngưỡng > 1% số yêu cầu đã đóng | Mẫu tin nhắn luôn ghi cách tính, ví dụ "30.000 đ × 50% (trễ 24–48 giờ) = 15.000 đ" | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu`, đếm theo `loai` hằng ngày; ngưỡng > 30% yêu cầu của một loại thì xem xét loại khỏi phạm vi | Giữ cách chuyển nhân viên kèm tóm tắt; đưa `quoc_te` ra khỏi phạm vi pilot (thành công 27,3%, 1,88× chi phí nhân viên [simulated], nhiệm vụ A3) | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm tra mẫu 100 đơn/tuần, so `so_tien_da_hoan` với `so_tien_dung` theo bảng giá hiện hành; ngưỡng ≥ 1% đơn lệch là cảnh báo | Xoá bộ nhớ đệm bảng giá mỗi khi có bảng giá mới; ghi phiên bản bảng giá vào trace để truy lại các đơn bị lệch | Kế toán trưởng |

