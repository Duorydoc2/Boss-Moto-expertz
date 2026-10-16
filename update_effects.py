import os

with open('gallery.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix line endings
content = content.replace('\r\r\n', '\n').replace('\r\n', '\n')

old_css_start = content.find('.masonry-item {')
old_css_end = content.find('/* Lightbox */')

new_css = '''
    .masonry-item {
      display: inline-block;
      width: 100%;
      margin-bottom: 1.5rem;
      border-radius: 16px;
      overflow: hidden;
      position: relative;
      cursor: pointer;
      background: var(--navy);
      border: 1px solid rgba(255, 255, 255, 0.05);
      transition: all 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
    }

    .masonry-item:hover {
      transform: translateY(-8px);
      box-shadow: 0 20px 40px rgba(0,0,0,0.6), 0 0 20px rgba(250, 114, 50, 0.2), 0 0 0 1px var(--orange);
      z-index: 10;
    }

    .masonry-item img {
      width: 100%;
      height: auto;
      display: block;
      transition: transform 0.7s cubic-bezier(0.25, 1, 0.5, 1), filter 0.5s ease;
      object-fit: cover;
      will-change: transform, filter;
    }

    .masonry-item:hover img {
      transform: scale(1.08);
      filter: blur(2px) brightness(0.7);
    }

    .masonry-overlay {
      position: absolute;
      inset: 0;
      background: linear-gradient(to top, rgba(6,35,45,0.95) 0%, rgba(6,35,45,0.6) 40%, transparent 100%);
      opacity: 0;
      transition: opacity 0.5s ease;
      display: flex;
      align-items: flex-end;
      padding: 1.5rem;
      pointer-events: none;
    }

    .masonry-item:hover .masonry-overlay {
      opacity: 1;
    }

    .masonry-info {
      transform: translateY(20px);
      transition: transform 0.5s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.5s ease;
      opacity: 0;
      width: 100%;
    }

    .masonry-item:hover .masonry-info {
      transform: translateY(0);
      opacity: 1;
    }

    .masonry-info .tag {
      display: inline-block;
      font-family: var(--font-heading);
      font-size: 0.75rem;
      font-weight: 700;
      letter-spacing: 0.15em;
      color: #fff;
      background: var(--orange);
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
      text-transform: uppercase;
      margin-bottom: 0.5rem;
      box-shadow: 0 4px 10px rgba(250,114,50,0.4);
    }

    .masonry-info h4 {
      font-family: var(--font-heading);
      font-size: 1.25rem;
      font-weight: 700;
      color: var(--white);
      line-height: 1.3;
      text-shadow: 0 2px 4px rgba(0,0,0,0.8);
    }

    .zoom-icon {
      position: absolute;
      top: 1rem;
      right: 1rem;
      width: 44px;
      height: 44px;
      background: rgba(255,255,255,0.1);
      backdrop-filter: blur(8px);
      border: 1px solid rgba(255,255,255,0.2);
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.2rem;
      color: #fff;
      opacity: 0;
      transform: scale(0.5) rotate(-45deg);
      transition: all 0.5s cubic-bezier(0.25, 1, 0.5, 1);
    }

    .masonry-item:hover .zoom-icon {
      opacity: 1;
      transform: scale(1) rotate(0deg);
      background: var(--orange);
      border-color: var(--orange);
      box-shadow: 0 4px 15px rgba(250, 114, 50, 0.5);
    }

    '''

content = content[:old_css_start] + new_css + content[old_css_end:]

with open('gallery.html', 'w', encoding='utf-8', newline='\n') as f:
    f.write(content)
print("CSS Effects Updated!")
