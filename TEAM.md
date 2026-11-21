# Team

## Thông tin nhóm

- Tên nhóm: D2HL
- Lớp: L3A
- Repo nhóm: `K5-L3A-DAY13-NhomD2HL-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: https://github.com/duyen26912/K5-L3A-DAY13-NhomD2HL-LaunchEconomics -  nhánh `main` - commit chốt:

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Võ Thị Kim Huyền | 2A202603679 | vothikimhuyenvta@gmail.com | copengoknghek | Chủ nhiệm vụ **A** (CP1) + quản lý repo; người gắn nhãn 2 (C) |
|   2 | Nguyễn Thị Duyên | 2A202603698 | nguyenduyen.260903@gmail.com | duyen26912 | Chủ nhiệm vụ **C** (CP3) rồi **B** (CP2); người gắn nhãn 1 (C) |
|   3 | Nguyễn Đức Huân | 2A202603690 | huanducj@gmail.com | NgHuanLHd | Chủ nhiệm vụ **D** (CP4) + soát hồ sơ, push bản nộp |
|   4 | Vũ Gia Linh | 2A202603677 | vugialinh905@gmail.com | vugialinh905-wq | Chủ nhiệm vụ **E** (CP5) + chốt hồ sơ launch v0, trình bày |

### Cách chia việc của nhóm (2 đợt)

Nhóm không tách vai "người viết code" và "người kiểm số": **mỗi người ôm trọn một nhiệm vụ**: tự viết code, tự chạy, tự tính tay đối chiếu, tự điền file hồ sơ, tự commit.

- **Đợt 1 – Huyền + Duyên:** chuẩn bị repo, nhiệm vụ A, B, C (CP1–CP3), điền mục 1, 2, 3, 5 của hồ sơ, viết `BAN_GIAO.md`.
- **Đợt 2 – Huân + Linh:** nhiệm vụ D, E (CP4–CP5), chốt hồ sơ, duyệt chéo Gate 2a, nộp bài.
- **Nhiệm vụ C:** Duyên (người gắn nhãn 1) và Huyền (người gắn nhãn 2) gắn nhãn 20 ca độc lập, không trao đổi.
- **`src/lab13.py`:** mỗi thời điểm chỉ một người sửa, lần lượt Huyền → Duyên → Huân → Linh (trước khi sửa `git pull`, sửa xong commit + push ngay).

### Người giữ bút từng file

| File | Người giữ bút |
| --- | --- |
| `TEAM.md` | Duyên (Huân cập nhật đóng góp cuối) |
| `src/lab13.py` | Huyền → Duyên → Huân → Linh |
| `report/team/bang_chi_phi.md` | Huyền (phần A), Duyên (phần B) |
| `report/team/bang_loi.md` | Duyên |
| `report/team/pilot_plan.yaml` | Huân |
| `report/team/chi_so.md` | Linh |
| `report/team/ho_so_launch_v0.md` | Mục 1, 3: Huyền · mục 2, 5: Duyên · mục 6: Huân · mục 4, 7 + chốt + đề xuất: Linh |
| `report/team/phieu_cham.md`, `report/team/group_report.md` | Linh |

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

## VoThiKimHuyen-2A202603679

### Phần việc phụ trách

- Tạo và quản lý repo nhóm; nhiệm vụ A (A1–A4); `bang_chi_phi.md` phần A; mục 1 và 3 hồ sơ; người gắn nhãn 2 ở nhiệm vụ C; `BAN_GIAO.md` phần A.

### Đóng góp cụ thể

- A1: viết ba hàm kinh tế của việc chạy lại; ba phép thử đáp án biết trước ĐẠT (1,20 · 1,25 · 1,25), có tính tay đối chiếu.
- A2: viết `mo_hinh`; chi phí mỗi việc thành công **4.472 đ** [simulated], gấp **16,3×** hoá đơn token + tool chia số yêu cầu (274,7 đ); làm lại chiếm 51,8%, xem lại 40,7% [simulated].
- A3: tách theo `loai`: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` 1,88× so với 12.000 đ [simulated]; chỉ ra chạy lại không giúp `quoc_te` (lần 2 đúng 11,4%, lần 3 còn 2,2%).
- A4: cộng chi phí cố định 40 triệu đ/tháng cho `noi_dia` + `hang_nang`: **4.599 đ = 0,38×**, nửa khối lượng **5.784 đ = 0,48×** [simulated].
- Điền mục 1 và mục 3 của `ho_so_launch_v0.md`.
- Gắn nhãn 2 độc lập 20 ca ở nhiệm vụ C (đồng thuận 19/20 = 95%).
- Soát và sửa phạm vi pilot: 6 depot chạy thử chỉ có 20 nhân viên (chia 10 + 10 dưới 20 cụm) nên đổi thành 12 depot, 40 nhân viên, chia 20 + 20.

### Bằng chứng

- Commit `6851c84` (A1), `2574056` và `7b6ecdf` (A2, A3), `3d86f1d` (A4), `7fb4dc4` (mục 1, 3 hồ sơ), `672670e` (hai bộ nhãn C), `3357dfd` (sửa phạm vi pilot).
- File: `src/lab13.py` (khối A1–A4), `report/team/bang_chi_phi.md` (bảng A1–A4), `report/team/ho_so_launch_v0.md` (mục 1, 3), `report/team/bang_loi.md` (cột nhãn người 2).
- Báo cáo cá nhân: `report/team/2A202603679_VoThiKimHuyen.md`.

## NguyenThiDuyen-2A202603698

### Phần việc phụ trách

- `TEAM.md`; toàn bộ nhiệm vụ C (`bang_loi.md`, người gắn nhãn 1); nhiệm vụ B (B1–B4, `bang_chi_phi.md` phần B); mục 2 và 5 hồ sơ; `BAN_GIAO.md` phần B, C.

### Đóng góp cụ thể

-

### Bằng chứng

-

## NguyenDucHuan-2A202603690

### Phần việc phụ trách

- Nhiệm vụ D (D1–D3); `pilot_plan.yaml`; mục 6 hồ sơ; soát toàn bộ hồ sơ; checklist và push bản nộp cuối.

### Đóng góp cụ thể

-

### Bằng chứng

-

## VuGiaLinh-2A202603677

### Phần việc phụ trách

- Nhiệm vụ E (E1–E3); `chi_so.md`; mục 4 và 7 hồ sơ; chốt `ho_so_launch_v0.md` và đề xuất; `phieu_cham.md`; `group_report.md`; trình bày trước hội đồng.

### Đóng góp cụ thể

- E1: viết khối tính thử ba chỉ số trong `src/lab13.py` trên 1.200 yêu cầu: chính **82,83%** (994/1.200), bỏ qua gợi ý **27,12%** (48/177), mở lại 7 ngày **4,25%** (51/1.200; 3,97% trong phạm vi). Ghi rõ đợt chạy thử không có đối chứng nên chưa kết luận được tác động.
- `chi_so.md`: đặc tả 3 chỉ số + 2 chỉ số tự đề xuất; 10 event đều có `trace_id`; kiểm tra chéo mọi chỉ số tính được từ event.
- E2: 4 dòng rủi ro kinh tế, mỗi dòng có tác động đã tính, dấu hiệu theo dõi, hành động và một vai trò (làm lại ×2: 6.787 đ; xem lại 100%: 0,98×–1,03×; xem lại ×2: 6.292 đ; khối lượng một nửa: +2.370 đ/việc) [simulated].
- E3: mục 4 và 7 hồ sơ; đề xuất **Go có điều kiện** với 4 điều kiện, mỗi điều kiện có vai trò và ngày kiểm tra.
- Viết `group_report.md` và điền kết quả duyệt chéo từ hội đồng (25/30, Go có điều kiện, câu hỏi và câu trả lời của nhóm).
- Báo cáo cá nhân: `report/team/2A202603677_VuGiaLinh.md`.

### Bằng chứng

- Commit `dc79c6f` (CP5-E: `src/lab13.py` khối E1, `chi_so.md`, mục 4, 7 và đề xuất trong `ho_so_launch_v0.md`, bản nháp `group_report.md`).
- File: `report/team/chi_so.md`, `report/team/ho_so_launch_v0.md` (mục 4, 7, đề xuất), `report/team/phieu_cham.md`, `report/team/group_report.md`.
- Báo cáo cá nhân: `report/team/2A202603677_VuGiaLinh.md`.
