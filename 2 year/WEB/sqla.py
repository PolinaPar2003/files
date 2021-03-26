from flask import Flask, render_template
from data import db_session
from data.users import User
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


@app.route("/")
def index():
    db_sess = db_session.create_session()
    job = db_sess.query(Jobs).filter(Jobs.is_finished is not True)
    return render_template("index.html", job=job)


def main():
    db_session.global_init("db/mars_explorer.db")
    user_kap = User()
    user_kap.surname = "Scott"
    user_kap.name = "Ridley"
    user_kap.age = 21
    user_kap.position = "captain"
    user_kap.speciality = "research engineer"
    user_kap.address = "module_1"
    user_kap.email = "scott_chief@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user_kap)
    db_sess.commit()

    user_1 = User()
    user_1.surname = "Peter"
    user_1.name = "Polosh"
    user_1.age = 44
    user_1.position = "junior commander"
    user_1.speciality = "senior mechanic"
    user_1.address = "module_2"
    user_1.email = "peter_starhot@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user_1)
    db_sess.commit()

    user_2 = User()
    user_2.surname = "Harry"
    user_2.name = "Brown"
    user_2.age = 23
    user_2.position = "executor"
    user_2.speciality = "sailor"
    user_2.address = "module_4"
    user_2.email = "harry_Brown1234@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user_2)
    db_sess.commit()

    user_3 = User()
    user_3.surname = "Naill"
    user_3.name = "Horan"
    user_3.age = 32
    user_3.position = "assistant captain"
    user_3.speciality = "radio operator"
    user_3.address = "module_2"
    user_3.email = "Horan_not_horn@mars.org"
    db_sess = db_session.create_session()
    db_sess.add(user_3)
    db_sess.commit()

    job = Jobs(team_leader=1, job="deployment of residential modules 1 and 2", work_size=15,
               collaborators="2, 3", is_finished=False)
    db_sess.add(job)
    db_sess.commit()
    app.run()


if __name__ == '__main__':
    main()
