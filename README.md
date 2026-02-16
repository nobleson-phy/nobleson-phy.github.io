# Research Profile Website

A Jekyll-based research profile website for GitHub Pages.

## Features

- Clean, academic-focused design
- Responsive layout that works on all devices
- Easy-to-update content using Markdown
- Separate pages for:
  - Home/Research introduction
  - About research
  - Publications (with optional .bib file support)
  - Talks & presentations
  - Conferences & workshops
  - Curriculum Vitae
  - Teaching
- Compatible with GitHub Pages

## Setup Instructions

1. **Upload to GitHub**: Create a new repository and upload all files
2. **Enable GitHub Pages**:
   - Go to repository Settings
   - Navigate to "Pages" section
   - Select "main" branch as source
   - Save changes
3. **Customize Content**:
   - Edit `_config.yml` with your information
   - Update each page (`.md` files) with your content
   - Replace placeholder text and links
4. **Add Publications**:
   - Edit `papers.md` manually, OR
   - Uncomment jekyll-scholar in `_config.yml` and `Gemfile`
   - Add your publications to `_bibliography/papers.bib`

## Local Development

1. Install Ruby and Bundler
2. Run `bundle install`
3. Run `bundle exec jekyll serve`
4. Visit `http://localhost:4000`

## Customization

- Edit CSS in `_sass/main.scss` and `assets/css/style.scss`
- Modify layouts in `_layouts/` directory
- Update navigation in `_data/navigation.yml`

## License

This project is available as a template for academic use.