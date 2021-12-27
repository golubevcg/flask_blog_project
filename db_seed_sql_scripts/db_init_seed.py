from main import app, db
from services.logger_service import main_logger

# seeding data
with app.app_context():
    existing_post1 = db.session().execute("SELECT * FROM public.posts WHERE id=12").first()
    existing_post2 = db.session().execute("SELECT * FROM public.posts WHERE id=13").first()

    if not existing_post1 or not existing_post2:
        sql_posts_init = open("db_seed_sql_scripts/init_posts.sql")
        db.session().execute(sql_posts_init.read())
        db.session.commit()
        sql_posts_init.close()

    admin_user = db.session().execute("SELECT * FROM public.users WHERE login='admin'").first()
    if not admin_user:
        sql_users_init = open("db_seed_sql_scripts/init_users.sql")
        db.session().execute(sql_users_init.read())
        db.session.commit()
        sql_users_init.close()
