FROM nginx
# need to install openssl
RUN set -eux; \
    apt-get update; \
    apt-get install -y \
        openssl \
    ; \
    rm -rf /var/lib/apt/lists/*
# then build self-signed cert
RUN openssl req -x509 -nodes -days 999 -newkey rsa:2048 -keyout /etc/ssl/private/nginx-selfsigned.key -out /etc/ssl/certs/nginx-selfsigned.crt -subj "/C=US/ST=Georgia/L=Atlanta/O=IT/CN=sprinkler.serenity.now"
COPY docker/ssl-params.conf /etc/nginx/ssl-params.conf
COPY docker/nginx.conf /etc/nginx/nginx.conf
COPY static_root /static/

