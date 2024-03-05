# Bottle webserver in a Codespace

This repo shows problems when Bottle runs in a Codespace. To reproduce:

1. Run `bash btest.sh`, which executes the Bottle-based webserver. Click the "Open local browser" button, then browse to `<github_forwaded_address>/my-great-book.html` in the new tab. Note that the page doesn't fully load.
2. Run `python -m http.server`, click "open in local browser", browse to `<github_forwaded_address>/my-great-book.html` as before. The page loads.