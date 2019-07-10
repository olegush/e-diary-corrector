import os
import random
from datacenter.models import Schoolkid, Mark, Сhastisement, Lesson, Commendation


MARKS_TO_FIX = [1, 2, 3]
NEW_MARKS = [4, 5]
SUBJECT_FOR_COMMENDATION = 'Музыка'
COMMENDATIONS = ['Молодец!', 'Отлично!', 'Хорошо!', 'Гораздо лучше моих ожиданий!', 'Ты меня приятно удивил!', 'Великолепно!', 'Прекрасно!', 'Ты меня очень обрадовал!', 'Сказано здорово – просто и ясно!', 'Ты, как всегда, точен!', 'Очень хороший ответ!', 'Талантливо!', 'Ты сегодня прыгнул выше головы!', 'Я в восхищении!', 'Уже существенно лучше!', 'Потрясающе!', 'Замечательно!', 'Прекрасное начало!', 'Так держать!', 'Ты на верном пути!', 'Здорово!', 'Это как раз то, что нужно!', 'Я тобой горжусь!', 'С каждым разом у тебя получается всё лучше!', 'Мы с тобой не зря поработали!', 'Я вижу, как ты стараешься!', 'Ты растешь над собой!', 'Ты многое сделал, я это вижу!', 'Теперь у тебя точно все получится!']


def fix_marks(schoolkid, marks_to_fix, new_marks):
    marks = Mark.objects.filter(schoolkid=schoolkid, points__in=marks_to_fix)
    if len(marks) == 0:
        print(f'Найдено плохих оценок: {len(marks)}. Исправлять нечего...')
        return
    print(f'Найдено плохих оценок: {len(marks)}. Запускаем исправление...')
    for mark in marks:
        old_mark = mark.points
        new_mark = random.choice(new_marks)
        mark.points = new_mark
        mark.save()
        print(f'Оценка "{old_mark}" от {mark.created} исправлена на "{new_mark}"')


def remove_chastisements(schoolkid):
    chastisements = Сhastisement.objects.filter(schoolkid=schoolkid)
    if len(chastisements) == 0:
        print(f'Найдено замечаний: {len(chastisements)}. Удалять нечего...')
        return
    print(f'Найдено замечаний: {len(chastisements)}. Запускаем удаление...')
    for chastisement in chastisements:
        chastisement.delete()
        print(f'Замечание "{chastisement.text}" от {chastisement.created} удалено')


def create_commendation(schoolkid, subject):
    lesson = Lesson.objects.filter(
                                year_of_study=schoolkid.year_of_study,
                                group_letter=schoolkid.group_letter,
                                subject__title=subject).order_by('?')[0]
    text = random.choice(COMMENDATIONS)
    Commendation.objects.create(
                            text=text,
                            created=lesson.date,
                            schoolkid=schoolkid,
                            subject=lesson.subject,
                            teacher=lesson.teacher)
    print(f'Похвала "{text}" добавлена, обновите страницу ученика')
