import os
import django
from decimal import Decimal
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'GearForBikes.settings')
django.setup()

from django.contrib.auth.models import User
from shop.models import Manufacturer, Category, Product, Cart, CartItem


def populate():

    # ОЧИСТКА БАЗЫ
    print("\n🗑️  Очистка старых данных...")
    CartItem.objects.all().delete()
    Cart.objects.all().delete()
    Product.objects.all().delete()
    Category.objects.all().delete()
    Manufacturer.objects.all().delete()
    User.objects.filter(is_superuser=False).delete()
    print(" База очищена")

    # СОЗДАНИЕ ПРОИЗВОДИТЕЛЕЙ (6 шт)
    print("\nСоздание 6 производителей...")
    manufacturers_data = [
        {"name": "Fuji Bikes", "country": "Япония / США", "description": "Легендарные трековые фиксы, синглспиды и гравийные велосипеды"},
        {"name": "Bear Bike", "country": "Россия", "description": "Стильные городские комплиты, фиксы и дорожные круизеры"},
        {"name": "Marin Bikes", "country": "США", "description": "Культовые стальные туринги, грейвелы и урбан-байки"},
        {"name": "Shimano", "country": "Япония", "description": "Высококлассное навесное оборудование, трансмиссии и тормозные системы"},
        {"name": "Schwalbe", "country": "Германия", "description": "Технологичные и защищенные от проколов велосипедные покрышки и камеры"},
        {"name": "Outleap", "country": "Китай", "description": "Доступные и современные городские, складные и гравийные велосипеды"},
    ]
    
    manufacturers = []
    for data in manufacturers_data:
        m = Manufacturer.objects.create(**data)
        manufacturers.append(m)
        print(f"   ✓ {m.name}")
    print(f"Создано производителей: {len(manufacturers)}")

    # СОЗДАНИЕ КАТЕГОРИЙ (11 шт)
    print("\n📦 Создание 11 категорий...")
    categories_data = [
        {"name": "Синглспиды и Фиксы", "description": "Велосипеды с фиксированной или одной передачей для города и трека"},
        {"name": "Грейвелы и Туринги", "description": "Гравийные и туристические велосипеды для дальних поездок и бездорожья"},
        {"name": "Городские велосипеды", "description": "Комьютеры, ситибайки и урбан-танки для комфортного перемещения по асфальту"},
        {"name": "Велопокрышки и Камеры", "description": "Резина разной ширины, слики, гравийные протекторы и камеры"},
        {"name": "Педали и Стрепы", "description": "Топталки, контактные педали SPD и текстильные стрепы для фиксов"},
        {"name": "Седла и Обмотка", "description": "Анатомические седла, кожаные Brooks и цепкие обмотки для рулей-дропбаров"},
        {"name": "Велосумки и Байкпакинг", "description": "Внутрирамные, подседельные и нарульные сумки для перевозки вещей"},
        {"name": "Цепи и Звезды", "description": "Ведущие и задние звезды, коги, локринги и износостойкие цепи"},
        {"name": "Тормоза и Ручки", "description": "Дисковая механика, гидравлика, клещевые тормоза и пистолеты"},
        {"name": "Инструменты и Смазки", "description": "Мультитулы, выжимки, насосы и парафиновые смазки для цепи"},
        {"name": "Аксессуары и Фляги", "description": "U-образные замки, флягодержатели, питьевые фляги и габаритный свет"},
    ]
    
    categories = []
    for data in categories_data:
        c = Category.objects.create(**data)
        categories.append(c)
        print(f"   ✓ {c.name}")
    print(f"Создано категорий: {len(categories)}")

    # СОЗДАНИЕ ТОВАРОВ (34 шт)
    print("\nСоздание 34 товаров...")
    
    products_data = [
        # Синглспиды и Фиксы - 3 товара
        {"name": "Велосипед Fuji Feather", "description": "Классический хромолевый трековый фикс на трубах Reynolds", "price": Decimal("2450.00"), "quantities_stock": 5, "category": categories[0], "manufacturer": manufacturers[0]},
        {"name": "Велосипед Bear Bike Minsk", "description": "Яркий и легкий городской синглспид со втулкой флип-флоп", "price": Decimal("1350.00"), "quantities_stock": 8, "category": categories[0], "manufacturer": manufacturers[1]},
        {"name": "Велосипед Fuji Declaration", "description": "Стильный сити-комплит на толстой стальной раме со строгим дизайном", "price": Decimal("1890.00"), "quantities_stock": 6, "category": categories[0], "manufacturer": manufacturers[0]},
        
        # Грейвелы и Туринги - 3 товара
        {"name": "Велосипед Marin Nicasio", "description": "Хромолевый гравийный байк с обилием бонок под байкпакинг", "price": Decimal("3850.00"), "quantities_stock": 4, "category": categories[1], "manufacturer": manufacturers[2]},
        {"name": "Велосипед Fuji Jari 2.5", "description": "Алюминиевый технологичный грейвел на компонентах Shimano Кlaris", "price": Decimal("3400.00"), "quantities_stock": 3, "category": categories[1], "manufacturer": manufacturers[0]},
        {"name": "Велосипед Outleap Hardway CRM", "description": "Стальной доступный грейвел на сквозных осях и трансмиссии 1х9", "price": Decimal("2200.00"), "quantities_stock": 7, "category": categories[1], "manufacturer": manufacturers[5]},
        
        # Городские велосипеды - 3 товара
        {"name": "Велосипед Marin Muirwoods", "description": "Культовый стальной урбан-комьютер на 29-х колесах", "price": Decimal("3600.00"), "quantities_stock": 5, "category": categories[2], "manufacturer": manufacturers[2]},
        {"name": "Велосипед Bear Bike Turku", "description": "Классический дорожный велосипед с планетарной втулкой и корзиной", "price": Decimal("1450.00"), "quantities_stock": 6, "category": categories[2], "manufacturer": manufacturers[1]},
        {"name": "Велосипед Outleap Urban", "description": "Легкий маневренный ситибайк с жесткой вилкой для асфальта", "price": Decimal("1250.00"), "quantities_stock": 10, "category": categories[2], "manufacturer": manufacturers[5]},
        
        # Велопокрышки и Камеры - 3 товара
        {"name": "Покрышка Schwalbe Marathon Plus", "description": "Максимальная защита от проколов (SmartGuard), размер 700x35C", "price": Decimal("165.00"), "quantities_stock": 40, "category": categories[3], "manufacturer": manufacturers[4]},
        {"name": "Покрышка Schwalbe G-One Allround", "description": "Топовая гравийная фолдинговая покрышка, Tubeless Easy, 700x40C", "price": Decimal("195.00"), "quantities_stock": 24, "category": categories[3], "manufacturer": manufacturers[4]},
        {"name": "Камера Schwalbe SV17", "description": "Качественная бутиловая камера с длинным спортивным ниппелем Presta", "price": Decimal("28.00"), "quantities_stock": 120, "category": categories[3], "manufacturer": manufacturers[4]},
        
        # Педали и Стрепы - 3 товара
        {"name": "Педали Shimano M520 SPD", "description": "Надежные двусторонние контактные педали для МТБ и грейвела", "price": Decimal("190.00"), "quantities_stock": 30, "category": categories[4], "manufacturer": manufacturers[3]},
        {"name": "Стрепы Bear Bike Fix", "description": "Плотные текстильные стрепы на липучках для надежной фиксации стопы", "price": Decimal("45.00"), "quantities_stock": 50, "category": categories[4], "manufacturer": manufacturers[1]},
        {"name": "Педали-платформы Shimano GR500", "description": "Широкие злые педали-топталки со сменными регулируемыми шипами", "price": Decimal("210.00"), "quantities_stock": 15, "category": categories[4], "manufacturer": manufacturers[3]},
        
        # Седла и Обмотка - 3 товара
        {"name": "Седло Marin Comfort", "description": "Мягкое эргономичное спортивное седло с гелевым наполнителем", "price": Decimal("115.00"), "quantities_stock": 20, "category": categories[5], "manufacturer": manufacturers[2]},
        {"name": "Обмотка руля Fuji Cork", "description": "Пробковая мягкая обмотка руля-барана, отлично гасит вибрации дорог", "price": Decimal("48.00"), "quantities_stock": 40, "category": categories[5], "manufacturer": manufacturers[0]},
        {"name": "Седло Bear Bike Urban Microfiber", "description": "Лаконичное узкое седло с покрытием из микрофибры для фикс-гира", "price": Decimal("75.00"), "quantities_stock": 25, "category": categories[5], "manufacturer": manufacturers[1]},
        
        # Велосумки и Байкпакинг - 3 товара
        {"name": "Сумка внутрирамная Marin Frame Bag", "description": "Влагозащищенная сумка, жестко фиксируется внутри треугольника рамы", "price": Decimal("140.00"), "quantities_stock": 12, "category": categories[6], "manufacturer": manufacturers[2]},
        {"name": "Фидбэг Outleap Handlebar Pouch", "description": "Удобная сумка-кормушка на руль для быстрого доступа к фляге или еде", "price": Decimal("45.00"), "quantities_stock": 35, "category": categories[6], "manufacturer": manufacturers[5]},
        {"name": "Подседельный баул Marin WP 12L", "description": "Герметичный большой баул для крепления за подседельный штырь", "price": Decimal("230.00"), "quantities_stock": 10, "category": categories[6], "manufacturer": manufacturers[2]},
        
        # Цепи и Звезды - 3 товара
        {"name": "Цепь Shimano HG54 10-speed", "description": "Направленная сверхузкая 10-скоростная цепь серии Deore/Tiagra", "price": Decimal("95.00"), "quantities_stock": 45, "category": categories[7], "manufacturer": manufacturers[3]},
        {"name": "Звезда трековая Bear Bike 48T", "description": "Алюминиевая жесткая звезда (Chainring) под стандарт BCD 144", "price": Decimal("80.00"), "quantities_stock": 20, "category": categories[7], "manufacturer": manufacturers[1]},
        {"name": "Ког Shimano Dura-Ace 16T", "description": "Профессиональная задняя звезда для глухой передачи трекового байка", "price": Decimal("110.00"), "quantities_stock": 15, "category": categories[7], "manufacturer": manufacturers[3]},
        
        # Тормоза и Ручки - 3 товара
        {"name": "Тормоз дисковый Shimano TX805", "description": "Механический надежный калипер дискового тормоза", "price": Decimal("85.00"), "quantities_stock": 30, "category": categories[8], "manufacturer": manufacturers[3]},
        {"name": "Тормозные ручки Outleap Dropbar", "description": "Раздельные шоссейные ручки (курки) для синглспидов с рулем-бараном", "price": Decimal("65.00"), "quantities_stock": 25, "category": categories[8], "manufacturer": manufacturers[5]},
        {"name": "Гидравлический тормоз Shimano MT200", "description": "Комплект заправленной дисковой гидравлики (ручка + калипер + гидролиния)", "price": Decimal("175.00"), "quantities_stock": 20, "category": categories[8], "manufacturer": manufacturers[3]},
        
        # Инструменты и Смазки - 3 товара
        {"name": "Мультитул Outleap 10-в-1", "description": "Компактный складной насадочный инструмент с выжимкой цепи", "price": Decimal("55.00"), "quantities_stock": 50, "category": categories[9], "manufacturer": manufacturers[5]},
        {"name": "Смазка цепи Shimano PTFE 100ml", "description": "Тефлоновая жидкая смазка для сухой погоды, снижает трение цепи", "price": Decimal("35.00"), "quantities_stock": 70, "category": categories[9], "manufacturer": manufacturers[3]},
        {"name": "Насос ручной Schwalbe Mini", "description": "Легкий карманный телескопический насос под ниппели Presta/Schrader", "price": Decimal("75.00"), "quantities_stock": 40, "category": categories[9], "manufacturer": manufacturers[4]},
        
        # Аксессуары и Фляги - 4 товара
        {"name": "Замок U-образный Bear Bike Heavy Lock", "description": "Тяжелая скоба из каленой стали для защиты от перекусывания болторезом", "price": Decimal("120.00"), "quantities_stock": 18, "category": categories[10], "manufacturer": manufacturers[1]},
        {"name": "Флягодержатель Shimano Pro Cage", "description": "Композитный легкий и цепкий держатель для стандартных велофляг", "price": Decimal("40.00"), "quantities_stock": 60, "category": categories[10], "manufacturer": manufacturers[3]},
        {"name": "Фляга Outleap Корса 750мл", "description": "Спортивная мягкая фляга из пищевого пластика без запаха BPA-free", "price": Decimal("25.00"), "quantities_stock": 100, "category": categories[10], "manufacturer": manufacturers[5]},
        {"name": "Фара передняя Fuji Neon LED", "description": "Яркий габаритный диодный свет со встроенным USB-аккумулятором", "price": Decimal("85.00"), "quantities_stock": 35, "category": categories[10], "manufacturer": manufacturers[0]},
    ]
    
    products = []
    for data in products_data:
        p = Product.objects.create(**data)
        products.append(p)
    print(f"Создано товаров: {len(products)}")

    # СОЗДАНИЕ ПОЛЬЗОВАТЕЛЕЙ (5 шт)
    print("\n📦 Создание 5 пользователей с корзинами...")
    users_data = [
        {"username": "user1", "email": "user1@example.com", "password": "pass1"},
        {"username": "user2", "email": "user2@example.com", "password": "pass2"},
        {"username": "user3", "email": "user3@example.com", "password": "pass3"},
        {"username": "user4", "email": "user4@example.com", "password": "pass4"},
        {"username": "user5", "email": "user5@example.com", "password": "pass5"},
    ]
    
    for user_data in users_data:
        user, created = User.objects.get_or_create(
            username=user_data["username"],
            defaults={"email": user_data["email"], "is_active": True}
        )
        if created:
            user.set_password(user_data["password"])
            user.save()
        
        cart, _ = Cart.objects.get_or_create(user=user)
        
        num_items = random.randint(2, 3)
        selected_products = random.sample(products, num_items)
        
        for product in selected_products:
            CartItem.objects.create(cart=cart, product=product, quantities=random.randint(1, 3))
        
        print(f" {user.username}: корзина с {num_items} товара(ми)")
    print(f"Создано пользователей: {len(users_data)}")

    # ИТОГИ
    print(f"\n📊 ИТОГИ ИМПОРТА:")
    print(f"Производителей: {Manufacturer.objects.count()}")
    print(f"Категорий: {Category.objects.count()}")
    print(f"Товаров: {Product.objects.count()}")
    print(f"Пользователей: {User.objects.filter(is_superuser=False).count()}")
    print(f"Корзин: {Cart.objects.count()}")


if __name__ == "__main__":
    populate()