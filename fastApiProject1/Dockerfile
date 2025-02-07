# 基础镜像
FROM python:3.11-slim-bullseye

# 设置工作目录
WORKDIR /app

ARG PROXY="https://mirrors.cloud.tencent.com/pypi/simple"

# 安装依赖，仅在 requirements 文件发生变化时重新安装
COPY ./requirements.txt ./

RUN pip install -r requirements.txt --no-cache -i $PROXY

COPY app.py ./

# 暴露端口
EXPOSE 8000

# 入口命令
ENTRYPOINT ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
