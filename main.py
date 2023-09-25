from pyswip import Prolog
import time
import json


def prolog_query(query_string):
    prolog = Prolog()
    prolog.consult("knowledge.pl")
    results = []
    for res in prolog.query(query_string):
        results.append(res)

    return results


def ask_question(query_string):
    answers = prolog_query(query_string)
    return answers


def make_json(data):
    json_str = ""
    for c in data:
        if c == "'":
            json_str += '"'
            continue
        json_str += c
    return json_str


def say_answers(prefix, suffix, question_i, answers_i):
    for ansi in answers_i:
        ansi = make_json(str(ansi))
        obj = json.loads(str(ansi))
        print(obj[question_i])
        text = prefix + " " + obj[question_i] + " " + suffix
        print(">>>> ", text)


print(
    "Hi, I'm here to tell you about Universidade federal do ceará. \
                what do you want to know about Universidade federal do ceará?"
)
flg = True
while flg:
    # Q/A
    print("\n\n")
    asked_question = str(input("Oque você quer saber? ")).lower()

    if (
        "name of the university" in asked_question
        or "university name" in asked_question
        or "nome da universidade" in asked_question
    ):
        # Q: what is the name of the university?
        question = "UniversityName"
        query = "name(" + question + ")."
        answers = ask_question(query)
        say_answers("The name of the university ", "", question, answers)

    elif (
        "introduction" in asked_question
        or "about ju" in asked_question
        or "about Universidade federal do ceará, Campus Jardins de Anita" in asked_question
        or "me fale sobre a universidade" in asked_question
    ):
        # Q: what is Universidade federal do ceará, Campus Jardins de Anita?
        question = "Introduction"
        query = "introduction('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "history of ju" in asked_question
        or "history of Universidade federal do ceará, Campus Jardins de Anita" in asked_question
        or "história da universidade" in asked_question
    ):
        # Q: history of Universidade federal do ceará, Campus Jardins de Anita.
        question = "History"
        query = "history('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers("Brief history: ", "", question, answers)

    elif (
        "localização da universidade" in asked_question
        or "situated" in asked_question
    ):
        # Q: where is Universidade federal do ceará, Campus Jardins de Anita?
        question = "Location"
        query = "location('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif ("area of Universidade federal do ceará, Campus Jardins de Anita" in asked_question
        or "area da faculdade" in asked_question
    ):
        # Q: where is Universidade federal do ceará, Campus Jardins de Anita?
        question = "Area"
        query = "area('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "total area of Universidade federal do ceará, Campus Jardins de Anita is about ", "", question, answers
        )

    elif (
        "current" in asked_question
        or "present" in asked_question
        or "now" in asked_question
        or "quem é o diretor da faculdade" in asked_question
        or "diretor" in asked_question
    )and ("vice chancellor" in asked_question or "vc" in asked_question):
        # Q: who is the current vice_chancellor of Universidade federal do ceará, Campus Jardins de Anita?
        question = "Vice_chancellor"
        query = "vice_chancellor('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "The current vice chancellor of Universidade federal do ceará, Campus Jardins de Anita is ",
            "",
            question,
            answers,
        )

    elif (
        "number of faculties" in asked_question
        or "how many faculties" in asked_question
        and asked_question.find("faculty of") == -1
    ):
        # Q how many faculties are in jahangirnagr university
        question = "Number_of_faculties"
        query = "number_of_faculties('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "faculties in Universidade federal do ceará, Campus Jardins de Anita", question, answers
        )

    elif (
        "number of departments" in asked_question
        or "how many departments" in asked_question
        or "quantos cursos tem a faculdade" in asked_question
    ):
        # Q how many departments are in jahangirnagr university
        question = "Number_of_departments"
        query = "number_of_departments('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "cursos in Universidade federal do ceará, Campus Jardins de Anita", question, answers
        )

    elif (
        "number of institutes" in asked_question
        or "how many institutes" in asked_question
    ):
        # Q how many institutes are in jahangirnagr university
        question = "Number_of_institutes"
        query = "number_of_institutes('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "There are ", "institutes in Universidade federal do ceará, Campus Jardins de Anita", question, answers
        )

    elif (
        "names of the faculties" in asked_question
        or "what are the faculties" in asked_question
    ):
        # Q what are the faculties in Universidade federal do ceará, Campus Jardins de Anita
        question = "Facultiy"
        query = "faculties('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "there are 1 faculties are in Universidade federal do ceará, Campus Jardins de Anita, they are, ",
            "",
            question,
            answers,
        )

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
        or "quais são os cursos" in asked_question
    ) and "under the faculty of" in asked_question:
        # Q what are the names departments in faculty of X?
        faculties = [
            "faculty of technology"
        ]
        id = -1
        for i in range(6):
            if faculties[i] in asked_question:
                id = i
                break
        if id != -1:
            print(faculties[id])
            question = "Departments"
            query = (
                "departments_under_faculty('Universidade federal do ceará, Campus Jardins de Anita', '"
                + faculties[id]
                + "',"
                + question
                + ")."
            )
            answers = ask_question(query)
            print(">>>>> ", "the departments under " + faculties[id] + " are, ")
            say_answers("", "", question, answers)

        else:
            print(">>>>> ", "sorry, there is no such faculty.")

    elif (
        "names of the departments" in asked_question
        or "what are the departments" in asked_question
    ):
        # Q what are the departments in Universidade federal do ceará, Campus Jardins de Anita
        question = "Departments"
        query = "departments('Universidade federal do ceará, Campus Jardins de Anita', " + question + ")."
        answers = ask_question(query)
        say_answers(
            "there are 3 departments in Universidade federal do ceará, Campus Jardins de Anita, they are, ",
            "",
            question,
            answers,
        )

    elif (
        "about department of cse" in asked_question
        or "about cse" in asked_question
        or "about computer science and engineering" in asked_question
        or "about department of computer science and engineering" in asked_question
    ):
        # Q what you know about dept of CSE Universidade federal do ceará, Campus Jardins de Anita
        question = "Cse"
        query = (
            "about_department_of_computer_science_and_engineering(\
                'Universidade federal do ceará, Campus Jardins de Anita', "
            + question
            + ")."
        )
        answers = ask_question(query)
        say_answers("", "", question, answers)

    elif (
        "chairman of department of cse" in asked_question
        or "chairman of cse" in asked_question
        or "chairman of computer science and engineering" in asked_question
        or "chairman of department of computer science and engineering"
        in asked_question
    ):
        # Q who is the chairman of dept of CSE JU?
        question = "Chairman"
        query = (
            "chairman_of_cse('department of computer science and engineering', "
            + question
            + ")."
        )
        answers = ask_question(query)
        say_answers(
            "",
            "is the chairman of department of computer science and engineering",
            question,
            answers,
        )

    elif (
        "who are the developers of this project" in asked_question
        or "who developed" in asked_question
        or "who created" in asked_question
    ):
        # Q who developed this program?
        question = "Developers"
        query = "developers(" + question + ")."
        answers = ask_question(query)
        print(
            ">>>>> ",
            "This project is supervised by professor doctor mohammad shorif uddin.",
        )
        say_answers("the developers are", "", question, answers)

    elif "stop" in asked_question or "exit" in asked_question:
        print(">>>>> ", "thank you, hope you have enjoyed the session")
        break

    else:
        if asked_question != "-----------------":
            confirmation = str(
                input(
                    "Sorry, this is out of my knowledge. whould you like to continue? "
                )
            ).lower()
            
            if "no" in confirmation or "nope" in confirmation or "stop" in confirmation:
                print(">>>>> ", "thank you, hope you have enjoyed the session")
                break
            else:
                continue

        time.sleep(2)
