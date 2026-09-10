def classify_logistics_feature(feature_name):
    feature = feature_name.lower()

    if any(keyword in feature for keyword in [
        "đã lấy hàng",
        "quét mã vạch",
        "nhập kho",
        "in phiếu cước"
    ]):
        return "TPS"

    if any(keyword in feature for keyword in [
        "báo cáo doanh thu",
        "báo cáo tổng hợp",
        "báo cáo thống kê",
        "báo cáo số lượng"
    ]):
        return "MIS"

    if any(keyword in feature for keyword in [
        "dự báo",
        "phân tích dự báo",
        "điểm nóng quá tải"
    ]):
        return "DSS"

    return "Không xác định"


features = [
    "Tài xế bấm nút Đã lấy hàng trên App Mobile",
    "Nhân viên kho quét mã vạch nhập kho",
    "In phiếu cước giao hàng cho khách tại bưu cục",
    "Báo cáo tổng hợp doanh thu tháng cho Trưởng bưu cục",
    "Báo cáo thống kê số lượng đơn giao tuần trước",
    "Công cụ phân tích dự báo điểm nóng quá tải đơn hàng mùa Tết"
]

for feature in features:
    print(feature, "->", classify_logistics_feature(feature))
