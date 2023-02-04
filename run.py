from flask import Flask

# Импортируем блюпринт
from app.main.views import main_blueprint
from app.candidates.views import candidates_blueprint
from app.vacancies.views import vacancies_blueprint


# Создаем экземпляр Flask
app = Flask(__name__)

# регистрируем блюпринт
app.register_blueprint(main_blueprint)
app.register_blueprint(candidates_blueprint)
app.register_blueprint(vacancies_blueprint)



if __name__ == "__main__":
    app.run()