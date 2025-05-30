# Markdown Style Guide

## General Principles
- Use ATX-style headers (with #)
- Limit line length to 100 characters
- Use relative links for internal documentation
- Include alt text for all images

## Formatting
### Headers
```markdown
# H1 - Document Title
## H2 - Main Sections
### H3 - Subsections
```

### Links
```markdown
[Link Text](relative/path/to/file.md)
[External Link](https://example.com){:target="_blank"}
```

### Images
```markdown
![Alt Text](images/filename.png){:width="400px"}
```

### Code
````markdown
```language
code block
```
````

## Metadata (Front Matter)
```yaml
---
title: Document Title
description: Short description
created: YYYY-MM-DD
updated: YYYY-MM-DD
---
```