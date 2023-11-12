from wagtail import blocks
from wagtail.snippets.blocks import SnippetChooserBlock


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
        
class AboutMeSection(BaseStructBlock):
    content = blocks.RichTextBlock(required=True)
    
    class Meta:
        template = "blocks/about_me.html"

class WorkExperienceSection(BaseStructBlock):
    works = blocks.ListBlock(SnippetChooserBlock('home.WorkExperience'))

    class Meta:
        template = "blocks/work_experience.html"


class PortfolioStreamBlock(blocks.StreamBlock):
    name_section = NameSection()
    about_me = AboutMeSection()
    work_experience = WorkExperienceSection()
