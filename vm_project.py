import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

'''
допущения: 
1) при загрузке своих данных родается "чистый" датасет
2) пользователь знает основные правила визуализации (что на оси x, что на оси y)
'''



def load_data():
    print('Вы хотите загрузить свой датасет (1) или скачать публичный (2)?')
    ans = int(input('Введите цифру: '))
    if ans == 1:
        path = input('Введите путь к файлу: ').strip('"').replace('\\', '/')
        df = pd.read_csv(path)
    elif ans == 2:
        print(f"Доступные датасеты: {sns.get_dataset_names()}")
        sett = str(input("Выберите датасет: "))
        df = sns.load_dataset(sett) 
    else:
        print("Некорректный ввод, попробуйте снова.")
        return load_data()
    
    print('\nИнформация о датасете:')
    print(df.info())
    print('\nПервые строки:')
    print(df.head())
    return df


def choose_plot_type():
    print("\nВыберите тип визуализации:")
    print("1 — Scatterplot (точечная диаграмма)")
    print("2 — Barplot (столбчатая диаграмма)")
    print("3 — Boxplot (ящик с усами)")
    choice = int(input("Введите цифру: "))

    if choice == 1:
        return "scatter"
    elif choice == 2:
        return "bar"
    elif choice == 3:
        return "box"
    else:
        print("Некорректный ввод. Попробуйте снова.")
        return choose_plot_type()


def choose_axes(df):
    print("Доступные колонки:", df.columns.tolist())

    columns_map = {col.lower(): col for col in df.columns}

    x_col_input = input("Выберите колонку для оси X: ").lower().strip()
    y_col_input = input("Выберите колонку для оси Y: ").lower().strip()

    if x_col_input not in columns_map or y_col_input not in columns_map:
        print("❌ Одна или обе колонки введены неверно.")
        return

    x_col = columns_map[x_col_input]
    y_col = columns_map[y_col_input]
    return x_col,y_col


def plot_data(df, plot_type, x_col, y_col):
    plt.figure(figsize=(8, 5))
    if plot_type == "scatter":
        sns.scatterplot(data=df, x=x_col, y=y_col)
    elif plot_type == "bar":
        sns.barplot(data=df, x=x_col, y=y_col)
    elif plot_type == "box":
        sns.boxplot(data=df, x=x_col, y=y_col)
    else:
        print("Неизвестный тип графика.")
        return

    plt.title(f"{plot_type.capitalize()} of {y_col} by {x_col}")
    plt.tight_layout()
    dl = input('Нажмите +, если хотите скачать этот график')
    if dl == '+':
        name = (input('Как назовете файл?').strip(' '))+'.png'
        plt.savefig(name)
    plt.show()

    

def visualize():
    df = load_data()
    plot_type = choose_plot_type()
    x_col, y_col = choose_axes(df)
    plot_data(df, plot_type, x_col, y_col) 


if __name__ == "__main__":
    visualize()


 
        
        