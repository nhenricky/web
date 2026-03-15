from nicegui import ui 

#Avtar oficial and Links
ui.dark_mode().enable()
ui.avatar('img:https://nicegui.io/logo_square.png', color='blue-5')
ui.link('Definição de Teologia', 'https://pt.wikipedia.org/wiki/Teologia')
ui.link('Teologia Bíblica - Wikipédia', 'https://pt.wikipedia.org/wiki/Teologia_b%C3%ADblica')

#Title
ui.markdown('Introdução à Teologia').classes('text-2xl font-bold text-center w-full')

with ui.column().classes('w-full items-center'):

    with ui.card().classes('w-[350px] p-6'):
        ui.label(
            'O termo "teologia" não aparece na Bíblia. Surgiu na Grécia antiga, '
            'mas o seu conceito epistemológico é encontrado nas páginas das '
            'Sagradas Escrituras. Deus é revelado em Gênesis capítulo 1, versículo 1, '
            'onde Ele é apresentado como o Criador de todas as coisas.\n\n'

            'Os pensadores da Grécia Antiga buscavam compreender a origem de todas '
            'as coisas por meio da razão. Para eles, o universo possuía uma ordem '
            'racional que podia ser investigada pela filosofia.\n\n'

            'Assim, as questões sobre a natureza divina não eram tratadas apenas '
            'como mitologia, mas também como um tema de reflexão intelectual. '
            'Essa busca por entender a realidade última abriu caminho para o '
            'desenvolvimento daquilo que mais tarde seria chamado de teologia.\n\n'

            'Entre os filósofos gregos surgiu também o conceito de logos, que '
            'significa razão, palavra ou princípio racional. Para pensadores como '
            'Heráclito, o logos era a lei universal que governava o cosmos. '
            'Mais tarde, esse conceito seria reinterpretado no contexto cristão, '
            'especialmente no prólogo do Evangelho de João, onde o Logos é '
            'identificado com o próprio Cristo.\n\n'

            'Quando o cristianismo começou a se desenvolver no mundo mediterrâneo, '
            'ele encontrou um ambiente cultural profundamente influenciado pela '
            'filosofia grega. Muitos teólogos utilizaram conceitos filosóficos '
            'gregos para explicar doutrinas cristãs. Dessa forma, a filosofia '
            'grega acabou servindo como uma ferramenta intelectual para a '
            'formulação de conceitos teológicos ao longo da história.'
            ).classes('text-justify leading-relaxed text-base')


ui.label('By Natã Henrique')
ui.label('@2026').classes('text-sm text-gray-500')
ui.run()
