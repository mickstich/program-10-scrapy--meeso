import scrapy
from ..items import MeeshoappItem


class mens_all(scrapy.Spider):
    name = "mens"
    page_no = 2
    start_urls = [
        "https://meesho.com/accessories-men/pl/3z79k?page=1"
    ]

    def parse(self, response):
        items = MeeshoappItem()

        all_code = response.xpath("//div[contains(@class, ' ProductList__GridCol-sc-8lnc8o-0')]")



        for i in all_code:
      #      name = i.xpath("//p[contains(@class,'NewProductCard__ProductTitle_Desktop-sc-j0e7tu-4')]/text()").extract()
      #     price = i.xpath("//h5[contains(@class,'Text__StyledText-sc-oo0kvp-0 hiHdyy')]/text()").extract()
            name  = i.css(".cQhePS::text").extract()
            price = i.css(".hiHdyy::text").extract()
            image = i.css(".ieioYG::attr(src)").extract()














            items['name']  = name
            items['price'] = price
            items['image'] = image




            yield items

        next_page = 'https://meesho.com/accessories-men/pl/3z79k?page=' + str(mens_all.page_no)
        print("mickstich")
        if mens_all.page_no < 50:
            mens_all.page_no +=1
            print(mens_all.page_no)
            yield response.follow(next_page, callback=self.parse)



        """
        next_page=response.css("div.sc-bdvvtL.Desktop__ContainerStyled-sc-1jz570n-0.byHcNc.kfIzHc:nth-child(3) div.sc-gsDKAQ.Grid__Row-sc-4ki5nk-0.iQiJjX.gfsqfL:nth-child(1) div.sc-dkPtRN.hteYJb div.sc-bdvvtL.ProductListingContent__ContainerStyled-sc-e96brm-1.byHcNc.leRIiF div.sc-gsDKAQ.Grid__Row-sc-4ki5nk-0.iQiJjX.gfsqfL:nth-child(4) div.sc-dkPtRN.hteYJb div.Pagination__PaginationContainer-sc-1dr2fjf-0.kjIqNz.Pagination__PaginationStyled-sc-27aohu-0.bwyUaC button.BaseButton-sc-1e0kf5s-0.hqllqe.Pagination__NavigationButtons-sc-1dr2fjf-2.ezIlof.Pagination__NavigationButtons-sc-1dr2fjf-2.ezIlof:nth-child(10) div.BaseButton__ButtonWrapper-sc-1e0kf5s-1.gzqhEM > span.Text__StyledText-sc-oo0kvp-0.gqvjrY.Button__StyledTextLink-sc-1r14yig-0.ctuAGF.Button__StyledTextLink-sc-1r14yig-0.ctuAGF").get()
        print(next_page)
        print("mickstich")

        if next_page is not None:
            yield response.follow(next_page,callback=self.parse)
        """

