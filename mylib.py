import numpy as np
import matplotlib.pyplot as plt

from statsmodels.distributions.empirical_distribution import ECDF
#15-50
# гистограммы
def show_bar_chart(numbers: list, bins: list, title = 'Гистограмма частот'):# matplotlib.pyplot as plt
    """
    input: numbers-data sample values   bins- (r- 1, r] r = 1,... borders hist
    """
    plt.figure(figsize=(8, 6))# аргументы щирина и высота в дюймах
    plt.hist(numbers, bins=bins, edgecolor='black', alpha=0.5) #создание гистограммы
    # alpha - прозрачность гистограммы

    plt.xlabel('Значения выборки')
    plt.ylabel('Частота значений')
    plt.title(title)

    plt.grid(True) # отображаем сетку
    plt.show()  

def show_hist_with_randUniform(count_numbers = 100, left_border_interval = 1, right_border_interval = 12):
    """
    exercise 15.50
    P.S.your right border += 2 and give to this function 
    """
    random_numbers = np.random.uniform(0, 1, count_numbers) # Генерация случайных чисел, распределенных равномерно с параметрами 1 и 0
    bins = [(r - 1) / 10 for r in range(left_border_interval, right_border_interval)] # Границы для гистограммы

    show_bar_chart(random_numbers, bins, f"15-50: Гистограмма частот для {count_numbers} чисел, распределенных равномерно")

def show_frequency_range(numbers, bins, title):
    plt.figure(figsize=(8, 6))
    freq, _ = np.histogram(numbers, bins=bins)
    plt.plot(bins[:-1], freq, color='blue')
    plt.xlabel('Значение')
    plt.ylabel('Частота')
    plt.title(title)
    plt.grid(True)
    plt.show()

def show_frequency_range_with_randUniform(count_numbers, left_border_interval = 1, right_border_interval = 13):
    """
    exercise 15.50
    P.S.your right border += 3 and give to this function 
    """
    random_numbers = np.random.uniform(0, 1, count_numbers) # Генерация случайных чисел, распределенных равномерно с параметрами 1 и 0
    bins = [(r - 1) / 10 for r in range(left_border_interval, right_border_interval)] # Границы для гистограммы

    show_frequency_range(random_numbers, bins, f"15-50: Полигон частот для {count_numbers} чисел, распределенных равномерно")
#testing function 15-50
def test_ex15_50():
    """
    testing function exercise №15-50
    """
    show_hist_with_randUniform(50)# test histogram
    show_hist_with_randUniform(80)# test histogram
    show_hist_with_randUniform(100)# test histogram

    show_frequency_range_with_randUniform(50)
    show_frequency_range_with_randUniform(80)
    show_frequency_range_with_randUniform(100)

# def plot_empirical_cdf(sample):
#     hist, edges = np.histogram(sample, bins=len(sample))
#     Y = hist.cumsum()
#     for i in range(len(Y)):
#         plt.plot([edges[i], edges[i+1]],[Y[i], Y[i]], c="blue")
#     plt.show()

def plot_empirical_distribution_function(sample, title = 'Эмпирическая функция распределения'):
    ecdf = ECDF(sample)
    plt.step(ecdf.x, ecdf.y)
    plt.ylabel('$F(x)$', fontsize=20)
    plt.xlabel('$x$', fontsize=20)# строим эмпирическую функцию по выборке
    plt.title(title)
    plt.grid(True)
    plt.show()

#testing function 15-53
def test_ex15_53():
    numbers = [0.01, 0.04, 0.17, 0.18, 0.22, 0.22, 0.25, 0.25,
    0.29, 0.42, 0.46, 0.47, 0.47, 0.56, 0.59, 0.67, 0.68,
    0.70, 0.72, 0.76, 0.78, 0.83, 0.85, 0.87, 0.93, 1.00,
    1.01, 1.01, 1.02, 1.03, 1.05, 1.32, 1.34, 1.37, 1.47,
    1.50, 1.52, 1.54, 1.59, 1.71, 1.90, 2.10, 2.35, 2.46,
    2.46, 2.50, 3.73, 4.07, 6.03]
    bins = [(r - 1) / 10 for r in range(1, 10)]
    show_bar_chart(numbers, bins, '15-53: Гистограмма для вариационного ряда')
    show_frequency_range(numbers, bins, '15-53: Полигон частот для вариационного ряда')
    plot_empirical_distribution_function(numbers, '15-53: Эмпирическая функция распределения')