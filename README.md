# AstroViz 🌌

Application web pour explorer et visualiser des données astronomiques en temps réel.

## Stack technique
- Back-end : Django + Django REST Framework
- Front-end : React + TypeScript
- Librairies scientifiques : astropy, skyfield (à venir)
- Base de données : SQLite (dev), PostgreSQL (prod)

## Installation

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py runserver