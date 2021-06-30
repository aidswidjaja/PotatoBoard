# PotatoBoard
PotatoBoard is a free and easy way to automate a bulletin board workflow, written with Django for Things You Should Know.

Oh, did I say free and easy? Oh, I meant *sorta* free and easy. It's definietly free. Not too sure about that last one tho.

This project's code is open-source, except it's not meant for general usage or development. Instead, if you're keen on using PotatoBoard yourself, you'll need to modify it in order to fit your specific use case (since I have designed it with my use case in mind). You'll also need to set environment variables and so on, so a relatively decent understanding of Python and web server development is required. This is not for the faint of heart.

However, if you *do* manage to get it up and running, it can simplify your workflow by like *a lot*, and for me personally it's amazing since I can post different announcements across different platforms. Just keep in mind I hardcoded a lot of things since this has been designed for a specific production instance in mind.

> Use PotatoBoard to serve data in different formats (webhooks, markup, email, push notifications) with only one originating request. Currently under active development, and is poised to support WhatsApp, Discord, Instagram, Google Calendar, Office 365, email, and even its own (primitive) web service.

Not so free and easy now, eh? Dw though, if you need help feel free to open a issue on GitHub and I'll do my best to help you out, though support isn't guaranteed and therefore you shouldn't consider this project production-ready.

**Note:** in some aspects of the code it may refer `API`, `TYSK`, `Alicization Push Integrations`, or simply `Alicization` which are the production names of this software. 

## Dependencies

- Python 3.9.0
- Django 3.1.4
- SQLite3
- [Twitter's Bootstrap 5.0.0-beta1](https://getbootstrap.com/)
- [Marked](https://marked.js.org/)
- [cure53/DOMPurify](https://github.com/cure53/DOMPurify)
- [Twitter's Twemoji](https://twemoji.twitter.com/)
- [zenorocha/clipboard.js](https://github.com/zenorocha/clipboard.js/)

Thank you to jsDelivr, MaxCDN and Cloudflare cdnjs for providing the free-of-charge CDN to host dependencies.

The reference implementation of PotatoBoard (Things You Should Know - potato.adrian.id.au) uses an Ubuntu LTS server with nginx.

## Developer Instructions

1. Clone the git repo

```bash
git clone https://github.com/aidswidjaja/PotatoBoard
```

2. Set environment variables (see [Environment](#Environment))
3. Source Python environment

```bash
source env/bin/activate.bash
```

Replace `bash` with your shell (e.g for new Macs this is `zsh`)

4. Make migrations

```bash
python makemigrations && python migrate
```

5. Start the development server

```bash
python manage.py runserver
```

## Deploy instructions

Deploy instructions for Ubuntu Server 18.04 LTS with nginx on Microsoft Azure - but you should be able to use your choice of stack (Apache, httpd, etc.) on any platform (self-hosted, Heroku, GCP, AWS).

## Environment

Don't forget to set environment variables in:

```
potato/.env
board/static/board/env.js
board/subjects.py
board/static/board/subjects.js
```