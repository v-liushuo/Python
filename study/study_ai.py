from selenium import webdriver
url = 'https://dgydrcfw-edu.51ee.cn/login'
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-automation'])
options.add_experimental_option('useAutomationExtension', False)
# 谷歌浏览器exe位置
options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
 # 是否要启动页面
        # options.add_argument("--headless")  # 启用无头模式
# GPU加速有时候会出bug
options.add_argument("--disable-gpu")  # 禁用GPU加速
options.add_argument("--disable-blink-features=AutomationControlled")
driver = webdriver.Chrome(options=options)
driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument',
                            {'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'})
 # 启动要填写的地址,这就启动浏览器
driver.get(url)
# 这是关闭浏览器
# 等待页面加载，可以根据实际情况调整等待时间
driver.implicitly_wait(10)

# 获取完整页面结构
full_page_content = driver.page_source

# 关闭浏览器
driver.quit()
