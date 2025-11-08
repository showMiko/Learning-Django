# Learning Django — Quick Start & Cheatsheet

Small, focused README to help you understand and work with this project.  
Comments and short explanations are included next to commands and snippets so you can quickly know what each step does.

---

## Project overview
This repository is a typical Django project with one main project (`learningDjango`) and one or more apps (for example `basics`). You will:
- Create apps with `startapp`
- Register apps in `settings.py`
- Add templates (app-level: `app/templates/app/...` or project-level `templates/...`)
- Use Tailwind for styling (via `django-tailwind`)

---

## Prerequisites (Windows)
- Python 3.x
- pip (packaged with Python; or run `python -m ensurepip --upgrade`)
- Node.js + npm (required for Tailwind)
  - Install: https://nodejs.org or via winget:  
    ```
    winget install --id OpenJS.NodeJS.LTS -e
    ```
  - Verify:
    ```
    node -v
    npm -v
    where.exe npm     # prints path to npm executable
    ```

Note: If `where.exe npm` prints a path like `C:\Program Files\nodejs\npm.cmd`, you can point Django to it (see Tailwind section).

---

## Virtual environment (recommended)
Create venv and activate (PowerShell):
```
python -m venv .venv
.\.venv\Scripts\Activate.ps1       # PowerShell
# or for cmd.exe:
.\.venv\Scripts\activate.bat
```
Explanation: keeps project dependencies isolated.

Install common packages:
```
pip install django
pip install django-tailwind
pip install 'django-tailwind[reload]'   # optional, for hot reload support
pip install Pillow                      # for image fields
```

---

## Useful Django commands (cheat list)
- Create project (done already):
  ```
  django-admin startproject <projectname>
  ```
- Create an app:
  ```
  python manage.py startapp <appname>
  ```
- Run dev server:
  ```
  python manage.py runserver 8001
  ```
- Migrations:
  ```
  python manage.py makemigrations <appname>
  python manage.py migrate
  ```
- Create superuser:
  ```
  python manage.py createsuperuser
  ```
- Tailwind (see Tailwind section for details):
  ```
  python manage.py tailwind init
  python manage.py tailwind install
  python manage.py tailwind start   # dev (watch)
  python manage.py tailwind build   # production
  ```

Explanation: `manage.py` is the CLI entry point for Django commands.

---

## Apps, Templates & URLs — workflow and notes
1. Add new app name to `settings.py` → `INSTALLED_APPS`.
   - Explanation: Django discovers templates and models for apps listed here.
2. Create `templates` folder inside app:
   - `basics/templates/basics/all_basics.html`
   - Or use project-level `templates/` and add `BASE_DIR / "templates"` to `TEMPLATES['DIRS']`.
3. Typical view rendering:
   ```python
   # basics/views.py
   from django.shortcuts import render

   def all_basics_view(request):
       items = Item.objects.all()
       return render(request, "basics/all_basics.html", {"items": items})
   ```
   - Template path must exactly match filename (watch plural/singular typos).
4. Add app urls and include in project `urls.py`:
   ```python
   # project urls.py
   from django.urls import path, include

   urlpatterns = [
       path('admin/', admin.site.urls),
       path('basics/', include('basics.urls')),
   ]
   ```
   - Explanation: `include()` transfers routing to the app's `urls.py`.

Common template loading error:
- If Django tried paths like:
  ```
  C:\... \learningDjango\templates\basics\all_basic.html (Source does not exist)
  ```
  Check:
  - File exists at `learningDjango\basics\templates\basics\all_basic.html` OR
  - You're using `all_basics.html` in view while file is named `all_basic.html` (typo mismatch).

---

## Layouts (base templates)
- Create `templates/layout.html` (project-level) with common header/footer.
- Child templates should `{% extends "layout.html" %}` and define `{% block content %}`.
- Explanation: centralizes navigation, CSS includes, etc.

---

## Tailwind setup (django-tailwind)
1. Add `'tailwind'` and your theme app (e.g. `'theme'`) to `INSTALLED_APPS`.
2. Initialize tailwind (first time):
   ```
   python manage.py tailwind init
   ```
   This creates a theme app (`theme`) scaffold with `static_src/package.json`.
3. Add to `settings.py`:
   ```python
   TAILWIND_APP_NAME = 'theme'
   INTERNAL_IPS = ['127.0.0.1']   # for django-browser-reload if used
   ```
4. Install Tailwind dependencies:
   ```
   python manage.py tailwind install
   ```
   If you get the Node/npm error:
   - Make sure Node and npm are on PATH.
   - Or set `NPM_BIN_PATH` in `settings.py` to the full path of `npm` on Windows, for example:
     ```python
     NPM_BIN_PATH = r"C:\Program Files\nodejs\npm.cmd"
     ```
     Use `where.exe npm` to find the correct path.
5. Start Tailwind watcher (dev):
   ```
   python manage.py tailwind start
   ```
   Build for production:
   ```
   python manage.py tailwind build
   ```

Troubleshooting:
- Error: "It looks like node.js and/or npm is not installed or cannot be found."
  - Install Node.js; verify with `node -v` and `npm -v`.
  - If installed but Django can't find it, set `NPM_BIN_PATH` as above.

Optional: For hot reload with templates and CSS:
- Install and configure `django_browser_reload`:
  - Add to `INSTALLED_APPS` and middleware:
    ```python
    INSTALLED_APPS += ['django_browser_reload']
    MIDDLEWARE += ['django_browser_reload.middleware.BrowserReloadMiddleware']
    ```
  - Add url in `project urls.py`:
    ```python
    path("__reload__/", include("django_browser_reload.urls")),
    ```
  - Explanation: reloads page automatically when files change.

---

## Serving media (images)
In `settings.py`:
```python
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
In project `urls.py` (development only):
```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```
Explanation: this allows `{{ item.image.url }}` to serve uploaded images during development.

---

## Forms (brief)
- Create `forms.py` in app and use `forms.ModelForm` for model-backed forms.
- Typical flow:
  - Render form in GET, process and save in POST.
  - Use `ModelChoiceField` for dropdown selections (Django handles choices).

---

## Helpful quick commands (PowerShell)
```
# Activate venv
Set-Location 'C:\Users\soumi\Desktop\Learning Django'
.\.venv\Scripts\Activate.ps1

# Run server
python manage.py runserver

# Tailwind install (after Node is available)
python manage.py tailwind install

# Tailwind start (watch)
python manage.py tailwind start

# Build Tailwind for production
python manage.py tailwind build

# Check npm location
where.exe npm
```

---

## Tips & common pitfalls
- Template name typos are a very common cause of `TemplateDoesNotExist`.
- Ensure `APP_DIRS=True` in `TEMPLATES` (in `settings.py`) so Django finds `app/templates/<app>/...`.
- When using images, install `Pillow`.
- Always activate the virtualenv before running `manage.py` to ensure correct Python packages are used.
- If a package install fails on Windows (peer deps), try `npm install --legacy-peer-deps` inside `theme/static_src`.

---