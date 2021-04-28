<br />
<p align="center">

  <h1 align="center">Open Scp Api</h3>

  <p align="center">
    An api based on the <a href='http://scp-wiki.wikidot.com'><strong>ScpWiki</strong></a>
    <br />
    <br />
    <a href="https://github.com/Trecto34/open-scp-api/issues">Report Bug</a>

  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#todo">Todo</a></li>
    <br/>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


I decided to do this project to increase my Django Rest Framework skills and knowledge, the reason I chose Project-SCP was due to the fact that there is no open API to query Foundation items


### Built With

* [Django](https://www.djangoproject.com)
* [Django Rest Framework](https://www.django-rest-framework.org)


<!-- GETTING STARTED -->
## Getting Started

<br />

### Prerequisites

* Python >= 3.8.5
* Pip >= 21.1

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/Trecto34/open-scp-api
   ```
2. Install pip packages
   ```sh
   pip install -r requirements.txt
   ```
3. Create a ```.env``` archive on ```./scp_api``` and add this:
   ```sh
   KEY = your-custom-key
   ```



<!-- USAGE EXAMPLES -->
## Usage

1. run:
   ```sh
   ./manage.py createsuperuser
   ```

2. then run:
   ```sh
   ./manage.py runserver
   ```


## Todo:
* Add register and login feature
* Document the api
* Host the api