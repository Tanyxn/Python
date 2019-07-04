# 请求json接口整体数据 抽取想要的 保存数据
import requests
import json
response=requests.get("https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=20")
py_data=json.loads(response.text)
for i in py_data:
    items={'电影名称':i['title'],'上映地区':i['regions'],
           '评分':i['score'],'上映时间':i['release_date']}
    # print(items)
    content=json.dumps(items,ensure_ascii=False)+".\n"
    with open("douban.json" , "a" , encoding="utf-8") as f:
        f.write(content)
        print(content)












# import requests
# import json
# response=requests.get("http://image.baidu.com/pv/pv.gif?dsp=pc&tn=result&hs=2&type=prerequire&t=1556545641129")
# py_data=json.loads(response.text)
# for i in py_data:
#     print(i)
#     # print(items)
#     # content=json.dumps(items,ensure_ascii=False)+".\n"
#     # with open("douban.json" , "a" , encoding="utf-8") as f:
#     #     f.write(content)
#     #     print(content)


