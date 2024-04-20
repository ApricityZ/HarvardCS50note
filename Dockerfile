# 使用官方 Anaconda 镜像作为基础镜像
FROM continuumio/anaconda3

# 设置工作目录
WORKDIR /app

# 复制当前目录下的 requirements.txt 文件到容器中的 /app 目录
COPY requirements.txt /app/

# 安装 Python 依赖
RUN conda install --yes --file requirements.txt

# 将当前目录下的所有文件复制到容器中的 /app 目录
COPY . /app

# 定义容器启动时执行的命令
CMD ["python", "app.py"]


