# Legal D+ Bio Page Implementation Plan

> **For agentic workers:** Execute inline using superpowers:executing-plans. Steps use checkbox tracking.

**Goal:** Build and privately publish the link-in-bio page specified by the Legal D+ PRD and design system.
**Architecture:** Static HTML with the approved CSS, original venue imagery and five external action cards. The compiled HTML embeds its font and hero image so it can also be opened or hosted independently.
**Tech Stack:** HTML, CSS, minimal JavaScript, Python source assembly, Sites static hosting.
**Spec:** docs/PRD-Legal-Dmais-Link-na-Bio.md and docs/Design-System-Legal-Dmais.md.

## Global Constraints

- Preserve banner, three quick links, five cards and footer.
- Container maximum 430 px, Nunito and colors specified in the design system.
- WhatsApp +55 27 98883-1009; Instagram and Maps use supplied URLs.
- Do not publish unconfirmed prices, capacity, opening hours or review counts.
- Main CTA visible at the 390 x 844 px reference viewport.
- No booking, payment or form features beyond the approved link page.

## Review Focus

- Narrow screen and larger text: no horizontal overflow or clipped copy.
- Keyboard: visible focus and meaningful link names.
- WhatsApp messages: accents, plus sign in the brand, editable date and guest fields.
- Portable HTML: font and main photograph load without local external files.
- Publication: native Site ID, exact pushed source and owner-private audience.

## Task 1: Implement and verify the page

**Files:** src/content.json; src/style.css; src/page.html; src/assets/*; scripts/build.py; scripts/verify.py; dist/index.html; dist/assets/social.jpg; README.md.
**Interfaces:** source files compile to a standalone dist/index.html; five cards consume the destination map in content.json.

- [x] Prepare assets and approved source documents.
- [x] Implement the page and generate the static output.
- [x] Validate HTML, URLs, messages, embedded assets, JavaScript syntax and initial size.
- [x] Inspect the mobile and desktop page through the managed preview.
- [x] Review the complete change and address material findings.
- [ ] Package the pushed source and privately deploy the new Site.

## Execution notes

This is an isolated new Site, created for this request. The native Sites workflow owns source synchronization and commit/push. Document/content checks and browser inspection provide verification appropriate to this static page.


## Verification evidence

- Build and static verification: five cards, three quick links, three footer links, embedded font and hero, valid WhatsApp messages, resolved CSS variables, valid JavaScript.
- Managed browser inspection: 320, 390 and 430 px iframe viewports, each 844 px tall; no horizontal overflow or clipped text. The primary card ends at 513.4 px in the 390 px frame (375 px content width with a desktop scrollbar).
- Text at 200% in a 390 px frame: card height grows; no horizontal overflow or clipped text.
- Desktop: 1363 x 936 px viewport; hero photograph and Nunito load; all five cards and footer inspected.
- Keyboard: fourth Tab reaches the primary card, with a visible 3 px outline and 3 px offset.
- Temporary browser QA fixtures were removed from dist before packaging.
- The local runtime could not encode WOFF2 because its optional Brotli encoder is absent. The official variable Nunito font is embedded as WOFF instead and was confirmed loaded in the browser.

## Final review

A fresh read-only review found no critical or important issues. The sole minor finding was the social-sharing image: this private demonstration deliberately uses the original 680 x 453 facade photo rather than a new 1200 x 630 brand composition. Metadata accurately declares the actual image size. A dedicated sharing composition can be added when the business approves its final branding. Browser presentation, text growth and keyboard focus were independently checked as recorded above. External account ownership and WhatsApp service availability were not remotely reverified; destinations reproduce the supplied prospect data. Native publication will verify the selected Site and preserve its owner-private audience.
