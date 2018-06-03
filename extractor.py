import requests as req
from scrapy.selector import Selector

base_url = 'https://www.bayt.com{}'


def clean(str_):
    return str_.strip()


def extract(page_number):
    url = 'https://www.bayt.com/en/uae/jobs/'
    post_fix = '?page={}'
    if page_number > 1:
        url = url + post_fix.format(page_number)
        print("url is :", url)
    """ below response text """
    text = req.get(url).text
    sel = Selector(text=text)

    job_header_list = sel.xpath('//div[@class="card"]//div//div//h2/a/text()').extract()
    apply_url_list = sel.xpath('//div[@class="card"]//div//div//h2/a/@href').extract()
    company_name_and_location_list = sel.xpath('//div[@class="card"] /div/div/ul/li/b/text()').extract()
    company_name_list = list()
    location_list = list()
    for index, item in enumerate(company_name_and_location_list):

        if index % 2 == 0:
            company_name_list.append(clean(company_name_and_location_list[index]))
        else:
            location_list.append(clean(company_name_and_location_list[index]))

    post_date_list = sel.xpath('//div[@class="card"]//div//div/ul/li[@class="t-mute"]/text()').extract()
    job_desc_list = sel.xpath('//div[@class="card"]//div//div/ul/li[@class="t-small m10y d"]/text()').extract()
    data_list = list()
    for index, item in enumerate(job_header_list):
        post_date = clean(post_date_list[index])
        job_header = clean(job_header_list[index])
        apply_url = base_url.format(apply_url_list[index])
        job_desc = clean(job_desc_list[index])
        company_name = company_name_list[index]
        location = location_list[index]
        data = {
            "provider": "www.bayt.com",
            "location": location,
            "post_date": post_date,
            "apply_url": apply_url,
            "company_name": company_name,
            "job_title": job_header,
            "job_desc": job_desc
        }
        data_list.append(data)
    return data_list


