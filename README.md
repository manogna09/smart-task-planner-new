# Smart Task Planner

This project is a **FastAPI-based Smart Task Planner** that automatically breaks down a goal into actionable tasks with dependencies and suggested deadlines.

---

## 🚀 Features
- Backend built with **FastAPI**
- Supports CORS for frontend integration
- Dynamic date-based task scheduling
- JSON schema validation with **Pydantic**
- Simple and clean API endpoints

---

## 🧩 API Endpoints

### Health Check
**GET** `/health` → Returns service status

### Generate Plan
**POST** `/generate_plan/`
Request Body:
```json
{
  "goal": "Launch a product in 2 weeks"
}
```

Response:
```json
{
  "goal": "Launch a product in 2 weeks",
  "prompt_used": "Break down this goal into actionable tasks with suggested deadlines and dependencies.",
  "tasks": [
    {
      "task": "Define project scope",
      "depends_on": null,
      "duration_days": 2,
      "start": "2025-10-23",
      "end": "2025-10-25"
    },
    ...
  ]
}
```

---

## 🖥️ Frontend Setup

The frontend is a simple **HTML + JavaScript interface** that sends a goal to the backend API and displays the task plan dynamically.

### Run Instructions
1. Open `index.html` in your browser.
2. Enter a goal (e.g., "Launch a product in 2 weeks").
3. Click "Generate Plan" to view results.

---

## 🛠️ Backend Setup

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run server
```bash
uvicorn main:app --reload
```

Then open your browser at `http://127.0.0.1:8000/docs` for Swagger UI.

---

## 📂 Project Structure

```
smart_task_planner/
│
├── main.py              # FastAPI backend
├── requirements.txt     # Dependencies
├── README.md            # Documentation
└── frontend/
    └── index.html       # Simple frontend UI
```

---

## 📽️ Demo Video
Add your recorded video link here once uploaded:
[Demo Video Placeholder](https://drive.google.com/)

---

## 👩‍💻 Author
**Sai Navya Jyesta**
