---
layout: archive
title: "Sitemap"
permalink: /sitemap/
author_profile: true
---

Browse the site’s pages and posts below. An [XML sitemap]({{ '/sitemap.xml' | relative_url }}) is also available.

<h2>Pages</h2>
<ul class="site-link-list">
  <li><a href="{{ '/' | relative_url }}">Home</a></li>
  {% for item in site.data.navigation.main %}
  <li><a href="{{ item.url | relative_url }}">{{ item.title | escape }}</a></li>
  {% endfor %}
</ul>

<h2>Blog posts</h2>
<ul class="site-link-list">
  {% for post in site.posts %}
  <li><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></li>
  {% endfor %}
</ul>
