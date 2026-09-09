SELECT
    t.last_name AS "Фамилия",
    t.first_name AS "Имя",
    d.department_name AS "Кафедра",
    t.base_rate AS "Оклад",
    t.allowance AS "Надбавка",
    (t.base_rate + t.allowance) AS "Итоговая Зарплата"
FROM teacher t
JOIN departments d ON t.department_id = d.department_id
WHERE d.department_name = 'Экономика и управление';
