# Git Fit
<!-- TODO: Add description of project: -->
Git Fit is a fitness subscription application.

The user's goal is to join a fitness community and purchase exercise plans and merchandise.

The site owner's goal is to build an active community around the product based on subscription and individual payments models, and to sell: exercise plans, nutrition plans, nutrition products and exercise products

Must haves for this project:
<!-- TODO: Must  haves -->
- Authentication and authorisation mechanism for subscribers and administrators
- Individual item purchase capability

Nice to have: 
<!-- TODO: nice to haves -->
- Functionality that allows subscribers to update fellow members on their successes, perhaps a forum?
- User proﬁles containing information that map to nutrition and/or exercise plans
- Product reviews
- A subscription-based payment model: on offer are 3 subscriptions, based on duration of subscription. Subscriptions get you access to workouts, nutrition plans, the community and a discount on the shop

To see the site in action, visit [Git Fit](https://code-institute-ms4.herokuapp.com/)

---

## UI and UX
 
### User stories
<!-- TODO: add screenshots -->
Not all User Stories have been completed. Basic shopping functionality has been completed, but user stories that are about the community side of the project have yet to be resolved.
  
**Viewing and Navigation**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 1 | Shopper | View a list of products | Select some to purchase | |
| ✔️ | 2 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes | |
| ✔️ | 3 | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase | |
| ✔️ | 4 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much | |
| ✔️ | 5 | Site User | Easily view the site on any device | Use the site whenever and wherever I'd like | |

**Registration and User Accounts**
| Done | User Story ID | As A/An   | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------  | :----------------------:| :---------------:| :---------:|
| ✔️ | 6 | Site User | Easily register for an account | Have a personal account and be able to view my profile | |
| ✔️ | 7 | Site User | Easily login or logout | Access my personal account information | |
| ✔️ | 8 | Site User | Easily recover my password in case I forget it | Recover access to my account | |
| ✔️ | 9 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful | |
| ✔️ | 10 | Site User | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information | |
| ❌ | 11 | Site User | Easily review products | Help my fellow fitness community members to find the right product | |

**Sorting and Searching**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| :✔️ | 12 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sorted products | |
| ✔️ | 13 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name | |
| ✔️ | 14 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as "clothing" or "exercise equipment" | |
| ✔️ | 15 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase | |
| ✔️ | 16 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available | |

**Purchasing and Checkout**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 17 | Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong quantity | |
| ✔️ | 18 | Shopper | View items in my cart to be purchased | Identify the total cost of my purchase and all items I will receive | |
| ✔️ | 19 | Shopper | Adjust the quantity of individual items in my cart | Easily make changes to my purchase before checkout | |
| ✔️ | 20 | Shopper | Easily enter my payment information  | Check out quickly and with no hassle | |
| ✔️ | 21 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | |
| ✔️ | 22 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes | |
| ✔️ | 23 | Shopper | Receive an email confirmation after checkout | Keep the confirmation of what I've purchased for my records | |

**Community**
| Done | User Story ID | As A/An      | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:-------------|:-----------------------:| :---------------:| :---------:|
| ❌ | 24 | Subscriber   | Post updates about my progress | Update my fellow members on my successes | |
| ❌ | 25 | Subscriber   | Add and edit information on my profile pertaining to my fitness goals | Receive nutrition and exercise plans tailored to my fitness goals | |
| ❌ | 26 | Subscriber   | Easily find other subscribers | Feel part of a community and get motivated | |
| ❌ | 27 | Subscriber   | Easily see updates from other subscribers | Feel part of a community and get motivated | |
| ❌ | 28 | Subscriber   | Easily find information about the subscriptions available | Make an informed choice about my subscription | |
| ❌ | 29 | Subscriber   | Easily find workouts | Work on my fitness goal | |
| ❌ | 30 | Subscriber   | Easily find nutrition plans | Work on my fitness goal | |


**Admin and Store Management**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 31 | Store Owner/Admin | Easily login or logout | Access the admin interface of the webapp | |
| ✔️ | 32 | Store Owner/Admin | Add a product | Add new items to my store | |
| ✔️ | 33 | Store Owner/Admin | Edit/update a product | Change product prices, descriptions, images and other product criteria | |
| ✔️ | 34 | Store Owner/Admin | Delete a product | Remove items that are no longer for sale | |
| ❌ | 35 | Store Owner/Admin | Add a subscription | Add new subscription options | |
| ❌ | 36 | Store Owner/Admin | Edit/update a subscription | Change subscription prices, descriptions, linked workouts and nutrition | |
| ❌ | 37 | Store Owner/Admin | Delete a subscription | Remove subscriptions that are no longer available | |
| ❌ | 38 | Store Owner/Admin | Add a workout | Add new workouts | |
| ❌ | 39 | Store Owner/Admin | Edit/update a workout | Change workouts | |
| ❌ | 40 | Store Owner/Admin | Delete a workout | Remove workouts that are no longer promoted | |
| ❌ | 41 | Store Owner/Admin | Add a nutrition plan | Add new nutrition plans | |
| ❌ | 42 | Store Owner/Admin | Edit/update a nutrition plan | Change nutrition plan | |
| ❌ | 43 | Store Owner/Admin | Delete a nutrition plan | Remove nutrition plans that are no longer promoted | |

---

### The 5 Planes of Design

Jesse James Garret's 5 planes of UX design were used to design the site. I started off at the Strategy Plane:

#### Strategy Plane
<!-- TODO: Write about Strategy Plane -->
The main goal for visitors is to find and join a fitness community they might like. This means giving visitors a feeling about the kind of community they are joining. Git Fit sets out to be no nonsense and active, aggressive almost. Git Fit is for goal-oriented people.
So the main page has to have a call to action in the form of a button to take you to subscriptions. We also need a hero image that exemplifies the image of Git Fit.
Some brief text to indicate what subscribers gain access to would also be good.
We also indicate that there is a shop and account option by having options for these in the navbar.

---

#### Scope Plane

The functional specifications of the site:
<!-- TODO: Write about Scope Plane -->
- a responsive website with mobile first design.
- a main page with a hero image, call to action (join our community) and navbar options indicating the shop and user account functionalities.
- a navbar which changes if a user is logged in or not.
- a footer.
- a profile page, only visible when logged in. Here members can set up their shopping details, but also personal details which map to exercise and nutrition plans.
- a page where subscribers can share their progress with other subscribers.
- a shop page, containing items for sale. Signed in users have the option to review items.
- a page containing exercises, only available for subscribers.
- a page containing nutrition plans, only available for subscribers.


Content requirements:
<!-- TODO: Write about content requirements -->
- a hero image evoking the idea of "active, aggressive, simplicity".
- some exercise and nutrition plans.
- some items for sale, with example reviews.
- some example subscribers.


---

#### Structure Plane
<!-- TODO: Structure Plane -->
All pages should have the same navigation bar and footer:

- the navigation bar contains links to all the pages, as well as the home page. The content does change depending on login status.
- the footer contains copyright info.

<ins>The Home Page</ins>
- a hero image evoking the idea of "active, aggressive, simplicity".
- a call to action to subscribe.

<ins>The Profile Page</ins>
- inspiring imagery.
- a form where subscribers can fill in their shopping details, but also personal details which map to exercise or nutrition.

<ins>The Community Page</ins>
- inspiring imagery.
- a form where subscribers can share their progress with fellow subscribers.

<ins>The Shop Page</ins>
- items for sale.
- the option to review items for signed in users.
- search functionality to search for items

<ins>The Exercise Page</ins>
- exercises for the subscriber to choose from.
- search functionality to search for exercises.

<ins>The Nutrition Page</ins>
- several nutrition plans to choose from.


---

#### Skeleton Plane
<!-- TODO: Skeleton Plane -->
The navigation bar will be added to the top of every page and will always remain visible. There are links to all pages on this navbar, though some links are only visible if the user has logged in. On the left will be the logo, which when clicked upon will take the visitor back to the home page.

The active page is indicated with a different font color for the navigation item. When hovering over navigation items, the navigation item will be highlighted.

At the bottom of every page will be the same footer.

---

#### Surface Plane
<!-- TODO: Surface Plane -->
We use icons from Font Awesome to add some visual interest but also visual cues to indicate functionality. We use Bootstrap as a basis, but add our own style. Git Fit needs to look no-nonsense, active, almost aggressive. We 


<ins>Wireframes</ins>
These wireframes were used as a basis to design the actual webapp. However, sometimes the actual project deviates from the wireframes, because the endresult looked better or was more easily achieved than the wireframe.
- [Home](readme-assets/media/home.png)
- [Home - tablet](readme-assets/media/home_tablet_view.png)
- [Home - mobile](readme-assets/media/home_mobile_view.png)
- [Shop](readme-assets/media/shop.png)
- [Shop - tablet](readme-assets/media/shop_tablet_view.png)
- [Shop - mobile](readme-assets/media/shop_mobile_view.png)
- [Product](readme-assets/media/product.png)
- [Product - tablet](readme-assets/media/product_tablet_view.png)
- [Product - mobile](readme-assets/media/product_mobile_view.png)
- [Product: add to cart](readme-assets/media/product_add-to-cart.png)
- [Cart](readme-assets/media/cart.png)
- [Cart - tablet](readme-assets/media/cart_tablet_view.png)
- [Cart - mobile](readme-assets/media/cart_mobile_view.png)
- [Checkout](readme-assets/media/checkout.png)
- [Checkout - tablet](readme-assets/media/checkout_tablet_view.png)
- [Checkout - mobile](readme-assets/media/checkout_mobile_view.png)
- [Checkout success](readme-assets/media/checkout_success.png)
- [Checkout success - tablet](readme-assets/media/checkout_success_tablet_view.png)
- [Checkout success - mobile](readme-assets/media/checkout_success_mobile_view.png)
- [Email confirmation](readme-assets/media/email_confirmation.png)
- [Profile](readme-assets/media/profile.png)
- [Profile - tablet](readme-assets/media/profile_tablet_view.png)
- [Profile - mobile](readme-assets/media/profile_mobile_view.png)
- [Login](readme-assets/media/login.png)
- [Login - tablet](readme-assets/media/login_tablet_view.png)
- [Login - mobile](readme-assets/media/login_mobile_view.png)
- [Forgot password](readme-assets/media/forgot_password.png)
- [Forgot password - tablet](readme-assets/media/forgot_password_tablet_view.png)
- [Forgot password - mobile](readme-assets/media/forgot_password_mobile_view.png)
- [Register](readme-assets/media/register.png)
- [Register - tablet](readme-assets/media/register_tablet_view.png)
- [Register - mobile](readme-assets/media/register_mobile_view.png)
- [Admin portal](readme-assets/media/admin_portal.png)

---

## Database Design
<!-- TODO: Database design -->
The database design can be found [here](https://dbdiagram.io/d/628bc76ff040f104c17efc98)


---

## Features

### Existing Features
<!-- TODO: Existing features -->
- the home page, with hero image, call to action, testimonials and features
- the navbar, with links to login and register hidden behind the "My Account" menu, a search bar, and various shopping links. Also has an icon representing the visitor's shopping cart, which updates when items are added.
- a shop page, where the user can sort products by for instance price and category, and can select products from different categories. 
- each product on the shop page links to a product details page, where users can find out more about the product, select a quantity and add it to their cart. This page also contains a breadcrumb and a category label, to allow quick navigation in the shop.
- a cart, accessible by clicking on the cart icon, where users can see the products in their cart, adjust the quantity, inspect a product's details and actually purchase the items
- a checkout page, where users can fill in their shipping details and creditcard information
- a checkout success page, where users get a confirmation of their order
- various user authentication pages: login, register and forget password. Also includes a profile page, where users can view and edit their delivery details and see their orders.


---

### Features Left to Implement
<!-- TODO: Features left to implement -->
- newsletter functionality, where visitors can sign up for the newsletter.
- giving customers the ability to choose the size of an item, where applicable
- related products functionality, showing related products when looking at product details
- subscriptions: giving registered users the option to sign up for, change and end their subscriptions
- the subscriber section, where subscribed users get access to exercises, nutrition plans and the community


---

## Technologies Used 
<!-- TODO: Technologies Used  -->
- [HTML5](https://en.wikipedia.org/wiki/HTML5): provides the content and structure of the site.
- [CSS3](https://en.wikipedia.org/wiki/CSS3): provides the formatting, layout and styling of the site.
- [Bootstrap](https://getbootstrap.com/): provides a popular CSS framework with many custom elements to quickly bootstrap a site. I've used Bootstrap 4.6.
- [Python3](https://www.python.org/): the backend of the webapp.
- [Selenium](https://selenium.dev/): software for automating and testing browser interactions. Used in this project to test functions of the webapp.
- [FontAwesome](https://fontawesome.com/): provides several icons I've used on the site.
- [Visual Studio Code](https://code.visualstudio.com/): a free IDE with enough features to be useful but not so many features as to confuse you.
- [GitHub](https://github.com): for hosting the git repository.
- [git](https://git-scm.com/): as one of the most popular source code management tools.
- [Heroku](https://heroku.com/): a Platform as a Service, for hosting the webapp.
- [Balsamiq](https://balsamiq.com): for creating wireframes of all the pages.
- [Chrome Developer Tools](https://developer.chrome.com/docs/devtools/): for quick debugging and testing of HTML and CSS. 
- [Am I Responsive?](https://ui.dev/amiresponsive): to generate screenshots of the site at various viewpoints, indicating responsiveness.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): an automated tool in Chrome DevTools that audits for performance, accessibility, progressive web apps, SEO and more.
- [Prettier VS Code plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): a code formatter that helps with code formatting, which is good for creating a consistent style.
- [Markdown link check](https://github.com/marketplace/actions/markdown-link-check): an automated tool to check for dead links in Markdown files.
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): to keep track of todos, bugs, things that need to be fixed and such in my project.
- [autopep8](https://pypi.org/project/autopep8/): a Python package that helps with formatting Python code according to PEP8.
- [dbdiagram.io](https://dbdiagram.io): an online tool to create a relational database schema.
- [Chromedriver](https://sites.google.com/chromium.org/driver/): for doing Chrome browser based automated tests


---

## Responsiveness of Pages
<!-- TODO: Responsiveness of Pages -->
These screenshots indicate the responsiveness of the pages on various screens. Pages that require a login are not included, as are checkout and checkout success, as these require adding items to the cart.
- [Home](readme-assets/media/home_responsive.png)
- [Products](readme-assets/media/products_responsive.png)
- [Product Details](readme-assets/media/product_details_responsive.png)
- [Cart](readme-assets/media/cart_responsive.png)
- [Login](readme-assets/media/login_responsive.png)
- [Register](readme-assets/media/register_responsive.png)
- [Forgot Password](readme-assets/media/forgot_password_responsive.png)


---

## Testing
<!-- TODO: Testing, either manual or automated -->
<!-- TODO: Look through Hello Django Github for tests -->
There are some unit tests using Django's own testing capabilities.

For the home app, tests can be found in home\tests.py:
`python manage.py test home.tests --verbosity=2
test_get_home (home.tests.TestViews) ... ok
test_get_login (home.tests.TestViews) ... ok
test_get_password_reset (home.tests.TestViews) ... ok
test_get_signup (home.tests.TestViews) ... ok`

Selenium tests for the home app:

The products app: products\test.py
`python manage.py test products.tests --verbosity=2
test_all_blank_product (products.tests.TestModels)
Test that when a product is created with no info, we get a ValidationError ... ok
test_all_blank_product_category (products.tests.TestModels)
Test that when a category is created with no info, we get a ValidationError ... ok
test_blank_description_product (products.tests.TestModels)
Test that when a product is created with no description, we get a ValidationError ... ok
test_blank_fields_product (products.tests.TestModels)
Test that when a product is created, category, sku, rating, image_url and image are blank ... ok
test_blank_name_product (products.tests.TestModels)
Test that when a product is created with no name, we get a ValidationError ... ok
test_blank_price_product (products.tests.TestModels)
Test that when a product is created with no price, we get a ValidationError ... ok
test_delete_category_of_product (products.tests.TestModels)
Test that when a category is deleted for a product, the category field on the product is emptied ... ok
test_friendly_name_blank_product_category (products.tests.TestModels)
Test that when a category is created, friendly name is blank ... ok
test_max_length_image_url_product (products.tests.TestModels)
Test that when a product is created with an image_url longer than 1024 characters, we get a ValidationError ... ok
test_max_length_name_product (products.tests.TestModels)
Test that when a product is created with a name longer than 254 characters, we get a ValidationError ... ok
test_max_length_name_product_category (products.tests.TestModels)
Test that when a category is created with a name longer than 254 characters, we get a ValidationError ... ok
test_max_length_price_product (products.tests.TestModels)
Test that when a product is created with a price longer than 6 characters, we get a ValidationError ... ok
test_max_length_rating_product (products.tests.TestModels)
Test that when a product is created with a rating longer than 6 characters, we get a ValidationError ... ok
test_max_length_sku_product (products.tests.TestModels)
Test that when a product is created with a sku longer than 254 characters, we get a ValidationError ... ok`




<ins>Code validation:</ins> 
<!-- TODO: Code validation: -->

1. [HTML validation](https://validator.w3.org/nu/)
<!-- TODO: HTML validation -->




2. [CSS validation](https://jigsaw.w3.org/css-validator/)
<!-- TODO: CSS validation -->



3. [Python Validation](http://pep8online.com/)
<!-- TODO: Python Validation:  -->
python3 -m flake8 # outputs linting problems to the console




### Notable Bugs
<!-- TODO: Notable Bugs -->
One big bug was with the checkout process not working: after clicking on the checkout button, the loading spinner would appear, but would never progress to the checkout success page.
To try and fix this bug I took the following steps:
1. Check if all the Stripe keys and secrets were correct
1. Check if the environment vars were using the correct Stripe information.
1. Go through the code for the checkout app: changed some variable names and fixed a typo where a dash was used instead of an underscore.
1. urls.py was missing the / after checkout_success/<order_number>, fixed that.
1. After changing variable names, I had to do another database migration.
2. After this, when trying to checkout, I could an error about adding a float and decimal together: fixed this as well.
3. It still wasn't working, and I found out the problem was within stripe_elements.js: when I changed code in there, checkout would work.
4. I was about to start working through the code using console.log when I noticed an error in the log: it couldn't parse $post. This piece of code should have been $.post, missing a period. After adding that, the code worked.


### Problems
<!-- TODO: Problems -->
The only real problem was the implementation of Stripe. Getting this up and running took a lot of time, which meant I did not have time to implement other features. Right now, the project is a basic webshop, but not yet the community it sets out to be.

---

## Deployment
<!-- TODO: Deployment -->
The project has been deployed to Heroku, with static files hosted on AWS S3. If  you want to do the same:
1. Fork the repository to your own GitHub: https://github.com/RicardoAzuul/code-institute-ms4-fullstack.
1. Log in to Heroku (www.heroku.com) - or register if you don't have an account yet.
1. In the Heroku dashboard, click the New button in the top right corner and create a new app.
1. Give your new app a name and choose a region. The name has to be unique within Heroku.
1. On the page for your new Heroku app, go to Deployment method and choose "Connect to GitHub". If you haven't connected your GitHub account to Heroku yet, you will be able to do so now.
1. Choose the forked repository of this project from your own GitHub account.
1. If you want, you can enable Automatic Deploys here: whenever you perform a push to your GitHub repository, the Heroku app can redeploy. Otherwise you can deploy manually. Heroku will use the PROCFILE and requirements.txt to install dependencies and build the app.
1. You will also have to set some Config Vars in the Settings section of your Heroku app. These are the Config Vars:
   1. AWS_ACCESS_KEY_ID: the id for your AWS S3 container
   1. AWS_SECRET_ACCESS_KEY: the secret key for your AWS S3 container
   1. DATABASE_URL: the url to the postgress database on Heroku
   1. EMAIL_HOST_PASS: the password or application key for the email account you use for emailing. This project uses Gmail
   1. EMAIL_HOST_USER: the emailadress
   1. SECRET_KEY: the Django secret key
   1. STRIPE_PUBLIC_KEY: Your Stripe public key
   1. STRIPE_SECRET_KEY: Your stripe secret key
   1. STRIPE_WH_SECRET: Your Stripe webhook secret
   1. USE_AWS: Set to true to tell Django to use the other AWS settings


### Run locally
<!-- TODO: Run locally -->
If you want to run the project locally:
1. First, fork the repository to your own GitHub: https://github.com/RicardoAzuul/code-institute-ms4-fullstack.
1. Clone the forked repository to your own machine.
1. Install Python 3.8.12, as this is what the project was built with: https://www.python.org/downloads/release/python-3812/ (though if you're running Windows, install 3.8.10)
1. From the terminal, run the below to install required modules:
  ``` pip3 install -r requirements.txt ```
1. You will need to create an env.py file for running the app locally. The content of this file:
```
import os

os.environ.setdefault("SECRET_KEY", [django secret key])
os.environ.setdefault("DEVELOPMENT", "True")
os.environ.setdefault("STRIPE_PUBLIC_KEY", "[stripe public key]") 
os.environ.setdefault("STRIPE_SECRET_KEY", "[stripe secret key]") 
os.environ.setdefault("STRIPE_WH_SECRET ", "[stripe webhook key]") 

```
1. To run the app:
   
   ``` python manage.py startserver ```

1. This will run the app locally, you can then browse to http://192.168.1.68:5000/ to interact with the app.



---

## Credits

### Inspiration
<!-- TODO: Inspiration -->
The color scheme, black with accents of white and red, was inspired by Netflix: it looks bold. For the font I did some research into bold aggressive font types and came upon slab serif fonts. I picked Kelly Slab, as it was available via Google Fonts.
Initially I wanted to do something different and go for warm and friendly, but I did not like the color scheme and couldn't find suitable images.



### Content
<!-- TODO: Add where I got the Content -->
Product images, prices, descriptions and ratings: www.decathon.nl


### Media
<!-- TODO: Add where I got the Media -->
Main page: https://www.pexels.com/photo/woman-doing-exercise-414029/
No image available file: https://commons.wikimedia.org/wiki/File:No_Image_Available.jpg


### Code
<!-- TODO: Add where I got the Code, if using other people's code -->


### Acknowledgements

- I received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). 
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, [Django](https://www.djangoproject.com/) for their documentation and [Stackoverflow](https://stackoverflow.com/) for helping with finding solutions to coding problems.
- My wife, Elizabeth Lane, for supporting me during this coding course.

# TODOS
<!-- TODO: database migrations -->
Set the database url hardcoded in the project so you can do migrations.


<!-- TODO: media migrations -->
Upload by hand using Upload functionality of AWS

<!-- TODO: Fix bug with product details -->

<!-- TODO:Rename project: https://stackoverflow.com/questions/18293875/easy-way-to-rename-a-django-project -->

<!-- TODO:Add to Heroku: see https://dashboard.heroku.com/apps/ricardoazuul-boutique-ado/settings --> 
STRIPE_PUBLIC_KEY
STRIPE_SECRET_KEY
STRIPE_WH_SECRET

<!-- TODO:Go through Stripe and copy settings --> 



<!-- TODO: Datasets: --> 
https://www.kaggle.com/datasets/edoardoba/fitness-exercises-with-animations
https://www.kaggle.com/datasets/afsaja/workout-supplements-and-nutrition-products

<!-- TODO: Django newsletter: --> 

<!-- TODO: Add margin-bottom to containers?: --> 
