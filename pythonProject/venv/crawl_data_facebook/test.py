def get_data_facebook():
    for url in url_all_post:
        browser.get(url)
        sleep(2)

        all_name = []
        url_all_comment = []
        all_comment = []
        name_and_comment = []

        try:
            page_source = BeautifulSoup(browser.page_source, "html.parser")
            name_posting = page_source.find('h3', class_='bs bt bu bv')
            info_loc = name_posting.find_all('span')
        except:
            continue

        # Ten nguoi dang bai
        name_persion_posting = info_loc[0].find('a').get_text()

        # Noi dung
        post = page_source.find('div', class_='by').get_text()

        # Ten nguoi commment

        class_comment = page_source.find_all('div', class_='dp')
        if class_comment == []:
            class_comment = page_source.find_all('div', class_='du')
        else:
            class_comment = page_source.find_all('div', class_='dp')

        del class_comment[0]
        del class_comment[-1]

        # URl comment
        for link in class_comment:
            url_comment = link.find_all('a')
            link_cmt = url_comment[0].get('href')
            url_comment_mbasic = 'https://mbasic.facebook.com' + link_cmt
            url_all_comment.append(url_comment_mbasic)

        # Name Cmt
        for cmt in class_comment:
            name_cmt = cmt.find_all('a')
            name = name_cmt[0].get_text()
            all_name.append(name)

        # Noi dung cmt
        for ndcmt in class_comment:
            cmt = ndcmt.find_all('div')
            all_cmt = cmt[1].get_text()
            all_comment.append(all_cmt)

        name_comment = map(lambda x, y, z: x + str(':') + y + str(':') + z, all_name, url_all_comment, all_comment)
        for i in name_comment:
            name_and_comment.append(i)

        try:
            time_posting = page_source.find('footer', class_='cg')
            info_loc_time = time_posting.find_all('div')
            time = info_loc_time[0].get_text()
            Number = re.findall('\d+', time)
            time_post = Number[0] + str('/') + Number[1]
        except:
            time_post = None

        ID = re.findall('\d+', url)[0] + re.findall('\d+', url)[1]

        my_details = {
            'Social_Network': 'Facebook',
            'Id': ID,
            'Key_word': key_word,
            'Names': name_persion_posting,
            'Link_post': url,
            'post': post,
            'comment': name_and_comment,
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
