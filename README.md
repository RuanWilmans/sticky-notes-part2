# Sticky Notes — Part 2 (with Authors & Tests)

Prepared by: Ruan Wilmans

This continues **Part 1** and implements mentor feedback:
- Add `Author` model and allow adding authors (UI + admin)
- Notes require an author; all pages show the author
- Unit tests cover models and core views
- Improved comments and spacing for readability

## Run locally
1. Create & activate a virtualenv.
2. `pip install django`
3. `python manage.py makemigrations && python manage.py migrate`
4. `python manage.py runserver` → http://127.0.0.1:8000/
5. Run tests: `python manage.py test`
