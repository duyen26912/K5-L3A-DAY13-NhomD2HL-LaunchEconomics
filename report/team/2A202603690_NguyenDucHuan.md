# Báo cáo cá nhân — NguyenDucHuan-2A202603690

## 1. Thông tin thành viên

- Họ tên: Nguyễn Đức Huân
- MSSV: 2A202603690
- Vai trong nhóm: Chủ nhiệm vụ **D** (CP4, `pilot_plan.yaml`) ở đợt 2; soát chéo hồ sơ; đẩy bản nộp lên GitHub (theo bản phân công 2 đợt của nhóm, không tách vai người viết code / người kiểm số)

## 2. Phần việc phụ trách

- Nhiệm vụ D: cỡ mẫu theo từng cách chia (D1), năm câu kiểm tra "tách được tác động" (D2), tỉ lệ mở lại hiện tại để đặt ngưỡng an toàn (D3).
- File `report/team/pilot_plan.yaml` (kế hoạch pilot, ba luật dừng, rollback, ngày quyết định).
- Khối code D trong `src/lab13.py` (mục "Nhiệm vụ D · Cỡ mẫu và kế hoạch pilot").
- Mục 6 (Pilot plan) của `report/team/ho_so_launch_v0.md`.
- Soát chéo hồ sơ của cả nhóm (nhãn `simulated`, số khớp giữa các file, không có từ bị cấm theo quy tắc 5 của lab), chạy checklist `SUBMISSION.md` và push bản nộp.
- Khi duyệt chéo Gate 2a: trả lời các câu hỏi về cỡ mẫu, cách chia nhóm, giới hạn số lần chạy và chi phí.

## 3. Đóng góp cụ thể

- **D1** (hàm `co_mau`, `he_so_thiet_ke` trong `lab13.py`): a) chia theo yêu cầu 1.251 yêu cầu mỗi nhóm; b) theo nhân viên, mỗi người 75 yêu cầu: hệ số thiết kế 2,48, 3.103 yêu cầu mỗi nhóm, 42 nhân viên mỗi nhóm, tổng 84 > 40 nên không đủ người; c) 20 nhân viên mỗi nhóm có cỡ mẫu hiệu dụng tối đa 20 ÷ 0,02 = 1.000 < 1.251; d) 6 depot mỗi nhóm tối đa 300; e) chấp nhận mức chênh 6 điểm (859 mỗi nhóm) thì mỗi người cần ít nhất 299 yêu cầu (hệ số thiết kế 6,96). Tính thêm power 0,64 nếu tác động thật chỉ 5 điểm.
- **Chọn cách chia:** theo nhân viên 20 + 20, ngẫu nhiên, phân tầng theo depot, đối chứng chạy cùng tuần. Loại chia theo yêu cầu (tràn tác động) và chia theo depot (chỉ 6 cụm, dưới 20). Ghi rõ đánh đổi: chỉ thấy được mức chênh 6 điểm và Giám đốc vận hành phải ký chấp nhận.
- **D3:** tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại là 4,25% (51/1.200), trong phạm vi `noi_dia` + `hang_nang` là 3,97%. Vì trần tuyệt đối 3% đã bị vượt từ đầu nên luật an toàn so với nhóm đối chứng (chênh từ 2 điểm) kèm trần 6%.
- **Ba luật dừng** đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ: an toàn (mở lại, hoàn trùng; Giám đốc vận hành tắt trong 30 phút), chi phí (trên 8.000 đ [simulated] hoặc làm lại trên 7% trong 2 tuần; PM trợ lý hoàn phí thu hẹp phạm vi), mức độ sử dụng (bỏ qua gợi ý trên 40% trong 1 tuần; Trưởng nhóm CSKH phỏng vấn nhân viên).
- Điền các trường `identifiability`, `interim_looks`, `rollback`, `decision_date` (2027-01-05) và `simulated_inputs` (liệt kê mọi số giả lập đã dùng).
- **Rà soát phạm vi pilot:** phát hiện `scope` ghi "6 depot đã chạy thử" mâu thuẫn với chia 20 + 20 (cần 40 nhân viên, trong khi 6 depot chạy thử chỉ có 20 nhân viên). Nhóm đã sửa thành cả 12 depot ở commit `3357dfd`.
- Điền mục 6 hồ sơ với số chính, trạng thái "Xong, có bằng chứng" (có ghi chú ngưỡng chi phí dựa trên số simulated) và người phụ trách là Giám đốc vận hành.

## 4. Bằng chứng

- Commit `1a77869` "CP4: code D1/D3, pilot_plan.yaml, muc 6 ho so" (`src/lab13.py`, `report/team/pilot_plan.yaml`, `report/team/ho_so_launch_v0.md`).
- `cd src && python lab13.py` in đúng các số D1 và D3 ở trên (1.251 · 3.103 · 1.000 · 300 · 299 · power 0,64 · 4,25% / 3,97%).
- `report/team/pilot_plan.yaml`: đọc được bằng `yaml.safe_load`, ba luật dừng đủ bốn vế, không còn dấu `?` ngoài dòng chú thích; chú thích đầu file ghi D1, D2, đánh đổi và tỉ lệ mở lại.
- Lệnh tìm từ bị cấm (quy tắc 5) trong `report/team` không in dòng nào.

## 5. Công cụ AI đã dùng

- **Claude (Claude Code, trên máy cá nhân):** đọc các tài liệu Lab 13 và giải thích khái niệm bằng ngôn ngữ thường; viết khối code D1/D3 trong `lab13.py`; soạn nội dung `pilot_plan.yaml` và mục 6 hồ sơ; rà soát hồ sơ nhóm và chỉ ra mâu thuẫn ở `scope`; soạn nháp báo cáo này. Claude không có khoá API hay dữ liệu nào ngoài repo của nhóm.
- **Cách tự kiểm tra, không tin kết quả của AI nguyên văn:**
  - Chạy `python lab13.py` và đối chiếu từng số D1 với đáp án trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch không quá 2%).
  - Đối chiếu độc lập bằng một script nháp viết riêng (không dùng chung code với `lab13.py`), cho cùng kết quả.
  - Đối chiếu câu e với cách giải đại số: 20m ≥ 859 × (0,98 + 0,02m), tức 2,82m ≥ 841,82 nên m ≥ 298,5, làm tròn thành 299.
  - Kiểm file YAML bằng `yaml.safe_load`, tìm dấu `?` và từ bị cấm bằng lệnh; kiểm từng luật dừng có đủ bốn vế.
  - Khi số lệch với bài của người khác trong nhóm (ví dụ B4: 12.414 đ hay 12.415 đ) thì dùng số do code của nhóm in ra.

## 6. Tự đánh giá

- **Làm tốt:** chọn cách chia dựa trên cỡ mẫu tính trước, nêu rõ con số bất lợi (power 0,64) và người ký chấp nhận; ngưỡng an toàn dựa trên dữ liệu chạy thử, không đặt tuỳ ý; các luật dừng có ngưỡng, thời hạn và vai trò có quyền dừng.
- **Chưa hoàn hảo, nhóm cần theo dõi:**
  - Bước rollout 0.50 bắt đầu sau 22/12 trong khi quyết định vào 05/01, cần kiểm xem mỗi nhân viên có kịp 299 yêu cầu không.
  - Ngưỡng chi phí 8.000 đ cần ghi rõ áp cho cả phạm vi pilot, vì riêng `hang_nang` trong đợt chạy thử đã tốn 8.221 đ.
  - Cột `Người phụ trách` ở một số mục hồ sơ vẫn ghi theo tên người thay vì vai trò có quyền quyết định.
- **Bài học:** cỡ mẫu không chỉ phụ thuộc số yêu cầu mà còn phụ thuộc số cụm (nhân viên); với 40 nhân viên, không cách chia nào đủ mẫu cho mức chênh 5 điểm, nên phải nói thẳng đánh đổi thay vì giấu đi.
