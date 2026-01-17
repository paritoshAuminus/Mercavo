# 1️⃣ What is **Jira Lite**?

### What Jira (the real one) does

Jira is a **project & issue tracking tool** used by teams to:

* Plan work
* Track tasks/bugs
* Assign work to people
* See progress over time

Companies use it for **Agile / Scrum / Kanban** workflows.

---

### 🧩 What **Jira Lite** means (for your project)

You are NOT rebuilding Jira.

**Jira Lite = a simplified backend system that supports:**

* Teams / Organizations
* Projects
* Tasks (issues)
* Roles & permissions
* Activity tracking

Think of it as:

> “A production-ready task management backend API”

This is **perfect** for backend interviews.

---

### Core concepts (simple)

| Concept      | Meaning                   |
| ------------ | ------------------------- |
| Organization | A company or team         |
| Project      | A workspace inside an org |
| Task / Issue | A unit of work            |
| Role         | Admin, Manager, Member    |
| Activity Log | Who did what & when       |

---

# 2️⃣ Jira Lite – FULL BACKEND API DESIGN (Interview-Ready)

Below is a **clean, realistic API** using **DRF + ViewSets**.

---

## 🔐 Authentication & Users

```
POST   /api/v1/auth/register/
POST   /api/v1/auth/login/
POST   /api/v1/auth/logout/
POST   /api/v1/auth/token/refresh/
```

```
GET    /api/v1/users/me/
PATCH  /api/v1/users/me/
```

---

## 🏢 Organizations (Multi-Tenant)

```
POST   /api/v1/organizations/
GET    /api/v1/organizations/
GET    /api/v1/organizations/{org_id}/
PATCH  /api/v1/organizations/{org_id}/
DELETE /api/v1/organizations/{org_id}/
```

### Membership & Roles

```
POST   /api/v1/organizations/{org_id}/invite/
POST   /api/v1/organizations/{org_id}/join/
```

```
GET    /api/v1/organizations/{org_id}/members/
PATCH  /api/v1/organizations/{org_id}/members/{user_id}/role/
DELETE /api/v1/organizations/{org_id}/members/{user_id}/
```

**Roles**

* OWNER
* ADMIN
* MEMBER

👉 **Permissions Interview Gold**
“Only org owners can delete orgs.”

---

## 📁 Projects

```
POST   /api/v1/projects/
GET    /api/v1/projects/
GET    /api/v1/projects/{project_id}/
PATCH  /api/v1/projects/{project_id}/
DELETE /api/v1/projects/{project_id}/
```

Filters:

```
GET /api/v1/projects/?organization=1
```

---

## 🧩 Tasks (Issues)

```
POST   /api/v1/tasks/
GET    /api/v1/tasks/
GET    /api/v1/tasks/{task_id}/
PATCH  /api/v1/tasks/{task_id}/
DELETE /api/v1/tasks/{task_id}/
```

### Task fields

* title
* description
* status (TODO / IN_PROGRESS / DONE)
* priority (LOW / MEDIUM / HIGH)
* assignee
* due_date

### Filtering & search

```
GET /api/v1/tasks/?project=1
GET /api/v1/tasks/?assignee=5
GET /api/v1/tasks/?status=IN_PROGRESS
GET /api/v1/tasks/?search=auth
```

---

## 🔁 Task Workflow Actions (Custom ViewSet Actions)

```
POST /api/v1/tasks/{id}/assign/
POST /api/v1/tasks/{id}/change-status/
POST /api/v1/tasks/{id}/comment/
```

This shows:

* `@action(detail=True, methods=["post"])`
* Clean DRF knowledge

---

## 💬 Task Comments

```
GET    /api/v1/tasks/{task_id}/comments/
POST   /api/v1/tasks/{task_id}/comments/
DELETE /api/v1/comments/{comment_id}/
```

---

## 🕵️ Activity Logs (Signals)

**Automatically created using Django signals**

```
GET /api/v1/activity-logs/
```

Logs like:

* “User A created Task X”
* “User B changed status to DONE”

💬 Interview answer:

> “I used Django signals to log all task-related activity.”

---

## 🚦 Permissions & Throttling

### Permissions

| Action         | Who        |
| -------------- | ---------- |
| Create org     | Any user   |
| Delete org     | Owner only |
| Create project | Admin+     |
| Create task    | Members    |
| Assign task    | Admin+     |

---

### Throttling

```
- Create task → 100/day
- Comment → 300/day
```

---

## ⚡ Caching (Redis)

Cache:

```
GET /projects/
GET /tasks/?project=
```

Invalidate cache when:

* Task created/updated
* Project updated

💬 Interview-ready:

> “I used per-view caching with cache invalidation on writes.”

---

## 📄 Pagination & Versioning

```
/api/v1/...
```

Pagination:

* PageNumberPagination for tasks
* CursorPagination for activity logs

---

## 🧪 Admin & Debug

```
/api/v1/health/
```

---

# 3️⃣ How this project sells you in interviews

You can confidently say:

> “I built a multi-tenant task management backend using Django REST Framework with ViewSets, custom permissions, signals, caching, throttling, and API versioning. It supports organizations, role-based access, task workflows, and activity tracking.”

That’s **mid-level backend engineer language**.

---

## 4️⃣ Want next?

I can:

* Design **models & relationships**
* Write **sample ViewSets**
* Help you choose **Redis vs DB cache**
* Turn this into **resume bullet points**
* Do **mock interview questions based on this project**

Just tell me what you want next 👌
