# Тутаев Сайд-Селим


# 1. b

# 2. b

# 3. c

# 4. c

# 5. a

# 6. b

# 7. b

# Почему-то нет 8 и 9 задания

# 10. b

# 11. Эти классы отличаются связями моделей. ManyToManyField - многие ко многим, ForeignKey - один ко многим, OneToOneField - один к одному.

# 12. DRF сам создает валидацию и правильную структуру, сериалайзер превращает из объекта модели в JSON и наоборот. Все происходит под капотом.

# 13. books = Book.objects.filter(author='Ivan Ivanov', publication_date__year__gt=2020).order_by('title')


# Для проверки практического задания - python manage.py runserver