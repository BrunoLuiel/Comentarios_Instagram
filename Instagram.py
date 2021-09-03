from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class Instagram_boot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Firefox(executable_path =r"C:\Users\ADM\Documents\Chrome Driver\geckodriver.exe")

    def login(self):
        driver = self.driver
        driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(2)
        driver.find_element_by_name('username').send_keys(self.username)
        driver.find_element_by_name('password').send_keys(self.password + Keys.RETURN)
        time.sleep(5)

    @staticmethod
    def digite_como_uma_pessoa(frase, onde_digitar):
        for letra in frase:
            onde_digitar.send_keys(letra)
            time.sleep(random.randint(1,5)/30)

    def comentar_na_hash(self,hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(5)

        for i in range (1,3):
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
        
        href = driver.find_elements_by_tag_name('a')
        pic_hrefs = [elem.get_attribute('href')for elem in href]
        [href for href in pic_hrefs if hashtag in href]
        print(hashtag + ' fotos ' + str(len(pic_hrefs)))


        for pic_hef in pic_hrefs:
            driver.get(pic_hef)
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            
            
            try:

                comentarios = ['Caramba, então tá', 'Top top top!', 'É disso que eu falo Brasil', 'Contabilidade é vida!', 'Concordo!', 'Me siga também no Insta que sigo de volta!', 'topzera']
                driver.find_element_by_class_name('Ypffh').click()
                campo_comentario = driver.find_element_by_class_name('Ypffh')
                time.sleep(5)              
                self.digite_como_uma_pessoa(random.choice(comentarios),campo_comentario)
                #driver.find_element_by_xpath('//buttom[contains(text(), "Publicar)]').click()
                driver.find_element_by_xpath('/html/body/div[1]/section/main/div/div[1]/article/div[3]/section[3]/div/form/button[2]').click()
                time.sleep(random.randint(5,15))

            except Exception as e:
                print(e)
                time.sleep(5)



boot = Instagram_boot('brunoluiel@gmail.com', 'minhasenha')
boot.login()
boot.comentar_na_hash('contabeis')
boot.digite_como_uma_pessoa
