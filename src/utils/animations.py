def fade_in(element, duration=0.5):
    """Apply a fade-in effect to the specified element."""
    element.style.transition = f"opacity {duration}s"
    element.style.opacity = 0
    element.style.opacity = 1

def scroll_animation(element, offset=100):
    """Apply a scroll animation effect to the specified element."""
    if element.getBoundingClientRect().top < window.innerHeight - offset:
        element.style.transition = "transform 0.5s ease-in-out"
        element.style.transform = "translateY(0)"
    else:
        element.style.transform = "translateY(50px)"  # Start position for animation

def hover_effect(element):
    """Add hover effect to the specified element."""
    element.style.transition = "transform 0.3s"
    element.onmouseover = lambda: element.style.transform = "scale(1.05)"
    element.onmouseout = lambda: element.style.transform = "scale(1)"