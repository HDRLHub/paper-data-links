---
layout: default
title: All Papers
---

# All Papers

{% assign sorted_pages = site.pages | sort: "path" | reverse %}
{% assign current_year = "" %}
{% assign current_journal = "" %}

<ul class="paper-list">
{% for page in sorted_pages %}
  {% if page.path contains 'papers/' and page.name == 'README.md' %}
    {% assign path_parts = page.path | split: "/" %}
    {% assign year = path_parts[1] %}
    {% assign journal = path_parts[2] %}
    
    {% if year != current_year %}
      {% unless forloop.first %}</ul></li>{% endunless %}
      <li class="year">
        <h2>{{ year }}</h2>
        <ul class="journals">
      {% assign current_year = year %}
      {% assign current_journal = "" %}
    {% endif %}
    
    {% if journal != current_journal %}
      {% unless current_journal == "" %}</ul></li>{% endunless %}
      <li class="journal">
        <h3>{{ journal }}</h3>
        <ul class="papers">
      {% assign current_journal = journal %}
    {% endif %}
    
    <li class="paper">
      <a href="{{ page.url | relative_url }}">{{ page.title }}</a>
    </li>
    
    {% if forloop.last %}
        </ul>
      </li>
    </ul>
  </li>
    {% endif %}
  {% endif %}
{% endfor %}
</ul>

<style>
  .paper-list { list-style-type: none; padding-left: 0; }
  .journals { list-style-type: none; padding-left: 20px; }
  .papers { list-style-type: none; padding-left: 20px; }
  .year > h2 { margin-bottom: 10px; }
  .journal > h3 { margin-bottom: 5px; }
</style>