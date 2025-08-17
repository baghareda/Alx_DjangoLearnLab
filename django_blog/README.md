# 📝 Django Blog Project

This is a simple blog application built with Django as part of the **ALX Django Learn Lab**.  
It demonstrates how to build a fully functional web application with authentication, CRUD features, and templates.

---

## 🚀 Features

### 🔐 Authentication
- User registration (with email, username, and password).
- User login and logout.
- User profile page with ability to update information.

### 📰 Blog Posts
- **List all posts** (newest first).
- **View post details**.
- **Create new posts** (only logged-in users).
- **Edit posts** (only the author).
- **Delete posts** (only the author).

---

## 🌍 URL Patterns

| URL                  | View              | Description                          |
|----------------------|------------------|--------------------------------------|
| `/`                  | Home              | Landing page.                        |
| `/login/`            | LoginView         | User login.                          |
| `/logout/`           | LogoutView        | User logout.                         |
| `/register/`         | `register`        | User registration.                   |
| `/profile/`          | `profile`         | View & edit profile.                 |
| `/posts/`            | PostListView      | List all blog posts.                 |
| `/post/<id>/`        | PostDetailView    | View a single post.                  |
| `/post/new/`         | PostCreateView    | Create a new post (login required).  |
| `/post/<id>/edit/`   | PostUpdateView    | Edit a post (author only).           |
| `/post/<id>/delete/` | PostDeleteView    | Delete a post (author only).         |

---

## ⚙️ How to Run Locally

1. **Clone the repo**:
   ```bash
   git clone <your-repo-link>
   cd Alx_DjangoLearnLab/django_blog
