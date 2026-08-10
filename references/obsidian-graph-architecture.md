# Obsidian Graph Architecture & Knowledge Link Protocol

#reference #obsidian #graph-architecture #rbe-book

This reference establishes the mandatory standards for maintaining Obsidian Graph View connectivity across the Resource-Based Economy (RBE) book project vault.

---

## 1. Central Map of Content (MOC) Architecture
* **File Location**: `00-Book-Map-of-Content.md` in the vault root.
* **Role**: Acts as the central hub in Obsidian Graph View, connecting all chapters, master references, and thematic pillars into a single interlinked knowledge web.
* **Maintenance**: Whenever a new chapter version is created or a new pillar is established, `00-Book-Map-of-Content.md` MUST be updated immediately to point to the active file version.

---

## 2. Standardized Chapter Navigation & Tagging Header
Every active chapter file in `/chapters/` MUST start with a standardized header block containing:
1. Title (`# Chapter N: ...`)
2. Navigation block (`*Navigation*: [[00-Book-Map-of-Content|Map of Content]] | [[references/thematic-pillars-and-style-guide|Thematic Pillars Guide]] | [[Previous Chapter]] | [[Next Chapter]]`)
3. Topic Tags (`*Tags*: #rbe-book #monetary-critique ...`)
4. Divider line (`---`)

### Example:
```markdown
# Chapter 1: The Case for Change: Structural Failures of the Monetary Paradigm

*Navigation*: **[[00-Book-Map-of-Content|Map of Content]]** | **[[references/thematic-pillars-and-style-guide|Thematic Pillars Guide]]** | **[[chapters/02-introducing-resourceism-v5-guided-viz|Chapter 2: Introducing Resourceism →]]**  
*Tags*: #rbe-book #monetary-critique #debt-math #synthetic-selection #technological-leverage #mental-health

---
```

---

## 3. Bidirectional Reference Linking
* **Pillars Guide**: `references/thematic-pillars-and-style-guide.md` MUST maintain explicit wikilinks pointing to the active chapters (`[[chapters/01-the-case-for-change-v7-guided-viz|Ch. 1]]`) that expand each pillar.
* **Citation Index**: `references/rbe-agent-handoff-reference.md` is linked from the MOC and reference guides (`[[references/rbe-agent-handoff-reference|Master Reference]]`).
* **Chapter In-Line Links**: When chapters reference core concepts or transition frameworks, use inline wikilinks (e.g. `[[references/thematic-pillars-and-style-guide|Pillar 13: Synthetic Selection]]` or `[[chapters/03-un-transition-pathway-v5-guided-viz|Chapter 3]]`).

---

## 4. Graph View Settings & Hidden Archive Directory
* **Hidden Archive Directory**: Superseded chapter drafts live in `chapters/.archive/`. Because Obsidian automatically ignores hidden dot-directories (`.*`), historical drafts stay safely preserved on disk and in Git without cluttering the Graph View as unlinked orphan nodes.
* **Excluded Files Filter**: `.obsidian/app.json` includes `"userIgnoreFilters": ["chapters/.archive", ".archive", "chapters/_archive", "_archive"]` for complete exclusion.
* **Tags Enabled**: Ensure **Tags** are enabled in Graph Settings $\rightarrow$ Filters.
* **Color Grouping**:
  * `path:chapters` $\rightarrow$ Active Drafts
  * `path:references` $\rightarrow$ Knowledge Base & Citation Indexes
  * `#tag/topic` $\rightarrow$ Thematic Clusters
