# Website maintenance

This is a Jekyll / Academic Pages website for Leiting Zhang.
The publishing repository is `leitingzhang/leitingzhang.github.io`.
The live site is `https://leitingzhang.com`, published from `master` at `/`.
`upstream` is the template repository; publish only to `origin`.

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
