# blogfolio

blogfolio is a mini blog application built with Django allowing users to view posts, view author profiles, and (if logged in) comment on posts.

## Features

* **User Authentication:**   Secure login and logout functionality for users.
* **Blog Management:** blog posts are sorted by the newest first
* **Blogger Profiles:** each blogger's profile includes a bio section and a list of their posts
* **Comments:** authenticated users can comment on blog posts. Comments are timestamped and attributed to the user.
* **Custom Styling:** modern layout with an original background I designed

## Quick Start (Bash on Windows)

**Prerequisites:** Python and Git installed

Copy the following commands into your terminal to set up and launch the project:

```bash
git clone https://github.com/briananandi/blogfolio.git
cd blogfolio
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Once the server is running, open your browser to:

* Site: http://127.0.0.1:8000/
* Admin Panel: http://127.0.0.1:8000/admin/
