import csv
class Product:
    def __init__(self, nm='Unknown', pr=0.00, qt=0, ctg='Unknown'):
        self.name = nm
        self.price = pr
        self.quantity = qt
        self.category = ctg

    def set_name(self, new_name):
        self.name = new_name

    def get_name(self):
        return self.name

    def set_price(self, new_price):
        self.price = new_price

    def get_price(self):
        return self.price

    def set_quantity(self, new_quantity):
        self.quantity = new_quantity

    def get_quantity(self):
        return self.quantity

    def set_category(self, new_category):
        self.categoray = new_category

    def get_category(self):
        return self.category

    def __str__(self):
        return f"Name of the Product : {self.name}\n" \
               f"Unit Price : {self.price}\n" \
               f"Available Quantity : {self.quantity}\n" \
               f"Category : {self.category}"

p1 = Product('TRI ANGELS HEADPHONE TA-501', 1899, 100, 'Electronic accessories')
p2 = Product('Logitech H151 Basic Headphones', 4200, 100, 'Electronic accessories')
p3 = Product('Logitech G Pro Gaming Headset with Pro Grade Mic', 25999, 100, 'Electronic accessories')
p4 = Product('Logitech M190 Full Size Wireless Mouse\nLag-Free 2.4Ghz Wireless Connection Grey', 1899, 15, 'Electronic accessories')
p5 = Product('Lenovo M120 Pro Wired Mouse \nFor Computer Laptops With 1000DPI', 2205, 100, 'Electronic accessories')
p6 = Product('64GB SE9 + (FREE OTG) , USB Data Traveler\n    (Metal)', 725, 100, 'Electronic accessories')
p7 = Product('SAMSUNG SSD 870 EVO 1TB\nInternal Solid State Drive SATA 3 6Gbps 2.5Inch', 25800, 100, 'Electronic accessories')
list_of_products = [p1, p2, p3, p4, p5, p6, p7]

p8 = Product("Fossil Men's the Minimalist\nStainless Steel Slim Casual Quartz Watch", 10287, 100, 'Watches and Eyewear')
p9 = Product("NAVIFORCE Luxury Brand Men's Quartz Multi-function\n Waterproof Watch With Brand Box - NF9188", 2899, 25,'Watches and Eyewear')
p10 = Product("Fitbit Versa 2 Health and Fitness\nSmartwatch with Heart Rate, Music", 23951, 100,'Watches and Eyewear')
p11 = Product("Emporio Armani Women's\nStainless Steel Two-Hand Dress Watch",  30445, 100,'Watches and Eyewear')
p12 = Product("Bose Frames Soprano - Cat Eye Polarized, \nBluetooth Sunglasses", 40039, 100,'Watches and Eyewear')
p13 = Product("Ray-Ban Rb3447 Metal Round Sunglasses", 25888, 100,'Watches and Eyewear')
p14 = Product("Ray-Ban Rb2180 Round Sunglasses", 24111, 100,'Watches and Eyewear')
list_of_products = [p8, p9, p10, p11, p12, p13, p14]

p15 = Product("STOTT PILATES Eco Mat", 5690, 100, 'Health and Fitness')
p16 = Product("Bowflex SelectTech Adjustable Dumbbell", 64873, 100, 'Health and Fitness')
p17 = Product("Whatafit Resistance Bands Set (11pcs),\n Exercise Bands with Door Anchor, Handles,\n Carry Bag, Legs Ankle Straps", 4065, 60, 'Health and Fitness')
p18 = Product("BlenderBottle Classic Shaker Bottle Perfect\n for Protein Shakes and Pre Workout, 20-Ounce", 1382, 100, 'Health and Fitness')
p19 = Product("Marcy Portable Magnetic Mini Cycle Compact\n Under-Desk Pedal Cardio Exerciser NS-9200", 19510, 100, 'Health and Fitness')
p20 = Product(" G Fuel Pewdiepie (40 Servings) Elite Energy\n  and Endurance Powder 9.8 oz.", 5853, 100, 'Health and Fitness')
p21 = Product("C4 Sport Pre Workout Powder Fruit Punch\n + Energy Supplement for Men & Women", 6500, 100, 'Health and Fitness')
p22 = Product("Ab Roller Wheel, Abs Workout Equipment\n with Knee Pad Accessories", 2764, 100, 'Health and Fitness')
p23 = Product("DEGOL Skipping Rope with Ball Bearings\n Jump Rope Cable and 6” Memory Foam", 2276, 100, 'Health and Fitness')
p24 = Product("Balancefrom Rubber Encased\n Hex Dumbbell in Pairs", 19510, 100, 'Health and Fitness')
p25 = Product("Echelon Fitness Mat, Black", 6292, 100, 'Health and Fitness')
p26 = Product("FIREOX Unit TT Blaze Tape Ball Bat\n White , HL 75 , Primal Edition", 2400, 100, "Sports and Outdoor")
p27 = Product("Gunn and Moore 2017 Original\n Easy-Load Wheeled Cricket Bag", 18697, 100, "Sports and Outdoor")
p28 = Product("Gunn & Moore 5 Teknik 3/4 Sleeve\n Cricket Shirt, Maroon Trim, Medium", 4855, 100, "Sports and Outdoor")
p29 = Product("SS Kashmir Willow Leather Ball Cricket Bat", 10405, 100, "Sports and Outdoor")
p30 = Product("Gunn & Moore Original Duplex GM Origional\n Duplex Compact Cricket Bag, Navy", 19835, 100, "Sports and Outdoor")
p31 = Product("Pro Style Boxing Gloves-(Black) (16oz) (PR)", 8779, 100, "Sports and Outdoor")
p32 = Product("MaxxMMA MMA Thai Pad Training\n Kickboxing Muay Thai Shield (Single Unit)", 4877, 100, "Sports and Outdoor")
p33 = Product("Venum 'Attack' MMA Gloves", 8942, 100, "Sports and Outdoor")
p34 = Product("Men's Nike Pro Hyperstrong Football Top", 9755, 100, "Sports and Outdoor")
p35 = Product("Adidas mens Real Madrid Club Ball\n White/Spring Pink/Dark Blue 5", 2600, 100, "Sports and Outdoor")
p36 = Product("Adidas Originals Women's Regista 20 Jsyw", 6500, 100, "Sports and Outdoor")
p37 = Product("Adidas Men's X 19.3\n Firm Ground Boots Soccer Shoe", 9917, 100, "Sports and Outdoor")
p38 = Product("Adidas TIERRO13 GK 3/4 Pants [Black]", 6500, 100, "Sports and Outdoor")
p39 = Product("Adidas Tango Rosario\n Manchester United Soccer Ball", 3250, 100, "Sports and Outdoor")
p40 = Product("Adidas Unisex-Child Goletto VII\n Fg J Football Shoe", 4877, 100, "Sports and Outdoor")

p41 = Product("NBA 2K21 - PlayStation 4", 2113, 100, "E-Gaming")
p42 = Product("Logitech G502 HERO High Performance\n 11 Programmable Buttons,PC/Mac", 10568, 100, "E-Gaming")
p43 = Product(" Marvel's Spider-Man: Miles Morales\n Ultimate Launch Edition – PlayStation 5", 11380, 100, "E-Gaming")
p44 = Product("Battlefield 2042 - PC(Pre-release (8,2021))", 9755, 100, "E-Gaming")
p45 = Product("SONY PlayStation 4 Slim 1TB Console,\n Light & Slim PS4 System, 1TB Hard Drive", 81295, 100, "E-Gaming")
p46 = Product("SteelSeries Apex Pro TKL\n Mechanical Gaming Keyboard–RGB Backlit", 25690, 100, "E-Gaming")
p47 = Product("Assassin’s Creed Valhalla PlayStation 4\n Standard Edition", 7480, 100, "E-Gaming")
p48 = Product("Microsoft - Xbox One S 1TB All-Digital Edition\n Console with Xbox One Wireless Controller", 95927, 100, "E-Gaming")
p49 = Product("Mortal Kombat 11 (PS4)", 3739, 100, "E-Gaming")
p50 = Product("Charger for Xbox One Controller\n Battery Pack, with 4 x 1200mAh Charging Kit", 4550, 100, "E-Gaming")
p51 = Product("Red Dead Redemption 2 (PS4)", 5920, 100, "E-Gaming")
p52 = Product("Minecraft Starter Collection - PlayStation 4", 4640, 100, "E-Gaming")
p53 = Product("American Fugitive - PlayStation 4\n (Pre-release (8,2021))", 4880, 100, "E-Gaming")
p54 = Product("Razer Kraken Kitty Edition PC Gaming Headset-\n THX Spatial Audio - Quartz Pink", 24388, 100, "E-Gaming")
p55 = Product("Cyberpunk 2077 - PC\n [Game Download Code in Box]", 8130, 100, "E-Gaming")


class CSVFiling:

    def __init__(self, filename):
        self.filename = filename

    def setting_fields(self, list_of_fields=['Name', 'Empty', 'Empty', 'Empty']):
        self.fields = list_of_fields

    def setting_rows(self, list_of_rows=[[]]):
        self.rows = list_of_rows

    def writing_to_file(self):
        with open(self.filename, 'a') as csvfile:
            csvwriter = csv.writer(csvfile)
            csvwriter.writerow(self.fields)
            csvwriter.writerows(self.rows)

    def reading_from_file(self):
        self.fields = []
        self.rows = []
        with open(self.filename, 'r') as csvfile:
            csvreader = csv.reader(csvfile)
            self.fields = next(csvreader)
            for row in csvreader:
                self.rows.append(row)
        return self.fields, self.rows


fields = ['Name', 'Price', 'Quantity', 'Category']
rows = [[p1.get_name(), p1.get_price(), p1.get_quantity(), p1.get_category()], [p2.get_name(), p2.get_price(), p2.get_quantity(), p2.get_category()], [p3.get_name(), p3.get_price(), p3.get_quantity(), p3.get_category()], [p4.get_name(), p4.get_price(), p4.get_quantity(), p4.get_category()], [p5.get_name(), p5.get_price(), p5.get_quantity(), p5.get_category()], [p6.get_name(), p6.get_price(), p6.get_quantity(), p6.get_category()], [p7.get_name(), p7.get_price(), p7.get_quantity(), p7.get_category()], [p8.get_name(), p8.get_price(), p8.get_quantity(), p8.get_category()], [p9.get_name(), p9.get_price(), p9.get_quantity(), p9.get_category()], [p10.get_name(), p10.get_price(), p10.get_quantity(), p10.get_category()], [p11.get_name(), p11.get_price(), p11.get_quantity(), p11.get_category()], [p12.get_name(), p12.get_price(), p12.get_quantity(), p12.get_category()], [p13.get_name(), p13.get_price(), p13.get_quantity(), p13.get_category()], [p14.get_name(), p14.get_price(), p14.get_quantity(), p14.get_category()], [p15.get_name(), p15.get_price(), p15.get_quantity(), p15.get_category()], [p16.get_name(), p16.get_price(), p16.get_quantity(), p16.get_category()], [p17.get_name(), p17.get_price(), p17.get_quantity(), p17.get_category()], [p18.get_name(), p18.get_price(), p18.get_quantity(), p18.get_category()], [p19.get_name(), p19.get_price(), p19.get_quantity(), p19.get_category()], [p20.get_name(), p20.get_price(), p20.get_quantity(), p20.get_category()], [p21.get_name(), p21.get_price(), p21.get_quantity(), p21.get_category()], [p22.get_name(), p22.get_price(), p22.get_quantity(), p22.get_category()], [p23.get_name(), p23.get_price(), p23.get_quantity(), p23.get_category()], [p24.get_name(), p24.get_price(), p24.get_quantity(), p24.get_category()], [p25.get_name(), p25.get_price(), p25.get_quantity(), p25.get_category()], [p26.get_name(), p26.get_price(), p26.get_quantity(), p26.get_category()], [p27.get_name(), p27.get_price(), p27.get_quantity(), p27.get_category()], [p28.get_name(), p28.get_price(), p28.get_quantity(), p28.get_category()], [p29.get_name(), p29.get_price(), p29.get_quantity(), p29.get_category()], [p30.get_name(), p30.get_price(), p30.get_quantity(), p30.get_category()], [p31.get_name(), p31.get_price(), p31.get_quantity(), p31.get_category()], [p32.get_name(), p32.get_price(), p32.get_quantity(), p32.get_category()], [p33.get_name(), p33.get_price(), p33.get_quantity(), p33.get_category()], [p34.get_name(), p34.get_price(), p34.get_quantity(), p34.get_category()], [p35.get_name(), p35.get_price(), p35.get_quantity(), p35.get_category()], [p36.get_name(), p36.get_price(), p36.get_quantity(), p36.get_category()], [p37.get_name(), p37.get_price(), p37.get_quantity(), p37.get_category()], [p38.get_name(), p38.get_price(), p38.get_quantity(), p38.get_category()], [p39.get_name(), p39.get_price(), p39.get_quantity(), p39.get_category()], [p40.get_name(), p40.get_price(), p40.get_quantity(), p40.get_category()], [p41.get_name(), p41.get_price(), p41.get_quantity(), p41.get_category()], [p42.get_name(), p42.get_price(), p42.get_quantity(), p42.get_category()], [p43.get_name(), p43.get_price(), p43.get_quantity(), p43.get_category()], [p44.get_name(), p44.get_price(), p44.get_quantity(), p44.get_category()], [p45.get_name(), p45.get_price(), p45.get_quantity(), p45.get_category()], [p46.get_name(), p46.get_price(), p46.get_quantity(), p46.get_category()], [p47.get_name(), p47.get_price(), p47.get_quantity(), p47.get_category()], [p48.get_name(), p48.get_price(), p48.get_quantity(), p48.get_category()], [p49.get_name(), p49.get_price(), p49.get_quantity(), p49.get_category()], [p50.get_name(), p50.get_price(), p50.get_quantity(), p50.get_category()], [p51.get_name(), p51.get_price(), p51.get_quantity(), p51.get_category()], [p52.get_name(), p52.get_price(), p52.get_quantity(), p52.get_category()], [p53.get_name(), p53.get_price(), p53.get_quantity(), p53.get_category()], [p54.get_name(), p54.get_price(), p54.get_quantity(), p54.get_category()], [p55.get_name(), p55.get_price(), p55.get_quantity(), p55.get_category()]]

# rows = [[p8.get_name(), p8.get_price(), p8.get_quantity(), p8.get_category()], [p9.get_name(), p9.get_price(), p9.get_quantity(), p9.get_category()], [p10.get_name(), p10.get_price(), p10.get_quantity(), p10.get_category()], [p11.get_name(), p11.get_price(), p11.get_quantity(), p11.get_category()], [p12.get_name(), p12.get_price(), p12.get_quantity(), p12.get_category()], [p13.get_name(), p13.get_price(), p13.get_quantity(), p13.get_category()], [p14.get_name(), p14.get_price(), p14.get_quantity(), p14.get_category()]]

file1 = CSVFiling(filename='E:/OOP Project/Products.csv')
file1.setting_fields(fields)
file1.setting_rows(rows)
file1.writing_to_file()

