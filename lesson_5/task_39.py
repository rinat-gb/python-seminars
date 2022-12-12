#!/usr/bin/python
#
# 39. Создайте программу для игры с конфетами человек против человека.
#
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать
# все конфеты у своего конкурента?
#
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""
#
import random

NUM_OF_CANDIES = 2021
NO_MORE = 28

first_name = input('Введите имя первого игрока: ')
second_name = input('Введите имя второго игрока игрока: ')

player_start = random.randint(0, 1)

print(f'Начинает игрок {first_name if player_start else second_name}')

bunch = NUM_OF_CANDIES

def take_candies(who_take):
    print(f'\nВ коробке сейчас {bunch} конфет.')
    while True:
        taken = int(input(f'Ну что, {first_name if who_take else second_name}, сколько конфет возьмёшь? '))
        if taken > NO_MORE:
            print(f'Нельзя брать больше {NO_MORE} конфет!\n')
            continue
        elif taken > bunch:
            print(f'В коробке всего {bunch} конфет, а ты хочешь взять {taken}!\n')
        else:
            break
    return taken


while True:
    taken = take_candies(player_start)
    bunch -= taken
    if not bunch:
        print(f'{first_name if player_start else second_name}, ты победил!')
        break
    taken = take_candies(not player_start)
    bunch -= taken
    if not bunch:
        print(f'{first_name if not player_start else second_name}, ты победил!')
        break
