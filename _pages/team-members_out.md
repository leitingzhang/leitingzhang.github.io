---
layout: archive
title: "Team members"
permalink: /team-members-out/
author_profile: true
---


{% include base_path %}

{% assign sortedGroup = site.group | sort: 'lastname' %}

{% for post in sortedGroup %}
  {% include group-single.html %}
{% endfor %}

---
Interested in joining the team? Please reach out to [Leiting](mailto:leiting.zhang@kemi.uu.se) or any group member to learn more.


---

## Collaborators
We are fortunate to work on interdisciplinary projects with fantastic collaborators. Here are a few of our science friends:
- Barbara Berrie ([National Gallery of Art; Washington, DC](https://www.nga.gov))
- Gwendoline Fife, René Hoppenbrouwers ([SRAL, Maastricht, The Netherlands](https://www.sral.nl/en))
- [Prof. Ville Telkki (The University of Oulu, Finland)](https://www.oulu.fi/university/researcher/ville-veikko-telkki)
- [Prof. Christian Hilti (Texas A&M University)](https://www.chem.tamu.edu/rgroup/hilty/)
- [Prof. Kristina Keating (Rutgers University)](https://www.keatinggeophysics.org/)
- [Metna, Co. (Lansing, MI)](https://www.metnaco.com)
- [Prof. Daphna Shimon (The Hebrew University of Jerusalem, Israel)](https://shimongroup.huji.ac.il/dr-daphna-shimon)
