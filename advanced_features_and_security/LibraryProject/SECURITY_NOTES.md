# SECURITY: X_FRAME_OPTIONS set to 'DENY' to block clickjacking
# SECURITY: CSRF_COOKIE_SECURE and SESSION_COOKIE_SECURE enforce HTTPS-only cookies
# SECURITY: ORM used for all queries to avoid SQL injection
# SECURITY: {% csrf_token %} added to all forms

## HTTPS & Redirects
- Enforced via `SECURE_SSL_REDIRECT = True`
- HSTS headers set for 1 year, with preload and subdomains

## Secure Cookies
- Session and CSRF cookies are sent only via HTTPS

## HTTP Security Headers
- X-Frame-Options set to DENY (Clickjacking protection)
- Content type sniffing disabled
- Browser XSS filter enabled

## Deployment
- Instructions provided for configuring Nginx with SSL/TLS

## Improvements
- Add CSP (Content Security Policy) for stricter XSS protection
- Use third-party monitoring tools for real-time security insights