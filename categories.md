---
layout: default
title: Categories
permalink: /categories/
---

{% for category in site.categories %}
  {% capture category_name %}{{ category | first }}{% endcapture %}
  <h2>{{ category_name }}</h2>
  <a name="{{ category_name | slugify }}"></a>
  <ul>
  {% for post in site.categories[category_name] %}
    <li><a href="{{ site.baseurl }}{{ post.url }}">{{post.title}}</a></li>
  {% endfor %}
  </ul>
{% endfor %}