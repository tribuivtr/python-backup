# pip install requests

import requests

url = 'https://api.fpt.ai/hmi/tts/v5'

payload = '''
Xin chào,
Chào mừng bạn đã đến với FPT Smart CloudI!
Hãy click vào nút dưới đây trong vòng 24h để kích hoạt tài khoản và sử dụng dịch vụ của FPT Smart Cloud.

Trong trường hợp không click được vào nút, hãy nhấp vào đường link sau để kích hoạt tài khoản:

Nếu bạn gặp bất kì khó khăn nào, hãy liên hệ ngay với chúng tôi. Chúng tôi luôn sẵn sàng được hỗ trợ.

Trân trọng,
Đội ngũ FPT Smart Cloud.'''

headers = {
    'api-key': 'your-key',
    'speed': '',
    'voice': 'banmai'
}

response = requests.request('POST', url, data=payload.encode('utf-8'), headers=headers)

print(response.text)