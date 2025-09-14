
1. Settings:
   - DEBUG must be False in production.
   - SECURE_CONTENT_TYPE_NOSNIFF=True
   - SECURE_BROWSER_XSS_FILTER=True
   - X_FRAME_OPTIONS='DENY'
   - SESSION_COOKIE_SECURE=True, CSRF_COOKIE_SECURE=True (HTTPS only)
   - HSTS configured for production (SECURE_HSTS_SECONDS)

2. Templates:
   - All forms include {% csrf_token %}.
   - Avoid using |safe; rely on Django autoescape.

3. Views:
   - Use Django ORM filters (no raw SQL).
   - Use ModelForm for validation and sanitizing inputs.

4. CSP:
   - Set CSP either via django-csp or the custom middleware.
   - Test CSP in staging to avoid blocking required resources.

5. File uploads:
   - Validate file types and sizes; prefer external storage in production.

6. Testing:
   - Try to submit forms without CSRF token (should fail).
   - Try injecting SQL-like strings in search (should not break).
   - Test with users lacking permissions (should get 403).
