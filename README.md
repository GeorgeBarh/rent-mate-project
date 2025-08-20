# RentMate – Equipment & Vehicle Rental Platform

## 1. Project Overview

### 1.1 Project Objective

**RentMate** is a full-stack Django e-commerce rental platform where users can explore and book rental equipment or vehicles for specific dates. Whether it’s a power tool, a van, or a luxury car — the system ensures users can check availability, make secure payments via Stripe, and manage their bookings.

This project was developed for Code Institute's Portfolio Project 5 (PP5) and emphasizes secure authentication, a smooth booking experience, payment integration, and mobile-friendly responsive design.

Live Site: [https://rentmate-pp5.herokuapp.com/](https://rentmate-pp5.herokuapp.com/)
GitHub Repo: [https://github.com/GeorgeBarh/rentmate](https://github.com/GeorgeBarh/rentmate)

---

## 2. Features

### 2.1 Core Features

#### User Authentication

* Registration, login, logout using **Django AllAuth**.
* Strong password validation.
* Authenticated users can make bookings, view their bookings, and cancel unpaid ones.

#### Product Browsing

* Users can view a catalog of equipment and vehicles.
* Each product includes a name, description, price per day, and image.
* Cloudinary is used to host product images.

#### Booking System

* Users select start and end dates to check availability.
* If the product is booked during selected dates, an error is shown.
* Available products proceed to **Stripe Checkout** for secure payment.

#### Stripe Payment Integration

* Stripe Checkout session is created with product name and rental fee.
* Webhook handles post-payment confirmation and updates booking as paid.
* Success and Cancel pages provide user feedback.

####  Newsletter Signup

* A signup form in the footer allows users to enter an email.
* Emails are stored in the database.
* Bootstrap alerts confirm success or validation error.

---

## 3. UX Design

### 3.1 Target Audience

* **General users** looking to rent tools or transport for short-term use.
* **Small business owners** needing equipment without upfront purchases.
* **Returning users** managing ongoing or past bookings.

### 3.2 Strategy

* Clear call-to-actions like “Book Now” buttons on each product.
* Only logged-in users can proceed to booking.
* Navigation bar updates dynamically based on auth state.

### 3.3 Layout

* Built using **Bootstrap 5**.
* Dark green + yellow branding for a professional, utility-driven aesthetic.
* Cards for each product, transparent modals, responsive layout.

### 3.4 Responsiveness

* Fully responsive layout tested across mobile, tablet, and desktop.
* Uses Bootstrap grid and media queries.

---

## 4. Agile & Planning

### 4.1 User Stories

| **EPIC**             | **As a user...**                                                     |
| -------------------- | -------------------------------------------------------------------- |
| Registration & Login | I can register, log in, and log out securely                         |
| Product Browsing     | I can view a catalog of rental items                                 |
| Booking              | I can book a product for specific dates and pay securely with Stripe |
| My Bookings          | I can view all my bookings and cancel unpaid ones                    |
| Newsletter           | I can enter my email to get updates                                  |
| SEO & Sitemap        | I can trust the site will rank and handle errors gracefully          |

### 4.2 MoSCoW Prioritization

#### Must Have

* Auth, Booking Model, Stripe, Ownership logic

#### Should Have

* Email signup, Sitemap, Admin tools

#### Could Have

* Dynamic calendar, Facebook embed

#### Won’t Have

* OTP / Email Verification (out of scope)

### 4.3 GitHub Project Board

* Tasks organized in a Kanban-style board.
* Issues and enhancements tracked with milestones.

---

## 5. Technologies Used

* **Python 3.12** + **Django 4.2**
* **PostgreSQL** for Heroku production DB
* **Cloudinary** for image hosting
* **Stripe API** for secure checkout and webhooks
* **Bootstrap 5**, **HTML5**, **CSS3** for UI
* **Django AllAuth** – authentication
* **GitHub**, **GitPod**, **Heroku**, **Gunicorn**, **Whitenoise**
* **Django Crispy Forms** for styled forms
* **W3C Validators**, **Lighthouse**, **Django TestCase** for testing

---

## 6. Testing

### 6.1 Manual Tests

| Feature           | Action/Test Case                           | Status |
| ----------------- | ------------------------------------------ | ------ |
| Registration      | Create account with strong password        |  Pass |
| Booking Conflict  | Attempt to book a date range already taken |  Pass |
| Stripe Flow       | Checkout, pay, redirect to success         |  Pass |
| View Bookings     | List only current user’s bookings          |  Pass |
| Cancel Booking    | Only unpaid bookings can be cancelled      |  Pass |
| Navbar Auth Logic | Nav updates on login/logout                |  Pass |
| Newsletter Form   | Validation and DB save                     |  Pass |
| Sitemap/404       | 404 shown on invalid page                  |  Pass |

### 6.2 Django Unit Tests

* `test_views.py`: Covers booking, payment, and cancel views.
* `test_forms.py`: Booking and newsletter form validation.

To run:

```bash
python manage.py test
```

### 6.3 Lighthouse & Validators

* HTML: 100%
* CSS: 100%
* Accessibility: 98%
* SEO: 90+

---

## 7. Deployment

### 7.1 Hosting

* Hosted on **Heroku**.
* PostgreSQL used in production.

### 7.2 Setup

* `.env` for secret keys and Stripe variables
* `Procfile`, `requirements.txt`, `runtime.txt`
* `collectstatic`, `migrate`, `createsuperuser` via Heroku CLI

### 7.3 Environment Variables

* `SECRET_KEY`
* `DEBUG`
* `DATABASE_URL`
* `STRIPE_PUBLIC_KEY`
* `STRIPE_SECRET_KEY`
* `STRIPE_WEBHOOK_SECRET`
* `ALLOWED_HOSTS`

---

## 8. Database Schema

### Product

* `name`, `description`, `price_per_day`, `image`

### Booking

* `user`, `product`, `start_date`, `end_date`, `paid`
* Date overlap checks prevent double-bookings.

### NewsletterSignup

* `email` field, unique constraint

---

## 9. Future Features

* Admin dashboard with booking insights
* Booking calendar UI
* Email confirmations (SendGrid)
* Review system for completed bookings
* Coupons or discount logic
* Facebook Business integration
* Dynamic pricing per season

---

## 10. Credits

### Code & Docs

* Code Institute walkthroughs (base structure)
* Django Docs
* Stripe Docs
* Bootstrap Docs
* Stack Overflow (bugs)

### Media & Assets

* Pexels – Stock images
* Cloudinary – Image hosting
* Font Awesome – Icons
* Google Fonts – Montserrat
* Responsively – Screenshots

### Special Thanks

* Code Institute mentors & peers
* ChatGPT – Debugging support
* GitHub Discussions – Deployment help

---

© 2025 George Barh – RentMate Project
