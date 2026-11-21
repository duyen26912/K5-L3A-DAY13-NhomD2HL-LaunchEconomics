# Bàn giao đợt 1 → đợt 2 (Huyền + Duyên → Huân + Linh)

- Commit cuối của đợt 1: `f0a4517` ("CP2-CP3: bang khac phuc 5 ca, muc 2 + 5 ho so, BAN_GIAO phan B, C")
- `cd src; python lab13.py` chạy **ĐẠT** ba phép thử A1 và in đủ A2, A3, A4, B1–B4.
- Từ đây **Huân giữ `src/lab13.py`** (D), sau đó tới Linh (E). Trước khi sửa: `git pull`.
- Mọi số có chữ [simulated] phải giữ nhãn đó khi dùng lại trong `chi_so.md`, `pilot_plan.yaml`, hồ sơ.

## Phần A · Chi phí (Huyền viết)

- CPS gốc: ...
- CPS phạm vi noi_dia + hang_nang: ...
- 4 dòng A3: ...
- A4: ...
- Phạm vi pilot đã chốt và lý do bằng số: ...

## Phần B · Độ nhạy (Duyên)

Nguồn: `report/team/bang_chi_phi.md`, code ở khối "Nhiệm vụ B" trong `src/lab13.py`. Tất cả là **simulated** (gồm tiền xem lại, làm lại).

| Số chính | Giá trị |
| --- | --- |
| Xếp hạng 3 yếu tố nhạy nhất | 1. Số ca làm lại (×2: +51,8%) · 2. Tỉ lệ xem lại (×2: +40,7%) · 3. Lương nhân viên (+25%: +23,1%) |
| Giá token gấp đôi | chỉ +5,6% (4.723 đ) |
| B2 · token ×2 + xem lại ×2 | 6.543 đ (+46,3%) = tổng hai tác động riêng (mô hình tuyến tính) |
| B3 · giới hạn rẻ nhất cho công ty | **2 lần**: 6.901.220 đ cả hệ thống (1 lần: 7.449.781 đ · 3 lần: 7.037.585 đ) |
| B3 · giới hạn cho CPS thấp nhất | 1 lần: 4.111 đ, nhưng đẩy thêm 85 yêu cầu sang nhân viên, đắt hơn 548.561 đ |
| B4 · xem lại 100% (noi_dia + hang_nang) | **11.743 đ = 0,98×** (9 phút làm lại/ca) · **12.415 đ = 1,03×** (15,3 phút/ca, trung bình trong dữ liệu) |
| B4 · hoà vốn | mỗi lần xem lại ≤ 5,1 phút (làm lại 9 phút) hoặc ≤ 4,8 phút (làm lại 15,3 phút) |

**Dùng cho đợt 2:**
- Linh (E2 rủi ro kinh tế): dùng "làm lại ×2 → +51,8%" và "xem lại ×2 → +40,7%" làm 2 dòng rủi ro; B4 cho thấy xem lại 100% thì gần như không tiết kiệm.
- Huân (`pilot_plan.yaml`): luật dừng chi phí nên bám tỉ lệ làm lại và tỉ lệ xem lại; giới hạn số lần chạy đề xuất là 2; đưa các số trên vào `simulated_inputs`.

**Câu hội đồng hay hỏi:**
- "Vì sao giới hạn 2 lần mà không phải 1 lần?" → 1 lần cho CPS thấp nhất nhưng thêm 85 việc nhân viên làm thay × 12.000 đ, cả hệ thống đắt hơn.
- "Xem lại 100% thì chi phí bao nhiêu?" → (948 × 5 + 48 × 9) × 2.000 + 224.513 = 10.568.513 ÷ 900 = 11.743 đ.

## Phần C · Bảng lỗi (Duyên)

Nguồn: `report/team/bang_loi.md`.

- Hai bộ nhãn độc lập: người gắn nhãn 1 Duyên, người gắn nhãn 2 Huyền. **Đồng thuận 19/20 = 95%.**
- Ca không trùng: ca 16 (Hệ thống / Ngữ cảnh) → thống nhất **Ngữ cảnh** (gửi 2:14 sáng đúng thiết kế "gửi ngay khi xong", sai ở giả định giờ nhận tin).
- Nhãn thống nhất: Do người dùng 1, 6, 9, 14 · Hệ thống 2, 7, 8, 15, 20 · Ngữ cảnh 3, 10, 16, 18 · Giới hạn hệ thống 4, 11, 13, 19 · Ngầm 5, 12, 17.
- Bảng khắc phục 5 ca: 9 (PM trợ lý hoàn phí) · 7 (Kỹ sư trưởng agent) · 18 (Trưởng nhóm CSKH) · 4 (PM trợ lý hoàn phí) · 17 (Kế toán trưởng).

**Dùng cho đợt 2:**
- Linh (`chi_so.md`): các event đã dùng ở bảng khắc phục: `input_validation_failed`, `reopen`, `handoff_to_staff`, đối soát tin nhắn "đã hoàn" với sổ cái theo `trace_id`. Có thể đưa vào bảng 10 event.
- Huân (luật dừng an toàn): ca 7 (báo "đã hoàn" khi sổ cái lỗi) và ca 20 (hoàn 2 lần) là lỗi mất tiền, ngưỡng 0 ca.

## Việc còn dở / chỗ chưa chắc

- Mục 1, 3 hồ sơ: Huyền điền.
- B4 phụ thuộc số phút làm lại: đề cho 9 phút/ca (0,98×), dữ liệu trung bình 15,3 phút/ca (1,03×) [simulated]. Hồ sơ nên ghi cả hai, chưa chắc đáp án dùng mức nào.
- Ca 9 (bảng khắc phục) dùng event `input_validation_failed`, chưa nằm trong 10 event của `chi_so.md`; Linh cân nhắc thêm hoặc giữ là event phụ.
