import matplotlib.pyplot as plt
import numpy as np

models = ["Kuggo Kirin M5", "Ninebot Max G30", "Xiaomi Mi Electric Scooter Pro 2", "Halten RS-02"]
name_char = [
    "Максимальная скорость(км/ч)",
    "Запас хода(км)",
    "Мощность мотора (Вт)",
    "Ёмкость батареи (А\Ч)",
    "Вес(кг)",
    "Максимальная нагрузка (кг)"
]
char = [
    [55, 60, 1000, 21, 35, 150],
    [30, 65, 350, 15, 19.2, 100],
    [25, 45, 300, 12.8, 14.2, 100],
    [40, 50, 800, 18, 28, 130]
]


def get_normal(char):
    normal = []
    for item in char:
        normal.append([a / b for a, b in zip(item, char[0])])
    return normal


def get_quality(normal):
    result = []
    for item in normal:
        result.append(round(sum(item) / len(item), 2))
    return result


def create_bar(name, values):
    plt.figure(figsize=(12, 6))           # Увеличиваем размер
    plt.bar(name, values, color='skyblue')
    plt.xlabel("Модель", fontsize=12)
    plt.ylabel("Kту", fontsize=12)
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.title("Коэффициент технического уровня (Kту)", fontsize=14)
    plt.subplots_adjust(bottom=0.35)      # Отступ снизу 35%
    plt.show()


def create_radial(models, name, values):

    for item in values:
        item += item[:1]

    angles = np.linspace(0, 2 * np.pi, len(name), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(projection="polar"))

    for i in range(len(values)):
        ax.plot(angles, values[i], "o-", linewidth=2, label=models[i])

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(name, fontsize=10)
    ax.set_ylim(0, 2)

    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.0))
    plt.title("Сравнение относительных характеристик", pad=20)
    plt.show()


data = get_quality(get_normal(char))
create_bar(models, data)
create_radial(models, name_char, get_normal(char))