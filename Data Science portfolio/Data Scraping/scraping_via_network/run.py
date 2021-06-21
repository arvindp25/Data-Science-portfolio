from scraper.PageCrawler import PageCrawler


if __name__ == "__main__":
    base_path = "C:/Users/offic/Desktop/scraping_freelance/scraped_data"


    sleep_time = 0
    url = "https://ec.europa.eu/info/law/better-regulation/have-your-say/initiatives/12910-Energy-efficiency-Revision-of-the-Energy-Performance-of-Buildings-Directive/feedback_en?p_id=22169990"
    download_pdf = True

    pc = PageCrawler(base_path = base_path, download_pdf= download_pdf, sleep_time=sleep_time)

    pc.eu_scraper(url = url)

    pc.save_data()