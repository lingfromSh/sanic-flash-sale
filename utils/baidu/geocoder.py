import hashlib
from dataclasses import dataclass
from urllib.parse import quote, quote_plus

from utils.app import app
from utils.baidu.api import Api
from utils.baidu.auth import Auth


@dataclass
class GeoLocation:
    """
    经纬度值
    """
    lat: int    # 纬度值	
    lng: int    # 经度值	


@dataclass
class GeoResult:
    """
    地理位置结果
    """
    status: int                     # 返回结果状态值， 成功返回0，其他值请查看返回码状态表。	
    location: GeoLocation           # 经纬度
    precise: int                    # 位置的附加信息，是否精确查找。1为精确查找，即准确打点；0为不精确，即模糊打点。	
    confidence: int                 # 描述打点绝对精度（即坐标点的误差范围）。
    comprehension: int              # 描述地址理解程度。分值范围0-100，分值越大，服务对地址理解程度越高（建议以该字段作为解析结果判断标准）；
    level: int                      # 能精确理解的地址类型，包含：UNKNOWN、国家、省、城市、区县、乡镇、村庄、道路、地产小区、商务大厦、政府机构、交叉路口、商圈、生活服务、休闲娱乐、餐饮、宾馆、购物、金融、教育、医疗 、工业园区 、旅游景点 、汽车服务、火车站、长途汽车站、桥 、停车场/停车区、港口/码头、收费区/收费站、飞机场 、机场 、收费处/收费站 、加油站、绿地、门址

    def __post_init__(self):
        # TODO: 校验status进行相应操作
        raise NotImplementedError

    def is_valid(self):
        if self.status == 0:
            return True
        elif self.status == 1:
            # TODO: 日志输出 百度地图api服务内部错误
            return False
        elif self.status == 2:
            # TODO: 日志输出 百度地图api服务请求参数非法
            return False
        elif self.status == 3:
            # TODO: 日志输出 权限校验失败, 并且邮件通知
            return False
        elif self.status == 4:
            # TODO: 日志输出 配额校验失败, 并且邮件通知
            return False
        elif self.status == 5:
            # TODO: 日志输出 ak不存在或非法 
            return False
        elif self.status == 101:
            # TODO: 日志输出 服务禁用
            return False
        elif self.status == 102:
            # TODO: 日志输出 不通过白名单
            return False
        elif 200 <= self.status < 300:
            # TODO: 日志输出 无权限
            return False
        elif self.status >= 300:
            # TODO: 日志输出 配额错误
            return False
        else:
            # TODO: 日志输出 未知错误, 并且邮件通知
            return False


class GeoCoder(Api):

    BASE_API_URL = "https://api.map.baidu.com"
    API = "/geocoding/v3/"
    HTTP_200_OK = 200

    def __init__(self, auth: Auth) -> None:
        super().__init__(auth)

    def sn(self, address, output='json') -> str:
        query = "{api}?address={address}&output={output}&ak={apikey}".format(api=self.API, address=address, output=output, apikey=self.auth.apikey)
        encoded_query = quote(query, safe="/:=&?#+!$,;'@()*[]")
        raw_string =  encoded_query + self.auth.secretkey
        return hashlib.md5(quote_plus(raw_string)).hexdigest()

    def geocode(self, address, city=None):
        # Making data
        data = {}
        data.update(address=address)
        data.update(ak=self.auth.apikey)        
        data.update(sn=self.sn(address))
        if city is not None:
            data.update(city=city)

        # Handling response from baidu map server
        resp = self.request(url=self.BASE_API_URL + self.API, data=data)
        return GeoResult(**resp.json())


geocoder = GeoCoder(Auth(app.config.BAIDU_MAP_API_KEY, app.config.BAIDU_MAP_SECRET_KEY))