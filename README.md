# Bidding Application with Django
This application was built as a side project, in order to learn how to design and build a bidding system from scratch. The theme is based on capital raising for companies. It includes an auth system, marketplace, companies, placements, dashboard, mobile friendly design. I used Django mainly, to develop this application.

# Before you get started
Concepts covered in this app
- Routing
- ORM, database design
- Form handling
- Templates
- Charting with `Chart.js`
- Design with `Materialize.css`

# Routes
- `/` The home page. Contains news.
- `about/` Holds details about the application.
- `register/` Allows users to register an account
- `login/` Allows users to login to an account
- `logout/` Allows users to logout and clear their session
- `marketplace/` Listing of placements from various companies.
- `marketplace/slug/` Detailed view for a placement within the marketplace.
- `my-bids/` User scope bid summary for available placements.
- `dashboard/` Basic analytics and animated charts for the database.

# Setup

**Modules/dependencies:**
- `django`

**Running locally:**
```sh
# Ffter activating your virtualenv
python manage.py runserver
```

# Tests
- Tests performed on this project. What did you do? Which files were used? Was it successful?

# Screenshots 

**Home page**
![home page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.14.19%20pm.jpg)

**About page**
![About page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.14.43%20pm.jpg)

**Login page**
![login page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.13.50%20pm.jpg)

**Registration page**
![registration page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.13.56%20pm.jpg)

**Placements page**
![placements page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.14.35%20pm.jpg)

**Bid summary page**
![bid summary page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.14.40%20pm.jpg)

**Dashboard page**
![Dashboard page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.14.47%20pm.jpg)

**Bid submission page**
![Bid submission page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.20.31%20pm.jpg)

**Responsive on small devices**
![Responsive](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/Screen%20Shot%202019-07-29%20at%202.20.45%20pm.jpg)

# Contributors
- Daniel Corcoran

# Sources
- [Materialize CSS](https://materializecss.com/)
- [Chart.js](https://www.chartjs.org/)
- [Django](https://docs.djangoproject.com/en/2.2/)
