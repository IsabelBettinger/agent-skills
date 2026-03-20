# Web Components Skill

Reusable HTML/CSS components for building professional portfolio websites.

## Design System

### Colors

| Variable | Hex | Usage |
|----------|-----|-------|
| `--bg` | `#F7F4EF` | Main background |
| `--bg2` | `#EDE9E2` | Section backgrounds |
| `--bg3` | `#E2DDD5` | Image placeholders |
| `--card` | `#FFFFFF` | Cards/containers |
| `--text` | `#1C1917` | Headings/body |
| `--muted` | `#78716C` | Secondary text |
| `--hint` | `#A8A29E` | Labels/hints |
| `--accent` | `#1D4ED8` | Primary brand blue |
| `--accent-light` | `#DBEAFE` | Tags/badges |

### Typography

- **Display/Headings**: Plus Jakarta Sans, 600-700 weight
- **Body**: Plus Jakarta Sans, 400-500 weight
- **Scale**: clamp() for fluid sizing

### Spacing

- Section padding: 6rem (96px)
- Container max-width: 1080px
- Card padding: clamp(2rem, 5vw, 3.5rem)
- Grid gap: 1.25rem

## Components

### Navigation

```html
<nav class="nav">
  <div class="container nav-inner">
    <a href="index.html" class="nav-logo">Your Name</a>
    <ul class="nav-links">
      <li><a href="#about">About me</a></li>
      <li class="nav-item">
        <a href="#projects">Projects ▾</a>
        <div class="dropdown">
          <a href="project.html">Project Name</a>
        </div>
      </li>
      <li><a href="#contact">Contact</a></li>
    </ul>
    <button class="hamburger" id="hamburger">
      <span></span><span></span><span></span>
    </button>
  </div>
</nav>
```

### Project Card

```html
<a href="project.html" class="proj-card">
  <div class="proj-img">
    <img src="project-image.png" alt="Project Name">
  </div>
  <div class="proj-body">
    <div class="proj-tags">
      <span class="proj-tag">Category</span>
    </div>
    <div class="proj-title">Project Name</div>
    <p class="proj-desc">Brief description of the project.</p>
    <span class="proj-link">Learn more <i class="fas fa-arrow-right"></i></span>
  </div>
</a>
```

### Timeline

```html
<div class="timeline">
  <div class="tl-item">
    <div class="tl-date">2024 — Present</div>
    <div class="tl-title">Job Title</div>
    <div class="tl-company">Company Name</div>
    <ul class="tl-list">
      <li>Achievement with metric</li>
      <li>Another key contribution</li>
    </ul>
  </div>
</div>
```

### Contact Link

```html
<a href="https://linkedin.com/in/username" target="_blank" class="contact-link">
  <i class="fab fa-linkedin"></i>
  <div>
    <div>Connect on LinkedIn</div>
    <div class="cl-label">linkedin.com/in/username</div>
  </div>
  <i class="fas fa-arrow-right"></i>
</a>
```

### Education Card

```html
<div class="edu-card">
  <div>
    <div class="edu-title">Degree or Certificate</div>
    <div class="edu-inst">Institution Name</div>
    <ul class="edu-list">
      <li>Relevant coursework or details</li>
    </ul>
  </div>
  <div class="edu-year">2020 – 2024</div>
</div>
```

### Skills Section

```html
<div class="skills-outer">
  <div>
    <div class="skill-group-title">Category</div>
    <ul class="skill-list">
      <li>Skill 1</li>
      <li>Skill 2</li>
    </ul>
  </div>
</div>
```

### Accordion

```html
<div class="accordion">
  <div class="ac-item">
    <button class="ac-trigger">
      <span class="ac-label"><i class="fas fa-icon"></i> Title</span>
      <i class="fas fa-chevron-down ac-icon"></i>
    </button>
    <div class="ac-body">
      <p>Content goes here.</p>
    </div>
  </div>
</div>
```

### Process Steps

```html
<div class="process-steps">
  <div class="process-step">
    <div class="step-num">1</div>
    <div class="step-body">
      <h4>Step Title</h4>
      <p>Description of the step.</p>
    </div>
  </div>
</div>
```

### Value Pillars

```html
<div class="pillars">
  <div class="pillar">
    <div class="pillar-icon"><i class="fas fa-icon"></i></div>
    <h4>Title</h4>
    <p>Description of the pillar.</p>
  </div>
</div>
```

## Animations

### Fade In on Scroll

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.55s var(--ease), transform 0.55s var(--ease);
}
.reveal.visible {
  opacity: 1;
  transform: none;
}
```

```javascript
const observer = new IntersectionObserver((entries) => {
  entries.forEach(e => { if (e.isIntersecting) { e.target.classList.add('visible'); } });
}, { threshold: 0.1 });
document.querySelectorAll('.reveal').forEach(el => observer.observe(el));
```

### Hover Effects

```css
/* Card hover */
.proj-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 30px rgba(0,0,0,0.09);
}

/* Button hover */
.btn-primary:hover {
  opacity: 0.85;
  transform: translateY(-1px);
}

/* Contact link hover */
.contact-link:hover {
  transform: translateX(4px);
}
```

## Responsive Breakpoints

```css
@media (max-width: 768px) {
  .nav-links { display: none; }
  .hamburger { display: flex; }
  .hero-grid { grid-template-columns: 1fr; }
  .skills-outer { grid-template-columns: 1fr; }
  section { padding: 4rem 0; }
}
```
