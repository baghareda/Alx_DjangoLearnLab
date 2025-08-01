# HTTPS Deployment Configuration

To support HTTPS in production, configure your web server (e.g., Nginx or Apache) as follows:

1. Obtain an SSL/TLS certificate (e.g., via Let's Encrypt).
2. Configure Nginx:

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    return 301 https://$host$request_uri;
}

server {
    listen 443 ssl;
    server_name yourdomain.com;

    ssl_certificate /etc/letsencrypt/live/yourdomain.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/yourdomain.com/privkey.pem;

    location / {
        proxy_pass http://localhost:8000;
        include proxy_params;
    }
}
