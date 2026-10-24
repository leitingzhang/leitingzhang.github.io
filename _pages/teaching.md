---
layout: archive
title: "Teaching"
permalink: /teaching/
author_profile: true
---

Teaching at Uppsala University, with courses grouped by role.

## Course coordination

{% assign coordinated_courses = site.data.teaching | where: "role", "Course coordinator" %}
{% include teaching-courses.html courses=coordinated_courses %}

## Lectures

{% assign lecture_courses = site.data.teaching | where: "role", "Lecturer" %}
{% include teaching-courses.html courses=lecture_courses %}

## Laboratory teaching

{% assign laboratory_courses = site.data.teaching | where: "role", "Laboratory instructor" %}
{% include teaching-courses.html courses=laboratory_courses %}
