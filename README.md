# <img src="icon.png" width="28"> Smart RSS Parser

[![hacs_badge](https://img.shields.io/badge/HACS-Custom-orange.svg)](https://github.com/hacs/integration)
![version](https://img.shields.io/badge/version-1.0.0-blue)
![HA](https://img.shields.io/badge/Home%20Assistant-2024.1+-green)
![license](https://img.shields.io/badge/license-MIT-lightgrey)
![downloads](https://img.shields.io/github/downloads/suxlala/rss_smart_parser/total.svg)

![Overview](https://github.com/suxlala/rss_smart_parser/blob/main/cardoverview.png)

## What is Smart RSS Parser ?

A Home Assistant Integration to easily create RSS feed sensors from the UI. It goes beyond Feedparser and parses all kind of RSS feed structures, extracting clean text as well as all type of pictures. 

### Features

- 📰 Create unlimited number of RSS feed sensors
- 🎨 No need to add YAML codes to your config, just add sensors from the UI
- 🏷️ Sensors will grab `title`, `publication date`, `link`, `description`, and `image` fields
- 🏞️ Any type of image will be extracted from any RSS structure (unlike Feedparser)
- ⌚️ Sensors will look for new content and update every 10 minutes
- 🪪 Display extracted articles on your Dashboard with a highly customisable, flexible custom card, the [RSS News Card](https://github.com/suxlala/rss-news-card)
 

## Installation

### Using HACS  

If you dont' have [HACS](https://hacs.xyz) installed yet, I highly recommend it.  
[![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=suxlala&repository=rss_smart_parser&category=integration) or search for `Smart RSS Parser`.

### Manual  

Download the `rss_smart_parser` directory and place it in your `/config/custom_component/` folder.

### ------------
After installation you need to **restart** Home-Assistant before using the integration.



## Configuration  

### Setup

[![Open your Home Assistant instance and start setting up a new integration.](https://my.home-assistant.io/badges/config_flow_start.svg)](https://my.home-assistant.io/redirect/config_flow_start/?domain=rss_smart_parser)

If you don't have [My Home Assistant](https://my.home-assistant.io/) redirects set up, go to Settings -> Devices & Services -> 
Click "Add integration" and search for `Smart RSS Parser`

### Create Sensors

Add an item:
- Give a `name` to the RSS feed source and the sensor
- Add the `URL` link of the RSS feed (in the form of _https://yourRSSfeed.com/feed_ , e.g. http://rss.cnn.com/rss/cnn_topstories.rss)
- Define a `limit` for the max number of the latest news articles to be extracted for this sensor
  
The `state` of the sensor will show the number of available extracted articles. The contents of the `title`, `publication date`, `link`, `description`, and `image` fields will go into the sensor attributes.
