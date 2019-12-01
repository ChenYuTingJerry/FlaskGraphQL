# Use an official Python runtime as an image
FROM python:3.7-alpine

# Copy all essentials file
COPY ./app /src/app
COPY ./uwsgi.ini /src/
COPY ./requirements.txt /src/
COPY ./requirements.txt /src/
COPY ./config/config.py /src/config/config.py
COPY entrypoint.sh /
COPY ./run.py /src/

# Set execution permission
RUN chmod +x /entrypoint.sh
RUN chmod +x /src/run.py

# Work Directory
WORKDIR /src

# Install requirements
RUN apk add --no-cache gcc libc-dev linux-headers
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir uwsgi
RUN pip install --no-cache-dir -r requirements.txt
RUN apk del gcc libc-dev linux-headers

# Start application
ENTRYPOINT ["/entrypoint.sh"]
