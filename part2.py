# Сначала - как мы не должны делать. То есть, без использования 2-го принципа open/closed

class Report():   #класс б. обрабат-ть данные и выводить отчеты
    def __init__(self, title, content):  # ф-я иниц-уии.У нашего отчета(док-та) будет заголовок и контент
        self.title = title    #все эти хар-ки привязываем к классу
        self.content = content

    def docPrinter(self):
        print(f"Сформирован отчет - {self.title} - {self.content}")
# Это - обычный класс.