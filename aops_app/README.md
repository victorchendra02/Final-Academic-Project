# Final Project Application
Description coming soon ![thumbnail](thumbnail_1.jpg)

-----

## A. Initialize

```bash
# 1. Backend
cd flask-backend
python -m venv env
env\Scripts\activate
pip install -r requirements.txt

# 2. Frontend
cd vuetify-frontend
pnpm install
```

-----

## B. How to run
Prepare 2 `cmd`

### 1. Python Flask (Back-end API)

Open `cmd`, then paste this:

```bash
flask-backend\env\Scripts\activate
cd flask-backend\package
flask --debug run
```

### 2. Web Application (Front-end)

Open `cmd`, then paste this:

```bash
cd vuetify-frontend
pnpm run dev
```
