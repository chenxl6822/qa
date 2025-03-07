# 使用官方的 Python 3.9 镜像作为基础镜像
FROM python:3.11-slim-bullseye

# 设置工作目录
WORKDIR /app

# 将当前目录下的所有文件复制到容器的 /app 目录
COPY . /app

# 安装依赖
RUN pip install --no-cache-dir -r arequirements.txt

# 暴露 Flask 应用的端口（默认是 5000）
EXPOSE 5000

# 设置环境变量
ENV FLASK_APP=app.py
ENV FLASK_ENV=production

# 运行 Flask 应用
CMD ["flask", "run", "--host=0.0.0.0"]