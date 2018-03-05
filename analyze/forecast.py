from dataBase.sql_helper import conn_db, exe_query, conn_close
from sklearn.linear_model import Lasso
import random


# import numpy as np
# import matplotlib.pyplot as plt
# import time
# from sklearn.metrics import r2_score


def get_data():
    """
    从数据库中获得数据
    :return:
    """
    x_train = []
    y_train = []
    x_test = []
    try:
        conn = conn_db()
        cur = conn.cursor()
        for i in range(2000):
            sql = "SELECT shop_id, location_id, per_pay, shop_level FROM ShopInfo WHERE shop_id='" + str(i + 1) + "'"
            shop_infos = exe_query(cur, sql)
            infos = shop_infos
            for m in range(14):
                for info in infos:
                    temp = []
                    temp.append(int(info[0]))
                    temp.append(int(info[1]))
                    temp.append(int(info[2]))
                    temp.append(int(info[3]))
                    temp.append(int(m + 489))
                x_test.append(temp)

            for j in range(489):
                for shop_info in shop_infos:
                    temp = []
                    temp.append(int(shop_info[0]))
                    temp.append(int(shop_info[1]))
                    temp.append(int(shop_info[2]))
                    temp.append(int(shop_info[3]))
                pay = [0, 0]
                # view = 0
                sql = "SELECT date,sum FROM UserPay WHERE shop_id='" + str(i + 1) + "' AND date='" + str(j) + "'"
                user_pays = exe_query(cur, sql)
                for user_pay in user_pays:
                    pay[0] += int(user_pay[0])
                    pay[1] += int(user_pay[1])
                temp.append(int(pay[0]))
                x_train.append(temp)
                y_train.append(int(pay[1]))
                # sql = "SELECT date,sum FROM UserPay WHERE shop_id='" + str(i + 1) + "' AND date='" + str(j) + "'"
                # user_views = exe_query(cur, sql)
                # for user_view in user_views:
                #     view += int(user_view[0])
                # x_train[5].append(int(view))
                # print(shop_info[0], user_pay[0])
    except Exception as e:
        print(e)
    finally:
        # conn_close(conn, cur)
        return x_train, y_train, x_test


def lasso():
    # Lasso 回归的参数

    alpha = 0.1

    lasso = Lasso(max_iter=10000, alpha=alpha)

    # 基于训练数据，得到的模型的测试结果

    # 这里使用的是坐标轴下降算法(coordinate descent)
    x_train, y_train, x_test = get_data()
    print(len(x_train), len(y_train), len(x_test))
    y_pred_lasso = lasso.fit(x_train, y_train).predict(x_test)
    i = 0
    n = 1
    try:
        f = open("prediction.csv", "w+")
        li = str(n) + ","
        for result in y_pred_lasso:
            ran = random.randint(-20, 20)  # 随机误差
            if i == 13:
                i = 0
                li += str(int(result+ran)) + "\n"
                f.writelines(li)
                n += 1
                li = str(n) + ","
            else:
                i += 1
                li += str(int(result+ran)) + ","
    except Exception as e:
        print(e)
    finally:
        f.close()

        # 这里是R2可决系数(coefficient of determination)

        # 回归平方和(RSS)在总变差(TSS)中所占的比重称为可决系数

        # 可决系数可以作为综合度量回归模型对样本观测值拟合优度的度量指标。

        # 可决系数越大，说明在总变差中由模型作出了解释的部分占的比重越大，模型拟合优度越好。

        # 反之可决系数小，说明模型对样本观测值的拟合程度越差。

        # R2可决系数最好的效果是1。

        # r2_score_lasso = r2_score(y_test, y_pred_lasso)
        #
        # print("测试集上的R2可决系数 : %f" % r2_score_lasso)
        #
        # plt.plot(lasso.coef_, label='Lasso coefficients')
        #
        # plt.plot(coef, '--', label='original coefficients')
        #
        # plt.legend(loc='best')
        #
        # plt.show()
