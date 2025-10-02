# 官方 Python 較小體積image
FROM python:3.10-slim

# 設定工作目錄
WORKDIR /app

# 安裝套件
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# 複製 frontend 內容到 /app
COPY frontend/ /app

# 啟動主程式 app.py
CMD ["python", "app.py"]

EXPOSE 5000

