---
layout: default
title: VSO Instrument Data Links
---

> **Notice:** This site is being deprecated. Please visit the new site at [paper-data.helioanalytics.io/public/papers](https://paper-data.helioanalytics.io/public/papers) for the latest data and features.
>
> **For automated CSV access:** Use the API endpoint at `https://paper-data.helioanalytics.io/builder/public/papers/csv/`

# Welcome to Paper Data Links

This repository currently focuses on data from the Virtual Solar Observatory (VSO). Our initial efforts are dedicated to cataloging and linking VSO data used in academic papers. We plan to expand our scope to include other data sources in the future.

<h1>Papers by Year</h1>

<ul class="years">
{% for year in site.years %}
  <li><a href="{{ year.url | relative_url }}">{{ year.title }}</a></li>
{% endfor %}
</ul>