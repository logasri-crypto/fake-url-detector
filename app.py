import re

def is_valid_url(url):
    pattern = re.compile(
        r'^(https?:\/\/)?'  # http or https
        r'([a-zA-Z0-9.-]+)\.([a-zA-Z]{2,})'  # domain
    )
    return re.match(pattern, url)

def check_url(url):
    # Step 1: Check valid URL
    if not is_valid_url(url):
        return "❌ Invalid URL"

    score = 0

    # Rule 1: HTTPS check
    if "https" not in url:
        score += 1

    # Rule 2: Suspicious words
    suspicious_words = ["login", "verify", "bank", "free", "win"]
    for word in suspicious_words:
        if word in url:
            score += 1

    # Rule 3: Length check
    if len(url) > 50:
        score += 1

    # Final result
    if score >= 2:
        return "⚠️ Suspicious URL"
    else:
        return "✅ Safe URL"

