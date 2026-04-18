# Basic Blog MVP

A simple Django blog MVP that allows visitors to:
- post a thought,
- read existing entries,
- delete their own content.

## Features

- Validates that the post content is not empty.
- Uses session-based ownership so visitors can only delete their own posts.
- Displays a confirmation page before deleting a post.
- Shows success feedback after saving or deleting.

## Setup

1. Create a virtual environment and activate it.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```bash
   python manage.py migrate
   ```
4. Start the development server:
   ```bash
   python manage.py runserver
   ```

Open `http://127.0.0.1:8000/` in your browser.
