from aiohttp import BasicAuth
from aiogram import types
from keyboards import ListOfButtons
from bucket import get_amount_of_products
from configparser import ConfigParser


config = ConfigParser()
config.read("config.ini")

#|------------------------- TOKENS --------------------|
TOKEN = config['token']['TOKEN']

#|------------------------- BOTS URL --------------------|
BOTS_URL = config['bot_url']['BOT_URL']

#|------------------------- ADMINS --------------------|
ADMINS_IDS = (config['chat_ids']['BOSS_ID'], config['chat_ids']['ARTYOM_ID'])
MANAGERS_GROUP_ID = config['chat_ids']['MANAGERS_GROUP_ID']

#|------------------- HEADERS ------------------|
HEADERS = {
    'accept': config['headers']['ACCEPT'],
    'user-agent': config['headers']['USER_AGENT']
}

#|-------------------- PROXIE ----------------|
PROXIE_URL = config['proxie']['PROXIE_URL']

PROXIE_LOGIN = config['proxie']['PROXIE_LOGIN']

PROXIE_PASSWORD = config['proxie']['PROXIE_PASSWORD']

PROXIE_AUTH = BasicAuth(
    login = PROXIE_LOGIN,
    password = PROXIE_PASSWORD
)

PROXIE_URL_W_AUTH = config['proxie']['PROXIE_URL_W_AUTH']

#|-------------------- PAYMENTS ----------------|

PAYMENTS_PROVIDER_TOKEN = config['payment']['PAYMENTS_PROVIDER_TOKEN']

SHIPPING_OPTIONS = [
    types.ShippingOption(id="pickup_shodnya", title="Самовывоз - Сходня").add(types.LabeledPrice("Самовывоз - Сходня", 1000)),
    types.ShippingOption(id="pickup_putilkovo", title="Самовывоз - Путилково").add(types.LabeledPrice("Самовывоз - Путилково", 1000)),
    types.ShippingOption(id="moscow_mkad", title="Доставка МКАД").add(types.LabeledPrice("Доставка МКАД", 50000)),
    types.ShippingOption(id="mkad15km", title="Доставка за МКАД").add(types.LabeledPrice("Доставка за МКАД", 70000)),
    types.ShippingOption(id="courier", title="Доставка курьером").add(types.LabeledPrice("Доставка курьером", 1000)),
]

#|-------------------- GOODS ----------------|

RESPIRATORS_LIST = """
Выберите номер респиратора из списка:
1. 3M™ 8101 Противоаэрозольная Фильтрующая Полумаска FFP1 NR D

2. 3M™ 8122 Противоаэрозольная Фильтрующая Полумаска FFP2 NR D, с клапаном выдоха

3. 3M™ VFlex® 9101 Противоаэрозольная Фильтрующая Полумаска класс защиты FFP1 NR D

4. 3M™ 8112 Противоаэрозольная Фильтрующая Полумаска FFP1 NR D, с клапаном выдоха

5. 3M™ Aura™ 9312+ Противоаэрозольная Фильтрующая маска класс защиты FFP1 NR D, с клапаном выдоха

6. 3М™ VFlex® 9162V противоаэрозольный фильтрующий респиратор, складная, с клапаном выдоха, класс защиты FFP2 NR D (12 ПДК)

7. 3M™ 9922P Специализированная Противоаэрозольная Фильтрующая Полумаска для защиты сварщика, класс защиты FFP2 NR D, с клапаном выдоха

8. Респиратор 3М™ 9926 / 9926P 2-ой класс защиты с угольным фильтром

9. 3M™ 7502 Полумаска серии 3М™ 7500 с фильтром, размер — средний (M)

10. Комплект сменных патронов 3М™ 6051 (А1) и предфильтров 5911 для масок и полумасок
"""

MASKS_LIST = """
Выберите номер защитной маски из списка:
1. Черная, тканевая маска

2. Белая, тканевая маска

3. Черные тканевые, многоразовые маски с принтами

4. Белые тканевые, многоразовые маски с принтами
"""

SUITS_LIST = """
Выберите номер зашитного костюма из списка:
1. Костюм для п/э-L-NOR-NPS
"""

GLOVES_LIST = """
Выберите номер защитных перчаток из списка:
1. Перчатки с резиновой облицовкой 10 класс

2. Перчатки нитриловые PROFLEX, черные, размер XL, упаковка 100 шт.

3. Перчатки нитриловые PROFLEX, черные, размер L, упаковка 100 шт.

4. Перчатки нитриловые PROFLEX, черные, размер M, упаковка 100 шт.
"""

GOODS = { 
    
    "categories": {
        
        "breath_care": {
            
            "respiratirs_3m": {
                "3m_8101" : 
                    """
3M™ 8101 Противоаэрозольная Фильтрующая Полумаска FFP1 NR D
Цена: 290₽
Использование: Одноразовая
Время использования: 4-6 часов

Описание продукта:
▪ Эффективный фильтр производства компании 3М обеспечивает качественную фильтрацию в сочетании с низким сопротивлением дыханию
▪ Чашеобразная форма: Легкая конструкция, устойчивая к смятию, с плотным прилеганием лицу; Обеспечивает удобное просторное внутреннее пространство; Легко надевается.
▪ Длинный и гибкий носовой зажим надежно фиксирует фильтрующую полумаску на лице.
▪ Экономичная модель с эффективным фильтрующим материалом производства компании 3М

Фильтрующая полумаска для защиты от аэрозолей FFP1 (до 4 ПДК), чашеобразная форма.
Чашеобразный респиратор удобной, привычной многим пользователям формы.

Тех. характеристики:
Aerosol Type - Масляный и не масляный аэрозоль
FDA Cleared - Да
Клапан выдоха - Да
Натуральный каучук и компоненты из латекса - Да
Области применения - Обрабатывающая промышленность
Особенности - Губчатая подкладка в области носа
Рекомендуемое применение - Сборка и механика
Стиль фильтрующей полумаски - Чашечка
Тип продукта - Dust and other Particles

Продукт на сайте: https://pbps.ru/product/filtruyushhaya-maska-3m-8101/
                """,

                "3m_8122": 
                """
3M™ 8122 Противоаэрозольная Фильтрующая Полумаска FFP2 NR D, с клапаном выдоха
Цена: 960₽
Использование: Одноразовая
Время использования: 14-18 часов

Описание продукта:
▪ Клапан выдоха 3M™ Cool Flow™ обеспечивает низкое сопротивление дыханию, облегчает общение, поток выдахаемого воздуха направляется вниз, что уменьшает запотевание защитных очков, лицевых и сварочных щитков. Конструкция клапана уникальна, разработана компанией 3М для максимально эффективного отведения тепла и влаги из-под маски.
▪ Чашеобразная форма : Легкая конструкция, устойчивая к смятию, с плотным прилеганием лицу; Обеспечивает удобное просторное внутреннее пространство; Легко надевается.
▪ Длинный и гибкий носовой зажим надежно фиксирует фильтрующую полумаску на лице.
▪ Эффективный фильтр производства компании 3М обеспечивает качественную фильтрацию в сочетании с низким сопротивлением дыханию
▪ Высокий коэффициент шумоподавления — 31дБ, несмотря на легкость и низкопрофильную конструкцию

Фильтрующая полумаска для защиты от аэрозолей FFP2 (до 12 ПДК), с клапаном выдоха. Чашеобразная форма.

Чашеобразный респиратор удобной, привычной многим пользователям формы.

Продукт на сайте: https://pbps.ru/product/3m-8122-protivoaerozolnaya-filtruyushhaya-polumaska-ffp2-nr-d-s-klapanom-vydoha/
                """,

                "3m_9101": 
                """
3M™ VFlex® 9101 Противоаэрозольная Фильтрующая Полумаска класс защиты FFP1 NR D
Цена: 470₽
Использование: Одноразовая
Время использования: 4-6 часов

Описание продукта:
▪ Складной репиратор с V-образным дизайном: — Респиратор плотно прилегает к различным типам лиц и следует за мимическими движеними — Респиратор легко и удобно транспортировать, складировать и хранить в перерывах — Увеличенная площадь фильтра
▪ Высокоэффективный фильтрующий материал обеспечивает качественную фильтрацию в сочетании с низким сопротивлением дыханию
▪ Рельефная внешняя поверхность помогает респиратору сохранять форму и не соприкасаться внутренней стороной с лицом при вдохе
▪ 2 размера для плотного прилегания к различным типам лица
▪ Полумаски 3M™ 7500 предназначены для длительного использования, имеют сменные части, просты в обслуживании и уходе. Сменные части: 3M™ 7581 – Ремни оголовья; 3M™ 7582 – Мембрана клапана вдоха; 3M™ 7583 – Мембрана клапана выдоха

Фильтрующая полумаска для защиты от аэрозолей FFP1 (до 4 ПДК). Складная форма. Стандартный размер.

Фильтрующие полумаски серии 3M™ VFlex® имеют следующие преимущества: • производятся на заводе компании 3М в России; • широкий ассортимент моделей для выбора наиболее эффективной защиты органов дыхания конечного пользователя; • большая часть ассортимента разработана в лаборатории компании 3М в России российскими инженерами с учетом пожеланий пользователей — российских предприятий; • оптимальным образом сочетают в себе качества, востребованные российскими предприятиями в различных индустриях и регионах • используется технологические достижения международной компании с полувековым опытом разработок средств индивидуальной защиты органов дыхания

Продукт на сайте: https://pbps.ru/product/3m-vflex-9101-protivoaerozolnaya-filtruyushhaya-polumaska-klass-zashhity-ffp1-nr-d/
                """
                ,
                "3m_8112": 
                """
3M™ 8112 Противоаэрозольная Фильтрующая Полумаска FFP1 NR D, с клапаном выдоха
Цена: 550₽
Использование: Одноразовая
Время использования: 5-7 часов

Описание продукта:
▪ Клапан выдоха 3M™ Cool Flow™ обеспечивает низкое сопротивление дыханию, облегчает общение, поток выдахаемого воздуха направляется вниз, что уменьшает запотевание защитных очков, лицевых и сварочных щитков. Конструкция клапана уникальна, разработана компанией 3М для максимально эффективного отведения тепла и влаги из-под маски.
▪ Чашеобразная форма : Легкая конструкция, устойчивая к смятию, с плотным прилеганием лицу; Обеспечивает удобное просторное внутреннее пространство; Легко надевается.
▪ Длинный и гибкий носовой зажим надежно фиксирует фильтрующую полумаску на лице.
▪ Эффективный фильтр производства компании 3М обеспечивает качественную фильтрацию в сочетании с низким сопротивлением дыханию

Фильтрующая полумаска для защиты от аэрозолей FFP1 (до 4 ПДК), с клапаном выдоха. Чашеобразная форма.

Чашеобразный респиратор удобной, привычной многим пользователям формы.

Продукт на сайте: https://pbps.ru/product/3m-8112-protivoaerozolnaya-filtruyushhaya-polumaska-ffp1-nr-d-s-klapanom-vydoha/
                """,

                "3m_9312+":
                """
3M™ Aura™ 9312+ Противоаэрозольная Фильтрующая маска класс защиты FFP1 NR D, с клапаном выдоха

Цена: 850₽
Использование: Одноразовая
Время использования: 11-14 часов

Описание продукта:
▪ Складная 3-х панельная конструкция обеспечивает надежное прилегание для различных типов и форм лица, приспосабливается к движениям лица и устойчива к смятию
▪ Применение высокотехнологичного фильтрующего материала с высоким качеством фильтрации и низким сопротивлением дыханию
▪ Клапан выдоха 3M™ Cool Flow™ обеспечивает низкое сопротивление дыханию, облегчает общение, поток выдахаемого воздуха направляется вниз, что уменьшает запотевание защитных очков, лицевых и сварочных щитков. Конструкция клапана уникальна, разработана компанией 3М для максимально эффективного отведения тепла и влаги из-под маски.
▪ Тисненая верхняя панель обеспечивает надежное прилегание для различных типов и форм лица
▪ Фигурная вырубка верхней панели для лучшей совместимости с очками и снижения риска запотевания линз
▪ Инновационный язычок на подбородке облегчает надевание и подгонку. Маска легко и просто складывается для удобства хранения
▪ Легко хранить со складным дизайном и индивидуальной упаковкой
▪ Окрашенное оголовье позволяет определить степень защиты: желтый для FFP1 (до 4 ПДК).

Противоаэрозольная фильтрующая полумаска 3M™ Aura™ модель 9312+ класс защиты FFP1 (до 4 ПДК), складного типа, 3-х панельной конструкции, с низким сопротивлением дыханию и рельефной верхней панелью, которая помогает уменьшить запотевание очков. Оснащена инновационным язычком для надевания и легкой регулировки, имеют цветовую маркировку оголовья для быстрой и легкой идентификации степени защиты. Клапан выдоха 3M™ Cool Flow™ эффективно отводит образующееся тепло, выдыхаемый воздух и влагу.

Фильтрующая полумаска 3M™ Aura™ модели 9312+ обеспечивает высокоэффективную защиту органов дыхания против аэрозолей различной природы. Специальный 3-х панельный дизайн поможет легко и удобно надеть респиратор практически на любое лицо, а также позволит респиратору не смещаться при движениях во время ношения. Кроме того, такие элементы конструкции, как рельефная верхняя панель, язычок для надевания респиратора, фигурная вырубка верхней панели для лучшей совместимости с очками, – делают эту серию респираторов еще более удобной в различных условиях труда – и при высоких концентрациях, и при высокой физической нагрузке, и при работе с особо вредными аэрозолями. Применяется специальный высокотехнологичный фильтрующий материал с высоким качеством фильтрации и низким сопротивлением дыханию. Клапан выдоха 3M™ Cool Flow™ обеспечивает комфортное и легкое дыхание в условиях повышенных температур и влажности, эффективно отводя образующееся тепло, влагу и выдыхаемый воздух вниз от лица. Окрашенное оголовье помогает легко определить степень защиты: желтый для FFP1 (до 4 ПДК). Респираторы серии 3M™ Aura™ является складными и гигиенично упакованы в индивидуальную упаковку, что позволяет удобно и безопасно хранить их до начала использования. Полностью совместимы для работы с очками 3M и другими СИЗ 3М. Для полной информации о продукте нажмите здесь: просмотр технических данных

Тех. характеристики:
Ассортимент Фильтрующих полумасок - Комфорт
Клапан выдоха - Да
Клапан выдоха Cool Flow™ - Да
Натуральный каучук и компоненты из латекса - Да
Области применения - Сельское хозяйство
Особенности - Рельефная верхняя панель, Индивидуальная упаковка, Трехпанельный дизайн, Инновационный подбородочный язычок, Изящная носовая панель
Рекомендуемое применение - Обрабатывающая промышленность
Стиль фильтрующей полумаски - Складная
Уровень защиты - FFP1

Продукт на сайте: https://pbps.ru/product/3m-aura-9312-protivoaerozolnaya-filtruyushhaya-maska-klass-zashhity-ffp1-nr-d-s-klapanom-vydoha/
                """,

                "3m_9162v": 
                """
3М™ VFlex® 9162V противоаэрозольный фильтрующий респиратор, складная, с клапаном выдоха, класс защиты FFP2 NR D (12 ПДК)
Цена: 880₽
Использование: Одноразовая
Время использования: 11-14 часов

Описание продукта:
▪ Складной респиратор с V-образным дизайном: — Респиратор плотно прилегает к различным типам лиц и следует за мимическими движениями — Респиратор легко и удобно транспортировать, складировать и хранить в перерывах — Увеличенная площадь фильтра
▪ Высокоэффективный фильтрующий материал обеспечивает качественную фильтрацию в сочетании с низким сопротивлением дыханию
▪ Рельефная внешняя поверхность помогает респиратору сохранять форму и не соприкасаться внутренней стороной с лицом при вдохе
▪ Клапан выдоха 3M™ Cool Flow™ обеспечивает низкое сопротивление дыханию, облегчает общение, поток выдыхаемого воздуха направляется вниз, что уменьшает запотевание защитных очков, лицевых и сварочных щитков. Конструкция клапана уникальна, разработана компанией 3М для максимально эффективного отведения тепла и влаги из-под респиратора
▪ Полумаски 3M™ 7500 предназначены для длительного использования, имеют сменные части, просты в обслуживании и уходе. Сменные части: 3M™ 7581 – Ремни оголовья; 3M™ 7582 – Мембрана клапана вдоха; 3M™ 7583 – Мембрана клапана выдоха

Фильтрующая полумаска для защиты от аэрозолей FFP2 (до 12 ПДК), с клапаном выдоха. Складная форма. Стандартный размер.

Фильтрующие полумаски серии 3M™ VFlex® имеют следующие преимущества: • производятся на заводе компании 3М в России; • широкий ассортимент моделей для выбора наиболее эффективной защиты органов дыхания конечного пользователя; • большая часть ассортимента разработана в лаборатории компании 3М в России российскими инженерами с учетом пожеланий пользователей — российских предприятий; • оптимальным образом сочетают в себе качества, востребованные российскими предприятиями в различных индустриях и регионах • используется технологические достижения международной компании с полувековым опытом разработок средств индивидуальной защиты органов дыхания

Описание товара носит информационный характер и может отличаться от описания, представленного в технической документации производителя. Рекомендуем при покупке проверять наличие желаемых функций и характеристик.

Производитель оставляет за собой право изменять характеристики товара, его внешний вид и комплектность без предварительного уведомления продавца.
                
Продукт на сайте: https://pbps.ru/product/3m-vflex-9162v-protivoaerozolnyj-filtruyushhij-respirator-skladnaya-s-klapanom-vydoha-klass-zashhity-ffp2-nr-d-12-pdk/
                """,

                "3m_9922p": 
                """
3M™ 9922P Специализированная Противоаэрозольная Фильтрующая Полумаска для защиты сварщика, класс защиты FFP2 NR D, с клапаном выдоха
Цена: 960₽
Использование: Одноразовая
Время использования: 14-18 часов

Описание продукта:
▪ Эффективный фильтр производства компании 3М, включая угольный фильтр, обеспечивает качественную фильтрацию в сочетании с низким сопротивлением дыханию
▪ Слой активированного угля обеспечивает защиту от озона и неприятных раздражающих запахов (паров органических веществ в пределах ПДК)
▪ Чашеобразная форма : Легкая конструкция, устойчивая к смятию, с хорошим прилеганием лицу; Обеспечивает удобное просторное внутреннее пространство; Легко надевается
▪ Длинный пластичный носовой зажим обеспечивает комфортную посадку и надежное прилегание; скрытый от контакта с окружающей средой; обнаруживается металлодетектором
▪ Для поддержания способности наушников подавлять шумы, соблюдения правил гигиены и комфорта использования – наличие сменных обтюраторов. Рекомендуется менять 2 раза в год

Специализированная фильтрующая полумаска для защиты от пылей, сварочных дымов, озона, органических паров степени защиты FFP2

Фильтрующие полумаски для защиты сварщиков от сварочных аэрозолей и сопутствующих вредных факторов воздушной среды. При производстве сварочных работ в воздухе рабочей зоны образуется сварочный дым состоящий из очень мелких частиц электродного покрытия и расплавленного металла, флюса, паров краски, антироррозионных и других покрытий. В сварочных дымах различных видов сварки могут присутствовать такие вредные вещества, как цинк, хром, марганец, свинец, железо, озон, окислы азота.
                
Продукт на сайте: https://pbps.ru/product/3m-9922p-speczializirovannaya-protivoaerozolnaya-filtruyushhaya-polumaska-dlya-zashhity-svarshhika-klass-zashhity-ffp2-nr-d-s-klapanom-vydoha/
                """,

                "3m_9926p": 
                """
Респиратор 3М™ 9926 / 9926P 2-ой класс защиты с угольным фильтром
Цена: 880₽
Использование: Одноразовая
Время использования: 14-18 часов

Описание продукта:
▪ Степень защиты FFP2.
▪ Респиратор крепится на оголовье прочными ремнями с цветовой кодировкой (синий), тем самым обеспечивает плотное прилегание к лицу. Подходит для большинства типов и форм лица.
▪ Сделан из мягкого гипоаллергенного материала. Прочная оболочка. Чашеобразная форма. Хорошо сохраняет форму во время использования.
▪ Применение — В условиях повышенной температуры воздуха и влажности. Для работы с электролитами, различными кислотами.

Продукт на сайте: https://pbps.ru/product/respirator-3m-9926-9926p-2-oj-klass-zashhity-s-ugolnym-filtrom/
                """,

                "3m_7502": 
                """
3M™ 7502 Полумаска серии 3М™ 7500 с фильтром, размер — средний (M)
Цена: 4,000₽

Описание продукта:
▪ Гипоаллергенная лицевая часть из силикона поддерживает температуру, близкую к температуре лица в условиях как повышенных, так и пониженных температур. Тонкая носовая перемычка обеспечивает повышенный комфорт.
▪ Очень плотно прилегает к лицу. За счет этого обеспечивает очень высокий реальный уровень защиты. Для легкости подгонки под любое лицо есть 3 размера. Производитель рекомендует подбирать полумаску по размеру лица — для комфорта и надежной защиты.
▪ Система крепления Drop-Down дает возможность легко снять полумаску, не снимая другие средства индивидуальной защиты, включая каску. Для активации системы надо перед использованием вынуть каждый строп оголовья из-под держателя со стрелкой.
▪ Клапан выдоха 3M™ Cool Flow™ снижает сопротивление при выдохе, накопление тепла и влаги. Меньшая вибрация клапана облегчает общение. Поток выдыхаемого воздуха направляется вниз, что уменьшает запотевание сварочных и лицевых щитков, защитных очков
▪ Байонетная система крепления фильтров дает возможность присоединения фильтров для защиты от газов, паров и/или частиц для оптимальной защиты в конкретных производственных условиях. Быстрая и безопасная замена фильтров, надежное крепление одним щелчком
▪ Полумаски 3M™ 7500 предназначены для длительного использования, имеют сменные части, просты в обслуживании и уходе. Сменные части: 3M™ 7581 – Ремни оголовья; 3M™ 7582 – Мембрана клапана вдоха; 3M™ 7583 – Мембрана клапана выдоха
▪ Размер М (средний) . Еще в серии есть размерыS (малый) и L (большой)
▪ Полумаски для защиты органов дыхания рекомендуется применять вместе с закрытыми очками для защиты органов зрения
▪ Полумаска серии 3M™ 7500 отлично совмещается с закрытыми очками серии 3M™ 2890 (поликарбонатными или ацетатными в зависимости от условий работы)
▪ Полумаски серии 3M™ 7500 с силиконовой лицевой частью, байонетным креплением фильтров производства компании 3М, эффективным клапаном выдоха 3M™ Cool Flow™, системой быстрого сброса полумаски 3M™ Drop-Down™. С фильтрами класса защиты Р3 защищает до 50 ПДК.
▪ Полумаски серии 3M™ 7500 — уникальное сочетание плотного прилегания и комфорта для пользователя, что определяет высокий уровень и надежность защиты. Лицевая часть из силикона лучше многих других материалов поддерживает температуру, близкую к температуре лица в условиях как повышенных, так и пониженных температур; гипоаллергенна. 3 размера — малый S, средний М и большой L, — для плотного прилегания полумаски к разным размерам лиц. Байонетное крепление компании 3М обеспечивает плотное присоединение фильтра к полумаске одним щелчком. Совместите риску на фильтре со стрелкой на полумаске и поверните фильтр по часовой стрелке до щелчка — тогда фильтр надежно прикреплен.

Тех. характеристики:
Вес - 136g
Используемые материалы - Силиконовый
Размер - Средний
Рекомендуемое применение - Строительство, Продукты питания и напитки Изготовление, Обрабатывающая промышленность, Металлообрабатывающая промышленность, Деревообрабатывающая промышленность
Серия - Полумаска серии 7500
Тип оголовья - 4 точки крепления
Тип продукта - Полумаска

Продукт на сайте: https://pbps.ru/product/3m-7502-polumaska-serii-3m-7500-razmer-srednij-m/
                """,

                "3m_6051":
                """
Комплект сменных патронов 3М™ 6051 (А1) и предфильтров 5911 для масок и полумасок
Цена: 1,900₽

В комплект входит:
Фильтр противоаэрозольный 3М™ модель 5911 класс защиты P1 R

Для защиты от органических паров с температурой кипения выше +65°С.
С полумасками – защита до 50 ПДК.
С полными масками – защита до 200 ПДК

Стоимость за комплект из двух фильтров 3М™ 6051 (А1) и двух предфильтров модель 5911

Продукт на сайте: https://pbps.ru/product/smennyj-patron-3m-6051-a1-dlya-masok-i-polumasok/
                """
            },

            "masks": {
                "black_mask": 
                """
Черная, тканевая маска
Цена: 150₽
Использование: Многоразовая
Время использования: 2-6 часов

Покупка оптом от 100 штук, предоставляется скидка. Обсуждается индивидуально по телефону или электронной почте.

Описание продукта:

Тканевая маска — многоразовое изделие, закрывающее рот и нос носителя, и обеспечивающее барьер для прямой передачи инфекционных частиц от носителя маски к другим людям, так и вам.
                
Продукт на сайте: https://pbps.ru/product/obychnaya-chernaya-mnogorazovaya-maska/
                """,

                "white_mask": 
                """
Белая, тканевая маска
Цена: 150₽
Использование: Многоразовая
Время использования: 2-6 часов

Покупка оптом от 100 штук, предоставляется скидка. Обсуждается индивидуально по телефону или электронной почте.

Описание продукта:
Тканевая маска — многоразовое изделие, закрывающее рот и нос носителя, и обеспечивающее барьер для прямой передачи инфекционных частиц от носителя маски к другим людям, так и вам.
                
Продукт на сайте: https://pbps.ru/product/obychnaya-belaya-mnogorazovaya-maska/
                """,

                "black_Pmask":
                """
Черные тканевые, многоразовые маски с принтами
Цена: 220₽
Использование: Многоразовая
Время использования: 2-6 часов

Покупка оптом от 100 штук, предоставляется скидка. Обсуждается индивидуально по телефону или электронной почте.

Описание товара:
Тканевая маска — многоразовое изделие, закрывающее рот и нос носителя, и обеспечивающее барьер для прямой передачи инфекционных частиц от носителя маски к другим людям, так и вам.

Продукт на сайте: https://pbps.ru/product/chernye-tkanevye-mnogorazovye-maski-s-printami/
                """,

                "white_Pmask":
                """
Белые тканевые, многоразовые маски с принтами
Цена: 220₽
Использование: Многоразовая
Время использования: 2-6 часов

Покупка оптом от 100 штук, предоставляется скидка. Обсуждается индивидуально по телефону или электронной почте.

Описание товара:
Тканевая маска — многоразовое изделие, закрывающее рот и нос носителя, и обеспечивающее барьер для прямой передачи инфекционных частиц от носителя маски к другим людям, так и вам.

Продукт на сайте: https://pbps.ru/product/belye-tkanevye-mnogorazovye-maski-s-printami/
                """
            }
        },

        "body_care": {
            "care_suit": 
            """
Костюм для п/э-L-NOR-NPS
Цена: 1,500₽
Использование: Многоразовая
Время использования: 10-14 суток

Описание продукта:
Легкий полиэстер пропускает воздух, антистатичен, легко моется.   Есть все размеры, от M до XL

Продукт на сайте: https://pbps.ru/product/kostyum-dlya-pokraski-l-nor-nps/
            """
        },

        "hand_care": {
            "rubbing_gloves": 
            """
Перчатки с резиновой облицовкой 10 класс
Цена: 20₽

Описание продукта:
Перчатки предназначены для защиты рук от повреждений при проведении неоднократно повторяющихся погрузочных и складских работ. Изготовлены из прочного трикотажного материала, хорошо пропускают воздух и обеспечивают максимальную чувствительность рук. Удобно подгоняются по форме кисти. Перчатки позволяют крепко удерживать инструмент во время работы за счет сплошного двойного латексного покрытия на ладонях и кончиках пальцев. Они удобны в эксплуатации, имеют повышенную прочность.
            
Продукт на сайте: https://pbps.ru/product/perchatki-s-rezinovoj-obliczovkoj/
            """,

            "proflex_xl": 
            """
Перчатки нитриловые PROFLEX, черные, размер XL, упаковка 100 шт.
Цена: 1,400₽
Цена указанна за 100 штук ( 1 упаковка )

Описание товара:

Для профессионального применения в Авто-ремонте. Идеально защищают руки от воздействия мелкодисперсных частиц и химических веществ (масел, жира, спирта, большинства растворителей, слабых растворов кислот).
            
Продукт на сайте: https://pbps.ru/product/perchatki-nitrilovye-proflex-chernye-razmer-xl-upakovka-100-sht/
            """,

            "proflex_l": 
            """
Перчатки нитриловые PROFLEX, черные, размер L, упаковка 100 шт.
Цена: 1,400₽
Цена указанна за 100 штук ( 1 упаковка )

Описание товара:

Для профессионального применения в Авто-ремонте. Идеально защищают руки от воздействия мелкодисперсных частиц и химических веществ (масел, жира, спирта, большинства растворителей, слабых растворов кислот).
            
Продукт на сайте: https://pbps.ru/product/perchatki-nitrilovye-proflex-chernye-razmer-l-upakovka-100-sht/
            """,

            "proflex_m": 
            """
Перчатки нитриловые PROFLEX, черные, размер M, упаковка 100 шт.
Цена: 1,400₽
Цена указанна за 100 штук ( 1 упаковка )

Описание товара:

Для профессионального применения в Авто-ремонте. Идеально защищают руки от воздействия мелкодисперсных частиц и химических веществ (масел, жира, спирта, большинства растворителей, слабых растворов кислот).
            
Продукт на сайте: https://pbps.ru/product/perchatki-nitrilovye-proflex-chernye-razmer-m-upakovka-100-sht/
            """
        }
    }
}

PRODUCT_CALLBACKS = {
    "3m_8101": ["3M™ 8101 Противоаэрозольная Фильтрующая Полумаска FFP1 NR D", 290],
    
    "3m_8122": ["3M™ 8122 Противоаэрозольная Фильтрующая Полумаска FFP2 NR D, с клапаном выдоха", 960],

    "3m_9101": ["3M™ VFlex® 9101 Противоаэрозольная Фильтрующая Полумаска класс защиты FFP1 NR D", 470],

    "3m_8112": ["3M™ 8112 Противоаэрозольная Фильтрующая Полумаска FFP1 NR D, с клапаном выдоха", 550],

    "3m_9312+": ["3M™ Aura™ 9312+ Противоаэрозольная Фильтрующая маска класс защиты FFP1 NR D, с клапаном выдоха", 850],

    "3m_9162v": ["3М™ VFlex® 9162V противоаэрозольный фильтрующий респиратор, складная, с клапаном выдоха, класс защиты FFP2 NR D (12 ПДК)", 880],

    "3m_9922p": ["3M™ 9922P Специализированная Противоаэрозольная Фильтрующая Полумаска для защиты сварщика, класс защиты FFP2 NR D, с клапаном выдоха", 960],

    "3m_9926p": ["Респиратор 3М™ 9926 / 9926P 2-ой класс защиты с угольным фильтром", 880],

    "3m_7502": ["3M™ 7502 Полумаска серии 3М™ 7500 с фильтром, размер — средний (M)", 4000],

    "3m_6051": ["Комплект сменных патронов 3М™ 6051 (А1) и предфильтров 5911 для масок и полумасок", 1900],

    "black_mask": ["Черная, тканевая маска", 150],

    "white_mask": ["Белая, тканевая маска", 150],

    "black_Pmask": ["Черные тканевые, многоразовые маски с принтами", 220],

    "white_Pmask": ["Белые тканевые, многоразовые маски с принтами", 220],

    "care_suit": ["Костюм для п/э-L-NOR-NPS", 1500],

    "rubbing_gloves": ["Перчатки с резиновой облицовкой 10 класс", 20],

    "proflex_xl": ["Перчатки нитриловые PROFLEX, черные, размер XL, упаковка 100 шт.", 1400],

    "proflex_l": ["Перчатки нитриловые PROFLEX, черные, размер L, упаковка 100 шт.", 1400],

    "proflex_m": ["Перчатки нитриловые PROFLEX, черные, размер M, упаковка 100 шт.", 1400]
}



#|---------- KEYBOARD ------------------------|

CATEGORIES_KEYBOARD = ListOfButtons(
    text = [
        'Защита органов дыхания', 
        'Защитные костюмы',
        'Защитные перчатки',
        'Моя корзина'
    ],
    callback=['breath', 'suit', 'gloves', 'bucket'],
    align = [1, 2, 1]
).reply_keyboard


# ---------- BREATH CARE

BREATH_KEYBOARD = ListOfButtons(
    text = [
        'Респираторы 3М', 
        'Тканевые многоразовые маски',
        'Моя корзина',
        'Назад на главную'
    ],
    callback=['respirators', 'masks', 'bucket', 'back_to_main'],
    align = [1, 1, 2]
).reply_keyboard

RESPIRATORS_KEYBOARD = ListOfButtons(
    text = [ str(i) for i in range(1, len(GOODS['categories']['breath_care']['respiratirs_3m'].keys()) + 1) ],

    callback=[ i for i in GOODS['categories']['breath_care']['respiratirs_3m'].keys() ],

    align = [3, 3, 3, 1]
).inline_keyboard

MASKS_KEYBOARD = ListOfButtons(
    text = [ str(i) for i in range(1, len(GOODS['categories']['breath_care']['masks'].keys()) + 1) ],

    callback=[ i for i in GOODS['categories']['breath_care']['masks'].keys() ],

    align = [2, 2]
).inline_keyboard

# ---------- BODY CARE

SUITS_KEYBOARD = ListOfButtons(
    text = [ str(i) for i in range(1, len(GOODS['categories']['body_care'].keys()) + 1) ],
    callback=[ i for i in GOODS['categories']['body_care'].keys() ],
    align = [1]
).inline_keyboard

# ---------- HANDS CARE

GLOVES_KEYBOARD = ListOfButtons(
    text = [ str(i) for i in range(1, len(GOODS['categories']['hand_care'].keys()) + 1) ],
    callback=[ i for i in GOODS['categories']['hand_care'].keys() ],
    align = [2, 2]
).inline_keyboard

ADD_TO_BUCKET_KEYBOARDS = {
    "3m_8101": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_8101_product_by_name', 'add_5_3m_8101_product_by_name', 'add_10_3m_8101_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_8122": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_8122_product_by_name', 'add_5_3m_8122_product_by_name', 'add_10_3m_8122_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_9101": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_9101_product_by_name', 'add_5_3m_9101_product_by_name', 'add_10_3m_9101_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_8112": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_8112_product_by_name', 'add_5_3m_8112_product_by_name', 'add_10_3m_8112_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_9312+": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_9312+_product_by_name', 'add_5_3m_9312+_product_by_name', 'add_10_3m_9312+_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_9162v": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_9162v_product_by_name', 'add_5_3m_9162v_product_by_name', 'add_10_3m_9162v_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_9922p": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_9922p_product_by_name', 'add_5_3m_9922p_product_by_name', 'add_10_3m_9922p_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_9926p": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_9926p_product_by_name', 'add_5_3m_9926p_product_by_name', 'add_10_3m_9926p_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_7502": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_7502_product_by_name', 'add_5_3m_7502_product_by_name', 'add_10_3m_7502_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "3m_6051":
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_3m_6051_product_by_name', 'add_5_3m_6051_product_by_name', 'add_10_3m_6051_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "black_mask": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_black_mask_product_by_name', 'add_5_black_mask_product_by_name', 'add_10_black_mask_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "white_mask": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_white_mask_product_by_name', 'add_5_white_mask_product_by_name', 'add_10_white_mask_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "black_Pmask":
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_black_Pmask_product_by_name', 'add_5_black_Pmask_product_by_name', 'add_10_black_Pmask_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "white_Pmask":
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_white_Pmask_product_by_name', 'add_5_white_Pmask_product_by_name', 'add_10_white_Pmask_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "care_suit": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_care_suit_product_by_name', 'add_5_care_suit_product_by_name', 'add_10_care_suit_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "rubber_lining_gloves": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_rubbing_gloves_product_by_name', 'add_5_rubbing_gloves_product_by_name', 'add_10_rubbing_gloves_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "proflex_xl": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_proflex_xl_product_by_name', 'add_5_proflex_xl_product_by_name', 'add_10_proflex_xl_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "proflex_l": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_proflex_l_product_by_name', 'add_5_proflex_l_product_by_name', 'add_10_proflex_l_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard,

    "proflex_m": 
    ListOfButtons(
    text = [
        'Добавить в корзину 1 штуку',
        'Добавить в корзину 5 штук',
        'Добавить в корзину 10 штук'
    ],
    callback=[ 'add_1_proflex_m_product_by_name', 'add_5_proflex_m_product_by_name', 'add_10_proflex_m_product_by_name' ],
    align = [1, 1, 1]
).inline_keyboard
}

EDIT_BUCKET_KEYBOARD = ListOfButtons(
    text = [
        'Редактировать корзину',
        #'Оформить заказ через телеграмм',
        'Оформить заказ через менеджера'
    ],
    callback=[ 'edit_bucket', 'checkout_menedger' ], #'checkout_escvair'
    align = [1, 1, 1]
).inline_keyboard

def create_edit_keyboard(chat_id):

    CHOOSE_PRODUCT_TO_EDIT_KEYBOARD = ListOfButtons(
        text = [ str(i) for i in range(1, get_amount_of_products(chat_id) + 1)],
        callback=[ f"edit_{i}_product_in_bucket" for i in range(1, get_amount_of_products(chat_id) + 1) ]
    ).inline_keyboard

    return CHOOSE_PRODUCT_TO_EDIT_KEYBOARD

EDIT_PRODUCT_KEYBOARD = ListOfButtons(
    text = [
        '-1',
        '+1',
        '-5',
        '+5',
        '-10',
        '+10',
        'Удалить продукт из корзины'
    ],
    callback=[ 'delete_1_product_by_number', 'add_1_product_by_number', 'delete_5_product_by_number', 'add_5_product_by_number', 'delete_10_product_by_number', 'add_10_product_by_number', 'delete_all_product_by_number' ],
    align = [2, 2, 2, 1]
).inline_keyboard

GROUP_BREATH = ListOfButtons(
    text = [
        'Респираторы 3М', 
        'Тканевые многоразовые маски',
        'Назад на главную'
    ],
    callback=['respirators', 'masks', 'back_to_main'],
    align = [1, 1, 1]
).reply_keyboard

GROUP_CATEGORIES = ListOfButtons(
    text = [
        'Защита органов дыхания', 
        'Защитные костюмы',
        'Защитные перчатки'
    ],
    callback=['breath', 'suit', 'gloves'],
    align = [1, 2]
).reply_keyboard

ORDER_INFO_TEXT = """
Для оформления заказа через менеджера, пожалуйста, отправьте сообщение, которое начинается со слова ЗАКАЗ и укажите в нем следующие данные:
-------------------
ЗАКАЗ
1. ФИО

2. Вариант доставки из предложенных:
Самовывоз - Сходня
Самовывоз - Путилково
Доставка в пределах МКАД - 500р
Доставка за МКАД - 700р
Доставка курьером - уточняйте у менеджера

3. Адрес доставки (если выбрали доставку, а не самовывоз)

4. Номер телефона

5. Электронная почта

6. Никнейм в телеграмме
-------------------
ПРИМЕР СООБЩЕНИЯ:
ЗАКАЗ
1. Иванов Иван Иванович
2. Доставка в пределах МКАД
3. г. Москва, ул. Пушкина, д.23, кв. 62
4. 8-800-555-3535
5. ivanov123@mail.ru
6. @ivanov_ivan

ВНИМАЕНИЕ! ПЕРЕД ОТПРАВКОЙ ЕЩЕ РАЗ ПРОВЕРЬТЕ СВОЮ КОРЗИНУ ЗАКАЗА И КОРРЕКТНОСТЬ ДАННЫХ В СООБЩЕНИИ.
ПОСЛЕ ОТПРАВКИ СООБЩЕНИЯ, ВАШИ ДАННЫЕ И ЗАКАЗ ИЗ КОРЗИНЫ БУДУТ ПЕРЕСЛАНЫ МЕНЕДЖЕРУ ДЛЯ ОФОРМЛЕНИЯ ЗАКАЗА.
В СКОРОМ ВРЕМЕНИ С ВАМИ СВЯЖЕТСЯ МЕНЕДЖЕР ДЛЯ ПОДТВЕРЖДЕНИЯ ВВЕДЕННЫХ ДАННЫХ И ЗАКАЗА В ЦЕЛОМ.
Спасибо за Вашу внимательность :)
"""