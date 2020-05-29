#! usr/bin/env python3
# -*- coding: utf-8 -*-

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

# get_next_target
# Find the first link in a given web page
# Parameters : a string, representing the web page
# Returns : a string, the link found
#           a number, representing were reading the page stopped
# This function searches the first link of a given web page, then returns it
# as well as number, which represents where the reading stopped.
# The web page must be written in HTML. Only the '<a href=' tag is supported.
# There should be no '"' between the tag and the link.
# NB: If no links were found, the function shall return None instead of the link,
# and 0 instead of the reading marker.
    
def get_next_target(page):
    # Find the link tag
    link_tag = '<a href='
    start_link = page.find(link_tag)
    if start_link == -1:
        return None, 0
    # Get the URL
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote + 1)
    url = page[start_quote + 1 : end_quote]
    return url, end_quote

def main():
    print(get_next_target(page))

if __name__ == '__main__':
    main()
