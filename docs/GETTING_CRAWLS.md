# Getting Ad Crawls
This is quite simple. AMRSystem offers both a JSON option and an option with just the content field.

The JSON option: `/adcrawls/:id.json`. This route offers just the necessities and the content field can be accessed at JSON location "content." This is nice if whatever language you're using has decent JSON support.

If you just want the crawl content, use `/adcrawls/:id/content.txt`. This is nice if you don't have good JSON support.