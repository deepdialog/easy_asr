FROM ubuntu
LABEL maintainer="tian.r.king@gmail.com"
LABEL author="w0x7ce"
LABEL version="v0.1"
WORKDIR /code
# 
COPY ./requirements.txt /code/requirements.txt
COPY ./nltk_data /root/nltk_data
#
RUN sed -i s/archive.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list && sed -i s/security.ubuntu.com/mirrors.aliyun.com/g /etc/apt/sources.list

RUN apt-get update && apt-get install ffmpeg -y
RUN apt-get install python -y  && apt-get install python3-pip -y
RUN pip install paddlepaddle==2.2.2 -i https://mirror.baidu.com/pypi/simple && \
    pip install paddlespeech -i https://pypi.tuna.tsinghua.edu.cn/simple
RUN pip config set global.index-url http://mirrors.aliyun.com/pypi/simple
RUN pip config set install.trusted-host mirrors.aliyun.com
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
RUN pip install numpy==1.20.1
RUN pip install librosa==0.8.1 
# 
COPY ./app /code/app
COPY ./silk-v3-decoder /code/silk-v3-decoder
# 
RUN apt-get install wget -y
RUN wget -c https://paddlespeech.bj.bcebos.com/PaddleAudio/zh.wav
RUN paddlespeech asr --input ./zh.wav
RUN paddlespeech text --input 1
RUN apt-get remove wget -y
RUN apt-get autoremove -y

RUN echo "EXPOSE PORT 81 "
CMD ["uvicorn", "app.fast_test:app", "--host", "0.0.0.0", "--port", "81"]

