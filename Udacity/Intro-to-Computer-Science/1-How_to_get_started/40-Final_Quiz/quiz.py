#! usr/bin/env python3
# -*- coding: utf-8 -*-

################################################################################
########################## Lesson 1 : FINAL QUIZ ###############################
################################################################################

def main():
    page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

    link_tag = '<a href="'
    start_link = page.find(link_tag) + len(link_tag)
    end_link = page.find('">', start_link)

    url = page[start_link:end_link]

if __name__ == '__main__':
    main()
