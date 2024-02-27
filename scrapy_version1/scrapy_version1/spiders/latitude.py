import scrapy
from scrapy_version1.items import GpuInfoItem


class LatitudeSpider(scrapy.Spider):
    name = 'latitude'
    allowed_domains = ['latitude.sh']
    start_urls = ['http://latitude.sh/accelerate/pricing']

    def parse(self, response):
        parent_node = response.xpath('//*[@id="__next"]/div/div[2]/div/div/div/div[2]/div')
        gpu_elements = parent_node.xpath('./div[contains(@class, "h-full")]')

        gpu_infos = []
        print(len(gpu_elements))

        for gpu_element in gpu_elements:
            name = gpu_element.xpath('.//h1/text()').get()
            gpu_info_elements = gpu_element.css('.c-gYfvVc ul li')
            gpu = gpu_info_elements[0].xpath('string()').get()
            processor = gpu_info_elements[1].xpath('string()').get().strip()
            ram = gpu_info_elements[2].xpath('string()').get()
            nvme = gpu_info_elements[3].xpath('string()').get()
            network = gpu_info_elements[4].xpath('string()').get()

            text_contents = gpu_element.css('.text-accent-seven::text').getall()
            hour_price = text_contents[0]
            month_price = text_contents[1]

            gii = GpuInfoItem()
            gii['name'] = name
            gii['gpu'] = gpu
            gii['scale'] = gpu[0] if gpu else None
            gii['gpu_ram'] = None
            gii['vcpus'] = None
            gii['cpu_info'] = processor
            gii['ram'] = ram[:-4] if ram else None
            gii['storage'] = nvme
            gii['bandwidth'] = network
            gii['type'] = None
            gii['regions'] = None
            gii['hour_price'] = hour_price[:-3] if hour_price else None
            gii['month_price'] = month_price[:-3] if month_price else None
            gii['year_price'] = None
            gii['account'] = None
            print(gii)


            gpu_infos.append(gii)

        return gpu_infos