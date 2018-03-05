from dataBase.sql_helper import conn_db, exe_table, exe_update, conn_close


def read_by_line(address):
    """
    带缓存的文件读取一行数据
    :param address:
    :return:
    """
    file = open(address)
    file_content = []
    while 1:
        lines = file.readlines(100000)
        if not lines:
            break
        for line in lines:
            file_content.append(line)
    return file_content


def shop_info_database(file_content):
    """
    将文本文件处理并存入数据库中
    :param file_content:
    :return:
    """
    try:
        conn = conn_db()
        cur = conn.cursor()
        sql = "DROP TABLE if EXISTS ShopInfo"
        exe_table(cur, sql)
        sql = "CREATE TABLE ShopInfo(shop_id INT NOT NULL AUTO_INCREMENT,city_name VARCHAR (255),location_id INT ," \
              "per_pay INT ,score INT ,comment_cnt INT ,shop_level INT ,cate_1_name VARCHAR (255) ,cate_2_name" \
              " VARCHAR (255) ,cate_3_name VARCHAR (255) ,PRIMARY KEY (shop_id)) ENGINE = InnoDB DEFAULT CHARSET = UTF8"
        exe_table(cur, sql)
        for i in range(0, len(file_content)):
            contents = file_content[i].split(",")
            if len(contents) == 10:
                sql = "INSERT INTO ShopInfo VALUES ('" + contents[0] + "','" + contents[1] + "','" + contents[2] + "'" \
                                                                                                                   ",'" + \
                      contents[3] + "','" + contents[4] + "','" + contents[5] + "','" + contents[6] + "'," \
                                                                                                      "'" + contents[
                          7] + "','" + contents[8] + "','" + contents[9] + "')"
            elif len(contents) == 9:
                sql = "INSERT INTO ShopInfo VALUES ('" + contents[0] + "','" + contents[1] + "','" + contents[2] + "'" \
                                                                                                                   ",'" + \
                      contents[3] + "','" + contents[4] + "','" + contents[5] + "','" + contents[6] + "'," \
                                                                                                      "'" + contents[
                          7] + "','" + contents[8] + "',NULL)"
            exe_update(conn, cur, sql)

    except Exception as e:
        print(e)
        print(contents[0])
    finally:
        conn_close(conn, cur)


def get_user_pay(address):
    """
    获得用户的购物信息并存入数据库
    :param address:
    :return:
    """
    try:
        conn = conn_db()
        cur = conn.cursor()
        sql = "DROP TABLE if EXISTS UserPay"
        exe_table(cur, sql)
        sql = "CREATE TABLE UserPay(id INT NOT NULL AUTO_INCREMENT,shop_id INT NOT NULL ,date INT,sum INT ," \
              "PRIMARY KEY (id) ,FOREIGN KEY (shop_id) REFERENCES ShopInfo(shop_id)) " \
              "ENGINE = InnoDB DEFAULT CHARSET = UTF8"
        exe_table(cur, sql)

        file = open(address)
        shop = ''
        num = []
        for i in range(489):
            num.append(0)
        while 1:
            lines = file.readlines(10000)
            if not lines:
                user_pay_database(conn, cur, num, shop)
                break
            for line in lines:
                file_content = line.split(",")
                if shop == '':
                    shop = file_content[1]
                    dates = file_content[2].split(" ")
                    num[cal_day(dates[0])] += 1
                elif shop == file_content[1]:
                    dates = file_content[2].split(" ")
                    num[cal_day(dates[0])] += 1
                elif shop != file_content[1]:
                    user_pay_database(conn, cur, num, shop)
                    shop = file_content[1]
                    for i in range(489):
                        num[i] = 0
                    dates = file_content[2].split(" ")
                    num[cal_day(dates[0])] += 1
    except Exception as e:
        print(e)
    finally:
        conn_close(conn, cur)


def cal_day(date):
    """
    计算与2015年7月01日相差的天数
    :param date:
    :return:
    """
    day1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    day2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    start = 0
    for i in range(6):
        start += day1[i]
    deal_date = date.split("-")
    num = 0
    if deal_date[0] == "2015":
        for i in range(int(deal_date[1]) - 1):
            num += day1[i]
        num += int(deal_date[2]) - 1
        return num - start
    elif deal_date[0] == "2016":
        for i in range(int(deal_date[1]) - 1):
            num += day2[i]
        num += int(deal_date[2]) - 1
        return 365 - start + num


def user_pay_database(conn, cur, num, shop):
    """
    将用户购买信息存入数据库
    :param conn:
    :param cur:
    :param num:
    :param shop:
    :return:
    """
    try:
        for i in range(489):
            sql = "INSERT INTO UserPay(shop_id ,date ,sum) VALUES ('" + shop + "','" + str(i) + "','" + str(
                    num[i]) + "')"
            exe_update(conn, cur, sql)
    except Exception as e:
        print(e)
        print(shop, i, num[i])


def get_user_view(address):
    """
    获得用户的浏览信息并存入数据库
    :param address:
    :return:
    """
    try:
        conn = conn_db()
        cur = conn.cursor()
        sql = "DROP TABLE if EXISTS UserView"
        exe_table(cur, sql)
        sql = "CREATE TABLE UserView(id INT NOT NULL AUTO_INCREMENT,shop_id INT NOT NULL ,date INT,sum INT ," \
              "PRIMARY KEY (id) ,FOREIGN KEY (shop_id) REFERENCES ShopInfo(shop_id)) " \
              "ENGINE = InnoDB DEFAULT CHARSET = UTF8"
        exe_table(cur, sql)

        file = open(address)
        shop = ''
        num = []
        for i in range(489):
            num.append(0)
        while 1:
            lines = file.readlines(10000)
            if not lines:
                user_view_database(conn, cur, num, shop)
                break
            for line in lines:
                file_content = line.split(",")
                if shop == '':
                    shop = file_content[1]
                    dates = file_content[2].split(" ")
                    num[cal_day(dates[0])] += 1
                elif shop == file_content[1]:
                    dates = file_content[2].split(" ")
                    num[cal_day(dates[0])] += 1
                elif shop != file_content[1]:
                    user_view_database(conn, cur, num, shop)
                    shop = file_content[1]
                    for i in range(489):
                        num[i] = 0
                    dates = file_content[2].split(" ")
                    num[cal_day(dates[0])] += 1
    except Exception as e:
        print(e)
    finally:
        conn_close(conn, cur)


def user_view_database(conn, cur, num, shop):
    """
    将用户浏览信息存入数据库
    :param conn:
    :param cur:
    :param num:
    :param shop:
    :return:
    """
    try:
        for i in range(489):
            sql = "INSERT INTO UserView(shop_id ,date ,sum) VALUES ('" + shop + "','" + str(i) + "','" + str(
                    num[i]) + "')"
            exe_update(conn, cur, sql)
    except Exception as e:
        print(e)
        print(shop, i, num[i])
