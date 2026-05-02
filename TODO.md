# shepherdresearchlab — TODO

Working list of outstanding items. Excluded from the Jekyll build via
`_config.yml`, so this file lives in the repo but never appears on the
live site. Use `- [ ]` checkboxes; GitHub renders them as tickable in
the web UI.

For tactical, code-adjacent reminders, prefer an `<!-- TODO: ... -->`
comment right next to the relevant code instead of an entry here.

Larger phase-level items (DNS cutover, 3DO host, oversize PLYs, etc.)
are tracked in the README's status checklist — keep them there, not
here. This file is for the next-action items.

## Site-wide

- [ ] Set a branded "Subscribe thank you" page in Mailchimp for the SRL
  audience (`9fe54583c5`), so footer subscribers don't see Mailchimp
  default chrome after submitting
- [ ] Confirm Formspree `xvzlgwae` (join-a-study) routing destination
  and restore a specific recipient comment in `join-a-study/index.md`
  (the previous comment named `bodycompstudies@cc.hawaii.edu` for the
  old placeholder ID)

## End-to-end smoke tests

- [ ] Footer "Stay in the loop" → confirm signup lands in SRL audience
  (`9fe54583c5`), **not** the IBDW audience
- [ ] `/contact/` Formspree (`xpqbwyde`) → confirm submission email
- [ ] `/join-a-study/` Formspree (`xvzlgwae`) → confirm submission email
- [ ] `/shapeup/3do-bodycomp-analyzer/` Formspree (`xdabkwzg`) → confirm
  submission email

## Done

(Move completed items here with the date and PR/commit, or just delete
them — whichever you prefer.)
