# BookServes

Для применения миграций, если файла `alembic.ini` ещё нет, нужно запустить в терминале команду:

```
alembic init migrations
```

- После этого будет создана папка с миграциями и конфигурационный файл для алембика.
- Дальше переходи в папку с миграциями и открываем `env.py`, там вносим изменения в блок, где написано

```
from myapp import mymodel
```

- Дальше вводим: ```alembic revision --autogenerate -m "comment"```
- Будет создана миграция
- Дальше вводим: ```alembic upgrade heads```

Видео https://www.youtube.com/watch?v=FYsOenDefkk&list=PLlKID9PnOE5jiWTTsshCXdz5qvg8JWezX&index=2
