---
layout: archive
title: "Funding"
permalink: /funding/
author_profile: true
---

We gratefully acknowledge the support of the following research funders.

## Ongoing projects

{% assign ongoing_funders = site.data.funders | where: "status", "ongoing" %}
{% include funding-grid.html funders=ongoing_funders label="Funders of ongoing projects" %}

## Finished projects

{% assign finished_funders = site.data.funders | where: "status", "finished" %}
{% include funding-grid.html funders=finished_funders label="Funders of finished projects" %}
