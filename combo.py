from bs4 import BeautifulSoup
import requests
from re import sub
import time
from decimal import Decimal
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def hotelChoice():
    i = 0
    while i == 0:
        choice = str(input('Enter the name of the hotel :'))
        if choice == 'Marriott': #not working as of 4/5/2021
            soupurl = 'https://www.booking.com/searchresults.en-gb.html?aid=355028&sid=d2a902f346650dc0b748848763652bdc&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D355028%3Bsid%3Dd2a902f346650dc0b748848763652bdc%3Btmpl%3Dsearchresults%3Bcheckin_month%3D5%3Bcheckin_monthday%3D8%3Bcheckin_year%3D2021%3Bcheckout_month%3D5%3Bcheckout_monthday%3D13%3Bcheckout_year%3D2021%3Bcity%3D-2601889%3Bclass_interval%3D1%3Bdest_id%3D-2601889%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D1%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Broom1%3DA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3D6eda76c5afe000a5%3Bss%3DLondon%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DLondon%3Bssne_untouched%3DLondon%3Btop_ufis%3D1%3Bsig%3Dv1yWyN9mHA%3B&ss=London+Marriott+Hotel+County+Hall%2C+London%2C+Greater+London%2C+United+Kingdom&is_ski_area=&ssne=London&ssne_untouched=London&city=-2601889&checkin_year=2021&checkin_month=5&checkin_monthday=8&checkout_year=2021&checkout_month=5&checkout_monthday=13&group_adults=1&group_children=0&no_rooms=1&from_sf=1&ss_raw=Marriott+London&ac_position=1&ac_langcode=en&ac_click_type=b&dest_id=36867&dest_type=hotel&place_id_lat=51.5010959924622&place_id_lon=-0.119165182113647&search_pageview_id=6eda76c5afe000a5&search_selected=true&search_pageview_id=6eda76c5afe000a5&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0'
            seleniumurl = ''
        if choice == 'Tower Hotel':
            soupurl = 'https://www.booking.com/searchresults.en-gb.html?aid=355028&sid=3694460fd4ecb2d451b9b5c52e537432&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D355028%3Bsid%3D3694460fd4ecb2d451b9b5c52e537432%3Btmpl%3Dsearchresults%3Bcheckin_month%3D6%3Bcheckin_monthday%3D3%3Bcheckin_year%3D2021%3Bcheckout_month%3D6%3Bcheckout_monthday%3D5%3Bcheckout_year%3D2021%3Bcity%3D-2601889%3Bclass_interval%3D1%3Bdest_id%3D-2601889%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D1%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Broom1%3DA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3Dbbff65b09ddd0152%3Bss%3DLondon%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DLondon%3Bssne_untouched%3DLondon%3Btop_ufis%3D1%3Bsig%3Dv1HCfPZXeY%3B&ss=The+Tower+A+Guoman+Hotel%2C+London%2C+Greater+London%2C+United+Kingdom&is_ski_area=&ssne=London&ssne_untouched=London&city=-2601889&checkin_year=2021&checkin_month=6&checkin_monthday=3&checkout_year=2021&checkout_month=6&checkout_monthday=5&group_adults=1&group_children=0&no_rooms=1&from_sf=1&ss_raw=tower+guo&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=220593&dest_type=hotel&place_id_lat=51.5063701880905&place_id_lon=-0.0732994079589844&search_pageview_id=bbff65b09ddd0152&search_selected=true&search_pageview_id=bbff65b09ddd0152&ac_suggestion_list_length=2&ac_suggestion_theme_list_length=0&sb_changed_destination=1'
            seleniumurl = 'https://bookings.guoman.com/100259?datein=06/05/2021&dateout=06/08/2021&rooms=1&adults=1&languageid=1#/accommodation/room'
            break
        if choice == 'Mornington':
            seleniumurl = 'https://www.bestwestern.co.uk/hotels/best-western-mornington-hotel-london-hyde-park-83187/in-2021-06-03/out-2021-06-05/adults-1/children-0/rooms-1'
            soupurl = 'https://www.booking.com/searchresults.en-gb.html?aid=355028&sid=d2a902f346650dc0b748848763652bdc&sb=1&src=searchresults&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Fsearchresults.en-gb.html%3Faid%3D355028%3Bsid%3Dd2a902f346650dc0b748848763652bdc%3Btmpl%3Dsearchresults%3Bcheckin_month%3D6%3Bcheckin_monthday%3D3%3Bcheckin_year%3D2021%3Bcheckout_month%3D6%3Bcheckout_monthday%3D5%3Bcheckout_year%3D2021%3Bclass_interval%3D1%3Bdest_id%3D-2601889%3Bdest_type%3Dcity%3Bdtdisc%3D0%3Bfrom_sf%3D1%3Bgroup_adults%3D1%3Bgroup_children%3D0%3Binac%3D0%3Bindex_postcard%3D0%3Blabel_click%3Dundef%3Bno_rooms%3D1%3Boffset%3D0%3Bpostcard%3D0%3Braw_dest_type%3Dcity%3Broom1%3DA%3Bsb_price_type%3Dtotal%3Bshw_aparth%3D1%3Bslp_r_match%3D0%3Bsrc%3Dsearchresults%3Bsrc_elem%3Dsb%3Bsrpvid%3Dc7cfa7f2e7b6003b%3Bss%3Dbest%2Bwestern%2Bmornington%3Bss_all%3D0%3Bssb%3Dempty%3Bsshis%3D0%3Bssne%3DLondon%3Bssne_untouched%3DLondon%3Btop_ufis%3D1%3Bsig%3Dv1VSYWZfwO%3B&ss=Best+Western+Mornington+Hotel+Hyde+Park%2C+London%2C+Greater+London%2C+United+Kingdom&is_ski_area=&ssne=London&ssne_untouched=London&city=-2601889&checkin_year=2021&checkin_month=6&checkin_monthday=3&checkout_year=2021&checkout_month=6&checkout_monthday=5&group_adults=1&group_children=0&no_rooms=1&from_sf=1&ss_raw=mornington&ac_position=2&ac_langcode=en&ac_click_type=b&dest_id=104382&dest_type=hotel&place_id_lat=51.5119450787344&place_id_lon=-0.178211331367493&search_pageview_id=c7cfa7f2e7b6003b&search_selected=true&search_pageview_id=c7cfa7f2e7b6003b&ac_suggestion_list_length=5&ac_suggestion_theme_list_length=0&sb_changed_destination=1'
            break
        if choice == 'Mayflower':
            soupurl = 'https://www.booking.com/searchresults.en-gb.html?aid=355028&sid=5b3ba02036d9329f4d26e3b97947d707&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Faid%3D355028%3Bsid%3D5b3ba02036d9329f4d26e3b97947d707%3Bsb_price_type%3Dtotal%26%3B&ss=Mayflower+Hotel+%26+Apartments%2C+London%2C+Greater+London%2C+United+Kingdom&is_ski_area=&checkin_year=2021&checkin_month=6&checkin_monthday=3&checkout_year=2021&checkout_month=6&checkout_monthday=5&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&ss_raw=mayflower+london&ac_position=0&ac_langcode=en&ac_click_type=b&dest_id=110267&dest_type=hotel&place_id_lat=51.4913674322905&place_id_lon=-0.195302367210388&search_pageview_id=c143959d2d90001d&search_selected=true&search_pageview_id=c143959d2d90001d&ac_suggestion_list_length=1&ac_suggestion_theme_list_length=0'
            seleniumurl = 'https://direct-book.com/properties/mayflower?locale=en&checkInDate=2021-06-03&numberNights=2&skin=1&items[0][adults]=1&items[0][children]=0&items[0][infants]=0&currency=GBP&checkOutDate=2021-06-05'
            break
        if choice == 'Four Seasons': #not working as of 30/04/2021
            soupurl = 'https://www.booking.com/searchresults.en-gb.html?aid=355028&sid=c52c53a3cbd66dab2b336e5f7426a7ca&sb=1&sb_lp=1&src=index&src_elem=sb&error_url=https%3A%2F%2Fwww.booking.com%2Findex.en-gb.html%3Faid%3D355028%3Bsid%3Dc52c53a3cbd66dab2b336e5f7426a7ca%3Bsb_price_type%3Dtotal%26%3B&ss=Four+Seasons+Hotel+London+at+Park+Lane%2C+London%2C+Greater+London%2C+United+Kingdom&is_ski_area=&checkin_year=2021&checkin_month=6&checkin_monthday=3&checkout_year=2021&checkout_month=6&checkout_monthday=5&group_adults=1&group_children=0&no_rooms=1&b_h4u_keep_filters=&from_sf=1&search_pageview_id=bb2699a703320186&ac_suggestion_list_length=2&ac_suggestion_theme_list_length=0&ac_position=0&ac_langcode=en&ac_click_type=b&_t=DgAAAOB7ImJjYiI6WzI0MDJdfQ&dest_id=447430&dest_type=hotel&place_id_lat=51.5042265240904&place_id_lon=-0.150056183338165&search_pageview_id=bb2699a703320186&search_selected=true&ss_raw=four+seasons+lond'
            seleniumurl = 'https://reservations.fourseasons.com/choose-your-room?hotelCode=LON509&checkIn=2021-06-03&checkOut=2021-06-05&adults=1&children=0&promoCode='
            break
        else:
            print ('This hotel is not supported, please re enter. ')
    return soupurl, seleniumurl, choice

def seleniumScrapeTower():
    driver = webdriver.Chrome(executable_path='C:\\Users\\Conor\\Desktop\\diss\\chromedriver.exe')
    driver.get(seleniumurl)
    WebDriverWait(driver, 15).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, ".CardList-price-title.ng-binding.ng-scope")))

    selname = driver.find_element_by_css_selector(".CardList-summary-title.ng-binding")
    originalname = str(selname.text)

    selprice = driver.find_element_by_css_selector(".CardList-price-title.ng-binding.ng-scope")
    originalprice = str(selprice.text)
    originalprice = originalprice.strip()
    originalvalue = Decimal(sub(r'[^\d.]', '', originalprice))

    driver.close()
    driver.quit()

    return originalname,originalprice,originalvalue

def seleniumScrapeMornington():
    driver = webdriver.Chrome(executable_path='C:\\Users\\Conor\\Desktop\\diss\\chromedriver.exe')
    driver.get(seleniumurl)
    time.sleep(10)


    working = driver.find_elements_by_class_name('room-type-block')

    for work in working:
        name = work.find_element_by_xpath('.//div/h2').text
        originalname=str(name)
        if originalname == 'Standard - Single Room':
            originalprice = work.find_element_by_xpath('.//div[3]/div/div[1]/div/div[2]/div[1]/div[2]/div[1]/div[1]/span[2]').text
            originalprice=str(originalprice)
            originalprice = originalprice.strip()
            originalvalue = Decimal(sub(r'[^\d.]', '', originalprice))
    
    driver.close()
    driver.quit()

    return originalname,originalprice,originalvalue

def seleniumScrapeMayflower():
    driver = webdriver.Chrome(executable_path='C:\\Users\\Conor\\Desktop\\diss\\chromedriver.exe')
    driver.get(seleniumurl)
    time.sleep(10)
    working = driver.find_elements_by_class_name('content-box.room-type')

    for work in working:
        name = work.find_element_by_xpath('.//div[1]/div/div/div[1]/h2/span').text
        originalname=str(name)
        originalname= originalname.strip()
        if originalname == 'Standard Single':
            originalprice = work.find_element_by_xpath('.//div[2]/span[2]').text
            originalprice= str(originalprice)
            originalprice = originalprice.strip()
            originalvalue = Decimal(sub(r'[^\d.]', '', originalprice))
    driver.close()
    driver.quit()

    return originalname,originalprice,originalvalue

def seleniumScrapeSeasons():
    driver = webdriver.Chrome(executable_path='C:\\Users\\Conor\\Desktop\\diss\\chromedriver.exe')
    driver.get(seleniumurl)
    time.sleep(10)
    working = driver.find_elements_by_class_name('search-result.ng-scope')

    for work in working:
        name = work.find_element_by_xpath('.//div[4]/h3').text
        originalname=str(name)
        originalname= originalname.strip()
        if originalname == 'SUPERIOR ROOM':
            originalprice = work.find_element_by_xpath('.//div/span[2]').text
            originalprice= str(originalprice)
            originalprice = originalprice.strip()
            originalvalue = Decimal(sub(r'[^\d.]', '', originalprice))
            originalvalue = originalvalue * 2
    driver.close()
    driver.quit()

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36'}


soupurl,seleniumurl, choice = hotelChoice()

if choice == 'Tower Hotel':
    originalname,originalprice,originalvalue = seleniumScrapeTower()
if choice == 'Mornington':
    originalname,originalprice,originalvalue = seleniumScrapeMornington()
if choice == 'Mayflower':
    originalname,originalprice,originalvalue = seleniumScrapeMayflower()
if choice == 'Four Seasons':
    originalname,originalprice,originalvalue = seleniumScrapeSeasons()

response=requests.get(soupurl, headers=headers)

soup=BeautifulSoup(response.content, "lxml")

for item in soup.select('.sr_property_block'):
    try:
        hotelname = item.select('.sr-hotel__name')[0].get_text()
        hotelname = hotelname.strip() #removing the leading and trailing space chars after scraping to make text
        

        if hotelname == 'The Tower Hotel':
            hotelprice = item.select('.bui-price-display__value')[0].get_text()
            hotelprice = hotelprice.strip() #removing blank chars
            value = Decimal(sub(r'[^\d.]', '', hotelprice)) #getting rid of currency symbol and commas for comparison
            if value > originalvalue:
                print("The cheapest price for the " +hotelname+" is " + originalprice + " and can be found at the hotel's website at this link")
                print(seleniumurl)
            else:
                print('This hotel is cheaper to be booked on bookings.com. You could save at least' + (originalvalue - value) + '£ by booking on booking.com')

        if hotelname == 'Best Western Mornington Hotel Hyde Park':
            hotelprice = item.select('.bui-price-display__value')[0].get_text()
            hotelprice = hotelprice.strip()
            value = Decimal(sub(r'[^\d.]', '', hotelprice))

            if value > originalvalue:
                print("The cheapest price for the " +hotelname+" is " + originalprice + " and can be found at the hotel's website at this link")
                print(seleniumurl)
            else:
                print('This hotel is cheaper to be booked on bookings.com. You could save at least' + (originalvalue - value) + '£ by booking on booking.com')

        if hotelname == 'Mayflower Hotel & Apartments':
            hotelprice = item.select('.bui-price-display__value')[0].get_text()
            hotelprice = hotelprice.strip()
            value = Decimal(sub(r'[^\d.]', '', hotelprice))
            if value > originalvalue:
                print("The cheapest price for the " +hotelname+" is " + originalprice + " and can be found at the hotel's website at this link")
                print(seleniumurl)
            else:
                print('This hotel is cheaper to be booked on bookings.com. You could save at least' + (originalvalue - value) + '£ by booking on booking.com')

        if hotelname == 'Four Seasons Hotel London at Park Lane':
            hotelprice = item.select('.bui-price-display__value')[0].get_text()
            hotelprice = hotelprice.strip()
            value = Decimal(sub(r'[^\d.]', '', hotelprice))
            if value > originalvalue:
                print("The cheapest price for the " +hotelname+" is " + originalprice + " and can be found at the hotel's website at this link")
                print(seleniumurl)
            else:
                print('This hotel is cheaper to be booked on bookings.com. You could save at least' + (originalvalue - value) + '£ by booking on booking.com')

        if hotelname == 'London Marriott Hotel County Hall':
            hotelprice = item.select('.bui-price-display__value')[0].get_text()
            hotelprice = hotelprice.strip() #removing blank chars
            value = Decimal(sub(r'[^\d.]', '', hotelprice)) #getting rid of currency symbol and commas for comparison
         
            if value > originalvalue:
                print("The cheapest price for the " +hotelname+" is " + originalprice + " and can be found at the hotel's website at this link")
                print(seleniumurl)
            else:
                print('This hotel is cheaper to be booked on bookings.com. You could save at least' + (originalvalue - value) + '£ by booking on booking.com')      
       
        
    except Exception as e:
        print('')


close = str(input("Type anything to close: ")) #This is here so when pyinstaller makes an exe of this, it doesn't close automatically after output
quit()