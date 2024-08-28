---
layout: default
title: All Papers
---

# All Papers

<ul class="paper-list">
{% raw %}{% assign sorted_years = site.pages | where_exp: "page", "page.path contains 'papers/'" | map: "path" | map: "split" | map: "first" | uniq | sort | reverse %}
{% for year in sorted_years %}
  <h2>{{ year }}</h2>
  {% assign year_papers = site.pages | where_exp: "page", "page.path contains 'papers/' and page.path contains year and page.name == 'README.md'" | sort: "path" | reverse %}
  {% for paper in year_papers %}
    {% assign path_parts = paper.path | split: "/" %}
    {% assign journal = path_parts[2] %}
    <li>
      <strong>{{ journal }}:</strong> <a href="{{ paper.url | relative_url }}">{{ paper.title }}</a>
    </li>
  {% endfor %}
{% endfor %}{% endraw %}
</ul>
```