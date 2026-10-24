---
layout: archive
title: "Team members"
permalink: /team-members/
author_profile: true
---

<figure class="team-photo">
  <img src="{{ '/images/team/team-2026-1600.webp' | relative_url }}"
       srcset="{{ '/images/team/team-2026-960.webp' | relative_url }} 960w, {{ '/images/team/team-2026-1600.webp' | relative_url }} 1600w"
       sizes="(min-width: 1280px) 960px, (min-width: 925px) 80vw, 100vw"
       width="1600" height="1067" alt="Research group gathered on the stairs at Ångström Laboratory"
       decoding="async" fetchpriority="high">
  <figcaption>The group at Ångström Laboratory, 2026.</figcaption>
</figure>

## Current members

<h3 class="team-section-title">Researchers and postdocs</h3>

{% assign researchers = site.data.team | where: "group", "Researchers and postdocs" %}
{% include team-members.html members=researchers %}

<h3 class="team-section-title">PhD students (main supervisor)</h3>

{% assign main_phd_students = site.data.team | where: "group", "PhD students" | where: "supervision", "main" %}
{% include team-members.html members=main_phd_students %}

<h3 class="team-section-title">PhD students (co-supervisor)</h3>

{% assign co_phd_students = site.data.team | where: "group", "PhD students" | where: "supervision", "co" %}
{% include team-members.html members=co_phd_students %}

<h3 class="team-section-title">Master’s students</h3>

{% assign masters_students = site.data.team | where: "group", "Master’s students" %}
{% include team-members.html members=masters_students %}

## Alumni

{% include team-alumni.html %}
