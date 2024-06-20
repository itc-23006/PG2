import pandas as pd


def create_multiplication_table(num):
    """
    九九の表を作成する
    :param num: 作成する表のサイズ
    :return: 九九の表
    """
    multiplication_table = [[i * j for j in range(1, num + 1)] for i in range(1, num + 1)]
    return multiplication_table


def write_multiplication_table_to_excel(multiplication_table):
    """
    九九の表をExcelファイルに書き込む
    :param multiplication_table:九九の表
    :return:
    """
    df = pd.DataFrame(multiplication_table, index=range(1, len(multiplication_table) + 1),
                      columns=range(1, len(multiplication_table) + 1))
    df.to_excel('multiplication_table.xlsx', index=True, header=True)


if __name__ == '__main__':
    num = 9
    multiplication_table = create_multiplication_table(num)
    write_multiplication_table_to_excel(multiplication_table)

    print('完了')
