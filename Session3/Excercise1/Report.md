
Các lỗi sai nghiệp vụ
1. Lỗi về môi trường hệ thống
Nhận định sai: Thông tư quản lý thuốc gây nghiện của Bộ Y tế là Môi trường Nội bộ của RikkeiCare.

Nguyên nhân sai: Thông tư của Bộ Y tế là quy định pháp luật bên ngoài mà RikkeiCare không thể trực tiếp kiểm soát hoặc thay đổi.

Hậu quả: Nếu xác định sai, hệ thống có thể không tuân thủ đúng quy định pháp luật, dẫn đến sai nghiệp vụ và có nguy cơ bị xử phạt.

2. Lỗi về quy trình

Nhận định sai: Kho dược vận hành hoàn hảo vì Dược sĩ luôn nhớ chính xác hạn dùng của từng lô thuốc.

Nguyên nhân sai: Nhận định này bỏ qua thực tế đã xảy ra trường hợp bệnh nhân khiếu nại do nhận thuốc quá hạn.

Hậu quả: Nếu không ghi nhận rủi ro thực tế, hệ thống có thể thiếu cơ chế kiểm soát hạn dùng và tiếp tục xảy ra tình trạng xuất nhầm thuốc quá hạn.

3. Lỗi phân loại yêu cầu

Nhận định sai: Hệ thống phải có chức năng tự động khóa các lô thuốc hết hạn sử dụng là Yêu cầu Phi chức năng.

Nguyên nhân sai: Tự động khóa các lô thuốc hết hạn là một hành động mà hệ thống bắt buộc phải thực hiện nên thuộc Yêu cầu Chức năng (FR).

Hậu quả: Nếu phân loại sai thành NFR, đội phát triển có thể bỏ sót chức năng quan trọng, làm tăng nguy cơ xuất thuốc hết hạn cho bệnh nhân.
- Phân loại môi trường và tác động

1. Kỹ năng vi tính và thói quen ghi sổ của Dược sĩ thuộc Môi trường Nội bộ.

Tác động: Hệ thống cần có giao diện đơn giản, dễ sử dụng và hỗ trợ quét mã vạch để giảm thao tác thủ công.

2. Thông tư và chế tài xử phạt của Bộ Y tế thuộc Môi trường Bên ngoài.

Tác động: Hệ thống phải tuân thủ quy định pháp luật, tự động khóa thuốc hết hạn và lưu audit log để truy vết thao tác.

3. Hạ tầng máy chủ và mạng LAN nội bộ bệnh viện thuộc Môi trường Nội bộ.

Tác động: Hệ thống phải hoạt động ổn định trên hạ tầng mạng nội bộ. Đối với các lô thuốc thuộc nhóm RESTRICTED như thuốc hướng thần, thuốc gây nghiện, hệ thống phải yêu cầu xác nhận kép (Dual-Authorization) từ Dược sĩ Trưởng khoa Dược trước khi hoàn tất xuất kho.

- Yêu cầu chức năng và phi chức năng

1. Yêu cầu chức năng 

FR-01: Hệ thống phải tự động khóa các lô thuốc đã hết hạn sử dụng và không cho phép xuất kho các lô thuốc này.

Đối với thuốc thuộc nhóm RESTRICTED, hệ thống phải yêu cầu xác nhận kép từ Dược sĩ Trưởng khoa Dược trước khi hoàn tất giao dịch xuất kho.

2. Yêu cầu phi chức năng

NFR-01: Hệ thống phải đảm bảo tính bảo mật và khả năng truy vết, mọi thao tác nhập, xuất, khóa thuốc và xác nhận giao dịch phải được lưu đầy đủ vào audit log, bao gồm người thực hiện và thời gian thực hiện.

Kết luận

Tài liệu khảo sát ban đầu có 3 lỗi chính cần hiệu chỉnh.

Thứ nhất, Thông tư của Bộ Y tế là yếu tố thuộc Môi trường Bên ngoài.

Thứ hai, không được đánh giá quy trình kho dược là hoàn hảo khi thực tế đã xảy ra khiếu nại về thuốc quá hạn.

Thứ ba, chức năng tự động khóa thuốc hết hạn là Yêu cầu Chức năng (FR), không phải Yêu cầu Phi chức năng.

Ngoài ra, các thuốc RESTRICTED phải được kiểm soát bằng cơ chế xác nhận kép để không cho phép một nhân viên tự ý hoàn tất xuất kho.
