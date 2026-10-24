
# Academic Pages

![pages-build-deployment](https://github.com/academicpages/academicpages.github.io/actions/workflows/pages/pages-build-deployment/badge.svg)

Academic Pages is a Github Pages template for academic websites.


# Getting Started

1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Click the "Use this template" button in the top right.
1. On the "New repository" page, enter your repository name as "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and add your content.
1. Upload any files (like PDFs, .zip files, etc.) to the `files/` directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section
1. (Optional) Use the Jupyter notebooks or python scripts in the `markdown_generator` folder to generate markdown files for publications and talks from a TSV file.

See more info at https://academicpages.github.io/

## Running Locally

When you are initially working your website, it is very useful to be able to preview the changes locally before pushing them to GitHub. To work locally you will need to:

1. Clone the repository and made updates as detailed above.
1. Make sure you have ruby-dev, bundler, and nodejs installed: `sudo apt install ruby-dev ruby-bundler nodejs`
1. Run `bundle install` to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.
1. Run `jekyll serve -l` to generate the HTML and serve it from `localhost:4000` the local server will automatically rebuild and refresh the pages on change.


## Gallery images

Add original photos to `images/picpic/work/` or `images/picpic/life/`, then list
them in `_data/pictures_work.yml` or `_data/pictures_life.yml`. Use a descriptive
`title` because it also supplies the image's alternative text.

Generate the responsive WebP thumbnails with:

```sh
python -m pip install Pillow PyYAML
python scripts/optimize_gallery.py
```

Commit the generated `images/picpic/thumbnails/` files and
`_data/gallery_thumbnails.json` alongside your changes. Jekyll uses these files
directly; Python is only needed when generating thumbnails. Originals remain
available by clicking each image. Regenerate after adding or replacing photos.

# Maintenance 

## Publishing completed changes

GitHub Pages builds the website from `master` in the repository root after each
push to `origin`. The repository's `AGENTS.md` instructs Codex to check, commit,
push, and verify deployment after completed website editing tasks. This is a
standing instruction from the owner, so a separate publishing request is not
needed for each task. Say "preview only" or "do not publish" to override it for
a particular change.

Publishing requires either local Git authentication or a connected GitHub
integration with repository Contents write permission. Codex can use that
connection when local Git authentication is unavailable, then synchronize the
local checkout. To renew an expired local GitHub sign-in on Windows, run
`git credential-manager github login --username leitingzhang --device --force`.
A successful push is followed by a Pages build; deployment is complete only when
that build succeeds. This workflow does not publish arbitrary file saves while
Codex is idle.

Bug reports and feature requests to the template  should be [submitted via GitHub](https://github.com/academicpages/academicpages.github.io/issues/new/choose). For questions concerning how to style the template, please feel free to start a [new discussion on GitHub](https://github.com/academicpages/academicpages.github.io/discussions).

This repository was forked (then detached) by [Stuart Geiger](https://github.com/staeiou) from the [Minimal Mistakes Jekyll Theme](https://mmistakes.github.io/minimal-mistakes/), which is © 2016 Michael Rose and released under the MIT License (see LICENSE.md). It is currently being maintained by [Robert Zupko](https://github.com/rjzupkoii) and additional maintainers would be welcomed.

## Bugfixes and enhancements

If you have bugfixes and enhancements that you would like to submit as a pull request, you will need to [fork](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo) this repository as opposed to using it as a template. This will also allow you to [synchronize your copy](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/syncing-a-fork) of template to your fork as well.

Unfortunately, one logistical issue with a template theme like Academic Pages that makes it a little tricky to get bug fixes and updates to the core theme. If you use this template and customize it, you will probably get merge conflicts if you attempt to synchronize. If you want to save your various .yml configuration files and markdown files, you can delete the repository and fork it again. Or you can manually patch.
