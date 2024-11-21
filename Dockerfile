# Chọn image Python
FROM python:3.11-slim

# Cài đặt các thư viện cần thiết
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn vào container
COPY . /app/

# Mở cổng 8000 để truy cập ứng dụng
EXPOSE 8000

# Thêm lệnh sao chép script vào Dockerfile
COPY wait-for-postgres.sh /wait-for-postgres.sh
RUN chmod +x /wait-for-postgres.sh

# Chạy script đợi PostgreSQL trước khi khởi động ứng dụng FastAPI
CMD /wait-for-postgres.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000


