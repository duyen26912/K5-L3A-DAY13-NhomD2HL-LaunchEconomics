# Báo cáo cá nhân — VoThiKimHuyen-2A202603679

## 1. Thông tin thành viên

- Họ tên: Võ Thị Kim Huyền
- MSSV: 2A202603679
- Email: vothikimhuyenvta@gmail.com
- GitHub: copengoknghek
- Vai trong nhóm: chủ nhiệm vụ **A** (CP1) kiêm quản lý repo; người gắn nhãn 2 ở nhiệm vụ C. Nhóm chia việc theo 2 đợt, mỗi người ôm trọn một nhiệm vụ (tự code, tự chạy, tự tính tay đối chiếu, tự điền hồ sơ), nên tôi vừa viết code vừa tự kiểm số phần A.

## 2. Phần việc phụ trách

- Tạo và quản lý repo nhóm `K5-L3A-DAY13-NhomD2HL-LaunchEconomics`.
- Nhiệm vụ A (A1–A4) trong `src/lab13.py` và phần A của `report/team/bang_chi_phi.md`.
- Mục 1 (chi phí mỗi việc thành công) và mục 3 (so với nhân viên tự làm) của `report/team/ho_so_launch_v0.md`.
- Người gắn nhãn 2 ở nhiệm vụ C: gắn 20 ca lỗi độc lập với người gắn nhãn 1 (Duyên).

## 3. Đóng góp cụ thể

- **A1 · Kinh tế của việc chạy lại:** viết ba hàm `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`; ba phép thử đáp án biết trước in ĐẠT (1,20 · 1,25 · 1,25). Tự tính tay: (1 − 0,2²) / 0,8 = 1,20; 1 / 0,8 = 1,25; (1 − 0,2³) / 0,8 / (1 − 0,2³) = 1,25.
- **A2 · Mô hình chi phí từ trace:** viết `mo_hinh(runs, reqs, …)`, tử số tính mọi lần chạy kể cả lần lỗi, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Kết quả: 978 việc thành công, chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ). Làm lại chiếm 51,8%, xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5%. Gắn nhãn `simulated` cho dòng xem lại, làm lại.
- **A3 · Tách theo loại:** vòng lặp theo cột `loai` và tỉ lệ lần chạy `ok` theo lần thử. `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` **1,88×** so với 12.000 đ [simulated]. Kết luận `quoc_te` không đáng để trợ lý xử lý: chỉ 27,3% thành công, lần chạy 2 đúng 11,4%, lần 3 còn 2,2%, nên chạy lại không giúp.
- **A4 · Chi phí cố định:** cộng 40 triệu đ/tháng cho phạm vi `noi_dia` + `hang_nang`: 33.750 việc thành công/tháng, 1.185 đ/việc, tổng **4.599 đ = 0,38×**; khi khối lượng còn một nửa **5.784 đ = 0,48×** [simulated]. Kết luận chi phí cố định không đổi quyết định ở hai mức khối lượng này.
- **Hồ sơ launch v0:** điền mục 1 và mục 3, ghi rõ đã cộng chi phí cố định hay chưa và tính ở khối lượng nào; đưa con số chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49× (đã cộng 222 ca nhân viên làm thay).
- **Nhiệm vụ C:** gắn nhãn 2 độc lập cả 20 ca, không trao đổi; commit hai bộ nhãn vào `bang_loi.md`. Đồng thuận 19/20 = 95%, ca lệch duy nhất là ca 16.
- **Soát phạm vi pilot:** phát hiện 6 depot đã chạy thử chỉ có 20 nhân viên (NV001–NV020), chia 10 + 10 thì dưới 20 cụm mỗi nhóm; sửa phạm vi trong `pilot_plan.yaml` và mục 6 hồ sơ thành cả 12 depot, 40 nhân viên, chia 20 + 20.

## 4. Bằng chứng

| Commit | Nội dung |
| --- | --- |
| `6851c84` | CP1-A1: ba hàm A1 trong `src/lab13.py`, bảng A1 trong `bang_chi_phi.md` |
| `672670e` | CP3: hai bộ nhãn độc lập trong `bang_loi.md`, đồng thuận 19/20 |
| `2574056` | CP1-A2: bảng A2 và hai câu trả lời trong `bang_chi_phi.md` |
| `7b6ecdf` | CP1-A2 + A3: hàm `mo_hinh`, tách chi phí theo `loai` |
| `3d86f1d` | CP1-A4: chi phí cố định phạm vi `noi_dia` + `hang_nang`, bảng A4 |
| `7fb4dc4` | Mục 1 và mục 3 trong `ho_so_launch_v0.md` |
| `3357dfd` | Sửa phạm vi pilot: 12 depot, 40 nhân viên, chia 20 + 20 (`pilot_plan.yaml`, mục 6 hồ sơ) |

Con số tự kiểm tay (ghi trong `bang_chi_phi.md`): `run_00001` = 4.759/1.000 × 26 + 492/1.000 × 130 + 5 × 15 = 262,7 đ; tool = 5.600 lần × 15 = 84.000 đ; A4: 45.000 × 900 / 1.200 = 33.750 việc/tháng, 40.000.000 / 33.750 = 1.185 đ/việc.

## 5. Công cụ AI đã dùng

- **Cursor (Claude):** hỗ trợ viết khung code cho các hàm A1, `mo_hinh`, vòng lặp A3 và phần A4; giải thích công thức số lần chạy kỳ vọng và hệ số chi phí; soát định dạng bảng trong `bang_chi_phi.md`.
- **Antigravity:** hỗ trợ đọc hiểu đề bài, đối chiếu yêu cầu từng checkpoint và soát câu chữ trong hồ sơ.
- **Cách tự kiểm tra:** không dùng thẳng số AI đưa ra. Ba phép thử A1 tính tay trước rồi mới chạy code; A2 tính tay một dòng `run_00001` và tổng tool để đối chiếu với code; A4 tính tay chi phí cố định mỗi việc. Khi bản phân công ghi `run_00001` = 263,7 đ mà dữ liệu cho 262,7 đ, tôi giữ số tính từ dữ liệu.

## 6. Tự đánh giá

- **Làm tốt:** nhiệm vụ A xong đủ A1–A4, ba phép thử ĐẠT, mọi số từ cột `_simulated` có nhãn; con số A3, A4 là căn cứ chính để nhóm thu hẹp phạm vi về `noi_dia` + `hang_nang`. Phát hiện kịp lỗi phạm vi pilot (6 depot chỉ có 20 nhân viên) trước khi gửi hồ sơ cho hội đồng.
- **Cần cải thiện:** phần A trong `BAN_GIAO.md` chưa điền đủ số, đợt 2 phải tự đọc lại `bang_chi_phi.md`; commit A2 tách thành hai lần (điền bảng trước, commit code sau) nên lịch sử commit chưa gọn. Lần sau sẽ commit code và bảng cùng lúc, và viết bàn giao ngay sau khi chốt số.
