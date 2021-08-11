import base64
import urllib.parse

import jinja2


def get_logo(path):
    with open(path, "rb") as f:
        logo = base64.b64encode(f.read()).decode("utf-8")
    if path.endswith(".svg"):
        return "data:image/svg+xml;base64," + logo
    elif path.endswith(".ico"):
        return "data:image/x-icon;base64," + logo
    elif path.endswith(".png"):
        return "data:image/png;base64," + logo
    else:
        raise ValueError(f"'{path}' has unknown extension")


def from_file(path):
    if type(path) is str:
        return get_logo(path)
    else:
        return [get_logo(p) for p in path]


LOGOS = [
    ("browser", "Chrome", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/chrome/chrome.svg"),
    ("browser", "Chromium", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/chromium/chromium.svg"),
    ("browser", "DuckDuckGo Privacy Browser", "https://icons.duckduckgo.com/ip3/spreadprivacy.com.ico"),
    ("browser", "Ecosia", "https://cdn-static.ecosia.org/assets/images/ico/favicon.ico"),
    ("browser", "Firefox", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/firefox/firefox.svg"),
    ("browser", "Microsoft Edge", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/edge/edge.svg"),
    ("browser", "Mobile App", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/android-webview/android-webview.png"),
    ("browser", "Opera", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/opera/opera.svg"),
    ("browser", "Opera Touch", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/opera-touch/opera-touch.png"),
    ("browser", "Pale Moon", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/pale-moon/pale-moon.png"),
    ("browser", "Safari", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/safari-ios/safari-ios.svg"),
    ("browser", "Samsung Browser", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/samsung-internet/samsung-internet.svg"),
    ("browser", "Waterfox", "https://upload.wikimedia.org/wikipedia/en/b/b5/Waterfox_Logo_June_2019.png"),
    ("browser", "Yandex Browser", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/yandex/yandex.png"),

    ("os", "Android", "https://upload.wikimedia.org/wikipedia/commons/3/31/Android_robot_head.svg"),
    ("os", "Chrome OS", "https://raw.githubusercontent.com/alrra/browser-logos/main/src/chrome/chrome.svg"),
    ("os", "Fedora", "https://upload.wikimedia.org/wikipedia/commons/4/41/Fedora_icon_%282021%29.svg"),
    ("os", "GNU/Linux", "https://upload.wikimedia.org/wikipedia/commons/3/35/Tux.svg"),
    ("os", "iOS", "https://upload.wikimedia.org/wikipedia/commons/6/63/IOS_wordmark_%282017%29.svg"),
    ("os", "Mac", "https://upload.wikimedia.org/wikipedia/commons/2/21/MacOS_wordmark_%282017%29.svg"),
    ("os", "Ubuntu", "https://upload.wikimedia.org/wikipedia/commons/a/ab/Logo-ubuntu_cof-orange-hex.svg"),
    ("os", "Windows", "https://upload.wikimedia.org/wikipedia/commons/8/87/Windows_logo_-_2021.svg"),
]


with open("plausible-logos.user.css.jinja2", "r") as t, open("plausible-logos.user.css", "w") as f:
    template = jinja2.Template(t.read())
    f.write(template.render(logos=LOGOS, urlquote=lambda u: urllib.parse.quote(u.replace(" ", "+"), safe="+")))
