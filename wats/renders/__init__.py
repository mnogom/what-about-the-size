from wats.renders.tree_render import tree_render


def pick_render(style):
    if style == "tree":
        return tree_render