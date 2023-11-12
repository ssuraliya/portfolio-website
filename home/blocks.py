from wagtail import blocks


class BaseStructBlock(blocks.StructBlock):
    id = blocks.CharBlock(
        null=True,
        required=False,
        help_text="ID of this block. Can be used to link the block in header",
    )


class NameSection(BaseStructBlock):
    name = blocks.CharBlock(required=True)
    position = blocks.CharBlock(required=True)
    company_name = blocks.CharBlock(required=True)    
    
    class Meta:
        template = "blocks/name_section.html"

class PortfolioStreamBlock(blocks.StreamBlock):
    name_section = NameSection()
