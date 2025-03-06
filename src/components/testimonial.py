from st.components.v1 import html

def display_testimonials(testimonials):
    testimonial_html = """
    <div style="margin: 20px; padding: 10px; border: 1px solid #ccc; border-radius: 5px;">
        <h3>Testimonials</h3>
    """
    
    for testimonial in testimonials:
        testimonial_html += f"""
        <div style="margin-bottom: 15px;">
            <p><strong>{testimonial['name']}</strong>: {testimonial['message']}</p>
        </div>
        """
    
    testimonial_html += "</div>"
    
    html(testimonial_html)

# Example usage
# testimonials = [
#     {"name": "Dr. Theodore", "message": "Clement is a brilliant problem solver! His final year project was truly innovative."},
#     {"name": "Classmate A", "message": "Working with Clement was a great experience. He is very dedicated."}
# ]
# display_testimonials(testimonials)