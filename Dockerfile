ARG JSON_FILE library.json
FROM python:3.12-slim as compiler
ENV PYTHONUNBUFFERED 1

WORKDIR /app/

RUN python -m venv /opt/venv
# Enable venv
ENV PATH="/opt/venv/bin:$PATH"

FROM python:3.12-slim as runner
WORKDIR /app/
COPY --from=compiler /opt/venv /opt/venv

# Install Tkinter
RUN apt-get update -y && apt-get install tk -y
ENV DISPLAY=127.0.0.1:0.0

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/

# Commands to run My Library application
CMD ["python", "my_library_db.py", "$JSON_FILE"]
