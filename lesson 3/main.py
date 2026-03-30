from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Bot():
    def __init__(self):
        self.browser = WebDriver()
        self.wait = WebDriverWait(self.browser, 5)
        self.wait_longer = WebDriverWait(self.browser, 15)
        self.names = []
        
    def connect(self):
        self.browser.get('https://pokemondb.net/pokedex/all')
        poke_table = self.wait.until(EC.presence_of_element_located((By.ID, 'pokedex')))
        # table_body = poke_table.find_element(By.TAG_NAME, 'tbody')
        # table_rows = table_body.find_elements(By.TAG_NAME, 'tr')
        # for row in table_rows:
        #     row_cells = row.find_elements(By.TAG_NAME, 'td')
        #     pokemon_name = row_cells[1].text
        #     if '\n' in pokemon_name: pokemon_name = pokemon_name.split('\n')[1]
        #     self.names.append(pokemon_name)
        name_cells = poke_table.find_elements(By.CLASS_NAME, 'cell-name')
        for cell in name_cells:
            pokemon_name = cell.text
            if '\n' in pokemon_name: pokemon_name = pokemon_name.split('\n')[1]
            self.names.append(pokemon_name)
            
                 
if __name__ == "__main__":
    try:
        bot = Bot()
        bot.connect()
        print(bot.names)
    finally:
        bot.browser.quit()