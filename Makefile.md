# Build and Serve Local Book Edition

This Makefile provides targets to build and serve the static book reader edition locally using `mdBook`.

## Architecture & Publishing Flow



- **Source Material:** Raw chapter files with agent notes live in `chapters/`.
- **Clean Reader Build (`src/`):** A dedicated preprocessing step strips out internal Agent First-Pass Validation & Revision notes from chapters and syncs `README.md` to `src/index.md` so that reviewers and readers see only polished book text.

## Usage




* **Build the book:**
  ```bash
  make build
  ```




* **Serve the book locally (live preview on http://localhost:3000):**
  ```bash
  make serve
  ```




* **Clean generated static assets:**
  ```bash
  make clean
  ```
