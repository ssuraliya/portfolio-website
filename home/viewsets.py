from wagtail.snippets.views.snippets import SnippetViewSet



class WorkExperienceCreateViewSet(SnippetViewSet):
    icon = "desktop"
    menu_label = "Work Experience"
    menu_name = "Work Experience"
    menu_order = 100
    add_to_admin_menu = True
    
class ProjectsCreateViewSet(SnippetViewSet):
    icon = "code"
    menu_label = "Projects"
    menu_name = "Projects"
    menu_order = 100
    add_to_admin_menu = True