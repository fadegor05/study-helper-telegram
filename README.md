# 📚 StudyHelper - Бот для Расписания и Домашнего Задания

## 📜 Описание

Этот Telegram-бот автоматически парсит школьное расписание с официального сайта и предоставляет актуальную информацию о занятиях и домашнем задании. В случае изменений расписания или заданий, редакторы могут легко внести правки через интерфейс бота.

## 🎯 Основные возможности

- **Автоматическое парсинг расписания:** Бот может обновлять расписание у себя, забирая его с сайта расписания школы и уведомляет учеников об изменениях.
- **Вся информация на кончиках пальцев:** Ученики могут запросить расписание на любой день недели, сегодня или завтра
- **Управление домашним заданием:** Редакторы могут добавлять, изменять и удалять домашние задания через бота, легко привязывая их к датам и предметам.
- **Уведомления о домашнем задании:** Ученики получают уведомления о новых домашних заданиях и сроках их выполнения.
- **Контроль над выполнением:** Ученики с легкостью смогут отслеживать выполненое домашнее задание, а также бот будет отображать сначала самое свежие и невыполненные задания, а только потом остальные.

## 🚚 Роадмап

- Парсинг расписания с сайта-сервиса школы mstimetables
- Редактирование созданного Д/З
- Уведомления об изменениях в расписании и об опубликованном Д/З
- Добавление дополнительных материалов к Д/З

## 📚 Как пользоваться

## 🚀 Установка и настройка

1. **Клонируйте репозиторий:**

   ```bash
   git clone git@github.com:fadegor05/Study-Helper-Telegram.git
   cd Study-Helper-Telegram
   ```

2. **Настройте .env**

   ```env
   TELEGRAM_TOKEN=
   MONGO_ROOT_USER=
   MONGO_ROOT_PASS=
   ```

3. **Запустите бота:**

   ```bash
   docker compose up
   ```

## 🛠 Стек

- **Python**
- **Aiogram**
- **Aiogram_dialog**
- **PostgreSQL**
- **Docker**

## 🗄️ MongoDB

### users

```
telegram_id: int
username: str
is_editor: boolean
homework_notification: boolean
schedule_notification: boolean
```

### hometasks

```
uuid: str
lesson_uuid: str
lesson: str
task: str
date: str
completed_by: [int]
images: [str]
```

### lessons

```
uuid: str
name: str

```

### schedule

```
day: int
name: str
lessons: [
    {
        name: str
        lesson_uuid: str
        start_time: str
        classroom: str
        building: str
    }
]
```
