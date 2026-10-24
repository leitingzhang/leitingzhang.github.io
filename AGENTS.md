# Website maintenance

This is a Jekyll / Academic Pages website for Leiting Zhang.
The publishing repository is `leitingzhang/leitingzhang.github.io`.
The live site is `https://leitingzhang.com`, published from `master` at `/`.
`upstream` is the template repository; publish only to `origin`.

## Content and layout conventions

- Use US English in general prose and sentence case for interface headings.
  Preserve official names, publication titles, quotations, and historical facts.
- Display full dates as `14 October 2026` and year ranges as `2023–2026`.
  Keep currency codes explicit and use `Grant no.` for grant references.
- Use site-relative links for internal pages and assets. Preserve public URLs.
- Main pages use the archive layout; articles use single. Both share the
  `site-content` typography: one body font at 1rem with a consistent heading scale.
- Keep shared presentation in `_sass/_site-content.scss` and structural page
  styles in their existing modules. Avoid inline style blocks and font overrides.
- Use YAML front matter, Markdown for prose, HTML for structured content, and
  Liquid includes for reusable data-driven sections. Keep each list or component
  internally consistent rather than mixing Markdown list syntax inside HTML.
- Check the main navigation pages and blog layouts on desktop and mobile after
  changing shared styles; preserve funding logos, responsive gallery images,
  member groups, publication numbering, and scientific notation.

## Standing authorization to publish

The owner has explicitly authorized automatically committing, pushing, and
publishing completed website changes after each requested editing task.
Follow this workflow without asking for another publishing confirmation unless
the owner later requests a draft, preview only, or no publication:

1. Inspect the working tree and preserve unrelated edits. Complete the requested
   work and review the resulting diff.
2. Run checks appropriate to the change, including `git diff --check`. Validate
   edited data, links, and image assets as applicable. Preview layout changes.
   Run `bundle exec jekyll build` when the dependencies are available. If they
   are unavailable, report that limitation, run targeted checks, and verify the
   GitHub Pages build after pushing. Fix actual check failures before publishing.
3. Fetch `origin` and confirm the work is based on the latest `origin/master`.
   Preserve other work when resolving divergence; do not force-push.
4. Stage only files belonging to the completed task using explicit paths. Commit
   with a concise description and push to `origin/master`. Do not create empty
   commits or include unrelated work. If there are no changes, report that.
   If local Git authentication fails but the connected GitHub integration has
   repository Contents write permission, use it to create blobs, a tree based on
   the latest remote tree, and a commit containing exactly the task files. Update `master`
   with an expected-head check and no force, then fetch and synchronize the local
   checkout to the published commit while preserving all working files and
   unrelated edits. Do not publish twice through both paths.
5. Check the GitHub Pages build/deployment for the exact pushed commit, and
   confirm the affected live page when practical. Fix deployment failures caused
   by the task and publish the correction. Report the commit, deployment result,
   and live page link. A successful push alone does not confirm publication.

Never save credentials in the repository. If neither local Git nor the connected
GitHub account can publish, report the sign-in needed, retain completed local
work, and clearly report what remains unpublished.

This instruction runs after completed Codex tasks. It is not an unattended
watcher that publishes every local file save.
