---
permalink: /gallery/
title: "Gallery"
author_profile: true
---


Jump to: [Work](#work), [Life](#life)


## Work

### ODACell Liquid Mixing Demonstration [(YouTube)](https://www.youtube.com/watch?v=7C7m4rLT9PY):
<iframe width="752" height="423" src="https://www.youtube.com/embed/7C7m4rLT9PY" title="ODACell Liquid Mixing Demonstration" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

### ODACell Coin Cell Assembly Demo [(YouTube)](https://www.youtube.com/watch?v=mAtBjrnRx-I):
<iframe width="752" height="423" src="https://www.youtube.com/embed/mAtBjrnRx-I" title="ODACell Coin Cell Assembly Demo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>

#### Gallery
(Right-click *'view image'* to see a larger image.)
{% assign number_printed = 0 %}
{% for pic in site.data.pictures %}

{% assign even_odd = number_printed | modulo: 4 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/work/{{ pic.image }}" class="img-responsive" width="75%" style="float: left" />
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd > 2 %}
</div>
{% endif %}


{% endfor %}

{% assign even_odd = number_printed | modulo: 4 %}
{% if even_odd == 1 %}
</div>
{% endif %}

{% if even_odd == 2 %}
</div>
{% endif %}

{% if even_odd == 3 %}
</div>
{% endif %}

<p> &nbsp; </p>

Note.
<figure>
<img src="{{ site.url }}{{ site.baseurl }}/images/profile.png" width="30%" >
</figure>


## Life
{% assign number_printed = 0 %}
{% for pic in site.data.pictures %}

{% assign even_odd = number_printed | modulo: 4 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-3 clearfix">
<img src="{{ site.url }}{{ site.baseurl }}/images/picpic/life/{{ pic.image }}" class="img-responsive" width="75%" style="float: left" />
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd > 2 %}
</div>
{% endif %}


{% endfor %}

{% assign even_odd = number_printed | modulo: 4 %}
{% if even_odd == 1 %}
</div>
{% endif %}

{% if even_odd == 2 %}
</div>
{% endif %}

{% if even_odd == 3 %}
</div>
{% endif %}

<p> &nbsp; </p>

Note.
<figure>
<img src="{{ site.url }}{{ site.baseurl }}/images/profile.png" width="30%" >
</figure>

