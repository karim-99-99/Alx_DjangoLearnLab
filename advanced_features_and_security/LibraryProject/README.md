django prject # Security Measures in LibraryProject

This project implements several security best practices in Django:

1. **Secure Settings**
   - DEBUG = False in production
   - SECURE_BROWSER_XSS_FILTER, X_FRAME_OPTIONS, SECURE_CONTENT_TYPE_NOSNIFF
   - CSRF_COOKIE_SECURE & SESSION_COOKIE_SECURE enforce HTTPS-only cookies

2. **CSRF Protection**
   - `{% csrf_token %}` included in all forms
   - CSRF middleware enabled

3. **Safe Data Handling**
   - All inputs handled via Django Forms (validation & sanitization)
   - ORM used instead of raw SQL → prevents SQL injection

4. **Permissions**
   - `@permission_required` decorators used for access control
   - Prevents unauthorized CRUD actions

5. **Content Security Policy (CSP)**
   - Enforced via `django-csp`
   - Restricts external scripts, styles, fonts

6. **Testing**
   - Manual testing of CSRF, XSS, SQL Injection attempted
   - Verified correct handling of malicious inputs
