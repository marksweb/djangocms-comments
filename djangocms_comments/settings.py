from django.conf import settings

COMMENT_PUBLISHED_BY_DEFAULT = True
AKISMET_API_KEY = ''
MIN_LENGTH_COMMENT_BODY = 50
MAX_LENGTH_COMMENT_BODY = 12000
MAX_BREAKLINES_COMMENT_BODY = 12
MAX_UPPERCASE_RATIO_COMMENT_BODY = 0.3
COMMENT_TEXTAREA_ROWS = 4
COMMENT_WAIT_SECONDS = 120
COMMENT_PREVENT_USURP_USERNAME = True

# Override my settings usign Django Settings
for var_name, value in dict(locals()).items():
    if var_name.isupper():
        locals()[var_name] = getattr(settings, var_name, value)
