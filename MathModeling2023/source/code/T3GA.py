import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
import pandas as pd


if __name__ == "__main__":
    price = pd.read_csv('../data/单价7月1日预估.csv', encoding='utf-8')
    costPrice = pd.read_csv('../data/成本价7月1日预估.csv', encoding='utf-8')
    volume = pd.read_csv('../data/销售量7月1日预估.csv', encoding='utf-8')
    ans = pd.DataFrame([])
    ans['P'] = 0
    ans['D'] = 0
    ans['F'] = 0
    for index in price:
        if index == '列数':
            continue
        if index in costPrice and index in volume:
            print(index)
            print('-'*30)

            DNA_SIZE = 24
            POP_SIZE = 200
            CROSSOVER_RATE = 0.8
            MUTATION_RATE = 0.005
            N_GENERATIONS = 50
            X_BOUND = [price[index][0] - 1, price[index][0] + 1]
            Y_BOUND = [2.5, 10]
            Q = volume[index][0]
            C = costPrice[index][0]

            def F(x, y):
                return x * 0.5 * (Q + y - abs(Q - y)) - y * C


            def get_fitness(pop):
                x, y = translateDNA(pop)
                pred = F(x, y)
                return (pred - np.min(
                    pred)) + 1e-3
                # 减去最小的适应度是为了防止适应度出现负数，通过这一步fitness的范围为[0, np.max(pred)-np.min(pred)],最后在加上一个很小的数防止出现为0的适应度


            def translateDNA(pop):
                # pop表示种群矩阵，一行表示一个二进制编码表示的DNA，矩阵的行数为种群数目
                x_pop = pop[:, 1::2]
                # 奇数列表示X
                y_pop = pop[:, ::2]
                # 偶数列表示y

                # pop:(POP_SIZE,DNA_SIZE)*(DNA_SIZE,1) --> (POP_SIZE,1)
                x = x_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (X_BOUND[1] - X_BOUND[0]) + \
                    X_BOUND[0]
                y = y_pop.dot(2 ** np.arange(DNA_SIZE)[::-1]) / float(2 ** DNA_SIZE - 1) * (Y_BOUND[1] - Y_BOUND[0]) + \
                    Y_BOUND[0]
                return x, y


            def crossover_and_mutation(pop, CROSSOVER_RATE=0.8):
                new_pop = []
                for father in pop:
                    # 遍历种群中的每一个个体，将该个体作为父亲
                    child = father
                    # 孩子先得到父亲的全部基因（这里我把一串二进制串的那些0，1称为基因）
                    if np.random.rand() < CROSSOVER_RATE:
                        # 产生子代时不是必然发生交叉，而是以一定的概率发生交叉
                        mother = pop[np.random.randint(POP_SIZE)]
                        # 再种群中选择另一个个体，并将该个体作为母亲
                        cross_points = np.random.randint(low=0, high=DNA_SIZE * 2)
                        # 随机产生交叉的点
                        child[cross_points:] = mother[cross_points:]
                        # 孩子得到位于交叉点后的母亲的基因
                    mutation(child)
                    # 每个后代有一定的机率发生变异
                    new_pop.append(child)

                return new_pop


            def mutation(child, MUTATION_RATE=0.003):
                if np.random.rand() < MUTATION_RATE:  # 以MUTATION_RATE的概率进行变异
                    mutate_point = np.random.randint(0, DNA_SIZE * 2)  # 随机产生一个实数，代表要变异基因的位置
                    child[mutate_point] = child[mutate_point] ^ 1  # 将变异点的二进制为反转


            def select(pop, fitness):
                # nature selection wrt pop's fitness
                idx = np.random.choice(np.arange(POP_SIZE), size=POP_SIZE, replace=True,
                                       p=(fitness) / (fitness.sum()))
                return pop[idx]


            def print_info(pop):
                fitness = get_fitness(pop)
                max_fitness_index = np.argmax(fitness)
                print("max_fitness:", fitness[max_fitness_index])
                x, y = translateDNA(pop)
                print("最优的基因型：", pop[max_fitness_index])
                print("(x, y):", (x[max_fitness_index], y[max_fitness_index]))
                ans.at[index, 'P'] = x[max_fitness_index]
                ans.at[index, 'D'] = y[max_fitness_index]
                ans.at[index, 'F'] = x[max_fitness_index] * 0.5 * (Q + y[max_fitness_index] - abs(Q - y[max_fitness_index])) - y[max_fitness_index] * C
                print(ans)
            fit = []
            pop = np.random.randint(2, size=(POP_SIZE, DNA_SIZE * 2))
            # matrix (POP_SIZE, DNA_SIZE)
            for i in range(N_GENERATIONS):
                # 迭代N代
                x, y = translateDNA(pop)
                pop = np.array(crossover_and_mutation(pop, CROSSOVER_RATE))
                # F_values = F(translateDNA(pop)[0], translateDNA(pop)[1])#x, y --> Z matrix
                fitness = get_fitness(pop)
                pop = select(pop, fitness)  # 选择生成新的种群
                fit.append(np.argmax(fitness))
            print(fit)
            print_info(pop)
    ans.to_csv('../data/遗传算法输出.csv', sep=',', encoding='utf_8_sig')

