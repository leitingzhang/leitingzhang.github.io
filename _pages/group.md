---
layout: archive
title: "Current team members"
permalink: /group/
author: leitingzhang
author_profile: true
---

<img src="{{ site.baseurl }}/group/group2022.JPG" alt="Group, Spring 2022">


{% include base_path %}

{% assign sortedGroup = site.group | sort: 'lastname' %}

{% for post in sortedGroup %}
  {% include group-single.html %}
{% endfor %}

---
Interested in joining the Meldrum lab? Please reach out to [Tyler](mailto:tkmeldrum@wm.edu) or any group member to learn more. Importantly, you do *not* need to have a background in magnets, materials, or NMR to join and learn with the group.


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
