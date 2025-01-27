# Real Honey

## 1. Key Project Information

**Description:**  
Real Honey is a user-friendly and scalable online marketplace that connects local beekeepers with customers, allowing them to purchase honey directly from producers. The platform offers a wide selection of honey products, categorized by the types of vegetation and flowers from which the nectar is sourced. This unique selection enables customers to explore different flavors of honey, each representing the distinctive characteristics of the region's flora.

**Key Goal:**  
To provide a seamless and enjoyable shopping experience for customers while supporting local beekeepers by offering a variety of honey options with unique flavor profiles.

**Target Audience:**  
Individuals who are health-conscious and interested in authentic, high-quality honey products, including those who appreciate sustainable and locally sourced goods.

**Live Version:**  
[Live Site URL]

**Dummy Card:**  
4242 4242 4242 4242, expiry 04/24, cvc 242, zip 42424

**Developer:**  
[Your Name]

---

## 2. Table of Contents

1. Key Project Information  
2. Table of Contents  
3. User Experience (UX)  
4. Features  
5. Marketing  
6. Validation, Testing & Bugs  
7. Deployment  
8. Technologies & Credits  
9. Handling Product Images

---

## 3. User Experience (UX)

### 3.1 The Strategy Plane

#### 3.1.1 The Idea
To create an e-commerce platform that offers locally sourced honey with a focus on authenticity, flavor variety, and sustainability.

#### 3.1.2 The Ideal User
- Health-conscious individuals
- Those who prefer locally sourced products
- People interested in unique honey flavors
- Online shoppers seeking convenience
- Customers who appreciate transparency and ethical sourcing

#### 3.1.3 Site Goals
- Offer an extensive selection of honey varieties
- Provide detailed information about each product and beekeeper
- Ensure a secure and convenient purchasing process
- Implement marketing strategies to attract and retain customers

#### 3.1.4 Epics and User Stories
[Link to Epics and User Stories Documentation]

### 3.2 The Scope Plane
#### 3.2.1 Features to be implemented
- **Product Listings & Categorization:** Detailed descriptions, images, prices, and sizes categorized by type (wildflower, clover, orange blossom, etc.).
- **Sorting and Filtering:** Customers can sort by price, rating, and flavor type.
- **Cart and Checkout:** Secure payment integration via Stripe.
- **User Authentication:** Register, log in, and manage profiles.
- **SEO and Marketing:** Social media integration and email sign-ups.
- **Local Beekeepers:** Story sections on each product page.
- **Responsive Design:** Optimized for all devices.

### 3.3 The Structure Plane
- Site Map
- Database Schema

### 3.4 Wireframes
[Link to Wireframes]

### 3.5 The Surface Plane
- Logo
- Color Palette
- Fonts
- Icons and Images

---

## 4. Features

### 4.1 Core Features
- Header with navigation
- Footer with contact info
- Wishlist management
- Order history
- Search functionality
- Notifications (on-screen and email)

### 4.2 Pages
- Landing Page
- Shop Page
- Item Detail Page
- Checkout Page
- Profile Management

### 4.3 Future Features
- Order tracking
- Product recommendations
- User review system
- Media file uploads: Using 'pillow' for dynamic image uploads via admin. 

---

## 5. Marketing

### 5.1 Social Media Presence
- Facebook and Instagram pages to promote local honey products.

### 5.2 Search Engine Optimization (SEO)
- SEO-friendly URLs, meta tags, and clear sitemaps for search engines.
- Social media sharing buttons on each product page.
- Email marketing campaigns and special promotions.

---

## 6. Validation, Testing & Bugs

### 6.1 Validation
- HTML/CSS validation
- Accessibility tests

### 6.2 Testing
- Manual and automated testing

### 6.3 Bugs
[Link to Bug Report]

---

## 7. Deployment

### 7.1 Deployment Steps
1. Transfer progress from IDE to GitHub
2. Offline cloning for local testing
3. Deployment to cloud platforms (Heroku, AWS, etc.)

### 7.2 Deployment Prerequisites
- Email Configuration
- Database Setup
- Cloud Storage Configuration
- Payment Gateway Integration

---

## 8. Technologies & Credits

### 8.1 Technologies Used
- Django
- Python
- HTML/CSS
- JavaScript
- Bootstrap
- PostgreSQL
- AWS
- Stripe

### 8.2 Credits
- [Contributor 1]
- [Contributor 2]
- FreePik (Images)
- Bootstrap Icons (Icons)

---

## 9. Handling Product Images in Real Honey Project

### Using Static Files for Images (Current Setup)

Currently, product images are manually stored in the `static/images/` directory and referenced directly in templates.

#### How to Add Product Images:
1. Place product images inside the `static/images/` folder.
2. Reference them in templates like this:

   ```django
   <img src="{% static 'images/honey-jar.jpg' %}" alt="Honey Jar">
   ```
