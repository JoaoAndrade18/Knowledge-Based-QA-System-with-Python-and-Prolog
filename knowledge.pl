name('Universidade federal do ceará, Campus Jardins de Anita').
breif_description('É bom demuaissss.').
location('Localizado no municipio de itapajé, no estado do ceará, Brasil. A 100 KM da capital Fortaleza.').
established('Universidade federal do ceará, Campus Jardins de Anita', '2021').
first_vice_chancellor('Mafizuddin Ahmed (PhD in chemistry, Penn State)').
current_vice_chancellor('Professor God Master Arthur Franco').
history('A área que receberá a unidade da UFC no município foi doada à Universidade, em janeiro de 2014, pela família do empresário José Maria de Sousa Melo, falecido em 2011. O nome do campus, Jardins de Anita, é uma homenagem à esposa do empresário, Anita Inará, nascida na Letônia, também já falecida.').
area('697.56 acres which is 2.8 square kilometres').

number_of_faculties('1').
number_of_departments('3').


faculty('faculty of technology').

departments('Segurança da informação, Ciência de dados, Análise e desenvolvimento de sistemas').

departments_under_faculty('faculty of technology', 'department of Segurança da informação').
departments_under_faculty('faculty of technology', 'department of ciencia de dados').
departments_under_faculty('faculty of technology', 'department of Análise e desenvolvimento de sistemas').

department('department of Segurança da informação').

about_department of Segurança da informação('the Information Security department is the best').

chairman_of_cse('department of computer science and engineering', 'professor doctor mohammad imdadul islam').
developers('shamim imtiaz and kamrul hasan tusher').
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
introduction(X, Y) :-
    name(X),
    breif_description(Y).
history(X, Y) :-
    name(X),
    history(Y).
location(X, Y) :-
    name(X),
    location(Y).
area(X, Y) :-
    name(X),
    area(Y).
first_vice_chancellor(X, Y) :-
    name(X),
    first_vice_chancellor(Y).
vice_chancellor(X, Y) :-
    name(X),
    current_vice_chancellor(Y).
number_of_faculties(X, Y) :-
    name(X),
    number_of_faculties(Y).
number_of_departments(X, Y) :-
    name(X),
    number_of_departments(Y).
number_of_institutes(X, Y) :-
    name(X),
    number_of_institutes(Y).

faculties(X, Y) :-
    name(X),
    faculties(Y).
departments(X, Y) :-
    name(X),
    departments(Y).
departments_under_faculty(X, Y, Z) :-
    name(X),
    faculty(Y),
    departments_under_faculty(Y, Z).
about_department_of_computer_science_and_engineering(X, Y) :-
    name(X),
    about_department_of_computer_science_and_engineering(Y).
