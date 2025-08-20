# RentMate

RentMate is a full-stack Django-based web application built for renting equipment and vehicles. It provides a seamless experience for users to browse, book, and pay for rental items in a secure and user-friendly environment. The platform features real-time availability checking, Stripe payment integration, user authentication, and a mobile-responsive design.

- Live site : https://rent-mate-39fb0669e05e.herokuapp.com/
- Repository : https://github.com/GeorgeBarh/rent-mate-project

---
![Responsive Screenshot](static\images\readme\respo.png)

## Table of Contents

2. [Features](#features)
3. [User Stories](#user-stories)
4. [Design](#design)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Debugging & Fixes During Testing](#debugging--fixes-during-testing)
8. [Deployment](#deployment)
9. [Facebook Business Page](#facebook-business-page)
10. [Future Features](#future-features)
11. [Credits](#credits)
12. [Disclaimer](#disclaimer)

---

## Project Overview
---

## Features

### Core Functionality

* **Product Browsing**: Paginated list of products by category (vehicles, equipment).
![List of Products ](static\images\readme\products1.png)
* **Booking System**: Users can select start and end dates and check real-time availability.
![Make a booking](static\images\readme\book.png)
* **Stripe Integration**: Secure payments are processed through [Stripe](https://stripe.com/), with success confirmed via webhook.
![Payment form](static\images\readme\stripeform.png)

* **My Bookings**: Authenticated users can view and cancel their bookings (if unpaid).
![My Bookings section](static\images\readme\bookings.png)

* **Availability Validation**: Prevents double-booking with backend logic.

### User Experience

* Responsive and mobile-friendly UI with a clean, professional layout.
* Styled using [Bootstrap](https://getbootstrap.com/) and [Font Awesome](https://fontawesome.com/).
* Clear user feedback via Django messages (e.g., booking confirmed, payment failed).
![Success message](static\images\readme\success_fix.png)

### Admin Panel

* Product and booking management via Django admin.

### Additional Features

* Newsletter subscription with email validation.
![Newsletter Subscription](static\images\readme\footer.png)

* Facebook business page integration for outreach.
![Facebook](static\images\readme\fb.png)


---

## User Stories

### EPIC 1: Registration and Authentication

* As a new user, I can register with a strong password.
![Sign up page](static\images\readme\register.png)

* As a user, I can log in and log out securely.
![Login page](static\images\readme\login.png)
![Log out message](static\images\readme\logout.png)


### EPIC 2: Product Browsing

* As a user/guest, I can browse products by type.
* As a guest, I can view but not book until I log in.
![Products list](static\images\readme\products4.png)


### EPIC 3: Booking

* As a user, I can book a product for a selected date range.
* As a user, I can see unavailable dates.
* As a user, I am prevented from overlapping bookings.
![Availability/Booking calendar](static\images\readme\book.png)


### EPIC 4: Payments

* As a user, I can pay securely via Stripe.
![Stripe](static\images\readme\stripeform.png)

* As a user, I get confirmation after successful payment.
![Success message](static\images\readme\success_fix.png)


### EPIC 5: Account Management

* As a user, I can view my bookings.
![My Bookings](static\images\readme\bookings.png)

* As a user, I can cancel unpaid bookings but not paid ones.

---

## Design

The project followed mobile-first responsive design principles. Visual elements include:

* Color palette: dark green with yellow contrast text.
* Fonts: Clean sans-serif typography.
* Layout: Card-based product listings, glass-effect forms.
* Booking form with a calendar widget.
* All pages responsive across devices.

---

## Technologies Used

* [Django](https://www.djangoproject.com/) – Backend framework
* [PostgreSQL](https://www.postgresql.org/) – Database (via Heroku add-on)
* [Bootstrap 5](https://getbootstrap.com/) – CSS framework
* [Font Awesome](https://fontawesome.com/) – Icons
* [Cloudinary](https://cloudinary.com/) – Image hosting
* [Stripe](https://stripe.com/) – Payment integration
* [Heroku](https://www.heroku.com/) – Deployment platform
* [Gunicorn](https://gunicorn.org/) – WSGI HTTP server
* [WhiteNoise](http://whitenoise.evans.io/en/stable/) – Static file handling

---

## Testing

### Automated Testing

#### rentals/tests.py

*  Model string representation
*  Authenticated user can access booking form
*  Overlapping dates rejected
*  My bookings shows correct user data
*  Booking cancellation (unpaid) allowed
*  Booking cancellation (paid) blocked
*  Anonymous user redirected
*  User can't cancel others' bookings

#### rentals/test\_forms.py

*  Valid booking form accepted
*  Invalid date range rejected

#### home/test\_forms.py

*  Valid email accepted
*  Invalid email rejected

### Manual Testing

* Registered and logged in as multiple users
* Submitted booking forms with valid/invalid dates
* Verified Stripe payment flow (test mode)
* Tested button visibility for login/logout states
* Checked mobile responsiveness

---

## Debugging & Fixes During Testing

### SECRET\_KEY must not be empty

**Issue**: Tests failed with missing SECRET\_KEY.
**Fix**: Set a dummy key in terminal:

```bash
$env:SECRET_KEY="test"; python manage.py test
```

### Booking form accepting invalid date range

**Issue**: Form accepted invalid date logic.
**Fix**: Added `clean()` method to validate start/end date logic.

### Static file error (preview\.jpg)

**Issue**: Test failed due to missing image.
**Fix**: Removed unused image reference from templates.

### ModuleNotFoundError: No module named 'home.test\_forms'

**Issue**: Used `.py` in test command.
**Fix**:

```bash
python manage.py test home.test_forms
```

### Test login/session issues

**Issue**: Test client failed to authenticate.
**Fix**:

```python
self.user = User.objects.create_user(username='testuser', password='testpass123')
self.client.login(username='testuser', password='testpass123')
```

---

## Deployment

### Hosted On:

* [Heroku](https://heroku.com/)

### Setup:

* PostgreSQL via Heroku add-on
* Stripe integration for payments
* Cloudinary for image hosting
* Gunicorn + WhiteNoise for production

### Steps:

1. Push code to [GitHub](https://github.com/GeorgeBarh/restaurant-booking-system-project)
2. Connect Heroku app to GitHub
3. Add env variables:

   * SECRET\_KEY
   * DEBUG
   * DATABASE\_URL
   * STRIPE\_PUBLIC\_KEY
   * STRIPE\_SECRET\_KEY
   * STRIPE\_WEBHOOK\_SECRET
   * ALLOWED\_HOSTS
4. Run migrations and collectstatic:

```bash
python manage.py migrate
python manage.py collectstatic
```

5. Upload fixtures for product seeding

---

## Facebook Business Page

RentMate also has a Facebook Business Page to:

* Share updates
* Build community
* Provide an additional contact channel

**Visit:** [RentMate on Facebook](https://www.facebook.com/profile.php?id=61579385408462)
![Facebook page](static\images\readme\fb.png)


---

## Future Features

* Calendar with date availability preview
* Admin dashboard for managing bookings/products
* Email confirmation system
* Loyalty and discount system for repeat customers

---

##  Code Validation & Accessibility


All code was tested for quality, accessibility, and standards compliance using widely accepted industry tools.

### Python - PEP8

All Python files were tested using [flake8](https://flake8.pycqa.org/) and passed without errors, except some lines that were "too long". 

### CSS - W3C Validator

The CSS was validated using [W3C CSS Validator](https://jigsaw.w3.org/css-validator/).

![CSS Validation](static\images\readme\css.png)

## Lighthouse Report

Lighthouse was used to validate performance, accessibility, SEO, and best practices.

![Lighthouse Scores](static\images\readme\lighthouse.png)

--- 


## Credits

* [Code Institute](https://codeinstitute.net/) – Project structure
* [Bootstrap](https://getbootstrap.com/) / [Font Awesome](https://fontawesome.com/) – UI framework
* [Stripe](https://stripe.com/) – Payment handling
* [Cloudinary](https://cloudinary.com/) – Image hosting
* [Pexels](https://www.pexels.com/) / [Unsplash](https://unsplash.com/) – Placeholder images
* Stack Overflow, GitHub Issues,ChatGPT – Debugging support

---

## Disclaimer

This site is built for educational purposes as a portfolio project. All payments are processed in **Stripe test mode** and no real transactions occur. Do not enter real credit card details.
