---
description: "{{ url }}"
term: "{{ title }}"
created_at: "{{ created_at }}"
updated_at: "{{ updated_at }}"
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
