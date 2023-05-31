import random


def get():
    header1 = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 "
                      "Safari/537.36"}
    header2 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; vivo X6S A Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/6.2 TBS/044207 Mobile Safari/537.36 "
                      "MicroMessenger/6.7.3.1340(0x26070332) NetType/4G Language/zh_CN Process/tools"}
    header3 = {
        "User-Agent": "Mozilla/5.0 (Linux; Android 8.1; EML-AL00 Build/HUAWEIEML-AL00; wv) AppleWebKit/537.36 (KHTML, "
                      "like Gecko) Version/4.0 Chrome/53.0.2785.143 Crosswalk/24.53.595.0 XWEB/358 MMWEBSDK/23 Mobile "
                      "Safari/537.36 MicroMessenger/6.7.2.1340(0x2607023A) NetType/4G Language/zh_CN"}
    header4 = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.0.0; zh-CN; MHA-AL00 Build/HUAWEIMHA-AL00) AppleWebKit/537.36 ("
                      "KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.1.4.994 Mobile Safari/537.36"}
    header5 = {
        "User-Agent": "Mozilla/5.0 (Linux; U; Android 8.1.0; zh-cn; BLA-AL00 Build/HUAWEIBLA-AL00) AppleWebKit/537.36 ("
                      "KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.132 MQQBrowser/8.9 Mobile Safari/537.36"}
    headers_list = [header1, header2, header3, header4, header5]
    i = random.randint(1, 4)
    return headers_list[i]


if '__main__' == __name__:
    print(get())
