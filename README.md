# "Windev" AMRSystem

Django-based ad crawl and music request manager.

Built originally for [KWSF-IP](https://live.mistwx.com/player?channel=kwsf01) but can be easily adapted for any STAR/OBS-based system!

# Stack
- django  

# App the cations
- `songrequests` - Song requests, obviously...
- `adcrawls` - Ad crawls. API-only.
- `miscpages` - All the static-ish pages - like, for instance, the index page.
- `agents` - Client-side APIs

# Basic Setup
do as you would any django application.
Note this is really only good for development, prod guide coming soonish.

- `pip install django`
- `python manage.py migrate`
- `python manage.py createsuperuser` - fill that out
- `python manage.py runserver`

# Pre-Prod Config
Before you open your instance up to the public - you SHOULD:

- Add a song: `http://[YOURURL]/admin/songrequests/song/`.
  - If you need a song to test its functionality, I've uploaded Playing with the Fish at `https://semistatic.fourteentrees.net/musiclib/pwtf.mp3`
- Brand your instance and change the default secret key in `AMRSystem/settings.py`, by changing the `APP_NAME` and `SECRET_KEY` vars respectively
- Determine if you want to hide the 'Administration' link in the navbar, and alter `HIDE_ADMIN_IN_NAVBAR` accordingly.
- Set up the agent, or write your own - docs for this coming soonish.
- Make sure it works by sending in a song request and LISTENING
- Optionally create groups with permissions to set ad crawls

# Contributing
Follow "Basic Setup." We do not have unit tests, so you will need to TEST YOUR CHANGES before sending them in.

If you don't have TailwindCSS 4.1.18 or above globally available, you must download it as we don't bundle it in the repo

```sh
curl https://github.com/tailwindlabs/tailwindcss/releases/download/latest/tailwindcss-linux-x64 -o AMRSystem/static/css/tailwindcss
```

If your change modifies any views at all, you should rerun TailwindCSS:

```sh
AMRSystem/static/css/tailwindcss -i AMRSystem/static/css/input.css -o AMRSystem/static/css/output.css
```

If your tailwindcss executable is globally installed, you can omit the first AMRSystem/static/css:

```sh
tailwindcss -i AMRSystem/static/css/input.css -o AMRSystem/static/css/output.css
```

If you need to make a value from settings available to views, you should add it to AMRSystem/context_process.py under the 'app_config' section. Currently `APP_NAME` and `HIDE_ADMIN_IN_NAVBAR` are available through here.