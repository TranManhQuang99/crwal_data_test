def get_data_facebook():
    for url in url_post:
        browser.get(url)
        sleep(2)

        # show full comment
        try:
            browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[4]/div[1]/div[2]').click()
        except:
            browser.find_element(By.XPATH,
                                 '/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[4]/div/div/div/div/div/div/div[1]/div/div/div/div/div/div/div/div/div/div/div[2]/div/div[4]/div/div/div[2]/div[2]/div[1]/div[2]/span').click()
        sleep(1)
        page_source = BeautifulSoup(browser.page_source, "html.parser")

        # ten nguoi post bai
        name_post = page_source.find('span',
                                     class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d3f4x2em fe6kdd0r mau55g9w c8b282yb iv3no6db jq4qci2q a3bd9o3v b1v8xokw m9osqain hzawbc8m').get_text()
        # Noi dung bai post
        post = page_source.find('div', class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql').get_text()
        href = page_source.find('a',
                                class_='oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso l9j0dhe7 i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl n00je7tq arfg74bv qs9ysxi8 k77z8yql abiwlrkh p8dawk7l oo9gr5id').get(
            'href')
        # ID nguoi viet bai
        ID = re.findall('\d+', href)[1]
        # Link fb nguoi post bai
        link_persion_post = 'https://www.facebook.com/' + ID

        # Lay ten nguoi comment
        all_comment = page_source.find('div', class_='cwj9ozl2 tvmbv18p')
        extract_cmt = all_comment.find_all('li')
        name_comment = []
        comment = []
        Link_persion_comment = []
        all_commment = []
        for li in extract_cmt:
            name_span_cmt = li.find('span',
                                    class_='d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh a8c37x1j keod5gw0 nxhoafnm aigsh9s9 d9wwppkn fe6kdd0r mau55g9w c8b282yb mdeji52x e9vueds3 j5wam9gi lrazzd5p oo9gr5id')
            try:
                name_cmt = name_span_cmt.get_text()
                name_comment.append(name_cmt)
            except:
                continue
            try:
                span_comment = li.find('div', class_='kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x c1et5uql').get_text()
                comment.append(span_comment)
            except:
                continue
            try:
                url_persion_comment = li.find('a',
                                              class_='oajrlxb2 g5ia77u1 qu0x051f esr5mh6w e9989ue4 r7d6kgcz rq0escxv nhd2j8a9 nc684nl6 p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso i1ao9s8h esuyzwwr f1sip0of lzcic4wl gmql0nx0 gpro0wi8').get(
                    'href')
                ID_persion_comment = 'https://www.facebook.com/' + re.findall('\d+', url_persion_comment)[1]
                Link_persion_comment.append(ID_persion_comment)
            except:
                continue

        map_all_comment = map(lambda x, y, z: x + str(':') + y + str(':') + z, name_comment, Link_persion_comment,
                              comment)
        for i in map_all_comment:
            all_commment.append(i)

        # ID_post
        ID_POST = re.findall('\d+', url)[0] + re.findall('\d+', url)[1]

        my_details = {
            'Social_Network': 'Facebook',
            'Id': ID_POST,
            'Key_word': key_word,
            'Names': name_post,
            'Link_post': url,
            'post': post,
            'comment': all_commment,
            'device': None,
            'location': None,
            'Job_title': None,
            'time': time_post
        }
        print(my_details)

        cluster = MongoClient(
            "mongodb+srv://minh15599:123456asdf@cluster0.wkj8v.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
        db = cluster['123a']
        collection = db['myapp_employee']
        collection.insert_one(my_details)


get_data_facebook()
