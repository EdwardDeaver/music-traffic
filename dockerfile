FROM python:3.10-bookworm
EXPOSE 8080
EXPOSE 80
EXPOSE 443
RUN pip install poetry
ENV POETRY_REQUESTS_TIMEOUT=120
COPY . .
RUN apt update && apt install -y libsm6 libxext6 ffmpeg libfontconfig1 libxrender1 libgl1-mesa-glx
RUN poetry install
ENTRYPOINT ["poetry", "run", "python", "-m", "constantUser"]