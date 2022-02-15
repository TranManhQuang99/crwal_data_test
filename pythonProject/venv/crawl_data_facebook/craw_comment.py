from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys

# 1. Khai báo browser
browser = webdriver.Chrome(executable_path="/Users/armi1/PycharmProjects/pythonProject/venv/crawl_data_facebook\chromedriver.exe")
# C:\Users\armi1\PycharmProjects\pythonProject\venv\crawl_data_facebook\chromedriver.exe
# 2. Mở URL của post
# https://www.facebook.com/groups/sanshopeesale/posts/954618662071091
# "https://www.facebook.com/groups/Grouptinhte/posts/3010538769070048/
browser.get("https://www.facebook.com/groups/sanshopeesale/posts/954618662071091")

sleep(3)
# 3. Lấy link hiện comment
showmore_link = browser.find_element_by_xpath("/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]")
showmore_link.click()
# showmore_link._execute("window.scrollTo(0,1000)")
sleep(2)
showmore_link.click()
# showmore_link._execute("window.scrollTo(0,1000)")
sleep(2)
showmore_link.click()
# showmore_link._execute("window.scrollTo(0,1000)")
sleep(2)


# tim tat ca cac comment ghi ra file
#comment_list = browser.find_elements_by_xpath("//div[@aria-label]")
comment_list = browser.find_elements_by_xpath("//div[@class='ni8dbmo4 stjgntxs l9j0dhe7']")

sleep(2)
for comment in comment_list:
    #hien thi ten nguoi va noi dung :
    data = {
        "Ho va ten" : comment.find_element_by_class_name("pq6dq46d").text,
        "Binh luan" : comment.find_element_by_css_selector('.ecm0bbzt.e5nlhep0.a8c37x1j').text
    }
    print(data)
#     with open("fb.csv", "a", encoding='utf-8') as f:
#         f.write(f"{data['Ho va ten']};{data['Binh luan']}\n")
#     # x = comment.find_element_by_

# for comment in comment_list:
# noi_dung = browser.find_elements_by_xpath("//div[@class='qzhwtbm6 knvmm38d']")
    # print(noi_dung)

# for i in noi_dung:
#     tieu_de = i.find_element_by_class_name(".qzhwtbm6.knvmm38d").text
#     print(tieu_de)


#lay links fb
# for comment in comment_list:
# links = browser.find_elements_by_xpath ("// a [@ role = 'link']")
# sleep(2)
# # print(links)
# for i in links:
#     fb = i.get_attribute('href')
#     print(fb)

sleep(5)
browser.close()
#.oajrlxb2.g5ia77u1.qu0x051f.esr5mh6w.e9989ue4.r7d6kgcz.rq0escxv.nhd2j8a9.nc684nl6.p7hjln8o.kvgmc6g5.cxmmr5t8.oygrvhab.hcukyx3x.jb3vyjys.rz4wbd8a.qt6c0cv9.a8nywdso.i1ao9s8h.esuyzwwr.f1sip0of.lzcic4wl.gmql0nx0.gpro0wi8'