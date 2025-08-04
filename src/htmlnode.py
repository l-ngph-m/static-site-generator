class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, prop=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.prop = prop

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        result = ""
        for prop in self.prop.items():
            result += f' {prop[0]}="{prop[1]}"'

        return result

    def __repr__(self):
        return f"""
                {self.tag}
                {self.value}
                {self.children}
                {self.prop}
        """


class LeafNode(HTMLNode):
    def __init__(self, tag, value, prop=None):
        super().__init__()
        self.tag = tag
        self.value = value
        self.prop = prop

    def to_html(self):
        if not self.value:
            raise ValueError("Value must not be empty")

        if not self.tag:
            return f"{self.value}"

        if not self.prop:
            return f"<{self.tag}>{self.value}</{self.tag}>"

        props = self.props_to_html()
        return f"<{self.tag} {props}>{self.value}</{self.tag}>"


class ParentNode(HTMLNode):
    def __init__(self, tag, children, prop=None):
        super().__init__()
        self.tag = tag
        self.children = children
        self.prop = prop

    def to_html(self):
        if not self.tag:
            raise ValueError("Tag must not be empty")

        if not self.children:
            raise ValueError("Children must not be empty")

        result = ""
        for child in self.children:
            result += child.to_html()

        return f"<{self.tag}>{result}</{self.tag}>"
