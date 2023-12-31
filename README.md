# Приклад завантаження файлів з FastAPI

Цей додаток FastAPI надає простий ендпоінт для завантаження файлів. Він використовує бібліотеку `fastapi` для створення веб-API та дозволяє користувачам завантажувати файли через ендпоінт `/file/`.

## Встановлення серверу

### Крок 1: Клонування цього репозиторію

```bash
git clone https://github.com/AlexBabilya/file-server.git
cd file-server
```

Для забезпечення чистого та ізольованого середовища для вашого проекту FastAPI рекомендується використовувати віртуальне середовище. Ось кроки для створення нового віртуального середовища, його активації та встановлення пакетів з файлу `requirements.txt`:

### Крок 2: Створення віртуального середовища

```bash
# На Windows
python -m venv venv

# На macOS та Linux
python3 -m venv venv
```

Це створить новий каталог з назвою `venv`, що містить віртуальне середовище.

### Крок 3: Активація віртуального середовища

#### На Windows:

```bash
venv\Scripts\activate
```

#### На macOS та Linux:

```bash
source venv/bin/activate
```

Після активації ваш командний рядок або термінал повинен відображати назву віртуального середовища, вказуючи, що ви працюєте в межах віртуального середовища.

### Крок 4: Встановлення залежностей з `requirements.txt`

Встановіть залежності за допомогою `pip`:

```bash
pip install -r requirements.txt
```

Це встановить зазначені пакети разом із їхніми залежностями у віртуальне середовище.

### Крок 5: Запуск додатку FastAPI:

Після активації віртуального середовища та встановлення залежностей ви можете запустити сервер:

```bash
uvicorn main:app --reload --host=0.0.0.0 --port=5000
```

Прапорець `--reload` вмикає автоматичне перезавантаження коду під час розробки
### Крок 6: Вимкнення віртуального середовища

Коли ви закінчите роботу у віртуальному середовищі, ви можете його вимкнути:

```bash
deactivate
```

По завершенні цих кроків ви створите ізольоване середовище для свого проекту FastAPI, що забезпечить встановлення залежностей без втручання в глобальне середовище Python. Крім того, це полегшить управління та обмін проектом з іншими користувачами.

## Встановлення плейбуку

### Крок 1: Створення API Key

Перейти до веб консолі, та стоврити навий API Key, у результаті отрмаємо API Key ID та API Key Secret у схожому форматі:
```bash
Key ID: 426af612-04ac-4c5e-93f7-3c159b1e811b
Key Secret: gb1ufYa5Bs7LmMu2hsoSrB_0F_bsO0Ck-Z2ZJWhG5Ic
```
Зберегти ці значення.

### Крок 2: Кодування API Key

Для кодування потрібно виконати команду

```bash
echo -n "API Key ID:API Key Secret" | base64
```

Приклад:
```bash
echo -n "426af612-04ac-4c5e-93f7-3c159b1e811b:gb1ufYa5Bs7LmMu2hsoSrB_0F_bsO0Ck-Z2ZJWhG5Ic" | base64
```
В результаті отримаєм ключ заковдований в base64:
```bash
NDI2YWY2MTItMDRhYy00YzVlLTkzZjctM2MxNTliMWU4MTFiOmdiMXVmWWE1QnM3TG1NdTJoc29TckJfMEZfYnNPMENrLVoyWkpXaEc1SWM=
```
Зберегти ключ.

### Крок 3: Створення зміної для аунтифікації

Перейти в app.config інтеграції REST API Functions for SOAR та натиснути Add Secret
```bash
Secret Name = ENCODED_AUTH_KEY
Secret Value = закодований ключ який ми отрмали в кроці 2
```
B app.config стоврити зміну. Під [fn_rest_api] додати soar_auth = $ENCODED_AUTH_KEY.
Збереги  конфігруацію.
Save and Push Changes

### Крок 4: Налаштування плейбуку

1) Імпортувати плейбку NBU_Attachment_Export.resz
Playbooks -> Import playbook -> NBU_Attachment_Export.resz

2) Перейти до плейбуку та змінити в 1 функції айпі соару та айді організації
  ```
  soar_fqdn = "soar.ip"
  org_id = soar.org_id
  ```
3)Зберегти зміни
  Save
4)Змінити в 2 функції айпі серверу
```
file_server_api = 'file_server.ip:5000'
```
Save
5)Зберегти плейбук
Save
## Налаштування

Ви можете змінити змінну `UPLOAD_DIRECTORY` у файлі `main.py`, щоб змінити каталог, де будуть збережені завантажені файли.

```python
UPLOAD_DIRECTORY = "./"
```

Переконайтеся, що вказаний каталог існує, і додаток має необхідні права для запису в нього.