# Tweakers Smileys Archive

An archive of all Tweakers.net forum smileys: the complete official SVG set, every legacy GIF, and three animated GIF → SVG conversions we made with an LLM.

**🌐 View the archive online:** https://kduvekot.github.io/tweakers-smileys

## Status: complete (17 November 2026)

This repo started in January 2026 as an experiment in LLM-assisted conversion of the animated GIF smileys to SVG. At that time Tweakers served 38 smileys as SVG and 26 as animated GIF. We converted three of them ourselves (`yes`, `no` and `lol`, see [`conversion-history/`](conversion-history/)).

On **26 October 2026** Tweakers released SVG versions of the remaining 26 themselves, so **all 64 smileys are now official SVGs** (25 of them animated with CSS). No smileys were added or removed. The original goal has been reached by Tweakers, so this repo is now a finished archive.

## Contents

| Folder | Files | What it holds |
|--------|-------|---------------|
| `tweakers-smileys/svg/` | 64 | The complete official SVG set, downloaded from `tweakers.net/g/s/` on 17 Nov 2026 |
| `tweakers-smileys/old-gif/` | 61 | Every legacy GIF: 35 replaced before Jan 2026, 26 replaced between Jan and Nov 2026 |
| `tweakers-smileys/new-svg/` | 3 | Our own conversions of `yes`, `no` and `lol` (Jan 2026) |
| `tweakers-smileys/tweak.zip` | 1 | The original January 2026 download (38 SVG + 26 GIF) |
| `conversion-history/` | | Frame analyses, logs and session transcripts of our three conversions |

`henk`, `ok` and `tweakers` never had a GIF version, which is why there are 61 legacy GIFs for 64 smileys.

Files keep their original Tweakers names, e.g. `smile.svg` and `smile.gif`.

## Changes found between January and November 2026

- **26 GIFs became SVG:** belgie, bonk, bonk3, bye, facepalm, farewell, frusty, hup, hypocrite, knuf, lol, loveys, no, nopompom, nosmile, oranje, pompom, pukey, rozewolk, shadey, shutup, sintsmiley, sleepey, sleephappy, yawnee, yes. All except shadey, sintsmiley and sleephappy are animated.
- **36 of the 38 existing SVGs are unchanged.**
- **shiny and worshippy** changed only in how their CSS is written (renamed keyframes, classes instead of inline styles). The drawing and the animation are the same. The January versions remain in git history.

## When Tweakers made the changes

The SVGs contain no dates or editor metadata, but the server's `Last-Modified` headers (read with a bookmarklet on 17 Nov 2026) do:

| Files | `Last-Modified` (UTC) | Meaning |
|-------|-----------------------|---------|
| All 26 new SVGs | Mon 26 Oct 2026, 08:34:59 | Released together in one deployment (09:34 Amsterdam time) |
| shiny, worshippy | Tue 27 Oct 2026, 15:50:05 | Follow-up the next day: CSS rewritten in the same style as the new batch |
| smile (reference) | Tue 5 Dec 2023, 13:12:41 | From the original vector redesign (Development-iteratie #270, Oct 2023) |
| henk (reference) | Mon 30 Jun 2025, 11:37:05 | Updated separately in 2025 |

These dates show when the files were placed on the server, not when they were drawn. The 26 new SVGs also share a format none of the older ones use (an explicit `viewBox` on a 15-unit grid, `fill="none"`, and minified CSS with generated class names like `e0`), which also points to one batch made with the same tool.

## How the files were collected

Tweakers' firewall blocks cloud servers, so the files were downloaded in a normal browser and uploaded to the repo:

- **January 2026:** a browser console script (`scripts/download-smileys-iframe.js`) opened every file for saving. The legacy GIFs were found by trying the `.gif` name for each `.svg`.
- **November 2026:** a bookmarklet run on tweakers.net fetched all 64 SVGs from `/g/s/` into one JSON file, which was split into separate files here.

## License

These smileys are property of Tweakers.net.
