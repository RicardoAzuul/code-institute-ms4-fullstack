# Simply Fit
<!-- TODO: Add description of project: A book review and recommendation site, using MongoDB, Python, Flask, HTML, CSS and JavaScript. -->
Fit Family is a fitness subscription application.

The user's goal is to join a fitness community and purchase exercise plans and merchandise.

The site owner's goal is to build an active community around the product based on subscription and individual payments models, and to sell: exercise plans, nutrition plans, nutrition products and exercise products

Must haves for this project:
<!-- TODO: Must  haves -->
- Functionality that allows subscribers to update fellow members on their successes --> a forum?
- User proﬁles containing information that map to nutrition and/or exercise plans
- Product reviews
- A subscription-based payment model: on offer are 3 subscriptions, based on duration of subscription. Subscriptions get you access to workouts, nutrition plans, the community and a discount on the shop
- Individual item purchase capability
- Authentication and authorisation mechanism for subscribers and administrators

Nice to have: 
<!-- TODO: nice to haves -->

To see the site in action, visit [Fit Family](https://code-institute-ms4.herokuapp.com/)

---

## UI and UX
 
### User stories
  
**Viewing and Navigation**
| User Story ID | As A/An | I Want To Be Able To... | So That I Can... |
| :-------------|:--------| :----------------------:| :---------------:|
|             1 | Shopper | View a list of products | Select some to purchase |
|             2 | Shopper | View individual product details | Identify the price, description, product rating, product image and available sizes |
|             3 | Shopper | Quickly identify deals, clearance items and special offers | Take advantage of special savings on products I'd like to purchase |
|             4 | Shopper | Easily view the total of my purchases at any time | Avoid spending too much |
|             5 | Site User | Easily view the site on any device | Use the site whenever and wherever I'd like |

**Registration and User Accounts**
| User Story ID | As A/An   | I Want To Be Able To... | So That I Can... |
| :-------------|:--------  | :----------------------:| :---------------:|
|             6 | Site User | Easily register for an account | Have a personal account and be able to view my profile |
|             7 | Site User | Easily login or logout | Access my personal account information |
|             8 | Site User | Easily recover my password in case I forget it | Recover access to my account |
|             9 | Site User | Receive an email confirmation after registering | Verify that my account registration was successful |
|            10 | Site User | Have a personalized user profile | View my personal order history and order confirmations, and save my payment information |
|            11 | Site User | Easily review products | Help my fellow fitness community members to find the right product |

**Sorting and Searching**
| User Story ID | As A/An | I Want To Be Able To... | So That I Can... |
| :-------------|:--------| :----------------------:| :---------------:|
|            12 | Shopper | Sort the list of available products | Easily identify the best rated, best priced and categorically sorted products |
|            13 | Shopper | Sort a specific category of product | Find the best-priced or best-rated product in a specific category, or sort the products in that category by name |
|            14 | Shopper | Sort multiple categories of products simultaneously | Find the best-priced or best-rated products across broad categories, such as "clothing" or "homeware" |
|            15 | Shopper | Search for a product by name or description | Find a specific product I'd like to purchase |
|            16 | Shopper | Easily see what I've searched for and the number of results | Quickly decide whether the product I want is available |

**Purchasing and Checkout**
| User Story ID | As A/An | I Want To Be Able To... | So That I Can... |
| :-------------|:--------| :----------------------:| :---------------:|
|            17 | Shopper | Easily select the size and quantity of a product when purchasing it | Ensure I don't accidentally select the wrong product, quantity or size |
|            18 | Shopper | View items in my bag to be purchased | Identify the total cost of my purchase and all items I will receive |
|            19 | Shopper | Adjust the quantity of individual items in my bag | Easily make changes to my purchase before checkout |
|            20 | Shopper | Easily enter my payment information  | Check out quickly and with no hassle |
|            21 | Shopper | Feel my personal and payment information is safe and secure | Confidently provide the needed information to make a purchase |
|            22 | Shopper | View an order confirmation after checkout | Verify that I haven't made any mistakes |
|            23 | Shopper | Receiv an email confirmation after checkout | Keep the confirmation of what I've purchased for my records |

**Community**
| User Story ID | As A/An      | I Want To Be Able To... | So That I Can... |
| :-------------|:-------------|:-----------------------:| :---------------:|
|            24 | Subscriber   | Post updates about my progress | Update my fellow members on my successes |
|            25 | Subscriber   | Add and edit information on my profile pertaining to my fitness goals | Receive nutrition and exercise plans tailored to my fitness goals |
|            26 | Subscriber   | Easily find other subscribers | Feel part of a community and get motivated |
|            27 | Subscriber   | Easily see updates from other subscribers | Feel part of a community and get motivated |
|            28 | Subscriber   | Easily find information about the subscriptions available | Make an informed choice about my subscription |
|            29 | Subscriber   | Easily find workouts | Work on my fitness goal |
|            30 | Subscriber   | Easily find nutrition plans | Work on my fitness goal |


**Admin and Store Management**
| User Story ID | As A/An | I Want To Be Able To... | So That I Can... |
| :-------------|:--------| :----------------------:| :---------------:|
|            31 | Store Owner/Admin | Easily login or logout | Access the admin interface of the webapp |
|            32 | Store Owner/Admin | Add a product | Add new items to my store |
|            33 | Store Owner/Admin | Edit/update a product | Change product prices, descriptions, images and other product criteria |
|            34 | Store Owner/Admin | Delete a product | Remove items that are no longer for sale |
|            35 | Store Owner/Admin | Add a subscription | Add new subscription options |
|            36 | Store Owner/Admin | Edit/update a subscription | Change subscription prices, descriptions, linked workouts and nutrition |
|            37 | Store Owner/Admin | Delete a subscription | Remove subscriptions that are no longer available |
|            38 | Store Owner/Admin | Add a workout | Add new workouts |
|            39 | Store Owner/Admin | Edit/update a workout | Change workouts |
|            40 | Store Owner/Admin | Delete a workout | Remove workouts that are no longer promoted |
|            41 | Store Owner/Admin | Add a nutrition plan | Add new nutrition plans |
|            42 | Store Owner/Admin | Edit/update a nutrition plan | Change nutrition plan |
|            43 | Store Owner/Admin | Delete a nutrition plan | Remove nutrition plans that are no longer promoted |


Screenshots that fulfill these user stories:
<!-- TODO: add screenshots -->




---

### The 5 Planes of Design

Jesse James Garret's 5 planes of UX design were used to design the site. I started off at the Strategy Plane:

#### Strategy Plane
<!-- TODO: Write about Strategy Plane -->
The main goal for visitors is to find and join a fitness community they might like. This means giving visitors a feeling about the kind of community they are joining. Fit Family sets out to be a friendly, warm community. Not necessarily for people interested in maximizing their fitness or muscle gain or weight loss, but for people who want to join a family of people who are all trying to work on their fitness without impossible goals.
So the main page has to have a call to action in the form of a button to take you to subscriptions. We also need a hero image that exemplifies the image of Fit Family.
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
- a hero image evoking the idea of family, warmth and fitness.
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
- a hero image evoking the idea of family, warmth and fitness.
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
We use icons from Font Awesome to add some visual interest but also visual cues to indicate functionality. We use Bootstrap as a basis, but add our own style. Fit Family needs to be warm and familiar.


<ins>Wireframes</ins>
- [Home](readme-assets\media\home.png)
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
- [Community](readme-assets/media/community.png)
- [Community - tablet](readme-assets/media/community_tablet_view.png)
- [Community - mobile](readme-assets/media/community_mobile_view.png)
- [Exercises](readme-assets/media/exercises.png)
- [Exercises - tablet](readme-assets/media/exercises_tablet_view.png)
- [Exercises - mobile](readme-assets/media/exercises_mobile_view.png)
- [Nutrition](readme-assets/media/nutrition.png)
- [Nutrition - tablet](readme-assets/media/nutrition_tablet_view.png)
- [Nutrition - mobile](readme-assets/media/nutrition_mobile_view.png)
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


---

## Features

### Existing Features
<!-- TODO: Existing features -->



---

### Features Left to Implement
<!-- TODO: Features left to implement -->



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
- [Am I Responsive?](http://ami.responsivedesign.is/): to generate screenshots of the site at various viewpoints, indicating responsiveness.
- [Lighthouse](https://developers.google.com/web/tools/lighthouse): an automated tool in Chrome DevTools that audits for performance, accessibility, progressive web apps, SEO and more.
- [Prettier VS Code plugin](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): a code formatter that helps with code formatting, which is good for creating a consistent style.
- [Markdown link check](https://github.com/marketplace/actions/markdown-link-check): an automated tool to check for dead links in Markdown files.
- [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree): to keep track of todos, bugs, things that need to be fixed and such in my project.
- [autopep8](https://pypi.org/project/autopep8/): a Python package that helps with formatting Python code according to PEP8.


---

## Responsiveness of Pages
<!-- TODO: Responsiveness of Pages -->
These screenshots indicate the responsiveness of the pages on various screens. Pages that require a login are not included.



---

## Testing
<!-- TODO: Testing, either manual or automated -->
<!-- TODO: Look through Hello Django Github for tests -->




<ins>Code validation:</ins> 
<!-- TODO: Code validation: -->

1. [HTML validation](https://validator.w3.org/nu/)
<!-- TODO: HTML validation -->




2. [CSS validation](https://jigsaw.w3.org/css-validator/)
<!-- TODO: CSS validation -->



3. [Python Validation](http://pep8online.com/)
<!-- TODO: Python Validation:  -->




### Notable Bugs
<!-- TODO: Notable Bugs -->



### Problems
<!-- TODO: Problems -->


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
<!-- TODO: Look at these websites for inspiration -->
https://www.precor.com/en-us/resources/5-online-fitness-communities-to-keep-you-motivated


### Content
<!-- TODO: Add where I got the Content -->


### Media
<!-- TODO: Add where I got the Media -->


### Code
<!-- TODO: Add where I got the Code, if using other people's code -->


### Acknowledgements

- I received help and support from my mentor at Code Institute, [Jack Wachira](https://github.com/iamjackwachira). 
- I would also like to thank to all the people at [Code Institute](https://codeinstitute.net/) for providing the Diploma in Software Development course and giving me the tools and guidance to create this app.
- And also thanks to [Bootstrap](https://getbootstrap.com/) for helping with implementing their Bootstrap stylings, and [Stackoverflow](https://stackoverflow.com/) for helping with finding solutions to coding problems.
- My wife, Elizabeth Lane, for supporting me during this coding course.
