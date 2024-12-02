# # Chọn image Python
# FROM python:3.11-slim

# # Cài đặt các thư viện cần thiết
# WORKDIR /app
# COPY requirements.txt /app/
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy mã nguồn vào container
# COPY . /app/

# # Mở cổng 8000 để truy cập ứng dụng
# EXPOSE 8000

# # Thêm lệnh sao chép script vào Dockerfile
# COPY wait-for-postgres.sh /wait-for-postgres.sh
# RUN chmod +x /wait-for-postgres.sh

# # Chạy script đợi PostgreSQL trước khi khởi động ứng dụng FastAPI
# CMD /wait-for-postgres.sh && uvicorn app.main:app --host 0.0.0.0 --port 8000
# Chọn image Python
# FROM python:3.11-slim

# # Cài đặt các thư viện hệ thống cần thiết (nếu có)
# RUN apt-get update \
#     && apt-get install -y gcc libpq-dev \
#     && apt-get clean

# # Đặt thư mục làm việc trong container
# WORKDIR /app

# # Copy các file yêu cầu vào container
# COPY requirements.txt .

# # Cài đặt các thư viện Python
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy toàn bộ mã nguồn vào container
# COPY . .

# # Cài đặt môi trường để chạy ứng dụng
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# Sử dụng image Python chính thức làm base image
FROM python:3.11-slim

# Đặt thư mục làm việc trong container
WORKDIR /app

# Cài đặt các dependencies hệ thống (nếu cần thiết)
RUN apt-get update && apt-get install -y gcc libpq-dev

# Cài đặt các phụ thuộc Python từ requirements.txt
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy tất cả các file trong project vào container
COPY . /app/

# Expose cổng mà FastAPI sẽ chạy
EXPOSE 8000

# Lệnh chạy ứng dụng FastAPI khi container khởi động
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]