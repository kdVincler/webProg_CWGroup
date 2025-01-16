# ECS639U Group 24 Coursework

## Group members and Contributions

### **Roman James John Pretty (210327061)**

Contribution 100%

**Tasks Assigned:**

- Setup of Vue Router and Pinia Stores
- Selenium E2E Testing
- Full Linking between API and Frontend for Auth
- Full Linking between API and Frontend for Hobbies
- Styling of all Components

**Tasks Completed or Worked on:**

- All of the above and:
- Edit Profile
- Sidebar (Hobbies, Friends, Friend Requests)
- Full Friend and Friend Request System (Frontend and Backend)
- Pagination Filter (Sort by Age)
- Open shift deployment

## Konrad Vincler (220594350)

Contribution 100%

**Tasks Assigned:**

- Account creation and login, using Django's authentication framework
- Hobbies API implementation (urls, views, api.ts fetch calls)
- Pagination for the main page
- Frontend typing
- Additional Global store implementation (Friend, hobby, page)
- Open Shift deployment

**Tasks Completed or Worked on:**

- All the above, and:
- Pagination filter test
- Profile edit modal and linkage to backend

## Alicia Marie Ferrera Pangan (220214632)

Contribution 100%

**Tasks Assigned:**

- User model
- Bug Searching

**Tasks Completed or Worked on:**

- All of the above, and:
- Skeleton of Ajax functions
- Serialisers implementation
- Updating code to use static types in Python (models)
- Bug fixing

## Gabrielle Gadjakaeva (220575485)

Contribution 100%

**Tasks Assigned:**

- Bug Searching
- Profile page, edit profile modal

**Tasks Completed or Worked on:**

- All of the above, and:
- Login and Register input validation bug
- Updating code to use static types in Python (views) and TypeScript (api.ts)

## Deployed site

<link>https://group24-web-apps-ec221017.apps.a.comp-teach.qmul.ac.uk/</link>

## Users (on both the deployed and submitted versions)

| # | Name | Username | D.o.B | Password |
| --- | --- | --- | --- | --- |
| 0 | admin | admin@email.com | - | administrator |
| 1 | Roman Pretty | romanjjpretty@gmail.com | 2002-09-29 | password |
| 2 | Gabrielle Gadjakaeva | gab@email.com | 2004-03-16 | password |
| 3 | Alicia Ferrera | ec22741@qmul.ac.uk | 2003-10-22 | password |
| 4 | Konrad Vincler | vincler.konrad@gmail.com | 2003-01-22 | password |
| 5 | Holly Thomson | holly@email.com | 1973-12-27 | password |
| 6 | Taylor Dodd | doddy@email.com | 1913-10-10 | password |
| 7 | Johnathan Smiths | johnathan@email.com | 1958-10-20 | password |
| 8 | Felonius Gru | moon@email.com | 1977-06-23 | password |
| 9 | Corran Horn | corran@email.com | 1944-09-09 | password |
| 10 | John Johnium | j.john@email.com | 1997-09-10 | password |
| 11 | Sarah Sogu | sarah@email.com | 1975-02-01 | password |
| 12 | Bjorn Bjornson | bjorn@email.com | 1932-09-02 | password |
| 13 | Mike Mikael | mike@email.com | 1956-07-14 | password |
| 14 | Mickey Haller | haller@email.com | 1961-08-04 | password |
| 15 | Izzy Wizzy | wizzy@email.com | 2007-07-17 | password |
| 16 | Hank Hughie | hank@email.com | 1954-05-23 | password |
| 17 | Leghie Mcrunk | leghie@email.com | 1932-03-24 | password |
| 18 | Harvey Specter | specter@email.com | 2010-12-24 | password |
| 19 | Pete Davidson | davidson@email.com | 1954-10-29 | password |
| 20 | Mylan Koma | mylan@email.com | 1987-02-21 | password |

## Local development

### Running locally with built frontend (Recommended)

To run this project in your development machine with built frontend, follow these steps:

1. Ensure that .env's VITE_DEV_MODE variable is **false**

2. Create and activate a conda environment

3. Download this repo as a zip, extract it and open it.

4. Install Pyhton dependencies (main folder):

    ```console
    $ pip install -r requirements.txt
    ```

5. Create a development database:

    ```console
    $ python manage.py migrate
    ```

7. If everything is alright, you should be able to start the Django development server from the main folder:

    ```console
    $ python manage.py runserver
    ```

9. Open your browser and go to http://localhost:8000, you will be greeted with a template page.

### Running locally with unbuilt Vite frontend

To run this project in your development machine with prebuilt Vite frontend, follow these steps:

1. Ensure that .env's VITE_DEV_MODE variable is **true**

2. Create and activate a conda environment

3. Download this repo as a zip, extract it and open it.

4. Install Pyhton dependencies (main folder):

    ```console
    $ pip install -r requirements.txt
    ```

5. Create a development database:

    ```console
    $ python manage.py migrate
    ```

6. Install JavaScript dependencies (from 'frontend' folder):

    ```console
    $ npm install
    ```

7. If everything is alright, you should be able to start the Django development server from the main folder:

    ```console
    $ python manage.py runserver
    ```

8. and the Vue server from the 'frontend' sub-folder:

    ```console
    $ npm run dev
    ```

9. Open your browser and go to http://localhost:5173, you will be greeted with a template page.

## License

This code is dedicated to the public domain to the maximum extent permitted by applicable law, pursuant to [CC0](http://creativecommons.org/publicdomain/zero/1.0/).
