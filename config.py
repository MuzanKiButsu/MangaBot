env_vars = {
  # Get From my.telegram.org
  "API_HASH": "593fe8c703eac6d6586e7bbdfb9a35b4",
  # Get From my.telegram.org
  "API_ID": "23432718",
  #Get For @BotFather
  "BOT_TOKEN": "7890746924:AAHnho6u0Bb1TlEX8zCkso_2ofNQgt4tLTo",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://postgres.wykeqyvumnnoghyfeqow:GOJOISTHEstrongest@2020@aws-1-us-east-2.pooler.supabase.com:6543/postgres",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "free_manga_dump",
  # Force Subs Channel username without @
  "CHANNEL": "@free_manga_dump",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
