# Claude Code Guide for nobleson-phy.github.io

This guide streamlines updates to the research website and CV. Follow these instructions for common tasks.

## Directory Structure

```
/
├── index.md                          # Home page with Recent News section
├── cv.md                             # Markdown CV (long-form)
├── papers.md                         # Publications page (pulls from _papers collection)
├── generate_cv.py                    # Python script to generate Research_CV.pdf
├── _papers/                          # Paper collection (Jekyll)
│   └── YYYY-MM-paper-title.md       # Individual paper entries
├── _bibliography/papers.bib          # BibTeX bibliography (reference only)
└── Research_CV.pdf                   # Generated PDF CV (published to web)
```

## Adding New Publications

### When Adding New Papers:

1. **Get paper metadata** from arXiv or journal (title, authors, abstract, DOI, arXiv ID)

2. **Create paper file** in `_papers/` directory:
   - Filename: `YYYY-MM-short-title.md` (e.g., `2026-09-pulsar-timing.md`)
   - Copy format from existing file in `_papers/` directory
   - Set `type: journal` for accepted papers, `type: preprint` for under-review
   - Include complete author list in YAML format
   - Include abstract
   - Set `status: accepted` or `status: under-review`

3. **Update index.md** - Add to "Recent News" section:
   ```
   - **[Date]**: [Paper title] accepted at [Journal] - [arXiv link if applicable]
   ```

4. **Update bibliography** (optional, for reference):
   - Add entry to `_bibliography/papers.bib` following BibTeX format

5. **Commit and push**:
   ```bash
   git add _papers/ index.md
   git commit -m "Add [Paper Title] paper"
   git push
   ```

## Updating Research Positions

### When Position Changes:

1. **Update cv.md**:
   - Add new position entry under "Research Positions" section
   - Format: Institution, Location, Date range, Bullet points of work

2. **Update generate_cv.py**:
   - Add corresponding position entry in the PDF generation script
   - Keep position list in reverse chronological order (newest first)

3. **Update index.md**:
   - Change `hero_position` to current position title
   - Add to "Recent News" section if promotion/new position

4. **Commit and push**:
   ```bash
   git add cv.md generate_cv.py index.md
   git commit -m "Update research positions"
   git push
   ```

## Regenerating the CV PDF

When CV content changes:

```bash
python3 generate_cv.py
git add Research_CV.pdf
git commit -m "Regenerate CV PDF with updated information"
git push
```

The PDF is auto-generated from `generate_cv.py` and includes:
- All research positions
- Education history
- Selected publications (hardcoded list)
- Teaching experience
- Professional memberships
- Talks and presentations

## Paper File Format Reference

```yaml
---
title: "Paper Title Here"
type: journal  # Options: journal, preprint, conference, chapter
year: 2026
authors:
  - "First, Author"
  - "Second, Author"
  - "Third, Author"
journal: "Journal Name"
volume: 53
issue: 1  # Optional
pages: "100-120"  # Optional
doi: "10.1234/example"
arxiv: "2608.12345"  # Without "arXiv:" prefix
pdf: ""  # URL to PDF if available
abstract: >
  Full abstract text goes here. Can span multiple lines.
  Use the `>` to preserve line breaks.
bibtex: |
  @article{FirstAuthor2026,
    ...bibtex entry...
  }
status: accepted  # Options: accepted, under-review, forthcoming, in-preparation
---
```

## Recent News Section Format

In `index.md`, format news entries as:
```markdown
## Recent News

- **[Month Year]**: [Description of achievement/paper] - [Link if applicable]
- **[Month Year]**: Paper accepted at [Journal]: "[Title]" - [arXiv/DOI link]
```

Keep in reverse chronological order (newest first).

## Website Build & Deployment

- **GitHub Pages** automatically rebuilds when you push changes
- **Build time**: Usually 1-2 minutes
- **Check build status**: Go to repo → Actions tab
- **Clear browser cache** if updates don't appear immediately

## Quick Checklist for Paper Additions

- [ ] Retrieve metadata from arXiv/journal (title, authors, abstract, DOI, arXiv ID)
- [ ] Create `_papers/YYYY-MM-*.md` file with complete information
- [ ] Update `index.md` Recent News section
- [ ] (Optional) Add to `_bibliography/papers.bib`
- [ ] Commit with message: "Add [Paper Title]"
- [ ] Push to remote
- [ ] Verify on https://nobleson-phy.github.io/papers/

## Quick Checklist for Position Updates

- [ ] Update `cv.md` Research Positions section
- [ ] Update `generate_cv.py` Research Positions section
- [ ] Update `index.md` hero_position field and Recent News
- [ ] Run: `python3 generate_cv.py`
- [ ] Commit CV files and PDF
- [ ] Push to remote
- [ ] Verify on https://nobleson-phy.github.io/cv/

## Contact Information Updates

If email, office, or department changes:
- Update in `index.md` Contact Information section
- Update in `generate_cv.py` contact line (line ~48)
- Commit and push

## Important Notes

- **Author format**: "Last, First" in YAML lists (e.g., "Nobleson, K.")
- **arXiv IDs**: Use format YYMM.XXXXX (e.g., 2608.12345)
- **Abstracts**: Can be truncated for preprints, but use full text for journal papers
- **Links**: Use relative URLs for internal links, absolute URLs for external
- **Special characters**: Use HTML entities or markdown escape sequences if needed

## Next Steps When User Provides Updates

1. Extract all information provided (papers, positions, dates)
2. Create/update necessary files following formats above
3. Generate PDF if CV-related
4. Commit all changes with descriptive message
5. Push to remote
6. No need for extensive back-and-forth—structure is predefined

