FROM python:3.8


RUN pip3.8 install Flask

COPY . /mock

WORKDIR /mock

CMD ["python3.8", "vk_mock.py"]