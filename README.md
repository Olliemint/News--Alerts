# News--Alerts

## By Oliver Maiyo

> Keep Up With The Current News Article (KUWTCNA) is a flask application that consumes the news API then lists and provides previews of news articles from various sources.

### Screenshot of the App
<img src="https://raw.githubusercontent.com/Olliemint/News--Alerts/main/app/static/assets/landing.png">



## Table of Content

+ [Description](#description)
+ [Setup/Installation Requirements](setup&installationrequirements)
+ [How To Access the Site](#howtoaccessthesite)
+ [Behaviour Driven Development](#bdd&tdd)
+ [Technology & Tools](#technology&tools)
+ [Reference](#reference)
+ [Known-Bugs](#knownbugs)
+ [Licence](#licence)
+ [Authors Info](#authors-info)


## Description

> This is a Flask application that lists various News sources retrieved from News API. A user can click on a News source and be directed to a page that contains News Articles from the selected News source. The article's title, image, and preview is displayed and a user can click on the article to be directed to the source's site to read the entire article.



## Setup/Installation Requirements

### You need to have the following installed
  * Python3.9
  * Flask

```
 
1.Download and install Git.
 Clone this [github repo] (https://github.com/)
2. Ensure python is installed on your machine
3. On the terminal for linux or command prompt for windows;
  * Open the containing folder by cd.
  * Run $ chmod +x start.sh
  * Run the application: $ ./start.sh

```

### Deployment environment
* Heroku

### How To Access the Site
> This App is being hosted by GitHub Pages. The link to the Repo is: https://github.com/


## BDD
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Display the preview of an article | **On page load** | Each article displays an image,description and source link |
| Display articles from various news source | **Click a news source** | Redirected to a page with articles from the source |
| To Read an entire article  | **Click an article** | Redirected to the news source's site to read the entire article |



## TDD

> To test the app, run this command in the terminal;

`$ python3.9 articles_test.py`

### Technology & Tools
* Python
* Flask
* HTML
* CSS
* Bootstrap

## Reference

* [Flask for Beginners](https://www.fullstackpython.com/flask.html)


## Known Bugs
> All known bugs were fixed (Bug fixed) . Seen any Bug? Feel free to reach me Asap!

## License

> [MIT License](license) this application's source code is free for any open source projects

> Copyright (c) 2022 **Oliver Maiyo**



## Authors information
> Feel free to add your contribution to the code.

> If you have any questions,comments or advice,feel free to contact me

* [Email](oliverkoechrj@gmail.com)
* [Twitter]()
