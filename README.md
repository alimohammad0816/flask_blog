# Flask Blog

A blog application built with **Flask**, with user registration, secure password hashing and session-based authentication.

## Features

- **User accounts**: registration and login with form validation (Flask-WTF, WTForms, email-validator).
- **Secure passwords**: hashed with `bcrypt` via Flask-Bcrypt.
- **Sessions**: Flask-Login handles "remember me", protected routes (`@login_required`) and safe `next` redirects.
- **ORM models**: `User` and `Post` (one-to-many) defined with Flask-SQLAlchemy on SQLite.
- **Pages**: home feed, about, register, login and a protected account page.
- **Templating**: Jinja2 layouts with a shared base template and flash messages.

## Tech stack

Python · Flask 2.0 · Flask-SQLAlchemy · Flask-Login · Flask-Bcrypt · Flask-WTF · SQLite

## Getting started

```bash
git clone https://github.com/alimohammad0816/flask_blog.git
cd flask_blog

python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The SQLite database (`site.db`) is git-ignored, so create it on first run:

```bash
python - <<'EOF'
from weblog.application import app, db
with app.app_context():
    db.create_all()
EOF

export SECRET_KEY='change-me'   # optional for local dev
python app.py
```

Then open <http://127.0.0.1:5000/>.

## Project structure

```
app.py              entry point
weblog/
  application.py    app factory-style setup (db, bcrypt, login manager)
  models.py         User and Post models
  forms.py          registration and login forms
  views.py          routes
  templates/        Jinja2 templates
  static/           CSS
```

## Status & roadmap

The home page renders posts from the database. Planned next steps:

- [ ] Create, edit and delete posts from the UI
- [x] Render posts from the database
- [x] Pagination (5 posts per page)
- [ ] Profile image upload

## License

No license specified yet.
