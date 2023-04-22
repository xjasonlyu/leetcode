---
description: "{{ url }}"
term: "{{ title }}"
comments: true
tags:
{% for tag in tags %}
  - {{ tag -}}
{% endfor %}
---

# {{ title }}

**Problem Page**: <{{ url }}>

```{{ lang }}
{{ code }}
```
