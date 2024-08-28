---
layout: default
title: All Papers
---

# All Papers

<ul class="paper-list">
{% for page in site.pages %}
  {% if page.path contains 'papers/' and page.name == 'README.md' %}
    {% assign path_parts = page.path | split: "/" %}
    <li>
      Year: {{ path_parts[1] }}, 
      Journal: {{ path_parts[2] }}, 
      Paper: <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    </li>
  {% endif %}
{% endfor %}
</ul>