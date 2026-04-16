import logging
import re
import aiohttp
import async_timeout
from datetime import timedelta
from homeassistant.components.sensor import SensorEntity

_LOGGER = logging.getLogger(__name__)
SCAN_INTERVAL = timedelta(minutes=10)
DOMAIN = "rss_smart_parser"

async def async_setup_entry(hass, config_entry, async_add_entities):
    """Setup sensor from a config entry (UI)."""
    config = config_entry.data
    name = config.get("name")
    url = config.get("url")
    limit = config.get("limit")
    
    sensor = SmartRSSSensor(name, url, limit, config_entry.entry_id)
    async_add_entities([sensor], True)

class SmartRSSSensor(SensorEntity):
    _attr_icon = "mdi:rss"
    def __init__(self, name, url, limit, entry_id):
        self._name = name
        self._url = url
        self._limit = limit
        self._entry_id = entry_id
        self._state = None
        self._articles = []
        self._attr_unique_id = f"rss_smart_{entry_id}"
        self._attr_icon = "mdi:rss"

    @property
    def icon(self): return self._attr_icon

    @property
    def name(self): return self._name    

    @property
    def extra_state_attributes(self):
        return {"articles": self._articles}

    @property
    def state(self): return self._state

    async def async_update(self):
        try:
            async with aiohttp.ClientSession() as session:
                async with async_timeout.timeout(10):
                    response = await session.get(self._url)
                    text = await response.text()
                    text = re.sub(r'\s+', ' ', text)
                    
                    items = re.findall(r'<item>(.*?)</item>', text)
                    parsed_articles = []

                    for item in items[:self._limit]:
                        title_match = re.search(r'<title>(.*?)</title>', item)
                        link_match = re.search(r'<link>(.*?)</link>', item)
                        pub_date = re.search(r'<pubDate>(.*?)</pubDate>', item)
                        desc_match = re.search(r'<description>(.*?)</description>', item)

                        # Cleaning up Description
                        desc = ""
                        if desc_match:
                            desc = desc_match.group(1).replace('<![CDATA[', '').replace(']]>', '')
                            desc = re.sub(r'<[^>]*>', '', desc).strip()
                            desc = desc.split("The post")[0].strip()

                        # Search for image
                        img = ""
                        # 1. attempts: media:content or enclosure url
                        img_match = re.search(r'(?:media:content|enclosure)[^>]+url=["\'](.*?)["\']', item)
                        if img_match:
                            img = img_match.group(1)
                        
                        # 2. attempt: simple img tag
                        if not img:
                            img_in_text = re.search(r'<img[^>]+src=["\'](.*?)["\']', item)
                            if img_in_text:
                                img = img_in_text.group(1)

                        # Formatting Date
                        formatted_date = ""
                        if pub_date:
                            raw_date = pub_date.group(1)
                            try:
                                from email.utils import parsedate_to_datetime
                                dt = parsedate_to_datetime(raw_date)
                                formatted_date = dt.isoformat()
                            except:
                                formatted_date = raw_date

                        parsed_articles.append({
                            "title": title_match.group(1).replace('<![CDATA[', '').replace(']]>', '').strip() if title_match else "No title",
                            "link": link_match.group(1).strip() if link_match else "",
                            "description": desc,
                            "pubDate": formatted_date,
                            "image": img
                        })

                    self._articles = parsed_articles
                    self._state = f"{len(parsed_articles)} articles"

        except Exception as e:
            _LOGGER.error("Error fetching RSS (%s): %s", self._url, e)
            self._state = "Error"