# recruitInfo

This is a **Scrapy** project to scrape recruit information from https://jobs.51job.com/ .

This project uses **MySQL/Mongodb** as database.

You can enter `pip install -r requirements.txt`  to make sure you have installed all the requirements.

## Extracted data

This project extracts information, combined with title, company, city, salary, link and createTime. The extracted data looks like this sample:<br />
{<br />
&emsp;"title": "Python开发工程师", <br />
&emsp;"company": "广州外宝电子商务有限公司", <br />
&emsp;"city": "广州-荔湾区", <br />
&emsp;"salary": "0.8-1万/月", <br />
&emsp;"link": "https://jobs.51job.com/guangzhou-lwq/113649350.html?s=01&t=0",<br />
&emsp;"createTime": "12-16"<br />
}

## Spiders

This project contains two spiders and you can list them using the list command:

`$ scrapy list`

> employ

This spider saves data in MySQL, you can alter the connection setting in `pipelins.py`.

You also can choose MongoDB to store the data,  the connection setting is in `settings.py`.

Obviously, you can choose another way of saving data in a json file instead of database.

You can learn more about using **Scrapy** by going through [my blog](https://stardust567.github.io/post/b2a.html).

## Running the spiders

**Make sure that you have altered `ITEM_PIPELINES` in `settings.py`.**

You can run a spider using the scrapy crawl command, such as:

`$ scrapy crawl employ`

