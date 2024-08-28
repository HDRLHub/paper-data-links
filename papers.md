---
layout: default
title: All Papers
---

# All Papers

<ul class="paper-list">
{% assign sorted_years = site.pages | where_exp: "page", "page.path contains 'papers/'" | map: "path" | map: "split" | map: "first" | uniq | sort | reverse %}
{% for year in sorted_years %}
  <li class="year">
    <h2>{{ year }}</h2>
    <ul class="journals">
      {% assign year_papers = site.pages | where_exp: "page", "page.path contains 'papers/' and page.path contains year and page.name == 'README.md'" | sort: "path" %}
      {% assign journals = year_papers | map: "path" | map: "split" | map: "second" | uniq | sort %}
      {% for journal in journals %}
        <li class="journal">
          <h3>{{ journal }}</h3>
          <ul class="papers">
            {% for paper in year_papers %}
              {% if paper.path contains journal %}
                <li class="paper">
                  <a href="{{ paper.url | relative_url }}">{{ paper.title }}</a>
                </li>
              {% endif %}
            {% endfor %}
          </ul>
        </li>
      {% endfor %}
    </ul>
  </li>
{% endfor %}
</ul>

<style>
  .paper-list {
    list-style-type: none;
    padding-left: 0;
  }
  .journals {
    list-style-type: none;
    padding-left: 20px;
  }
  .papers {
    list-style-type: none;
    padding-left: 20px;
  }
  .year > h2 {
    margin-bottom: 10px;
  }
  .journal > h3 {
    margin-bottom: 5px;
  }
</style>