# SEARCH group website

Repository with the homepage of the SEARCH research group, part of the Bernoulli Institute, Faculty of Science and engineering of the university of Groningen.

The website is built with [Jekyll](https://jekyllrb.com/) and the style is inspired on the theme [Jekyll Serif](https://github.com/zerostaticthemes/jekyll-serif-theme) by [Zerostatic](https://www.zerostatic.io).

## Running locally

If you know your way around Jekyll, you know what to do to serve the it locally. If you don't, the simplest way is to:
1. Install [Docker Desktop](https://www.docker.com/products/docker-desktop/).
1. Start Docker Desktop.
1. Start Jekyll container in the `scripts` directory:
   - Linux/Mac
     ```bash
     bash scripts/jekyll_debug.sh
     ```
   - Windows PowerShell
     ```ps1
     .\scripts\jekyll_debug.ps1
     ```
1. Open the website in your browser at http://localhost:4000.
