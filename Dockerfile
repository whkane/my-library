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

ARG JSON_FILE
ENV JSON_FILE=$JSON_FILE

# Enable venv
ENV PATH="/opt/venv/bin:$PATH"
COPY . /app/

# Commands to run My Library application
CMD ["bash", "-c", "python my_library_db.py $JSON_FILE"]
