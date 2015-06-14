from django import template
from django_components.component import registry

register = template.Library()

@register.simple_tag(name="component_dependencies")
def component_dependencies_tag():
    out = []
    for component_class in registry._registry.values():
        out.append(component_class.render_dependencies())

    return "\n".join(out)

@register.simple_tag(name="component")
def component_tag(name, *args, **kwargs):
    component_class = registry._registry[name]
    component = component_class()
    return component.render(*args, **kwargs)
