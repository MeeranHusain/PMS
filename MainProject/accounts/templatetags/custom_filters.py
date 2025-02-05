# myapp/templatetags/custom_filters.py
# from django import template

# register = template.Library()

# @register.filter
# def add_class(field, css_class):
#     """
#     Adds a CSS class to a form field's widget.
#     """
#     if hasattr(field, 'widget'):
#         # Get the current class from the widget's attrs
#         existing_classes = field.widget.attrs.get('class', '')
#         new_classes = f'{existing_classes} {css_class}'.strip()
#         field.widget.attrs['class'] = new_classes
#     return field
