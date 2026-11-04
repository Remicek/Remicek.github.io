# HowYouDoin

All your chats in one inbox: WhatsApp, Messenger, Instagram, Telegram, Signal, Slack, Bluesky, LinkedIn, Discord, X and
Matrix, connected straight from your Android phone. No HowYouDoin account, no HowYouDoin servers.

- Website: https://howyoudoin.app
- Download: [latest release](https://github.com/Remicek/howyoudoin/releases/latest) (the `.apk` file; Android 8 or
  newer). Google Play and the App Store are coming.
- [Privacy policy](https://howyoudoin.app/privacy.html) · [Terms of use](https://howyoudoin.app/terms.html)
  (sources: [privacy-policy.md](privacy-policy.md), [terms-of-use.md](terms-of-use.md); run `python3 build-legal.py` after editing them)

This repository holds the website and the app's downloads.

## Publishing

https://howyoudoin.app is served by Caddy on the OVHcloud server behind Cloudflare (`matcha-api/deploy/Caddyfile`,
the `howyoudoin.app` block). Upload:
`rsync -az --delete --exclude .git --exclude '*.md' --exclude '*.py' ./ <user>@213.32.18.211:/var/www/howyoudoin/`
