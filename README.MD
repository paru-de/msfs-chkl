# A simple website for MSFS checklists

[Github page](https://paru-de.github.io/msfs-chkl/)

## Intro

This repository contains a simple website with checklists for my most-used planes. Checklists are adapted from other sources, and a link to the original document is provided.

I was tired of having to search and open PDF's all over the place, with inconsistent formatting, so I decided to bundle everything in one organized place. I also wanted to keep it simple - no additional programs running in the background, no servers or npm packages required: a browser is all this needs.

These checklists don't aim to be exhaustive, nor are they intended for anything beyond casual simming. I'm not a pilot, and you will most likely find some egregious mistakes. They do however fulfill their purpose of getting me from A to B nicely. If you find mistakes, feel free to open an issue.

**Disclaimer**: I'm not a hackerman, and most of the code in this repository was written by an LLM.

## Converting MD to html

The provided Python script, located in the ./md directory, converts Markdown files into HTML. Simply drag and drop a \*.md file onto the script, and you'll find the converted HTML in the ./checklists directory. Note: You still have to manually add the generated checklist HTML to the index page.

For proper formatting, see the provided ./md/example-formatting.md.
A Python installation is required.
