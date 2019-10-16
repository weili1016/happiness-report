import pandas as pd
import matplotlib.pyplot as plt
# scatter between ladder and freedom
def main():
    df = pd.read_csv('new-happiness-2019.csv')
    ladder = df['Ladder']
    freedom = df['Freedom']
    plt.scatter(ladder,freedom)
    plt.title('relation between ladder and freedom')
    plt.xlabel('ladder')
    plt.ylabel('freedom')
    plt.show()
if __name__=='__main__':
    main()
# scatter between ladder and social support

def main():
    df = pd.read_csv('new-happiness-2019.csv')
    ladder = df['Ladder']
    social_support = df['Social_support']
    plt.scatter(ladder,social_support,c='r')
    plt.title('relation between ladder and social support')
    plt.xlabel('ladder')
    plt.ylabel('social_support')
    plt.show()
if __name__=='__main__':
    main()

# scatter between ladder and generosity
def main():
    df = pd.read_csv('new-happiness-2019.csv')
    ladder = df['Ladder']
    generosity = df['Generosity']
    plt.scatter(ladder,generosity)
    plt.title('relation between ladder and generosity')
    plt.xlabel('ladder')
    plt.ylabel('generosity')
    plt.show()
if __name__=='__main__':
    main()
# scatter between ladder and corruption
def main():
    df = pd.read_csv('new-happiness-2019.csv')
    ladder = df['Ladder']
    corruption = df['Corruption']
    plt.scatter(ladder,corruption)
    plt.title('relation between ladder and corruption')
    plt.xlabel('ladder')
    plt.ylabel('corruption')
    plt.show()
if __name__=='__main__':
    main()
# scatter between ladder and GDP
def main():
    df = pd.read_csv('new-happiness-2019.csv')
    ladder = df['Ladder']
    GDP = df['Log_of_GDP']
    plt.scatter(ladder,GDP,c='r')
    plt.title('relation between ladder and GDP')
    plt.xlabel('ladder')
    plt.ylabel('GDP')
    plt.show()
if __name__=='__main__':
    main()
# scatter between ladder and life expectancy

def main():
    df = pd.read_csv('new-happiness-2019.csv')
    ladder = df['Ladder']
    life_expectancy= df['Healthy_life']
    plt.scatter(ladder,life_expectancy,c='r')
    plt.title('relation between ladder and life_expectancy')
    plt.xlabel('ladder')
    plt.ylabel('life_expectancy')
    plt.show()
if __name__=='__main__':
    main()