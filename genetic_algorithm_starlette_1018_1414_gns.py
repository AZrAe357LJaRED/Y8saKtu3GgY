# 代码生成时间: 2025-10-18 14:14:09
import random
from typing import Callable, List, Tuple
from starlette.applications import Starlette
from starlette.responses import JSONResponse
from starlette.routing import Route

# 定义遗传算法的基础类
class GeneticAlgorithm:
    def __init__(self, 
                 population_size: int, 
                 gene_length: int, 
                 crossover_rate: float, 
                 mutation_rate: float, 
                 fitness_function: Callable):
        self.population_size = population_size
        self.gene_length = gene_length
        self.crossover_rate = crossover_rate
        self.mutation_rate = mutation_rate
        self.fitness_function = fitness_function
        self.population = [self.generate_individual() for _ in range(population_size)]

    # 生成个体
    def generate_individual(self) -> List[int]:
        return [random.randint(0, 1) for _ in range(self.gene_length)]

    # 计算适应度
    def calculate_fitness(self, individual: List[int]) -> float:
        return self.fitness_function(individual)

    # 选择
    def selection(self) -> List[List[int]]:
        fitness_scores = [self.calculate_fitness(individual) for individual in self.population]
        fitness_sum = sum(fitness_scores)
        selected = []
        for _ in range(self.population_size):
            r = random.uniform(0, fitness_sum)
            cumulative_sum = 0
            for individual, score in zip(self.population, fitness_scores):
                cumulative_sum += score
                if r <= cumulative_sum:
                    selected.append(individual)
                    break
        return selected

    # 交叉
    def crossover(self, parent1: List[int], parent2: List[int]) -> Tuple[List[int], List[int]]:
        if random.random() > self.crossover_rate:
            return parent1, parent2

        crossover_point = random.randint(1, self.gene_length - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        return child1, child2

    # 变异
    def mutate(self, individual: List[int]) -> List[int]:
        for i in range(self.gene_length):
            if random.random() < self.mutation_rate:
                individual[i] = 1 - individual[i]
        return individual

    # 进化一代
    def evolve(self) -> None:
        new_population = []
        for _ in range(self.population_size // 2):
            parent1, parent2 = random.sample(self.population, 2)
            child1, child2 = self.crossover(parent1, parent2)
            new_population.extend([self.mutate(child1), self.mutate(child2)])
        self.population = new_population

# 示例适应度函数
def example_fitness_function(individual: List[int]) -> float:
    """
    适应度函数示例，计算个体中1的个数。
    """
    return sum(individual)

# 创建遗传算法实例
ga = GeneticAlgorithm(
    population_size=100, 
    gene_length=10, 
    crossover_rate=0.7, 
    mutation_rate=0.01, 
    fitness_function=example_fitness_function
)

# 创建Starlette应用
app = Starlette(debug=True)

# 路由和视图函数
@app.route("/evolve", methods=["GET"])
async def evolve(request):
    """
    用于进化遗传算法的一代。
    """
    try:
        ga.evolve()
        return JSONResponse({"message": "Evolution completed"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)

# 运行应用
if __name__ == "__main__":
    app.run()
