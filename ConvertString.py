import re
import requests

# Văn bản chứa các link
text = """
https://shorten.asia/Q3Kx5mnN giảm 25k đơn từ 79k
https://shorten.asia/U7nksdEU giảm 15% tối đa 39k đơn từ 129k
https://shorten.asia/35ycpbFy giảm 20% tối đa 49k đơn từ 179k
https://shorten.asia/6fZQzU82 giảm 25% tối đa 79k đơn từ 299k
https://shorten.asia/JQFBnJHx giảm 20k đơn từ 50k
https://shorten.asia/35ycpbFyY giảm 25% tối đa 33k đơn từ 99k
https://shorten.asia/9Buu4kur giảm 25% tối đa 30k đơn từ 99k
https://shorten.asia/4979cJdU giảm 25% tối đa 99k đơn từ 259k
https://shorten.asia/Z2edV51W giảm 25% tối đa 50k đơn từ 150k
https://shorten.asia/HquFXvDX giảm 50% tối đa 25k đơn từ 50k
https://shorten.asia/PMMUQQU1 giảm 30k đơn từ 99k
https://shorten.asia/aGaMrGQv giảm 18% tối đa 99k đơn từ 299k
https://shorten.asia/bFrF9kjy giảm 15% tối đa 119k đơn từ 399k
https://shorten.asia/pz4w6nvS giảm 20k đơn từ 50k
https://shorten.asia/u8DQXDja giảm 20% tối đa 99k đơn từ 250k
https://shorten.asia/pmMA3tzt giảm 20% tối đa 50k đơn từ 159k
https://shorten.asia/gkNpEeDQ giảm 25% tối đa 50k đơn từ 150k
https://shorten.asia/zMghqvMT giảm 20% tối đa 50k đơn từ 200k
https://shorten.asia/ZBtt5rzy giảm 30k đơn từ 99k
https://shorten.asia/wfuTnnRN giảm 20% tối đa 70k đơn từ 299k
https://shorten.asia/HCVD2mGU 14% max 300k đơn 999K
https://shorten.asia/nVhKC7f5 giảm 14% max 111k đơn 599K
https://shorten.asia/yGqxMCH5 giảm 15% tối đa 100k đơn từ 500k
mã toàn sàn, đơn lớn hơn 1 xíu thì dùng mã này
Sale ngày 11/11 có khác toàn số 1 các bác ạ . List mã cực thơm cho các bác săn 0h 

Giảm 100% đơn 1tr1 ( shopmall)
Vào ví : https://s.shopee.vn/7UwDu0CVmJ
Nhập Code :
BMO1111H1

2, Mã Giảm 1tr1/3tr ( thanh toán bằng app pay)
Vào ví : https://s.shopee.vn/7UwDu0CVmJ
Nhập Code :
SPP0HGIAM1TR100

3, Mã 50% Giảm 1111k ( Lưu và dùng luôn 0h)
Banner :
https://s.shopee.vn/7fHgDdfWnR

4, Mã 15% 1tr ( áp sp xtra và mã dễ nhất)
Banner :
https://s.shopee.vn/VpKA43ZXV

Nếu thêm mã nào em sẽ bổ sung tiếp , 3 mã đầu cực khó mã cuối dễ hơn nhé các bác . Chúc các bác săn sale vui vẻ 😁😁
https://shorten.asia/HCVD2mGU 14% max 300k đơn 999K
https://shorten.asia/nVhKC7f5 giảm 14% max 111k đơn 599K
https://shorten.asia/yGqxMCH5 giảm 15% tối đa 100k đơn từ 500k
mã toàn sàn, đơn lớn hơn 1 xíu thì dùng mã này
"""

# Sử dụng biểu thức chính quy để tìm các link ngắn
short_links = re.findall(r'https?://\S+', text)

# Hàm mở rộng short link
def expand_short_link(short_link):
    try:
        response = requests.get(short_link, allow_redirects=True)
        return response.url  # Link đầy đủ sau khi chuyển hướng
    except requests.exceptions.RequestException as e:
        print(f"Không thể mở link {short_link}: {e}")
        return short_link  # Trả lại link gốc nếu không thể mở rộng

# Mở rộng từng link và lưu vào mảng
full_links = [expand_short_link(link) for link in short_links]

# Hiển thị mảng chứa các link đầy đủ
print(full_links)
