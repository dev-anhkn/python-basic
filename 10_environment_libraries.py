
# Môi trường & Thư viện ngoài
guide = r"""
Hướng dẫn nhanh (Windows/Linux/macOS):
1) Tạo môi trường ảo venv:
   Windows: py -m venv .venv && .venv\Scripts\activate
   macOS/Linux: python3 -m venv .venv && source .venv/bin/activate
2) Cài thư viện:
   pip install requests
3) Lưu phiên bản:
   pip freeze > requirements.txt
4) Cài lại từ requirements:
   pip install -r requirements.txt
"""
print(guide)
