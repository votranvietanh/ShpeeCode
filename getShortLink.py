import re

# Văn bản chứa các link
text = """
https://shorten.asia/Q3Kx5mnN giảm 25k đơn từ 79k
https://shorten.asia/U7nksdEU giảm 15% tối đa 39k đơn từ 129k
https://s.shopee.vn/7UwDu0CVmJ
https://s.shopee.vn/7fHgDdfWnR
https://s.shopee.vn/VpKA43ZXV
"""

# Danh sách các link đã chuyển đổi theo thứ tự (nhập vào thủ công)
converted_links = [
    "https://full-link-1.com",
    "https://full-link-2.com",
    "https://full-link-3.com",
    "https://full-link-4.com",
    "https://full-link-5.com"
]

# Bước 1: Tìm các link rút gọn trong văn bản
short_links = re.findall(r'https?://\S+', text)

# Bước 2: Thay thế lần lượt từng link ngắn bằng link đã chuyển đổi theo thứ tự
for short_link, full_link in zip(short_links, converted_links):
    text = text.replace(short_link, full_link, 1)  # Thay thế chỉ một lần cho mỗi short link

# Hiển thị văn bản đã thay link
print("Văn bản sau khi thay link:")
print(text)
