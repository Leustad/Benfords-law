import os

import matplotlib.pyplot as plt


class BenfordsLaw:
    guidelines = [30.1, 17.6, 12.5, 9.7, 7.9, 6.7, 5.8, 5.1, 4.6]

    def __init__(self):
        self.file_names = [name for name in os.listdir('./source') if '.txt' in name]
        self.pool_size = 0
        self.numbers = []
        self.counts = {}

    def _clear(self):
        self.pool_size = 0
        self.numbers = []
        self.counts = {}

    def get_numbers(self, filename):
        for i in self.numbers:
            first_digit = str(i)[0]
            if first_digit not in self.counts.keys():
                self.counts[first_digit] = 0
            self.counts[first_digit] += 1

        self.counts = {k: self.counts[k] for k in sorted(self.counts)}
        self.report(filename)

    def report(self, filename):
        numbers = [k for k in self.counts.keys()]
        percents = [(v / self.pool_size) * 100 for v in self.counts.values()]

        fig = plt.figure(num=1, figsize=(15, 5), dpi=80, facecolor='w', edgecolor='k')

        plt.bar(numbers, percents, color='maroon', width=0.4)
        plt.plot(numbers, BenfordsLaw.guidelines, color='mediumblue', label="Benford's Law")
        plt.margins(y=0.1)
        plt.plot([], [], ' ', label="""
1: 30.1 %
2: 17.6 %
3: 12.5 %
4: 9.7 %
5: 7.9 %
6: 6.7 %
7: 5.8 %
8: 5.1 %
9: 4.6 %"""
                 )
        plt.legend(bbox_to_anchor=(1.05, 1.0), loc='upper left')

        plt.xlabel('First Digit of the Numbers')
        plt.ylabel('P_k[%]')
        plt.title(filename)
        plt.tight_layout()

        print(filename)
        for k, v in sorted(self.counts.items()):
            print(f'{k}: %{(v / self.pool_size) * 100}')
        print('\n')

        for x, y in zip(numbers, percents):
            label = "{:.2f}".format(y)

            plt.annotate(
                    label,
                    (x, y),
                    textcoords="offset points",  # how to position the text
                    xytext=(0, 10),  # distance from text to points (x,y)
                    ha='center'
            )

        # plt.show()
        plt.savefig(f"./output/{filename}.jpg")
        plt.clf()

    def run(self):
        for file_name in self.file_names:
            self._clear()
            with open(f'source/{file_name}', 'r') as file:
                for _ in file.readlines():
                    self.pool_size += 1
                    self.numbers.append(_)
            self.get_numbers(file_name.split('.')[0])


def main():
    BenfordsLaw().run()


if __name__ == '__main__':
    main()
