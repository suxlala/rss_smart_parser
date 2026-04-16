# rss_smart_parser
An integration to easily create RSS feed sensors from the UI. It goes beyond Feedparser and parses all kind of RSS feed structures, extracting clean text as well as all type of pictures.


[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
![version](https://img.shields.io/badge/version-1.0.0-blue)
![HA](https://img.shields.io/badge/Home%20Assistant-2024.1+-green)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

![Overview](https://github.com/suxlala/rss-news-card/blob/main/cardoverview.png)

## What is RSS News Card ?

A scrollable and highly customisable RSS newsfeed reader card for Home Assistant Dashboard, with multi-source support, automatic language detection, and full visual editor. RSS News Card is designed to scrape the content of various types of RSS feeds with pictures and display it on your HA Dashboard the way you want, with many options to tweak.

### Features

- 📰 Multiple RSS sources in a single card, sorted by date/time
- 🌍 Automatic language & date format detection from Home Assistant settings
- 📱 iOS-compatible scrolling, with adjustable card size
- 🎨 Full visual editor with color picker, toggle switches, and font size controls
- ⚠️ Built-in sensor diagnostics with setup instructions
- 🌐 Community localization support (English, Hungarian, German included)
- 🏷️ News source labels
- 💪🏻 Flexible layout
 

## Installation

### HACS (Recommended)

[![Open HACS Repository](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=suxlala&repository=rss-news-card&category=plugin)

> If the button doesn't work, add manually:

1. Go to the HACS store 
2. Click on the 3 dots in the upper right corner
3. Select Custom repos and add the url `https://github.com/suxlala/rss-news-card` 
4. Choose Dashboard as a type

Then, in Home Assistant's global settings, add the resource:

1. Go to **Settings → Dashboards → Three-dots menu → Resources** in the top right
2. Click **+ Add Resource** button in the bottom right
3. Enter in the following:
    * **URL:** /local/community/rss-news-card/rss-news-card.js
    * **Resource Type:** JavaScript Module
4. Click Create
**Note:** If you do not see the Resources menu, you will need to enable _Advanced Mode_ in your _User Profile_

_or_

### Manual Installation

1. Download `rss-news-card.js` file from the latest release.
2. Put `rss-news-card.js` file into `config/www/community/rss-news-card/` folder.
3. Add reference to `rss-news-card.js` in Dashboard. Either as above, using UI in Dashboard settings
	_or_
   - **Using YAML:** Add following code to `lovelace` section.
     ```yaml
     resources:
       - url: /local/community/rss-news-card/rss-news-card.js
         type: module
     ```

## Configuration

For every RSS news feed you want to track, create an individual `command_line` sensor in `configuration.yaml`. Copy and paste the YAML code below and amend it with your selected news feed source name and RSS web URL.
Put more sensors one by one under one 'command_line:' line.
