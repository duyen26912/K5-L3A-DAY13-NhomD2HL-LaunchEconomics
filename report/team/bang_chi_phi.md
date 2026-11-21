# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 (tính tay: (1 − 0,2²) / 0,8 = 0,96 / 0,8) |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 (tính tay: 1 / 0,8) |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 (tính tay: [(1 − 0,2³) / 0,8] / (1 − 0,2³) = 1,24 / 0,992 = 1/p) |

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585 | | simulated (gồm xem lại, làm lại) |
| Số việc thành công | 978 | `ket_qua` | |
| Chi phí mỗi việc thành công | 4.472 | | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | | đo từ trace |

Tự kiểm tay: `run_00001` = 4.759/1.000 × 26 + 492/1.000 × 130 + 5 × 15 = 123,7 + 64,0 + 75 = 262,7 đ; tool = 5.600 lần × 15 = 84.000 đ; xem lại = 890 phút × 2.000, làm lại = 1.132 phút × 2.000 [simulated].

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? 4.472 / 274,7 = **16,3 lần** [simulated]: tử số tính mọi lần chạy kể cả lần lỗi (93.804 đ là của lần chạy thứ 2, 3) cộng giờ nhân viên, mẫu số chỉ là 978 việc thành công thay vì 1.200 yêu cầu.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại, 51,8%** [simulated], tiếp theo là xem lại 40,7% [simulated]; giờ nhân viên chiếm 92,5%, token + tool chỉ 7,5%.
- Lưu ý khi so với 12.000 đ: 4.472 đ chưa tính 222 yêu cầu không thành công do nhân viên làm thay; chi phí cả hệ thống = (4.373.585 + 222 × 12.000) / 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 [simulated] | 0,85× |

Tỉ lệ lần chạy `ok` theo lần thử (đo từ trace): noi_dia 91,0% → 75,7% → 38,9%; hang_nang 70,9% → 39,1% → 17,9%; doi_tac 51,5% → 18,2% → 14,8%; quoc_te 30,0% → 11,4% → 2,2%.

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **quoc_te** không đáng: chi phí mỗi việc thành công 22.515 đ = 1,88× nhân viên tự làm [simulated], chỉ 27,3% thành công. Chạy lại không giúp: lần 2 chỉ đúng 11,4%, lần 3 còn 2,2% (lỗi lặp lại trên cùng yêu cầu), trong khi quoc_te tiêu 2,32 lần chạy/yêu cầu. doi_tac sát ngưỡng (0,85×, thành công 54,4%) và có điều khoản riêng nên cũng loại khỏi phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng (22.500 yêu cầu/tháng) | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

Tự kiểm tay: phạm vi `noi_dia` + `hang_nang` có 900/1.200 việc thành công (CPS 3.072.513 / 900 = 3.414 đ [simulated]); 45.000 × 900 / 1.200 = 33.750 việc/tháng; 40.000.000 / 33.750 = 1.185 đ/việc.

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? **Không đổi kết luận** ở quy mô đầy đủ (4.599 đ = 0,38×) lẫn khi giảm một nửa khối lượng (5.784 đ = 0,48×) [simulated]. Chi phí cố định chỉ đội lên và làm đổi kết luận khi khối lượng rất nhỏ (dưới ~6.212 yêu cầu/tháng, tức ~4.659 việc thành công/tháng, là ngưỡng hoà vốn 12.000 đ). Hồ sơ cần nêu rõ đã cộng chi phí cố định hay chưa và tính ở khối lượng nào.

## B1 · Đổi từng yếu tố

Gốc (A2): 4.472 đ [simulated]. Mọi chi phí mỗi việc thành công dưới đây đều là **simulated** (gồm tiền xem lại, làm lại).

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Tự kiểm: mỗi kịch bản "giảm một nửa" giảm đúng bằng nửa mức tăng của "gấp đôi" (5,6 → 2,8; 40,7 → 20,3; 51,8 → 25,9), vì mô hình cộng tuyến tính; `lab13.py` kiểm bằng `assert` và in ĐẠT.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng 5,6% + 40,7% = 46,3% vì mô hình cộng tuyến tính.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **Số ca làm lại** (+51,8%) · 2. **Tỉ lệ xem lại** (+40,7%) · 3. **Lương nhân viên** (+23,1% khi tăng 25%) [simulated]. Giá token gấp đôi chỉ +5,6%: pilot phải theo dõi tỉ lệ làm lại và xem lại, không phải giá token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công (nhân viên làm thay). Tất cả là simulated.

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ (rẻ nhất)** | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ)** [simulated], **không trùng** với giới hạn 1 lần (chi phí mỗi việc thành công thấp nhất 4.111 đ). Tối ưu riêng chỉ số này sẽ đẩy thêm 319 − 234 = 85 yêu cầu sang nhân viên, làm cả hệ thống đắt thêm 548.561 đ.

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang` (982 yêu cầu): 948 yêu cầu có lần chạy ok × 5 phút × 2.000 = 9.480.000 đ; 48 ca lam_lai × 9 phút × 2.000 = 864.000 đ; token + tool 224.513 đ; tổng 10.568.513 đ ÷ 900 việc thành công.

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** [simulated] với 9 phút/ca làm lại theo đề. Nếu dùng phút làm lại trung bình trong dữ liệu (15,3 phút/ca, trung vị 14,5): **12.415 đ = 1,03×** [simulated], tức đắt hơn nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% thì trợ lý gần như không tiết kiệm (tiền xem lại chiếm 90% chi phí). Pilot phải đo được tỉ lệ xem lại có thể giảm an toàn tới đâu và mỗi lần xem lại có dưới mức hoà vốn **5,1 phút** (làm lại 9 phút) hoặc **4,8 phút** (làm lại 15,3 phút) không [simulated].
