Báo cáo phân tích

#Phần 1. Thanh lọc danh sách Stakeholder

1. Bác sĩ điều trị trực tiếp: Là Stakeholder vì bác sĩ trực tiếp sử dụng hệ thống EHR để xem và cập nhật hồ sơ bệnh nhân.

2. Máy chủ cơ sở dữ liệu Oracle: Không phải Stakeholder vì đây là thiết bị kỹ thuật của hệ thống.

3. Ban Giám đốc Bệnh viện RikkeiCare:Là Stakeholder vì có quyền quyết định và quản lý dự án.

4. Bệnh nhân và Thân nhân người bệnh: Là Stakeholder vì họ chịu ảnh hưởng trực tiếp từ việc quản lý hồ sơ sức khỏe.

5. Thanh tra Pháp chế & Bảo mật Y tế (Bộ Y tế): Là Stakeholder vì có nhiệm vụ kiểm tra việc tuân thủ pháp luật và bảo mật thông tin y tế.

Phần 2. Ma trận Stakeholder

1. Quản lý chặt chẽ (Manage Closely)

Stakeholder: Ban Giám đốc Bệnh viện RikkeiCare.

Hành động: Báo cáo tiến độ và xin ý kiến trong các quyết định quan trọng.

2. Giữ hài lòng (Keep Satisfied)

Stakeholder: Thanh tra Pháp chế & Bảo mật Y tế (Bộ Y tế).

Hành động: Đảm bảo hệ thống tuân thủ đúng quy định và cung cấp thông tin khi được yêu cầu.

3. Giữ thông tin

Stakeholder: Bác sĩ điều trị trực tiếp.

Hành động: Thường xuyên thông báo và lấy ý kiến của bác sĩ về hệ thống EHR.

4. Giám sát tối thiểu 

Stakeholder: Bệnh nhân và Thân nhân người bệnh.

Hành động: Thông báo những thông tin cần thiết qua ứng dụng hoặc email.

Phần 3. Giải quyết xung đột

Giải pháp là bình thường phải có Consent bằng mã xác nhận của bệnh nhân khi xem thông tin nhạy cảm. Tuy nhiên, nếu bệnh nhân hôn mê hoặc bất tỉnh và không thể xác nhận thì bác sĩ được sử dụng Emergency Override để xem thông tin cần thiết cho việc cấp cứu. Mọi lần sử dụng Emergency Override phải được ghi lại trong nhật ký hệ thống (audit log) để kiểm tra sau này.

Kết luận

Trong danh sách ban đầu, Máy chủ cơ sở dữ liệu Oracle là thực thể kỹ thuật và cần loại bỏ khỏi Stakeholder.

Các Stakeholder còn lại được phân loại dựa trên quyền lực và mức độ quan tâm.

Khi xảy ra xung đột giữa bác sĩ và pháp chế, hệ thống cần vừa đảm bảo bảo mật thông tin, vừa cho phép Emergency Override trong trường hợp cấp cứu để không ảnh hưởng đến việc điều trị bệnh nhân.
