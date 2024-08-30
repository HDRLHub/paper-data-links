---
layout: default
title: All Papers
---

# All Papers

<ul class="paper-list" style="list-style-type: none; padding-left: 0;">
{% for page in site.pages %}
  {% if page.path contains 'papers/' and page.name == 'README.md' %}
    {% assign path_parts = page.path | split: "/" %}
    <li style="margin-bottom: 20px;">
      <strong>Year:</strong> {{ path_parts[1] }} <br>
      <strong>Journal:</strong> {{ path_parts[2] }} <br>
      <strong>Paper:</strong> <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    </li>
    <hr>
  {% endif %}
{% endfor %}
</ul>
