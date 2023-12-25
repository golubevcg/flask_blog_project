from main import app, db
from services.logger_service import main_logger

# seeding data
with app.app_context():
    admin_user = db.session().execute("SELECT * FROM public.users WHERE login='admin'").first()
    if not admin_user:
        sql_users_init = open("db_seed_sql_scripts/init_users.sql")
        db.session().execute(sql_users_init.read())
        db.session.commit()
        sql_users_init.close()

    # debug=True
    # if debug:
    #     sql_test_posts_data = open("db_seed_sql_scripts/db_init_test_data.sql")
    #     db.session().execute(sql_test_posts_data.read())
    #     db.session.commit()
    #     sql_test_posts_data.close()
