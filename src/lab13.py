"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    # Lần chạy thứ i chỉ xảy ra khi i-1 lần trước đều sai: P = (1-p)^(i-1)
    # Cộng i = 1..k  →  (1 - (1-p)^k) / p ;  k → ∞  →  1/p
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    # Thất bại khi cả k lần đều sai: (1-p)^k
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    # Tử số: mọi lần chạy (kể cả lần lỗi); mẫu số: chỉ việc thành công
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict gồm: token, tool, xem_lai, lam_lai, tong, thanh_cong, cps (chi phí mỗi việc thành công).
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × LUONG_PHUT. Đây là số GIẢ LẬP, phải ghi nhãn simulated khi báo cáo.
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - Các tham số giá/hệ số/max_lan_chay dùng cho Nhiệm vụ B (độ nhạy, giới hạn số lần chạy); giữ mặc định ở A2.
    """
    reqs = reqs.copy()
    # Chỉ giữ các lần chạy thuộc tập yêu cầu đang xét (để A3 lọc theo loai là đủ)
    runs = runs[runs['request_id'].isin(reqs['request_id'])]

    # Giới hạn số lần chạy (dùng cho B1, B3): bỏ lần chạy vượt giới hạn,
    # yêu cầu cần nhiều lần hơn coi như chuyển nhân viên (không còn phút xem lại/làm lại)
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0

    # TỬ SỐ: cộng trên MỌI lần chạy, kể cả lần lỗi (lần lỗi vẫn bị tính tiền)
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai   # simulated
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai   # simulated
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai

    # MẪU SỐ: chỉ đếm yêu cầu thành công
    thanh_cong = int((reqs['ket_qua'] == 'thanh_cong').sum())

    return dict(
        token=tien_token.sum(),
        tool=tien_tool.sum(),
        chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),  # phần của lần chạy thứ 2, 3
        xem_lai=xem_lai,
        lam_lai=lam_lai,
        tong=tong,
        thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else float('nan'),
        hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs),
    )


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    print('\n=== A2 · Mô hình chi phí (xem_lai, lam_lai, tong, cps là simulated) ===')
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:15s} {gia_tri:>14,.1f}')
    print(f"cps / hoá đơn mỗi yêu cầu = {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f}×")
    for khoan in ['token', 'tool', 'xem_lai', 'lam_lai']:
        print(f"Tỉ trọng {khoan:8s} {ket_qua[khoan] / ket_qua['tong']:6.1%}")
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    print('\n=== A3 · Theo loại yêu cầu (cps là simulated) ===')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_TC':>9s} {'chay/yc':>8s} {'cps':>9s} {'so_12k':>7s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        reqs_loai = reqs[reqs['loai'] == loai]
        kq = mo_hinh(runs, reqs_loai)
        so_yc = len(reqs_loai)
        so_lan_chay = runs['request_id'].isin(reqs_loai['request_id']).sum()
        print(f"{loai:10s} {so_yc:6d} {kq['thanh_cong'] / so_yc:9.1%} {so_lan_chay / so_yc:8.2f} "
              f"{kq['cps']:9,.0f} {kq['cps'] / BASELINE:6.2f}×")

    # Tỉ lệ lần chạy 'ok' theo từng lần thử: chạy lại có giúp không?
    runs_loai = runs.merge(reqs[['request_id', 'loai']], on='request_id')
    runs_loai['ok'] = (runs_loai['status'] == 'ok').astype(float)
    print('\nTỉ lệ ok theo lần thử (attempt):')
    print(runs_loai.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='mean')
          .map(lambda x: f'{x:.1%}'))
    print('Số lần chạy theo lần thử:')
    print(runs_loai.pivot_table(index='loai', columns='attempt', values='ok', aggfunc='count'))

    # ---------- Nhiệm vụ A4 · Chi phí cố định (phạm vi noi_dia + hang_nang) ----------
    CO_DINH_THANG = 40_000_000   # đồng / tháng
    YC_THANG = 45_000            # yêu cầu / tháng ở quy mô đầy đủ
    reqs_pham_vi = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    kq_pv = mo_hinh(runs, reqs_pham_vi)
    print('\n=== A4 · Chi phí cố định, phạm vi noi_dia + hang_nang (simulated) ===')
    print(f"Phạm vi: tong {kq_pv['tong']:,.0f} đ / {kq_pv['thanh_cong']} việc TC "
          f"→ cps {kq_pv['cps']:,.0f} đ ({kq_pv['cps'] / BASELINE:.2f}×)")
    for ten_kl, yc_thang in [('45.000 yc/tháng', YC_THANG), ('Một nửa (22.500)', YC_THANG / 2)]:
        # Quy ra quy mô tháng theo tỉ lệ: việc TC trong phạm vi / 1.200 yêu cầu của mẫu
        tc_thang = yc_thang * kq_pv['thanh_cong'] / len(reqs)
        co_dinh_moi_viec = CO_DINH_THANG / tc_thang
        tong_moi_viec = kq_pv['cps'] + co_dinh_moi_viec
        print(f"{ten_kl:18s} TC/tháng {tc_thang:>8,.0f}  cố định/việc {co_dinh_moi_viec:>6,.0f} đ  "
              f"cps + cố định {tong_moi_viec:>6,.0f} đ  = {tong_moi_viec / BASELINE:.2f}×")
    # ---------- Nhiệm vụ B · Bảng độ nhạy (CP2) — toàn bộ cps là simulated ----------
    goc = mo_hinh(runs, reqs)['cps']

    # B1 · Đổi từng yếu tố: mỗi kịch bản là một lần gọi mo_hinh với một tham số đã đổi
    kich_ban = {
        'Giá token gấp đôi':      dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa': dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':        dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':   dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':        dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':   dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':         dict(luong_phut=2500),
        'Tối đa 2 lần chạy':      dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':         dict(max_lan_chay=1),
    }
    print(f'\n=== B1 · Đổi từng yếu tố (gốc {goc:,.0f} đ, simulated) ===')
    thay_doi = {}
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = (cps / goc - 1) * 100
        print(f'{ten:25s} {cps:8,.0f} đ  {thay_doi[ten]:+6.1f}%')
    # Tự kiểm: "giảm một nửa" = nửa mức tăng của "gấp đôi" (mô hình tuyến tính)
    for yeu_to in ['Giá token', 'Xem lại', 'Làm lại']:
        tang, giam = thay_doi[f'{yeu_to} gấp đôi'], thay_doi[f'{yeu_to} giảm một nửa']
        assert abs(tang / 2 + giam) < 1e-9, f'{yeu_to}: giảm nửa phải bằng nửa mức tăng gấp đôi'
    print('Tự kiểm "giảm một nửa = nửa mức tăng gấp đôi": ĐẠT')

    # B2 · Đổi một cặp: giá token gấp đôi + xem lại gấp đôi
    cps_cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'\n=== B2 · Token ×2 + xem lại ×2: {cps_cap:,.0f} đ ({(cps_cap / goc - 1) * 100:+.1f}%), '
          f'tổng hai tác động riêng {tong_rieng:+.1f}% ===')
    xep_hang = sorted([(abs(thay_doi['Làm lại gấp đôi']), 'Số ca làm lại'),
                       (abs(thay_doi['Xem lại gấp đôi']), 'Tỉ lệ xem lại'),
                       (abs(thay_doi['Lương tăng 25%']), 'Lương nhân viên (+25%)'),
                       (abs(thay_doi['Giá token gấp đôi']), 'Giá token'),
                       (abs(thay_doi['Chỉ 1 lần chạy']), 'Giới hạn số lần chạy')], reverse=True)
    print('Xếp hạng:', ' · '.join(f'{i}. {ten} ({muc:.1f}%)' for i, (muc, ten) in enumerate(xep_hang, 1)))

    # B3 · Giới hạn chạy lại: chi phí cả hệ thống = tổng trợ lý + 12.000 đ × số yêu cầu không thành công
    print('\n=== B3 · Giới hạn số lần chạy (simulated) ===')
    print(f"{'giới hạn':>8s} {'tổng trợ lý':>12s} {'không TC':>9s} {'cả hệ thống':>12s} {'cps':>7s}")
    for gioi_han in [1, 2, 3]:
        kq = mo_hinh(runs, reqs, max_lan_chay=gioi_han)
        khong_tc = len(reqs) - kq['thanh_cong']
        he_thong = kq['tong'] + BASELINE * khong_tc
        print(f"{gioi_han:8d} {kq['tong']:12,.0f} {khong_tc:9d} {he_thong:12,.0f} {kq['cps']:7,.0f}")

    # B4 · Xem lại 100% cho noi_dia + hang_nang: 5 phút mỗi yêu cầu có lần chạy ok, 9 phút mỗi ca lam_lai
    reqs_pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(reqs_pv['request_id'])]
    so_yc_ok = runs_pv.loc[runs_pv['status'] == 'ok', 'request_id'].nunique()
    so_lam_lai = int((reqs_pv['ket_qua'] == 'lam_lai').sum())
    token_tool_pv = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
                     + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = int((reqs_pv['ket_qua'] == 'thanh_cong').sum())
    tien_xem_lai_100 = so_yc_ok * 5 * LUONG_PHUT
    phut_lam_lai = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated']
    print(f'\n=== B4 · Xem lại 100% noi_dia + hang_nang ({len(reqs_pv)} yêu cầu, simulated) ===')
    print(f'Yêu cầu có lần chạy ok: {so_yc_ok} → xem lại {tien_xem_lai_100:,.0f} đ; '
          f'ca lam_lai: {so_lam_lai}; token + tool: {token_tool_pv:,.0f} đ; việc TC: {tc_pv}')
    print(f'Phút làm lại/ca trong dữ liệu: trung bình {phut_lam_lai.mean():.1f}, trung vị {phut_lam_lai.median():.1f}')
    for ten, phut in [('9 phút/ca (theo đề)', 9), (f'{phut_lam_lai.mean():.1f} phút/ca (dữ liệu)', phut_lam_lai.mean())]:
        tien_lam_lai = so_lam_lai * phut * LUONG_PHUT
        tong_b4 = tien_xem_lai_100 + tien_lam_lai + token_tool_pv
        hoa_von = (BASELINE * tc_pv - tien_lam_lai - token_tool_pv) / (so_yc_ok * LUONG_PHUT)
        print(f'{ten:26s} tổng {tong_b4:12,.0f} đ → cps {tong_b4 / tc_pv:7,.0f} đ = {tong_b4 / tc_pv / BASELINE:.2f}×; '
              f'hoà vốn khi xem lại ≤ {hoa_von:.1f} phút')
    # ---------- Nhiệm vụ D · Cỡ mẫu và kế hoạch pilot (CP4) ----------
    from statistics import NormalDist
    ICC, BASE = 0.02, 0.70

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    def he_so_thiet_ke(m):
        return 1 + (m - 1) * ICC

    n5, n6 = co_mau(BASE, 0.75), co_mau(BASE, 0.76)
    print('=== D1 · Cỡ mẫu (baseline 0,70; alpha 0,05; power 0,8; ICC 0,02) ===')
    print(f'a) Chia theo yêu cầu: {n5} yêu cầu mỗi nhóm')
    de75 = he_so_thiet_ke(75)
    n_b = math.ceil(n5 * de75)
    nv_b = math.ceil(n_b / 75)
    print(f'b) Theo nhân viên, m = 75: DE = {de75:.2f}, {n_b} yêu cầu mỗi nhóm, {nv_b} nhân viên mỗi nhóm, '
          f'tổng {2 * nv_b} > 40 → không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: cỡ mẫu hiệu dụng tối đa 20 / ICC = {20 / ICC:,.0f} < {n5} → không đạt 5 điểm')
    print(f'd) 6 depot mỗi nhóm: tối đa 6 / ICC = {6 / ICC:,.0f}')
    m_e = next(m for m in range(1, 10_000) if 20 * m / he_so_thiet_ke(m) >= n6)
    print(f'e) Mức chênh 6 điểm ({n6} mỗi nhóm), 20 nhân viên mỗi nhóm: m ≥ {m_e} yêu cầu mỗi người '
          f'(DE {he_so_thiet_ke(m_e):.2f}; hiệu dụng {20 * m_e / he_so_thiet_ke(m_e):,.0f})')
    try:
        from statsmodels.stats.power import NormalIndPower
        from statsmodels.stats.proportion import proportion_effectsize
        pw = NormalIndPower().power(proportion_effectsize(0.75, BASE), nobs1=n6, alpha=0.05)
        print(f'   Power nếu tác động thật chỉ 5 điểm với {n6}/nhóm: {pw:.2f}')
    except ImportError:
        print('   (cài statsmodels để tính power)')

    # D3 · Tỉ lệ mở lại hiện tại, trước khi đặt luật an toàn
    print('=== D3 · mo_lai_trong_7_ngay hiện tại (đợt chạy thử) ===')
    print(f"Toàn mẫu: {reqs['mo_lai_trong_7_ngay'].mean():.2%} ({int(reqs['mo_lai_trong_7_ngay'].sum())}/{len(reqs)}); "
          f"noi_dia + hang_nang: {reqs_pham_vi['mo_lai_trong_7_ngay'].mean():.2%}")
    print(f"Tỉ lệ làm lại trong phạm vi: {(reqs_pham_vi['ket_qua'] == 'lam_lai').mean():.1%}")
    print(f'Nếu đặt trần tuyệt đối 3% thì đã vượt ({reqs["mo_lai_trong_7_ngay"].mean():.2%}) → pilot dừng ngay tuần đầu')

    # ---------- Nhiệm vụ E1 · Đặc tả chỉ số, tính thử trên 1.200 yêu cầu (CP5) ----------
    # Không có nhóm đối chứng: chỉ viết "chỉ số trong đợt chạy thử là ...", không viết "trợ lý đã nâng chỉ số".
    chinh = (reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo'])
    an_toan = reqs['mo_lai_trong_7_ngay'] == 1
    print('\n=== E1 · Ba chỉ số trong đợt chạy thử (1.200 yêu cầu) ===')
    print(f"Chính   · đóng 24h, không mở lại 7 ngày: {chinh.mean():.2%} ({chinh.sum()}/{len(reqs)})")
    print(f"Dùng    · bỏ qua gợi ý (sua + bo) / được xem lại: {bo_qua.mean():.2%} ({bo_qua.sum()}/{len(xem)})")
    print(f"An toàn · mở lại trong 7 ngày: {an_toan.mean():.2%} ({an_toan.sum()}/{len(reqs)})")
    print('Phân bố quyết định xem lại:', xem['quyet_dinh_xem_lai'].value_counts().to_dict())
    print('Chỉ số chính theo loại:', reqs.assign(c=chinh).groupby('loai')['c'].mean().map(lambda x: f'{x:.1%}').to_dict())
