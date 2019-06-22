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

### Home page
Users receive notification if not logged in.
![Home page](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/1.png)

### Logged in
Once logged in a user has access to all the routes.
![Once logged in](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/2.png)

### Marketplace
Shows all placements for each company.
![Marketplace](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/4.png)

### Placement detail view
Shows details for a specific placement.
![Placement detail view](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/5.png)

### Responsive on mobile
![Responsive on mobile](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/9.png)

### Dashboard view
![Dashboard view](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/8.png)

### About page
![About](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/7.png)

### Individual Bid Summary
![Individual Bid Summary](https://github.com/danielc92/django-bidding-app/blob/master/screenshots/3.png)

# Contributors
- Daniel Corcoran

# Sources
- [Materialize CSS](https://materializecss.com/)
- [Chart.js](https://www.chartjs.org/)
- [Django](https://docs.djangoproject.com/en/2.2/)