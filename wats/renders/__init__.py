from wats.renders.tree_render import tree_render
from wats.renders.plain import plain_render


def pick_render(style):
    if style == "tree":
        return tree_render
    if style == "plain":
        return plain_render
