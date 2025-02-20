from scripts.get_elements_by_template.get_blue_elements_by_template import(
    get_blue_elements_by_template,
)
from scripts.get_elements_by_template.get_red_elements_by_template import(
    get_red_elements_by_template,
)
from scripts.get_elements_by_template.get_template_color import(
    get_color_from_template,
)
from scripts.configs import(
    RED, BLUE, UNKNOWN,
)

def get_elemets_by_template(template_path: str, image_path: str) -> str:
    
    template_color = get_color_from_template(
        template_path=template_path
    )
    if template_color == RED:
        get_red_elements_by_template(
            image_path=image_path,
            template_path=template_path
        )
    elif template_color == BLUE:
        get_blue_elements_by_template(
            image_path=image_path,
            template_path=template_path
        )
    elif template_color == UNKNOWN:
        print('Неразспознанный цвет шаблона для поиска на черчеже')




image_path = 'media/drowing_images/extracted_drawing_27.png'


blue_template_path = 'media/elements/blue_square.png'
red_template_path = 'media/elements/red_square.png'

blue_image_path = 'media/detect_elements/blue_elements.png'
red_image_path = 'media/detect_elements/red_elements.png'

get_elemets_by_template(
    template_path=blue_template_path,
    image_path=blue_image_path
)
