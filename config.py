env_vars = {
  # Get From my.telegram.org
  "API_HASH": "593fe8c703eac6d6586e7bbdfb9a35b4",
  "API_ID": "23432718",

  # Get From @BotFather
  "BOT_TOKEN": "7890746924:AAHnho6u0Bb1TlEX8zCkso_2ofNQgt4tLTo",

  # MongoDB connection string
  "DATABASE_URL_PRIMARY": "mongodb+srv://fbpmmv59gm:23032020@cluster0.11mn5yj.mongodb.net/?retryWrites=true&w=majority",

  # Logs Channel Username Without @
  "CACHE_CHANNEL": "free_manga_dump",

  # Force Subs Channel username without @
  "CHANNEL": "@free_manga_dump",

  # {chap_num}: Chapter Number
  # {chap_name}: Manga Name
  "FNAME": "",

  # Thumbnail link
  "THUMB": ""
}

# Just use MongoDB directly
dbname = env_vars.get('DATABASE_URL_PRIMARY') or 'mongodb://localhost:27017'
