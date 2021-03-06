# Git Fit
Git Fit is a fitness subscription application.

The user's goal is to join a fitness community and purchase exercise plans and merchandise.

The site owner's goal is to build an active community around the product based on subscription and individual payments models, and to sell: exercise plans, nutrition plans, nutrition products and exercise products

Must haves for this project:
- Authentication and authorisation mechanism for users and administrators
- Individual item purchase capability

Nice to have: 
- Functionality that allows subscribers to update fellow members on their successes, perhaps a forum?
- User proﬁles containing information that map to nutrition and/or exercise plans
- Product reviews
- A subscription-based payment model: on offer are 3 subscriptions, based on duration of subscription. Subscriptions get you access to workouts, nutrition plans, the community and a discount on the shop

To see the site in action, visit [Git Fit](https://code-institute-ms4.herokuapp.com/)

Initially I wanted to name the project Fit Family, and create a more family oriented webapp, but I didn't like the colour palette and couldn't find suitable images. Leftovers from this are still present in the code, but it doesn't affect the webapp.

---

## UI and UX
 
### User stories
Not all User Stories have been completed. Basic shopping functionality has been completed, but user stories that are about the community side of the project have yet to be resolved.


**Viewing and Navigation**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 1 | Shopper | View a list of products | Select some to purchase | [Products](readme-assets/media/user_story_1.png) |
| ✔️ | 2 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes | [Product details](readme-assets/media/user_story_2.png) |
| ✔️ | 3 | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase | [Deals](readme-assets/media/user_story_3.png) |
| ✔️ | 4 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much | [Cart](readme-assets/media/user_story_4.png) |
| ✔️ | 5 | Site User | Easily view the site on any device | Use the site whenever and wherever I'd like | See the Responsiveness of Pages section  |

**Registration and User Accounts**
| Done | User Story ID | As A/An   | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------  | :----------------------:| :---------------:| :---------:|
| ✔️ | 6 | Site User | Easily register for an account | Have a personal account and be able to view my profile | [Register](readme-assets/media/user_story_6.png) |
| ✔️ | 7 | Site User | Easily login or logout | Access my personal account information | [Login](readme-assets/media/user_story_7.png) |
| ✔️ | 8 | Site User | Easily recover my password in case I forget it | Recover access to my account | [Recover](readme-assets/media/user_story_8.png) |
| ✔️ | 9 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful | [Registration](readme-assets/media/user_story_9.png) |
| ✔️ | 10 | Site User | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information | [Profile](readme-assets/media/user_story_10.png) |
| ❌ | 11 | Site User | Easily review products | Help my fellow fitness community members to find the right product | |

**Sorting and Searching**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 12 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sorted products | [Sort](readme-assets/media/user_story_12.png) |
| ✔️ | 13 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name | [Category](readme-assets/media/user_story_13.png) |
| ✔️ | 14 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as "clothing" or "exercise equipment" | [Multi Category](readme-assets/media/user_story_14.png) |
| ✔️ | 15 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase | [Search](readme-assets/media/user_story_15.png) |
| ✔️ | 16 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available | Screenshot for user story 15 works here too |

**Purchasing and Checkout**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 17 | Shopper | Easily select the quantity of a product when purchasing it | Ensure I don't accidentally select the wrong quantity | [Screenshot user story 2](readme-assets/media/user_story_2.png) |
| ✔️ | 18 | Shopper | View items in my cart to be purchased | Identify the total cost of my purchase and all items I will receive | [Screenshot user story 4](readme-assets/media/user_story_4.png) |
| ✔️ | 19 | Shopper | Adjust the quantity of individual items in my cart | Easily make changes to my purchase before checkout | Same as above |
| ✔️ | 20 | Shopper | Easily enter my payment information  | Check out quickly and with no hassle | [Checkout](readme-assets/media/user_story_20.png) |
| ✔️ | 21 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase | Same as above |
| ✔️ | 22 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes | [Confirmation](readme-assets/media/user_story_22.png) |
| ✔️ | 23 | Shopper | Receive an email confirmation after checkout | Keep the confirmation of what I've purchased for my records | [Email](readme-assets/media/user_story_23.png) |

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
| ✔️ | 31 | Store Owner/Admin | Easily login or logout | Access the admin interface of the webapp | [Admin](readme-assets/media/user_story_31.png) |
| ✔️ | 32 | Store Owner/Admin | Add a product | Add new items to my store | [Add Product](readme-assets/media/user_story_32.png) |
| ✔️ | 33 | Store Owner/Admin | Edit/update a product | Change product prices, descriptions, images and other product criteria | [Edit Product](readme-assets/media/user_story_33.png) |
| ✔️ | 34 | Store Owner/Admin | Delete a product | Remove items that are no longer for sale | [Delete Product](readme-assets/media/user_story_34.png) |
| ❌ | 35 | Store Owner/Admin | Add a subscription | Add new subscription options | |
| ❌ | 36 | Store Owner/Admin | Edit/update a subscription | Change subscription prices, descriptions, linked workouts and nutrition | |
| ❌ | 37 | Store Owner/Admin | Delete a subscription | Remove subscriptions that are no longer available | |
| ✔️ | 38 | Store Owner/Admin | Add a workout | Add new workouts | [Add Workout](readme-assets/media/user_story_38.png) |
| ✔️ | 39 | Store Owner/Admin | Edit/update a workout | Change workouts | [Edit Workout](readme-assets/media/user_story_39.png) |
| ✔️ | 40 | Store Owner/Admin | Delete a workout | Remove workouts that are no longer promoted | [Delete Workout](readme-assets/media/user_story_40.png) |
| ❌ | 41 | Store Owner/Admin | Add a nutrition plan | Add new nutrition plans | |
| ❌ | 42 | Store Owner/Admin | Edit/update a nutrition plan | Change nutrition plan | |
| ❌ | 43 | Store Owner/Admin | Delete a nutrition plan | Remove nutrition plans that are no longer promoted | |
| ✔️ | 44 | Store Owner/Admin | Add subscription features to the home page | To entice visitors to subscribe | [Add Feature](readme-assets/media/user_story_44.png) |
| ✔️ | 45 | Store Owner/Admin | Edit subscription features visible on the home page | To tweak the features and entice visitors to subscribe | [Edit Feature](readme-assets/media/user_story_45.png) |
| ✔️ | 46 | Store Owner/Admin | Delete subscription features visible on the home page | To remove features that are no longer offered  | Same as above |
| ✔️ | 47 | Store Owner/Admin | Add shop alerts to the products page | To update the shop and make visitors aware of for example new deals | [Add Shop Alert](readme-assets/media/user_story_47.png) |
| ✔️ | 48 | Store Owner/Admin | Edit shop alerts visible on the products page | To change shop alerts | [Edit Shop Alert](readme-assets/media/user_story_48.png)  |
| ✔️ | 49 | Store Owner/Admin | Delete shop alerts visible on the products page | To remove shop alerts that are no longer applicable  | Same as above |

**Viewing and Navigation - Workouts**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 50 | Registered User | View a list of workouts | Select workouts to do | [Workouts](readme-assets/media/user_story_50.png)  |
| ✔️ | 51 | Registered User | View individual workout details | Identify the description, rating, equipment needed and what the workout targets | [Workout Details](readme-assets/media/user_story_51.png)  |

**Sorting and Searching - Workouts**
| Done | User Story ID | As A/An | I Want To Be Able To... | So That I Can... | Screenshot |
| :---:| :-------------|:--------| :----------------------:| :---------------:| :---------:|
| ✔️ | 52 | Registered User | Sort the list of available workouts | Easily identify the best rated, categorically sorted workouts | [Sort](readme-assets/media/user_story_52.png)  |
| ✔️ | 53 | Registered User | Sort a specific category of workout | Find the best-rated workout in a specific category, or sort the workouts in that category by name | [Category](readme-assets/media/user_story_53.png)  |


---

### The 5 Planes of Design

Jesse James Garret's 5 planes of UX design were used to design the site. I started off at the Strategy Plane:

#### Strategy Plane
The main goal for visitors is to find and join a fitness community they might like.

This means giving visitors a feeling about the kind of community they are joining. 

Git Fit sets out to be no nonsense and active, aggressive almost. Git Fit is for goal-oriented people. For now it is just a shop, but by adding subscriptions, we can create a community, with exercise and nutrition plans and a way for subscribers to connect.

So the main page has to have a call to action in the form of a button to take you to subscriptions. We also need a hero image that exemplifies the image of Git Fit.
Some brief text to indicate what subscribers gain access to would also be good.

We also indicate that there is a shop, workouts and account option by having options for these in the navbar.

---

#### Scope Plane

The functional specifications of the site:
- a responsive website with mobile first design.
- a main page with a hero image, call to action (join our community) and navbar options indicating the shop and user account functionalities.
- a navbar with menus that if a user is logged in or not.
- a footer.
- a profile page, only accessible when logged in. Here members can set up their shopping details, but also personal details which map to exercise and nutrition plans.
- a page where subscribers can share their progress with other subscribers - not yet implemented.
- a shop page, containing items for sale. Signed in users have the option to review items (not yet implemented).
- a page containing exercises, only available for subscribers - not yet implemented.
- a page containing nutrition plans, only available for subscribers - not yet implemented.


Content requirements:
- a hero image evoking the idea of "active, aggressive, simplicity".
- some exercise and nutrition plans - not yet implemented.
- some items for sale.
- some example subscribers - not yet implemented.


---

#### Structure Plane
All pages should have the same navigation bar and footer:

- the navigation bar contains links to all the pages, as well as the home page. The content does change depending on login status.
- the footer contains the company logo, icons for various creditcards and links to social media pages.

<ins>The Home Page</ins>
- a hero image evoking the idea of "active, aggressive, simplicity".
- a call to action to subscribe.
- features that indicate the benefits of subscribing. Admins can change these features using the admin portal.

<ins>The Profile Page</ins>
- a form where subscribers can fill in their shopping details, but also personal details which map to exercise or nutrition (not yet implemented).

<ins>The Community Page - not yet implemented</ins>
- inspiring imagery.
- a form where subscribers can share their progress with fellow subscribers.

<ins>The Shop Page</ins>
- items for sale.
- shop alerts, to make visitors aware of deals for instance. Admins can change these alerts using the admin portal.
- the option to review items for signed in users (not yet implemented).
- search functionality to search for items

<ins>The Workouts Page </ins>
- exercises for the subscriber to choose from.
- search functionality to search for exercises: not yet implemented.

<ins>The Nutrition Page - not yet implemented</ins>
- several nutrition plans to choose from.


---

#### Skeleton Plane
The navigation bar will be added to the top of every page and will always remain visible. It contains a home link on the left side, a search bar for searching in the store in the middle, an icon containing the workout options, an icon containing the account options - register and login, and if you're logged in a link to your profile, and if you're a superuser, a link to add a product.

There is also a cart icon, which updates when you add items to your cart and which links to the cart page, from where you can do checkouts.

There are links to all pages on this navbar, though some links are only visible if the user has logged in. On the left will be the logo, which when clicked upon will take the visitor back to the home page.

The home page has a hero image, a call to action to register, a button to take you to the shop and features of subscriptions.

The shopping page has cards for the products. You can choose different categories of products, sort by price and category and rating and click on a product to get more information and add it to your cart.

The cart page keeps track of the items you've added to your cart, giving you a running total and the option to check out.

The checkout page allows you to fill in shipping details and a creditcard for payment.

The checkout success page contains a summary of your order and order details.

The profile page contains a form to fill in delivery details or show prefilled delivery details, and has links to the order history for registered users.

The workouts page has cards for different workouts. You can choose workouts by body part they target, equipment needed or specific muscle groups they target. You can click on a workout to get more information about it.

At the bottom of every page will be the same footer, containing the brand, icons of various payment methods and links to various social media sites.

---

#### Surface Plane
We use icons from Font Awesome to add some visual interest but also visual cues to indicate functionality. 

We use Bootstrap as a basis, but add our own style. Git Fit needs to look no-nonsense, active, almost aggressive. To create a bold, active, almost aggressive look we use a black, red and white color scheme, similar to Netflix.

The header font is also chosen to reflect this: a slab serif font that is bold and in your face.

Buttons have no rounded borders, to create a sleek design. Red is mainly used as an accent color, to draw attention to elements on the page.


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

The layout of the workouts section is very similar to the shop and product pages, just with some slight change in details.

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

The database design can be found [here](https://dbdiagram.io/d/628bc76ff040f104c17efc98)
There are 11 models:
1. Profiles
2. Orders
3. Order Line Items
4. Products
5. Product Categories (only editable via admin portal)
6. Workouts
7. BodyParts (linked to Workouts, only editable via admin portal)
8. Equipment (linked to Workouts, only editable via admin portal)
9. Targets (linked to Workouts, only editable via admin portal)
10. Features (only editable via admin portal)
11. ShopAlerts (only editable via admin portal)

The Profiles model is linked to the allauth User model, but I don't know how this model is constructed.

---

## Features

### Existing Features
- the home page, with hero image, call to action and features
- the navbar, with links to login and register hidden behind the "My Account" menu, a search bar, and various shopping links. Also has an icon representing the visitor's shopping cart, which updates when items are added.
- a shop page, where the user can sort products by for instance price and category, and can select products from different categories. 
- each product on the shop page links to a product details page, where users can find out more about the product, select a quantity and add it to their cart. This page also contains a breadcrumb and a category label, to allow quick navigation in the shop.
- a cart, accessible by clicking on the cart icon, where users can see the products in their cart, adjust the quantity, inspect a product's details and actually purchase the items
- a checkout page, where users can fill in their shipping details and creditcard information
- a checkout success page, where users get a confirmation of their order
- various user authentication pages: login, register and forget password. Also includes a profile page, where users can view and edit their delivery details and see their orders.
- a workout page, where the user can sort workouts by for instance rating and category, and can select workouts from different categories. 
- each workout on the workouts page links to a workout details page, where users can find out more about the workout. This page also contains a breadcrumb and a category label, to allow quick navigation in the workouts page.

---

### Features Left to Implement
- newsletter functionality, where visitors can sign up for the newsletter.
- giving customers the ability to choose the size of an item, where applicable
- related products functionality, showing related products when looking at product details
- subscriptions: giving registered users the option to sign up for, change and end their subscriptions
- the subscriber section, where subscribed users get access to exercises, nutrition plans and the community
- the option for subscribers to review products
- allowing subscribers to favorite workouts


---

## Technologies Used 
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
- [Prettier VS Code plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): a code formatter that helps with code formatting, which is good for creating a consistent style.
- [Markdown link check](https://github.com/marketplace/actions/markdown-link-check): an automated tool to check for dead links in Markdown files.
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): to keep track of todos, bugs, things that need to be fixed and such in my project.
- [autopep8](https://pypi.org/project/autopep8/): a Python package that helps with formatting Python code according to PEP8.
- [dbdiagram.io](https://dbdiagram.io): an online tool to create a relational database schema.
- [Chromedriver](https://sites.google.com/chromium.org/driver/): for doing Chrome browser based automated tests
- [Django](https://www.djangoproject.com/): the Python framework that helped to quickly bootstrap the project.
- [black](https://pypi.org/project/black/): a Python package that helps with formatting Python code according to PEP8.


---

## Responsiveness of Pages
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

<ins>Tests for Readme.md:</ins>
- :heavy_check_mark: A Github Action Workflow checks all the links in markdown files. There are some errors in here, but these are acceptable: 1 is for the locally running server, the other two are for websites that have received too many requests from this Github Action Workflow 

<ins>Automated tests</ins>

There are some automated tests using Django's own testing capabilities.
```python manage.py test --verbosity=2```

Output:
```
test_get_cart (cart.tests.TestViews)
When browsing to /cart/ we get ... ok
test_blank_feature (home.tests.TestModels)
When a feature is created with no ... ok
test_max_length_name_feature (home.tests.TestModels)
When a feature is created with a header longer than ... ok
test_get_home (home.tests.TestViews)
When browsing to / we get a 200 code, ... ok
test_get_login (home.tests.TestViews)
When browsing to /accounts/login we ... ok
test_get_password_reset (home.tests.TestViews)
When browsing to /accounts/password/reset ... ok
test_get_signup (home.tests.TestViews)
When browsing to /accounts/signup we ... ok
test_all_blank_product_category (products.tests.TestModels)
When a category is created with no ... ok
test_blank_description_product (products.tests.TestModels)
When a product is created with no description, ... ok
test_blank_fields_product (products.tests.TestModels)
When a product is created, category, sku, ... ok
test_blank_name_product (products.tests.TestModels)
When a product is created with no name, ... ok
test_blank_price_product (products.tests.TestModels)
When a product is created with no price, ... ok
test_blank_shopalert (products.tests.TestModels)
When a shopalert is created with no ... ok
test_friendly_name_blank_product_category (products.tests.TestModels)
When a category is created, friendly name is blank ... ok
test_max_length_image_url_product (products.tests.TestModels)
When a product is created with an image_url ... ok
test_max_length_name_product (products.tests.TestModels)
When a product is created with a name ... ok
test_max_length_name_product_category (products.tests.TestModels)
When a category is created with a name longer than ... ok
test_max_length_name_shopalert (products.tests.TestModels)
When a shopalert is created with a name longer than ... ok
test_max_length_sku_product (products.tests.TestModels)
When a product is created with a sku ... ok
test_delete_category_of_product (products.tests.TestViews)
When a category is deleted for a product, ... ok
test_all_blank_bodypart (workouts.tests.TestModels)
When a bodypart is created with no ... ok
test_all_blank_equipment (workouts.tests.TestModels)
When a equipment is created with no ... ok
test_all_blank_target (workouts.tests.TestModels)
When a target is created with no ... ok
test_blank_description_workout (workouts.tests.TestModels)
When a workout is created with no description, ... ok
test_blank_fields_workout (workouts.tests.TestModels)
When a workout is created, bodypart, equipment, ... ok
test_blank_image_workout (workouts.tests.TestModels)
When a workout is created with no image, ... ok
test_blank_name_workout (workouts.tests.TestModels)
When a workout is created with no name, ... ok
test_delete_fields_of_workout (workouts.tests.TestModels)
When the bodypart, equipment and target objects are deleted for a workout, ... ok
test_friendly_name_blank_bodypart (workouts.tests.TestModels)
When a bodypart is created, friendly name is blank ... ok
test_friendly_name_blank_equipment (workouts.tests.TestModels)
When a equipment is created, friendly name is blank ... ok
test_friendly_name_blank_target (workouts.tests.TestModels)
When a target is created, friendly name is blank ... ok
test_max_length_name_bodypart (workouts.tests.TestModels)
When a bodypart is created with a name longer than ... ok
test_max_length_name_equipment (workouts.tests.TestModels)
When a equipment is created with a name longer than ... ok
test_max_length_name_target (workouts.tests.TestModels)
When a target is created with a name longer than ... ok
test_max_length_name_workout (workouts.tests.TestModels)
When a workout is created with a name ... ok
test_get_workouts (workouts.tests.TestViews)
When browsing to /workouts/ we get a 302 code, ... ok
```

Coverage report:
```coverage run --source='.' manage.py test```
Name                                    Stmts   Miss  Cover
-----------------------------------------------------------
cart\__init__.py                            0      0   100%
cart\apps.py                                4      0   100%
cart\contexts.py                           24      7    71%
cart\migrations\__init__.py                 0      0   100%
cart\templatetags\__init__.py               0      0   100%
cart\templatetags\cart_tools.py             5      1    80%
cart\tests.py                               6      0   100%
cart\urls.py                                3      0   100%
cart\views.py                              40     31    22%
checkout\__init__.py                        1      0   100%
checkout\admin.py                          12      0   100%
checkout\apps.py                            6      0   100%
checkout\forms.py                          18     11    39%
checkout\migrations\0001_initial.py         7      0   100%
checkout\migrations\__init__.py             0      0   100%
checkout\models.py                         51     14    73%
checkout\signals.py                         9      2    78%
checkout\urls.py                            4      0   100%
checkout\views.py                          86     70    19%
checkout\webhook_handler.py                71     56    21%
checkout\webhooks.py                       28     19    32%
custom_storages.py                          6      6     0%
env.py                                      6      0   100%
fit_family\__init__.py                      0      0   100%
fit_family\asgi.py                          4      4     0%
fit_family\settings.py                     68     20    71%
fit_family\urls.py                          5      0   100%
fit_family\wsgi.py                          4      4     0%
home\__init__.py                            0      0   100%
home\admin.py                               6      0   100%
home\apps.py                                4      0   100%
home\migrations\0001_initial.py             5      0   100%
home\migrations\__init__.py                 0      0   100%
home\models.py                              4      0   100%
home\tests.py                              31      0   100%
home\urls.py                                3      0   100%
home\views.py                               6      0   100%
manage.py                                  12      2    83%
products\__init__.py                        0      0   100%
products\admin.py                          14      0   100%
products\apps.py                            4      0   100%
products\forms.py                          15      6    60%
products\migrations\0001_initial.py         6      0   100%
products\migrations\0002_shopalert.py       4      0   100%
products\migrations\__init__.py             0      0   100%
products\models.py                         26      3    88%
products\tests.py                          70      1    99%
products\urls.py                            3      0   100%
products\views.py                          92     77    16%
products\widgets.py                         7      0   100%
profiles\__init__.py                        0      0   100%
profiles\apps.py                            4      0   100%
profiles\forms.py                          18     11    39%
profiles\migrations\0001_initial.py         8      0   100%
profiles\migrations\__init__.py             0      0   100%
profiles\models.py                         21      4    81%
profiles\urls.py                            3      0   100%
profiles\views.py                          26     17    35%
workouts\__init__.py                        0      0   100%
workouts\admin.py                          18      0   100%
workouts\apps.py                            4      0   100%
workouts\forms.py                          25     16    36%
workouts\migrations\0001_initial.py         6      0   100%
workouts\migrations\__init__.py             0      0   100%
workouts\models.py                         37      7    81%
workouts\tests.py                          86      0   100%
workouts\urls.py                            3      0   100%
workouts\views.py                          95     79    17%
workouts\widgets.py                         7      0   100%
-----------------------------------------------------------
TOTAL                                    1141    468    59%


<ins>Manual tests</ins>
The webapp has been tested with Google Chrome, Firefox and Microsoft Edge, and on a Huawei P smart+ 2019 Android smartphone and found to be working fine.
Below are more elaborate tests:



**Viewing and Navigation**
| Test | Expected | Passed |
| :--: | :------: | :----: |
| Browsing to the home page as an anonymous user | I see a call to action to sign up, as well as several features that signing up will get me | ✔️ |
| Browsing to the home page as a logged in user | I just see the hero image and the 'Buy' button | ✔️ |
| Clicking on the social media links as either an anonymous user or logged in user | A new tab opens going to that social media page | ✔️ |
| Clicking on the navbar brand as either an anonymous user or logged in user | I go back to the home page | ✔️ |
| Clicking on the 'Buy' button as either an anonymous user or logged in user | I go to the products page and see a list of products | ✔️ |
| Clicking on the 'Register' button as an anonymous user | I go to the register page and see a form to register for an account | ✔️ |
| Clicking on the 'Workouts' button as an anonymous user | I see options to either register or login, which take me to either a register or login page | ✔️ |
| Clicking on the 'Workouts' button as logged in user | I see links to view all workouts, including workouts sorted in different ways | ✔️ |
| Clicking on the links under the 'Workouts' button as logged in user | I go to the workouts page, and if I selected a particular sorting, the workouts are sorted that way | ✔️ |
| Clicking on a workout image as a logged in user | I see workout details | ✔️ |
| Clicking on the 'My Account' button as an anonymous user | I see options to either register or login, which take me to either a register or login page | ✔️ |
| Clicking on the 'My Account' button as a logged in user | I see options to go to my profile or to logout, which take me to either my profile page or logout page | ✔️ |
| Clicking on a product image as an anonymous or a logged in user | I see product details and the option to add a product to my cart | ✔️ |
| Clicking on the 'Special Offers/All Specials' link as an anonymous or a logged in user | I see a list of products that are on some kind of special offer | ✔️ |
| Clicking on the cart icon as an anonymous or a logged in user after I added products to my cart | I see a list of products in my cart, with subtotals, delivery costs and the order total. The cart icon itself also indicates my current order total | ✔️ |



**Registration and User Accounts**
| Test | Expected | Passed |
| :--: | :------: | :----: |
| Registering for an account via either the Register button on the home screen or the Register link in 'My Account' | I can fill in a form, receive an email with a confirmation link, confirm my account and then I have an account | ✔️ | 
| Opening the 'My Account' menu | I can either login to my account, or logout if I'm already logged in | ✔️ |
| Recover my password | I can use the 'Forgot Password' button on the login page, fill in my email and then receive a working link to recover my password | ✔️ |
| Register for an account | I can use the 'Forgot Password' button on the login page, fill in my email and then receive a working link to recover my password | ✔️ |
| Clicking on 'My Account/My Profile' as a logged in user after I made an order | I see a form where I can fill in personal details, which I can update. I also see my order history, with links to the order confirmations | ✔️ |



**Sorting and Searching**
| Test | Expected | Passed |
| :--: | :------: | :----: |
| As either an anonymous user or logged in user, I click on the sorting menu on the products page | I can sort the list of products using the sort menu, sorting by price, category, rating or name | ✔️ | 
| As either an anonymous user or logged in user, I choose a collection of product categories and  click on the sorting menu on the products page | I can sort this subcollection of products using the sort menu, sorting by price, category, rating or name | ✔️ | 
| As either an anonymous user or logged in user, I enter a search term in the search bar | I get a page with the term I searched for, a counter with how many products were found, and if there are any products, a list of these products | ✔️ | 
| As a logged in user, I click on the sorting menu on the workouts page | I can sort the list of workouts using the sort menu, sorting by body part, equipment, target, rating or name | ✔️ | 



**Purchasing and Checkout**
| Test | Expected | Passed |
| :--: | :------: | :----: |
| As either an anonymous user or logged in user, I use the quantity selector functionality on the product details page | I can adjust the quantity and add the product and desired quantity to my cart | ✔️ | 
| As either an anonymous user or logged in user, I click on the cart icon in the navbar | I can view the items in my cart, subtotals, delivery costs and my order total | ✔️ | 
| As either an anonymous user or logged in user, I use the quantity selector or delete functionality in the cart | I can adjust the quantity of a product in my cart or delete the product from my cart | ✔️ | 
| As either an anonymous user or logged in user, I click on the 'Checkout' button | I can fill in my delivery details and card details and then checkout | ✔️ | 
| As either an anonymous user or logged in user, I click on the 'Complete Order' button | I am taken to a checkout confirmation page, with details for my order | ✔️ | 
| As either an anonymous user or logged in user, I click on the 'Complete Order' button | I receive an email with confirmation of my order | ✔️ | 



**Admin and Store Management**
| Test | Expected | Passed |
| :--: | :------: | :----: |
| I log in using superuser credentials at https://code-institute-ms4.herokuapp.com/admin | I am taken to the admin portal, where I can see and edit elements of the webapp | ✔️ | 
| In the admin portal I perform CRUD operations on a Product | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on a Product_Category | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on an Order | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on an Shop alert | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on a Feature | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on a Workout | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on a Body part | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on an Equipment | The CRUD operations are applied | ✔️ | 
| In the admin portal I perform CRUD operations on a Target | The CRUD operations are applied | ✔️ | 
| Logged in as a superuser, I click on 'My Account' | I see a link for 'Add Product' which allows me to add a product to the store | ✔️ | 
| Logged in as a superuser, I go to the Products page | I see links on each product that allow me to edit the product  | ✔️ | 
| Logged in as a superuser, I go to the product details page for a product | I see a link that allows me to edit the product  | ✔️ | 
| Logged in as a superuser, I go to the Products page | I see links on each product that allow me to delete the product  | ✔️ | 
| Logged in as a superuser, I go to the product details page for a product | I see a link that allows me to delete the product  | ✔️ | 
| Logged in as a superuser, I click on 'Workouts' | I see a link for 'Add Workout' which allows me to add a workout to the site | ✔️ | 
| Logged in as a superuser, I go to the Workouts page | I see links on each workout that allow me to edit the product  | ✔️ | 
| Logged in as a superuser, I go to the workout details page for a workout | I see a link that allows me to edit the product  | ✔️ | 
| Logged in as a superuser, I go to the Workouts page | I see links on each workout that allow me to delete the product  | ✔️ | 
| Logged in as a superuser, I go to the workout details page for a workout | I see a link that allows me to delete the product  | ✔️ | 



<ins>Code validation:</ins> 
1. [HTML validation](https://validator.w3.org/nu/)
- https://code-institute-ms4.herokuapp.com/
   1. First check: 5 errors, 4 warnings
   2. Second check: 2 error, 4 warnings. The errors I ignore: the duplicate ID is no problem, as one is used on mobile screens, the other on desktop screens. Removing the stray </div> actually breaks the footer container, so it has to stay. https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2F
- https://code-institute-ms4.herokuapp.com/products/
   1. First check: 1 error, 4 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Fproducts%2F#l248c81
- https://code-institute-ms4.herokuapp.com/products/1/
   1. First check: 1 error, 3 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Fproducts%2F1%2F#l248c81
- https://code-institute-ms4.herokuapp.com/accounts/signup/
   1. First check: 1 error, 2 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Faccounts%2Fsignup%2F#l248c81
- https://code-institute-ms4.herokuapp.com/accounts/login/
   1. First check: 1 error, 2 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Faccounts%2Flogin%2F#l248c81
- https://code-institute-ms4.herokuapp.com/accounts/password/reset/
   1. First check: 1 error, 2 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Faccounts%2Fpassword%2Freset%2F#l248c81
- https://code-institute-ms4.herokuapp.com/cart/
   1. First check: 1 error, 3 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Fcart%2F#l248c81
- https://code-institute-ms4.herokuapp.com/checkout/
   1. First check: 1 error, 3 warnings, same as home page: https://validator.w3.org/nu/?showsource=yes&doc=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2Fcheckout%2F#l248c81

I tried fixing the stray </div> error, but doing so results in breaking the DOM flow, causing the footer to be part of the container.




1. [CSS validation](https://jigsaw.w3.org/css-validator/)
- https://code-institute-ms4.herokuapp.com/ 
Validation: https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fcode-institute-ms4.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en 
1 warning in base.css, which is on purpose. Then there's a whole bunch of warnings in Bootstrap.css, which I'm not going to fix.
- profile.css: no errors.
- checkout.css: no errors.



1. [Python Validation]
1. Run ```python3 -m flake8``` and fix problems:
- Lots of messages about line too long, whitespace, no newline. Installed autopep8 ```pip install -U autopep8``` and ran it to fix many of the problems ```autopep8 --in-place --recursive .```
- Installed black: ```pip install black```
- Ran black: ```black .```
- Ignoring all the migrations files
- Ignoring env.py, as it is only a local file and used for development
- Ignoring tests.py, as these are not production code
- .\fit_family\settings.py:17:5: F401 'env' imported but unused --> env is used
- .\fit_family\settings.py:145:80: E501 line too long (91 > 79 characters) --> acceptable, as it belongs to the Django framework. I also don't know how to adjust the layout --> # noqa
- .\fit_family\settings.py:148:80: E501 line too long (81 > 79 characters) --> acceptable, as it belongs to the Django framework. I also don't know how to adjust the layout --> # noqa
- .\fit_family\settings.py:151:80: E501 line too long (82 > 79 characters) --> acceptable, as it belongs to the Django framework. I also don't know how to adjust the layout --> # noqa
- .\fit_family\settings.py:154:80: E501 line too long (83 > 79 characters) --> acceptable, as it belongs to the Django framework. I also don't know how to adjust the layout --> # noqa
- .\checkout\apps.py:9:9: F401 'checkout.signals' imported but unused --> used in another file 
- .\checkout\views.py:1:80: E501 line too long (87 > 79 characters) --> no easy way to reformat --> # noqa
- .\checkout\webhook_handler.py:71:80: E501 line too long (80 > 79 characters) --> no easy way to reformat --> # noqa
- .\checkout\webhook_handler.py:72:80: E501 line too long (80 > 79 characters) --> no easy way to reformat --> # noqa
- .\checkout\webhooks.py:43:80: E501 line too long (86 > 79 characters) --> no easy way to reformat --> # noqa
- .\profiles\forms.py:33:80: E501 line too long (85 > 79 characters) --> no easy way to reformat --> # noqa
- .\products\widgets.py:9:80: E501 line too long (87 > 79 characters) --> no easy way to reformat --> # noqa
- .\products\views.py:62:80: E501 line too long (80 > 79 characters) --> no easy way to reformat --> # noqa
- .\products\urls.py:9:80: E501 line too long (82 > 79 characters) --> no easy way to reformat --> # noqa
- .\checkout\models.py:63:80: E501 line too long (87 > 79 characters) --> no easy way to reformat --> # noqa
- .\checkout\urls.py:12:80: E501 line too long (88 > 79 characters) --> no easy way to reformat --> # noqa
- .\profiles\urls.py:6:80: E501 line too long (84 > 79 characters) --> no easy way to reformat --> # noqa
- .\workouts\urls.py:11:80: E501 line too long (82 > 79 characters) --> no easy way to reformat --> # noqa



### Notable Bugs
One big bug was with the checkout process not working: after clicking on the checkout button, the loading spinner would appear, but would never progress to the checkout success page.
To try and fix this bug I took the following steps:
1. Check if all the Stripe keys and secrets were correct.
1. Check if the environment vars were using the correct Stripe information.
1. Go through the code for the checkout app: changed some variable names and fixed a typo where a dash was used instead of an underscore.
1. urls.py was missing the / after checkout_success/<order_number>, fixed that.
1. After changing variable names, I had to do another database migration.
2. After this, when trying to checkout, I could an error about adding a float and decimal together: fixed this as well.
3. It still wasn't working, and I found out the problem was within stripe_elements.js: when I changed code in there, checkout would work.
4. I was about to start working through the code using console.log when I noticed an error in the log: it couldn't parse $post. This piece of code should have been $.post, missing a period. After adding that, the code worked.

Another bug I discovered was that updating the quantity in the cart didn't always work. Troubleshooting steps:
1. Checking the browser console for errors
2. Adding debugging statements to the code for updating the quantity, both the jQuery that triggers the form submit as the actual Python code for the view.
3. I discovered that sometimes the Python code would not run, while the jQuery code would always run.
4. I also noticed that in the VS Code console there would be an error if the Python code did run: Broken pipe from ('127.0.0.1', 62554)
5. While troubleshooting, I realized that the product_details page handled submitting the form differently: on this page it was just a button to submit the form. Adding this to cart.html worked all the time, while using jQuery did not.
6. I replaced the <a href> with a submit button, applied some CSS and adjusting the quantity in the cart now works.


### Problems
The only real problem was the implementation of Stripe. Getting this up and running took a lot of time, which meant I did not have time to implement other features. Right now, the project is a basic webshop, but not yet the community it sets out to be.

---

## Deployment
The project has been deployed to Heroku, with static files hosted on AWS S3. If  you want to do the same:
1. Fork the repository to your own GitHub: https://github.com/RicardoAzuul/code-institute-ms4-fullstack.
1. Log in to Heroku (www.heroku.com) - or register if you don't have an account yet.
1. In the Heroku dashboard, click the New button in the top right corner and create a new app.
1. Give your new app a name and choose a region. The name has to be unique within Heroku.
1. On the page for your new Heroku app, go to Deployment method and choose "Connect to GitHub". If you haven't connected your GitHub account to Heroku yet, you will be able to do so now.
1. Choose the forked repository of this project from your own GitHub account.
1. If you want, you can enable Automatic Deploys here: whenever you perform a push to your GitHub repository, the Heroku app can redeploy. Otherwise you can deploy manually. Heroku will use the PROCFILE and requirements.txt to install dependencies and build the app.
1. You will also have to create an S3 bucket on AWS, one that is publicly accessible.
1. And you will have to set up a Stripe webhook, using a public key, secret key and webhook secret. 
3. You will also have to set some Config Vars in the Settings section of your Heroku app. These are the Config Vars:
   - AWS_ACCESS_KEY_ID: the id for your AWS S3 container
   - AWS_SECRET_ACCESS_KEY: the secret key for your AWS S3 container
   - DATABASE_URL: the url to the postgress database on Heroku
   - EMAIL_HOST_PASS: the password or application key for the email account you use for emailing. This project uses Gmail
   - EMAIL_HOST_USER: the emailadress
   - SECRET_KEY: the Django secret key
   - STRIPE_PUBLIC_KEY: Your Stripe public key
   - STRIPE_SECRET_KEY: Your stripe secret key
   - STRIPE_WH_SECRET: Your Stripe webhook secret
   - USE_AWS: Set to true to tell Django to use the other AWS settings


### Run locally
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
The color scheme, black with accents of white and red, was inspired by Netflix: it looks bold. For the font I did some research into bold aggressive font types and came upon slab serif fonts. I picked Kelly Slab, as it was available via Google Fonts.
Initially I wanted to do something different and go for warm and friendly, but I did not like the color scheme and couldn't find suitable images.



### Content
Product images, prices, descriptions and ratings: www.decathon.nl
Workout information: from a dataset on Kaggle: https://www.kaggle.com/datasets/edoardoba/fitness-exercises-with-animations
The descriptions of workouts came from: https://www.bodybuilding.com/


### Media
Main page: https://www.pexels.com/photo/woman-doing-exercise-414029/
No image available file: https://commons.wikimedia.org/wiki/File:No_Image_Available.jpg


### Code
I've used some code from Bootstrap, as indicated by comments, and I found a nice way to do a back to top button that only appeared when scrolling down and slowly scrolls you back on Stackoverflow, as indicated by comments.


### Acknowledgements

- I received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). 
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- I also received help from the Code Institute Slack Community when I had to resubmit my project, so thanks to the community as well.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, [Django](https://www.djangoproject.com/) for their documentation and [Stackoverflow](https://stackoverflow.com/) for helping with finding solutions to coding problems.
- My wife, Elizabeth Lane, for supporting me during this coding course.
