class Supermarket :
    count = 0

    def __init__(self, location, name, product, customer):
        self.__location = location
        self.__name = name
        self.__product = product
        self.__customer = int(customer)
        Supermarket.count += 1 # 그냥 count가 아니라 Supermarket class의 count

    def print_location(self) :
        print(f"위치 : {self.__location}")

    def change_category(self, product) :
        self.__product = product
    
    def show_list(self) :
        print(f"현재 파는 물건 : {self.__product}")

    def enter_customer(self) :
        self.__customer += 1

    def show_info(self) :
        print(f"가게 이름:{self.__name}  위치:{
            self.__location}  파는 물건:{
                self.__product}  손님 수:{self.__customer}")

    def show_supermarket_count(self) : 
        print(f"슈퍼마켓 갯수 : {Supermarket.count}")

sup1 = Supermarket("마포구", "사포마트", "두부", "10")
sup1.print_location()
sup1.show_list()
sup1.change_category("치킨")
sup1.show_list()
sup1.enter_customer()
sup1.show_info()
sup1.show_supermarket_count()

sup2 = Supermarket("음앙구", "으앙마트", "스테이크", "30")
sup1.show_supermarket_count()
sup2.show_supermarket_count()