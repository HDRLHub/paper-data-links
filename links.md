---
layout: default
title: All Papers Links
---

<h1>All Papers Links (CSV Format)</h1>

<p>Click the button to download the CSV file:</p>

<button onclick="downloadCSV()">Download CSV</button>

<div class="code-container">
  <pre><code id="csvData">Bibcode,URL
{% for page in site.pages %}{% if page.bibcode %}"{{ page.bibcode }}","{{ page.url | absolute_url }}"
{% endif %}{% endfor %}</code></pre>
</div>

<script>
function downloadCSV() {
  var csvContent = document.getElementById('csvData').innerText;
  var blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
  var link = document.createElement("a");
  if (link.download !== undefined) {
    var url = URL.createObjectURL(blob);
    link.setAttribute("href", url);
    link.setAttribute("download", "all_papers.csv");
    link.style.visibility = 'hidden';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
  }
}
</script>

<style>
.code-container {
  overflow-x: auto;
  background-color: #f4f4f4;
  border: 1px solid #ddd;
  border-radius: 4px;
  padding: 10px;
}

pre {
  margin: 0;
  white-space: pre;
  word-wrap: normal;
}

code {
  display: inline-block;
  min-width: 100%;
}

button {
  background-color: #4CAF50;
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  margin: 4px 2px;
  cursor: pointer;
}
</style>