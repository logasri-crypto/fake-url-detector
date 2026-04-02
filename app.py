from urllib.parse import urlparse

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except:
        return False

def check_url(url):
    # Step 1: Ensure URL has http/https
    if not url.startswith("http://") and not url.startswith("https://"):
        return "❌ Invalid URL (must start with http:// or https://)"

    # Step 2: Validate structure
    if not is_valid_url(url):
        return "❌ Invalid URL"

    score = 0

    # Rule 1: HTTPS check
    if "https" not in url:
        score += 1

    # Rule 2: Suspicious words
    suspicious_words = ["login", "verify", "bank", "free", "win"]
    for word in suspicious_words:
        if word in url.lower():
            score += 1

    # Rule 3: Length check
    if len(url) > 50:
        score += 1

    # Final result
    if score >= 2:
        return "⚠️ Suspicious URL"
    else:
        return "✅ Safe URL"




