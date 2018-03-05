class User:
    """
    用户行为
    """
    shop_id = 0  # 商家id，与shop_info对应
    date = 0  # 距离2015年07月01号的天数
    sum = 0  # 用户当天某种行为的次数

    def __init__(self):
        """
        构造函数
        :return:
        """
        self.shop_id = 0
        self.date = 0
        self.sum = 0

    def __init__(self, shop_id, date, sum):
        """
        构造函数重置
        :param shop_id:
        :param date:
        :param sum:
        :return:
        """
        self.shop_id = shop_id
        self.date = date
        self.sum = sum
