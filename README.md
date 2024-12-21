## Документация Telegram-бота прогноза погоды

### Описание проекта
Telegram-бот предоставляет прогноз погоды на ближайшие три дня (“Сегодня”, “Завтра” и “Послезавтра”). Пользователи могут выбрать день через удобный интерфейс с кнопками, предоставить доступ к своей геолокации, и бот отправит актуальный прогноз с минимальной и максимальной температурой, а также количеством осадков.

### Функциональность
1. **Отображение клавиатуры с выбором дня:** “Сегодня”, “Завтра”, “Послезавтра”.
2. **Получение прогноза погоды на выбранный день:** бот запрашивает доступ к геолокации пользователя и предоставляет прогноз для текущего местоположения.
3. **Кнопка “Назад”:** позволяет вернуться к выбору дня.

### Требования
- Python 3.7 или выше
- Доступ к интернету
- Токен Telegram-бота

### Установка зависимостей
```bash
pip install pyTelegramBotAPI
pip install requests
```

### Настройка проекта
1. Создайте нового бота через @BotFather в Telegram и получите токен.
2. Замените значение переменной `TOKEN` в коде на ваш токен:
```python
TOKEN = 'ваш_токен_бота'
```

### Структура проекта

#### Основные компоненты
1. **Константы:**
   - `DAYS` — словарь, соответствующий дням (“Сегодня”, “Завтра”, “Послезавтра”) и их индексам.
2. **Функции:**
   - `send_welcome` — обрабатывает команду `/start` и создает клавиатуру для выбора дня.
   - `echo_message` — обрабатывает выбор дня и отображает кнопку для предоставления доступа к геолокации.
   - `handle_location` — получает координаты пользователя и отправляет прогноз погоды.

#### Используемые библиотеки
- **telebot:** для работы с Telegram Bot API.
- **requests:** для выполнения HTTP-запросов.

### Запуск бота
1. Сохраните код в файл с расширением `.py` (например, `weather_bot.py`).
2. Откройте терминал в директории с файлом.
3. Запустите бот командой:
```bash
python weather_bot.py
```

### Использование бота
1. Найдите бота в Telegram по его имени.
2. Отправьте команду `/start`.
3. Выберите интересующий день нажатием на соответствующую кнопку.
4. Предоставьте доступ к геолокации.
5. Получите прогноз погоды на выбранный день.

### Возможные проблемы и их решение
- **Бот не отвечает:**
  - Проверьте правильность токена.
  - Убедитесь, что бот не заблокирован пользователем.
  - Проверьте подключение к интернету.
- **Прогноз погоды не отображается:**
  - Проверьте доступность API Open-Meteo.
  - Проверьте, передаются ли корректные координаты.

### Безопасность
- Не публикуйте токен бота в публичном доступе.
- Регулярно проверяйте и обновляйте зависимости.
- Используйте актуальные версии Python и библиотек.

---

## Telegram Weather Bot Documentation

### Project Description
The Telegram bot provides weather forecasts for the next three days (“Today”, “Tomorrow”, and “Day After Tomorrow”). Users can select a day using a convenient button-based interface, share their location, and receive the forecast with minimum and maximum temperatures as well as precipitation amounts.

### Features
1. **Day Selection Keyboard:** Options for “Today”, “Tomorrow”, and “Day After Tomorrow”.
2. **Weather Forecast Retrieval:** The bot requests access to the user’s location and provides a forecast for the current location.
3. **Back Button:** Allows users to return to the day selection menu.

### Requirements
- Python 3.7 or higher
- Internet access
- Telegram bot token

### Installing Dependencies
```bash
pip install pyTelegramBotAPI
pip install requests
```

### Project Setup
1. Create a new bot using @BotFather on Telegram and obtain the token.
2. Replace the value of the `TOKEN` variable in the code with your token:
```python
TOKEN = 'your_bot_token'
```

### Project Structure

#### Main Components
1. **Constants:**
   - `DAYS` — a dictionary mapping days (“Today”, “Tomorrow”, “Day After Tomorrow”) to their indices.
2. **Functions:**
   - `send_welcome` — handles the `/start` command and creates a keyboard for day selection.
   - `echo_message` — processes the selected day and displays a button to request location access.
   - `handle_location` — retrieves user coordinates and sends the weather forecast.

#### Libraries Used
- **telebot:** for interacting with the Telegram Bot API.
- **requests:** for making HTTP requests.

### Running the Bot
1. Save the code to a `.py` file (e.g., `weather_bot.py`).
2. Open a terminal in the file’s directory.
3. Start the bot with the command:
```bash
python weather_bot.py
```

### Using the Bot
1. Find the bot on Telegram using its name.
2. Send the `/start` command.
3. Select the desired day by pressing the corresponding button.
4. Provide location access.
5. Receive the weather forecast for the selected day.

### Troubleshooting
- **Bot Not Responding:**
  - Verify the token.
  - Ensure the bot is not blocked by the user.
  - Check the internet connection.
- **Weather Forecast Not Displayed:**
  - Verify Open-Meteo API availability.
  - Ensure correct coordinates are being passed.

### Security
- Do not publish the bot token publicly.
- Regularly check and update dependencies.
- Use the latest versions of Python and libraries.

