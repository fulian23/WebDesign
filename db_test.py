from app.models import db, Cases

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from db_config import Config

Base = declarative_base()
engine = create_engine(Config.SQLALCHEMY_DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
all=[{
                "title": "作业帮AI教育工具",
                "description": "通过AI技术实现作业智能批改、学情分析与个性化学习方案生成，覆盖超2亿用户。",
                "image": "https://www.xinhuanet.com/tech/20230719/03faf469361f4f46b48594d235543b67/2023071903faf469361f4f46b48594d235543b67_2023071990118542fc8a42a8925360620c3fc0dc.jpg",
                "link": "http://www.xinhuanet.com/tech/20230719/03faf469361f4f46b48594d235543b67/c.html",
                "category": "智慧教育"
            },
            {
                "title": "全球智慧教育大会",
                "description": "聚焦教育数字化转型，发布《在线学习中的个人数据和隐私保护手册》等成果。",
                "image": "https://news.bnu.edu.cn/images/2024-08/5eaa488edb9c4259ae4e3914c0d3dc9a.jpg",
                "link": "https://news.bnu.edu.cn/zx/ttgz/65fddd3612934c84b0ad1d7775efdaaf.htm",
                "category": "智慧教育"
            },

            {
                "title": "摩根大通区块链+供应链融资",
                "description": "利用区块链与零知识证明技术实现跨境供应链金融T+0清算，融资成本降低40%。",
                "image": "https://p26-sign.toutiaoimg.com/tos-cn-i-axegupay5k/7c7d96bf661649928458b1df466d0aaf~tplv-tt-origin-web:gif.jpeg?_iz=58558&from=article.pc_detail&lk3s=953192f4&x-expires=1745659204&x-signature=XGswQYraHYbSBziboo4hr2T%2BEs0%3D",
                "link": "http://m.toutiao.com/group/7489841854473601577/?upstream_biz=doubao",
                "category": "区块链金融"
            },
            {
                "title": "中国交建雄安项目区块链融资",
                "description": "全国首例区块链分包商融资业务，实现供应链金融穿透式管理。",
                "image": "https://q7.itc.cn/images01/20250418/63111735a8be4597b882bcb23702fba6.png",
                "link": "http://wap.sasac.gov.cn/n2588025/n2588124/c9175433/content.html",
                "category": "区块链金融"
            },
            {
                "title": "2021中国互联网大会跨境电商论坛",
                "description": "探讨跨境电商政策创新与人才培养，发布“2*48小时中国通达全球”物流体系。",
                "image": "https://www.isc.org.cn/resource/editor/attached/image/20210718/20210718145220_75826.jpg",
                "link": "https://www.isc.org.cn/article/40274.html",
                "category": "跨境电商"
            },
            {
                "title": "拼多多农业数字化",
                "description": "通过“农地云拼”模式推动农产品上行，2024年农产品交易额突破5000亿元。",
                "image": "https://www.xinhuanet.com/tech/20230306/9874c09670ef4f2b8b21bb60c5eac98a/202303069874c09670ef4f2b8b21bb60c5eac98a_202303060c0f919e2f304f1fba82497bd3a9edb0.png",
                "link": "https://www.xinhuanet.com/tech/20230306/9874c09670ef4f2b8b21bb60c5eac98a/c.html",
                "category": "跨境电商"
            },
            {
                "title": "雅安大数据产业园",
                "description": "国内首个“碳中和”绿色数据中心，支撑《流浪地球2》等影视渲染。",
                "image": "https://i2.chinanews.com.cn/simg/ypt/2023/231012/b535ea51-3325-43f3-b1d9-9579d8f3b873_zsite.jpg",
                "link": "https://www.chinanews.com.cn/cj/2023/10-12/10092887.shtml",
                "category": "绿色数据中心"
            },
            {
                "title": "全国智能制造示范工厂",
                "description": "培育421家国家级智能制造示范工厂，90%以上应用AI与数字孪生技术。",
                "image": "https://img.cinn.cn/a/10001/202404/873366f560cbe79340c2cd657b7f123e.jpeg",
                "link": "https://www.gov.cn/yaowen/liebiao/202411/content_6988583.htm",
                "category": "人工智能"
            },

            {
                "title": "华为RuralStar案例",
                "description": "为偏远地区提供低成本、易部署的无线通信解决方案，消除数字鸿沟。",
                "image": "https://www-file.huawei.com/-/media/corporate/images/news4/2021/q3/210926.jpg?la=zh",
                "link": "https://www.huawei.com/cn/news/2021/9/ruralstar-connects-together-cyberspace-award-2021",
                "category": "数字基础设施"
            },
            {
                "title": "通州会员企业获中国互联网创新大赛一等奖",
                "description": "以数据资产为核心，实现数据流转全流程监测与安全防护，提升复杂业务系统的数据安全管理质效。",
                "image": "https://www.isc.org.cn//profile//2024/07/12/61ebb5c1-cab7-40db-b1da-cb1747ba38c5.jpg",
                "link": "https://www.isc.org.cn/article/21402593669148672.html",
                "category": "数据安全"
            },
            {
                "title": "高校在首届“金灵光杯”中国互联网创新大赛中获奖",
                "description": "聚焦数字教育赛道，推动数据驱动的大规模因材施教，提升教学模式创新与新质生产力发展。",
                "image": "https://www.sdivc.edu.cn/__local/F/D1/93/2AD5DFEE33B94BBBC071612959C_5FE6A6A8_1B0B7.png",
                "link": "https://www.sdivc.edu.cn/info/1041/7362.htm",
                "category": "数字教育"
            },
            {
                "title": "中国移动“AI+行动计划”",
                "description": "通过AI技术赋能工业互联网，推动制造业数字化转型，提升生产效率与安全管理。",
                "image": "https://n.sinaimg.cn/sinakd20240627s/66/w1000h666/20240627/5bb2-ffc27649029308ca8a857a8abf16c598.png",
                "link": "https://finance.sina.com.cn/tech/roll/2024-06-27/doc-incaemyi9295162.shtml",
                "category": "人工智能"
            },
            {
                "title": "拼多多“高质量发展与新质生产力”",
                "description": "分享电商平台在农业数字化、供应链优化等领域的实践经验。",
                "image": "https://www.isc.org.cn//profile//2024/07/10/846b7919-e585-4408-a8a2-9242e364835a.jpg",
                "link": "https://www.isc.org.cn/article/21380049838403584.html",
                "category": "数字贸易"
            },
            {
                "title": "科技引领，联通全球：大数据与人工智能在反诈治理中的新实践",
                "description": "利用AI外呼系统提升反诈劝阻效率，构建“事前-事中-事后”全流程治理体系。",
                "image": "https://imgpolitics.gmw.cn/attachement/jpg/site2/20241119/00d86156b03428a6b84817.jpg",
                "link": "https://politics.gmw.cn/2024-11/19/content_37686679.htm",
                "category": "数字治理"
            },

            {
                "title": "2Africa国际海缆项目",
                "description": "构筑环非信息高速公路，推动非洲数字经济发展。",
                "image": "https://n.sinaimg.cn/spider2020514/632/w1428h804/20200514/ba20-itriatr8618030.jpg",
                "link": "https://tech.sina.com.cn/roll/2020-05-14/doc-iirczymk1555721.shtml",
                "category": "国际合作"
            },
            {
                "title": "快手“可灵AI”平台",
                "description": "基于自研大模型生成高质量视频与图像，赋能内容创作。",
                "image": "https://inews.gtimg.com/news_bt/OioEoNydJT-2vijXyviuVSa1ZnaJ0anPBm8QpQvRESXKcAA/641",
                "link": "https://news.qq.com/rain/a/20250415A080PT00",
                "category": "内容创作"
            },
            {
                "title": "数字经济与农业融合",
                "description": "农业数字化解决方案数量显著提升，覆盖种植、养殖、物流等全链条。",
                "image": "https://www.isc.org.cn//profile//2023/07/21/94a72a4e-468d-4e2c-ab6c-15fddd6ffecd.jpg",
                "link": "https://www.isc.org.cn/mobile/article/17359313814810624.html",
                "category": "数字农业"
            },
            {
                "title": "工业互联网平台",
                "description": "工业数字化解决方案初具规模，推动制造业提质增效。",
                "image": "http://www.qstheory.cn/dukan/qs/2024-12/01/1130224011_17328444244271n.jpg",
                "link": "http://www.qstheory.cn/dukan/qs/2024-12/01/c_1130224011.htm",
                "category": "工业互联网"
            },
            {
                "title": "大同中联绿色大数据基地",
                "description": "采用国际先进节能技术，入选“2024年度数据中心实施样板项目”。",
                "image": "https://www.zlhuiyun.com/uploads/allimg/20240412/f5f016256a5841788eb3f98323fdaae9.png",
                "link": "http://www.dt.gov.cn/dtszf/zsxm/202504/78e8b22d2c6d4e399eab2d445c633a26.shtml",
                "category": "绿色数据中心"
            },
            {
                "title": "数智融合潮涌 共绘发展新篇——2025年世界互联网大会亚太峰会观察",
                "description": "分析AI、算力网络在亚太地区的应用趋势。",
                "image": "https://www.xinhuanet.com/20250416/69f1912ba47e429a965167f26e9b9c31/JzbO1J2fJGJB00tY.jpg",
                "link": "http://www.xinhuanet.com/20250416/69f1912ba47e429a965167f26e9b9c31/c.html",
                "category": "数智融合"
            },

            {
                "title": "乘“数”而上，共享创新发展成果",
                "description": "解读数字技术在医疗、教育、养老等民生领域的应用。",
                "image": "https://epaper.gmw.cn/gmrb/images/2024-11/22/07/res0715_attpic_brief.jpg",
                "link": "https://epaper.gmw.cn/gmrb/html/2024-11/22/nw.D110000gmrb_20241122_1-07.htm",
                "category": "数字民生"
            },
            {
                "title": "中国互联网协会年度报告",
                "description": "汇总数字化转型优秀案例，覆盖数字经济、数字政务、数字社会等领域。",
                "image": "https://www.isc.org.cn//profile//2024/07/01/8155f2ba-bd38-4fbc-85bc-e82508e4f0e8.jpg",
                "link": "https://www.isc.org.cn/article/21276709814923264.html",
                "category": "行业报告"
            },
            {
                "title": "数据安全一体化监测预警系统",
                "description": "以数据资产为核心，实现数据流转全流程监测与安全防护，提升复杂业务系统的数据安全管理质效。",
                "image": "https://www.mchz.com.cn/public/upload/spectacle/2023/10-25/2cb5899086e24817514c0ae88eb0e9e9.png",
                "link": "https://www.zhongfu.net/products/info/161.html",
                "category": "数据安全"
            },
            {
                "title": "中国平安数字金融创新",
                "description": "分享AI风控与数字金融创新实践，覆盖超1亿企业。",
                "image": "https://xqimg.imedao.com/195cd1c3a7af19203fec86cb.jpg!800.jpg",
                "link": "http://m.toutiao.com/group/7493720774101139983/?upstream_biz=doubao",
                "category": "数字金融"
            }]
for i in all:

    session.add(Cases(title=i['title'], description=i['description'], image=i['image'], link=i['link'], category=i['category']))
    session.commit()