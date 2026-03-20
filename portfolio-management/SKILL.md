# Portfolio Management Skill

Comprehensive skill for managing, updating, and optimizing personal portfolio websites.

## Capabilities

- Add/update/remove portfolio projects
- Manage navigation consistency across pages
- Optimize SEO metadata
- Update contact information and social links
- Maintain design system consistency
- Generate project case studies
- Manage image assets

## Workflow

### Adding a New Project

1. Create new HTML file: `projekt-{slug}.html`
2. Copy structure from existing project page
3. Update all sections:
   - Navigation links
   - Hero (title, subtitle, tags)
   - Content blocks (challenge, approach, result)
   - Sidebar metadata
   - "Next Project" link
4. Add project card to index.html
5. Update all navigation dropdowns
6. Add project image

### Updating Navigation

All pages must share the same navigation structure:

```html
<nav class="nav">
  <div class="container nav-inner">
    <a href="index.html" class="nav-logo">Your Name</a>
    <ul class="nav-links">
      <li><a href="index.html#about">About me</a></li>
      <li class="nav-item">
        <a href="index.html#projects">Projects <i class="fas fa-chevron-down"></i></a>
        <div class="dropdown">
          <a href="projekt-example.html">Example Project</a>
        </div>
      </li>
      <li><a href="index.html#contact">Contact</a></li>
    </ul>
  </div>
</nav>
```

### Design Tokens

```css
:root {
  --bg: #F7F4EF;
  --bg2: #EDE9E2;
  --bg3: #E2DDD5;
  --card: #FFFFFF;
  --text: #1C1917;
  --muted: #78716C;
  --hint: #A8A29E;
  --accent: #1D4ED8;
  --accent-light: #DBEAFE;
  --border: rgba(28,25,23,0.10);
  --border-hover: rgba(28,25,23,0.22);
}
```

## File Structure

```
portfolio/
├── index.html
├── projekt-{name}.html
├── project-{name}.png
├── favicon.svg
└── .nojekyll
```

## Deployment Checklist

- [ ] All navigation links work
- [ ] All images load correctly
- [ ] Favicon displays in browser tab
- [ ] Mobile menu functions properly
- [ ] GitHub Pages source set to main/root
- [ ] No broken links or 404s

## Commands

```bash
# Push changes
git add . && git commit -m "Update message" && git push origin main

# Check for broken links
# (manual verification via browser)
```

## Tips

- Always use `.nojekyll` to prevent GitHub Pages from processing HTML
- Keep design tokens in CSS variables for consistency
- Test on mobile viewport before deploying
- Use semantic HTML (nav, main, section, article)
- Optimize images before uploading (max 500KB)
