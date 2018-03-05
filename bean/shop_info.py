class ShopInfo:
    """
    商家信息
    """
    shop_id = 0  # 商家id
    city_name = ''  # 市名
    location_id = 0  # 所在位置编号，位置接近的商家具有相同的编号
    per_pay = 0  # 人均消费（数值越大消费越高）
    score = 0  # 评分（数值越大评分越高）
    comment_cnt = 0  # 评论数（数值越大评论数越多）
    shop_level = 0  # 门店等级（数值越大门店等级越高）
    cate_1_name = ''  # 一级品类名称
    cate_2_name = ''  # 二级分类名称
    cate_3_name = ''  # 三级分类名称

    def __init__(self):
        """
        构造函数
        :return:
        """
        self.shop_id = 0
        self.city_name = ''
        self.location_id = 0
        self.per_pay = 0
        self.score = 0
        self.comment_cnt = 0
        self.shop_level = 0
        self.cate_1_name = ''
        self.cate_2_name = ''
        self.cate_3_name = ''

    def __init__(self, shop_id, city_name, location_id, per_pay, score, comment_cnt, shop_level, cate_1_name,
                 cate_2_name, cate_3_name):
        """
        构造函数重置
        :param shop_id:
        :param city_name:
        :param location_id:
        :param per_pay:
        :param score:
        :param comment_cnt:
        :param shop_level:
        :param cate_1_name:
        :param cate_2_name:
        :param cate_3_name:
        :return:
        """
        self.shop_id = shop_id
        self.city_name = city_name
        self.location_id = location_id
        self.per_pay = per_pay
        self.score = score
        self.comment_cnt = comment_cnt
        self.shop_level = shop_level
        self.cate_1_name = cate_1_name
        self.cate_2_name = cate_2_name
        self.cate_3_name = cate_3_name

