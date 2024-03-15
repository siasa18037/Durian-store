import uvicorn
import random
import uuid

from BaseModel import *
from Account import *
from Product import *
from Promotion import *
from Order import *
from Payment import *
from Apple import *
from Apple import *
from Cart import *
from Category import *
from Help import *
from Admin import *
from Customer import *
from Address import *



# generate number
def generate_number():
    order_number = ''.join([str(random.randint(0, 9)) for _ in range(8)])
    return order_number

def generate_uuid_int():
    uuid_str = str(uuid.uuid4())
    uuid_int = int(uuid_str.replace("-", "")[:16], 16)
    return uuid_int

def generate_uuid_int_10_digits():
    uuid_int = int(uuid.uuid4().hex, 16)
    uuid_int_10_digits = uuid_int % 10**10
    return uuid_int_10_digits

def generate_uuid_int_8_digits():
    uuid_int = int(uuid.uuid4().hex, 16)
    uuid_int_8_digits = uuid_int % 10**8
    return uuid_int_8_digits


apple = Apple()

# Add Customer
apple.add_customer(Customer(10001, "siasa18037@gmail.com", "Sia18037", "siasa", "23-07-2004" ))
apple.add_customer(Customer(10002, "pim17925@gmail.com", "Pim17925", "pim", "25-09-2004" ))
apple.add_customer(Customer(10003, "kalun17902@gmail.com", "Gun17902", "gun", "24-06-2004" ))
apple.add_customer(Customer(10004, "focus17919@gmail.com", "Focus17919", "focus", "20-09-2004" ))
apple.add_customer(Customer(10005, "peepo16506@gmail.com", "peepo19596", "peepo", "28-01-2004" ))

# Add admin
apple.add_admin(Admin(90001, "admin@admin", "admin", "siasa group", "23-07-2004" ))

# call Customer
siasa = apple.search_customer_from_id(10001)
pim = apple.search_customer_from_id(10002)
gun = apple.search_customer_from_id(10003)
focus = apple.search_customer_from_id(10004)
peepo = apple.search_customer_from_id(10005)

#call admin
adminsiasa = apple.search_admin_from_id(90001)

# add addresses customers
# siasa.add_address(Address(100001, "ธนกฤต สุไชยชิต" ,"0933616996", "343/65 หมู่ 14 ซ.บ้านเก่าจาน" , "หมากเเข้ง" , "อ.เมือง" , "อุดร" , "41000"))
# siasa.add_address(Address(100002, "awdeawdawd" ,"0933616996", "343/65 หมู่ 14 ซ.บ้านเก่าจาน" , "หมากเเข้ง" , "อ.เมือง" , "อุดร" , "41000"))


# add app_payment
apple.add_payment(Payment(101,"Card","บัตรเครดิตหรือบัตรเดบิต" ,None ,"Visa, MasterCard" , None , "OPEN", "https://www.2010megastore.com/wp-content/uploads/2017/03/transparent-logo-visa.png"))
apple.add_payment(Payment(102,"QR","PromptPay" ,"0933616996" , None , None , "OPEN", "https://www.designil.com/wp-content/uploads/2020/04/prompt-pay-logo.png"))
apple.add_payment(Payment(103,"QR","truewallet" , "0933616996" ,"truewallet" , None , "CLOSED", "https://www.truemoney.com/wp-content/uploads/2020/12/truemoneywallet-logo-20190424.png"))
apple.add_payment(Payment(104,"Bank","ชำระเงินผ่านธนาคาร" , "0861170608" ,"กสิกรไทย" , "ธนกฤต สุไชยชิต" , "OPEN" , "https://i.pinimg.com/originals/cb/7c/ca/cb7cca77e49eece5ce042aa9f25ad27c.png"))
apple.add_payment(Payment(105,"Bank","ชำระเงินผ่านธนาคาร" , "0345345508" ,"SCB" , "ธนกฤต สุไชยชิต" , "CLOSED" , "https://i.pinimg.com/736x/02/31/87/023187a2f2dc47bbdc809b43c7667b3a.jpg"))
apple.add_payment(Payment(106,"Bank","ชำระเงินผ่านธนาคาร" , "5464564564" ,"กรุงเทพ" , "ธนกฤต สุไชยชิต" , "OPEN" , "https://yt3.googleusercontent.com/ytc/AIdro_lT_XAcdlqIBtCEg3sqDXl0w3iYTLX1G5ONJNMs=s900-c-k-c0x00ffffff-no-rj"))

#add Category
apple.add_category(Category(101,"Iphone", "" ,"https://www.apple.com/th/iphone/home/images/meta/iphone__ky2k6x5u6vue_og.png"))
apple.add_category(Category(102,"Ipad", "" ,"https://www.apple.com/newsroom/images/product/ipad/standard/Apple-iPad-10th-gen-hero-221018_Full-Bleed-Image.jpg.xlarge.jpg"))
apple.add_category(Category(103,"Mac","" ,"https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/mac-og-image-202310?wid=1200&hei=630&fmt=jpeg&qlt=95&.v=1697128365925"))
apple.add_category(Category(104,"Watch","" , "https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/s9-case-unselect-gallery-1-202403_GEO_TH_LANG_TH?wid=5120&hei=3280&fmt=p-jpg&qlt=80&.v=1708729830879"))
apple.add_category(Category(105,"Airpods","" , "https://t.ctcdn.com.br/CLMG2wxaBHY6MbhXzkGgVv-7Jnw=/1024x576/smart/i363596.jpeg"))
apple.add_category(Category(106,"Accessories","" , "https://futureworld.com.lk/wp-content/uploads/2023/09/article-head.jpg"))
iphone = apple.search_category_from_id(101)
ipad = apple.search_category_from_id(102)
mac = apple.search_category_from_id(103)
watch = apple.search_category_from_id(104)
airpods = apple.search_category_from_id(105)
accessories = apple.search_category_from_id(106)

#add product
apple.add_product(Product(100001, iphone , "iphone 15" , "iPhone 15 เปลี่ยนวัสดุตัวเครื่องเป็นไทเทเนียมที่แข็งแกร่งและมีน้ำหนักเบาเกรดเดียวกับที่ใช้ในอุตสาหกรรมอวกาศ พร้อมกล้องระดับโปรที่อเนกประสงค์ยิ่งกว่าเดิม ถ่ายภาพระยะใกล้ได้คมชัดจากที่ที่ไกลกว่าเดิมด้วยกล้องเทเลโฟโต้ 5 เท่า ให้คุณได้ภาพจากระยะที่ชอบในมุมที่ใช่\nการเชื่อมต่อระดับโปร ด้วยช่องต่อ USB-C\nชิป A17 Pro GPU ระดับโปรให้เล่นเกมมือถือรู้สึกเต็มอิ่มสมจริงยิ่งขึ้น\nปุ่มแอ็คชั่นที่ปรับแต่งได้ตามต้องการทั้ง ปิดเสียง กล้อง บันทึกเสียง และอีกมากมาย", 28900 , "20-6-2022", 100 , "https://media.studio7thailand.com/109315/iPhone_15_Pink_1-square_medium.jpg"))
apple.add_product(Product(100002, iphone , "iPhone 15 Pro" , "iPhone 15 Pro เปลี่ยนวัสดุตัวเครื่องเป็นไทเทเนียมที่แข็งแกร่งและมีน้ำหนักเบาเกรดเดียวกับที่ใช้ในอุตสาหกรรมอวกาศ พร้อมกล้องระดับโปรที่อเนกประสงค์ยิ่งกว่าเดิม ถ่ายภาพระยะใกล้ได้คมชัดจากที่ที่ไกลกว่าเดิมด้วยกล้องเทเลโฟโต้ 5 เท่า ให้คุณได้ภาพจากระยะที่ชอบในมุมที่ใช่\nการเชื่อมต่อระดับโปร ด้วยช่องต่อ USB-C\nชิป A17 Pro GPU ระดับโปรให้เล่นเกมมือถือรู้สึกเต็มอิ่มสมจริงยิ่งขึ้น\nปุ่มแอ็คชั่นที่ปรับแต่งได้ตามต้องการทั้ง ปิดเสียง กล้อง บันทึกเสียง และอีกมากมาย", 42500, "20-6-2022", 134 , "https://media.studio7thailand.com/109215/iPhone_15_Pro_Blue_Titanium_1-square_medium.jpg"))
apple.add_product(Product(100003, iphone , "iPhone 15 Pro Max" , "iPhone 15 Pro Max เปลี่ยนวัสดุตัวเครื่องเป็นไทเทเนียมที่แข็งแกร่งและมีน้ำหนักเบาเกรดเดียวกับที่ใช้ในอุตสาหกรรมอวกาศ พร้อมกล้องระดับโปรที่อเนกประสงค์ยิ่งกว่าเดิม ถ่ายภาพระยะใกล้ได้คมชัดจากที่ที่ไกลกว่าเดิมด้วยกล้องเทเลโฟโต้ 5 เท่า ให้คุณได้ภาพจากระยะที่ชอบในมุมที่ใช่\nการเชื่อมต่อระดับโปร ด้วยช่องต่อ USB-C\nชิป A17 Pro GPU ระดับโปรให้เล่นเกมมือถือรู้สึกเต็มอิ่มสมจริงยิ่งขึ้น\nปุ่มแอ็คชั่นที่ปรับแต่งได้ตามต้องการทั้ง ปิดเสียง กล้อง บันทึกเสียง และอีกมากมาย", 43900 , "20-6-2022", 14 , "https://media.studio7thailand.com/109626/iPhone_15_Pro_Max_Natural_Titanium_1-square_medium.jpg"))
apple.add_product(Product(100004, iphone , "iphone 14" , "iPhone 14 · กล้อง 12MP · รูรับแสงขนาด ƒ/1.9 · ออโต้โฟกัสด้วย Focus Pixels · Retina Flash · Photonic Engine · Deep Fusion · HDR อัจฉริยะ 4 กล้อง TrueDepth · กล้องความละเอียด 12MP · รูรับแสงขนาด ƒ/1.9 · ออโต้โฟกัสด้วย Focus Pixels · ชุดเลนส์ 6 ชิ้น", 25200 , "23-7-2021", 60 , "https://media.studio7thailand.com/93319/iPhone_14_Yellow_1-square_medium.jpg"))
apple.add_product(Product(100005, iphone , "iphone 14 Pro" , "iPhone 14 Pro· กล้อง 12MP · รูรับแสงขนาด ƒ/1.9 · ออโต้โฟกัสด้วย Focus Pixels · Retina Flash · Photonic Engine · Deep Fusion · HDR อัจฉริยะ 4 กล้อง TrueDepth · กล้องความละเอียด 12MP · รูรับแสงขนาด ƒ/1.9 · ออโต้โฟกัสด้วย Focus Pixels · ชุดเลนส์ 6 ชิ้น", 58500 , "23-7-2021", 70 , "https://media.studio7thailand.com/75842/iPhone_14_Pro_Gold_PDP_Image_Position-1A_Gold_1-square_medium.jpg"))
apple.add_product(Product(100006, iphone , "iphone 13" , "iPhone 13 เป็นโทรศัพท์มือถือรุ่นล่าสุดของ Apple ที่เปิดตัวในปี 2021 มาพร้อมกับหลายฟีเจอร์ที่น่าสนใจ เช่น ชิป A15 Bionic ที่มีประสิทธิภาพสูง การอัพเกรดกล้องและฟีเจอร์การถ่ายภาพ แบตเตอรี่ที่อัพเกรดให้มีอายุการใช้งานนานขึ้น รองรับ 5G และมีการออกแบบใหม่ด้านดีไซน์อีกด้วย", 25000 , "3-6-2020", 10 , "https://media.studio7thailand.com/7107/iPhone_13_PDP_Position-1A_Color_Starlight__1.jpg"))
apple.add_product(Product(100007, iphone , "iphone SE" , "ชิป A15 Bionic ที่เร็วสุดขั้วและ 5G สุดเร็ว การยกระดับครั้งใหญ่ของแบตเตอรี่และกล้องระดับซูเปอร์สตาร์ พร้อมด้วยกระจกที่แข็งแกร่งที่สุดในสมาร์ทโฟนและปุ่มโฮมพร้อม Touch ID ที่ปลอดภัย\nระบบเซลลูลาร์ 5G\nจอภาพ Retina HD ขนาด 4.7 นิ้ว\nระบบกล้องเดี่ยวสุดล้ำที่ประกอบด้วยกล้องไวด์ ความละเอียด 12MP\nกล้อง FaceTime HD ความละเอียด 7MP\nชิป A15 Bionic เพื่อประสิทธิภาพที่เร็วสุดขั้ว\nเล่นวิดีโอนานสูงสุด 15 ชั่วโมง", 17000 , "3-6-2020", 10 , "https://media.studio7thailand.com/9023/iPhone_SE_Starlight_1-square_medium.jpg"))
apple.add_product(Product(100008, ipad , "iPad pro 2022" , "iPad Pro มาพร้อมประสิทธิภาพที่น่าทึ่ง การเชื่อมต่อแบบไร้สายที่เร็วสุดแรง และประสบการณ์การใช้งาน Apple Pencil เจเนอเรชั่นถัดไป บวกกับคุณสมบัติใหม่อันทรงพลังสำหรับประสิทธิภาพการทำงานและการทำงานร่วมกันใน iPadOS 16 นี่แหละ iPad Pro ที่สุดแห่งประสบการณ์ iPad\nจอภาพ Liquid Retina ขนาด 11 นิ้ว\nชิป M2 พร้อม CPU แบบ 8-core และ GPU แบบ 10-core\nกล้องไวด์ความละเอียด 12MP\nกล้องหน้าอัลตร้าไวด์ความละเอียด 12MP\nใช้งานได้กับ Apple Pencil (รุ่นที่ 2)\niPadOS 16", 38000 , "23-7-2021", 60 , "https://media.studio7thailand.com/81229/iPad_Pro_Wi-Fi_11_in_4th_Gen_Space_Gray_1-square_medium.jpg"))
apple.add_product(Product(100009, ipad , "iPad Air 5" , "iPad Air (5th Gen) รุ่นล่าสุดสำหรับ iPad Air อัพเกรดขึ้นไปอีกขั้นด้วยจอภาพที่ใหม่และกว้าง พร้อมชิปประมาลผลที่ทรงประสิทธิภาพ ให้การทำงานหรือเล่นเกมหนัก ๆ ตัดต่อคลิป วาดรูป กลายเป็นเรื่องง่าย ๆ แต่ยังคงความเบาและบางไว้ได้อยู่\nชิป Apple M1 พร้อม Neural Engine\nใช้งานได้กับ Apple Pencil (รุ่นที่ 2)\nจอภาพ Liquid Retina ขนาด 10.9 นิ้ว\nพอร์ตการเชื่อมต่อแบบ USB-C", 26000 , "3-6-2020", 10 , "https://media.studio7thailand.com/8488/iPad_Air_Wi-Fi_Starlight_1-square_medium.jpg"))
apple.add_product(Product(100010, ipad , "iPad 10 2022" , "ได้รับการออกแบบใหม่ให้มีสีสันสดใสและอเนกประสงค์ยิ่งขึ้นกว่าครั้งไหนๆ โดยมาในดีไซน์แบบหน้าจอทั้งหมดบวกกับจอภาพ Liquid Retina ขนาด 10.9 นิ้ว และ 4 สีสวยสะดุดตา เรียกว่า iPad เป็นวิธีที่ทรงพลังในการทำนั่นทำนี่ให้เสร็จ สร้างสรรค์ และต่อติดกับทุกเรื่องอยู่เสมอ\nจอภาพ Liquid Retina ขนาด 10.9 นิ้ว\nชิป A14 Bionic พร้อม CPU แบบ 6-core และ GPU แบบ 4-core\nกล้องหลังไวด์ความละเอียด 12MP\nกล้องหน้าอัลตร้าไวด์ความละเอียด 12MP\nTouch ID เพื่อการยืนยันตัวตนที่ปลอดภัย\nใช้งานได้กับ Apple Pencil (รุ่นที่ 1)\niPadOS 16", 13500 , "3-6-2020", 19 , "https://media.studio7thailand.com/81309/iPad_10th_Gen_Wi-Fi_Silver_1-square_medium.jpg"))
apple.add_product(Product(100011, ipad , "iPad mini 6 2021" , "iPad mini 6 ใหม่ มาในดีไซน์แบบหน้าจอทั้งหมด พร้อมจอภาพ Liquid Retina ขนาด 8.3 นิ้ว ชิป A15 Bionic อันทรงพลังและ Neural Engine กล้องหน้าอัลตร้าไวด์ ความละเอียด 12MP พร้อมคุณสมบัติ จัดให้อยู่ตรงกลาง การเชื่อมต่อแบบ USB-C อีกทั้งยังจดโน้ต ทำเครื่องหมายในเอกสาร หรือถ่ายทอดไอเดียสุดยิ่งใหญ่ได้ด้วย Apple Pencil (รุ่นที่ 2) ที่ยึดติดกับตัวเครื่องไว้ด้วยแม่เหล็กและชาร์จแบบไร้สาย\nจอภาพ Liquid Retina ขนาด 8.3 นิ้ว\nชิป A15 Bionic พร้อม Neural Engine\nTouch ID เพื่อการยืนยันตัวตนที่ปลอดภัย\nกล้องหลังไวด์ ความละเอียด 12MP", 21000 , "3-6-2020", 50 , "https://media.studio7thailand.com/6630/iPad_mini_Wi-Fi_Starlight_1-square_medium.jpg"))
apple.add_product(Product(100012, watch, "Apple watch SE", "Apple Watch SE เป็นสมาร์ทวอทช์รุ่นที่เน้นความคุ้มค่า มาพร้อมกับฟีเจอร์หลักๆ ของ Apple Watch แต่ในราคาที่เบาบางกว่า มีขนาดหน้าปัด 40 มิลลิเมตรหรือ 44 มิลลิเมตร มีหลายสีให้เลือก เช่น เทา, เงิน, ทอง, และสีน้ำเงิน มีฟีเจอร์การตรวจวัดการออกกำลังกายและการเฝ้าติดตามสุขภาพ รวมถึงฟีเจอร์การเปิดตัวการติดตามการนอน Apple Watch SE ยังมีการเชื่อมต่อกับ iPhone เพื่อรับการแจ้งเตือนและการเพิ่มฟังก์ชันอื่นๆ ที่ทำงานร่วมกันกับแอปพลิเคชันบน iPhone",11000,"13-4-2022",0,"https://media.studio7thailand.com/111077/Apple_Watch_SE_GPS_40mm_Silver_Aluminum_Winter_Blue_Sport_Loop_1-square_medium.jpg"))
apple.add_product(Product(100013, watch, "Apple Watch Series 9", "Apple Watch 9 คือร่นพิเศษของ Apple Watch ที่ได้รับการออกแบบมาเพื่อนักวิ่งและนักกีฬา มีลักษณะที่เด่นคือมีนาฬิกาและสายข้อมือที่ออกแบบโดย Nike ซึ่งมีลายการ์ตูนและสีสดชัด มีฟีเจอร์ที่ช่วยให้นักกีฬาสามารถติดตามและวัดผลการออกกำลังกายได้ดี เช่น แอป Nike Run Club และการแข่งขันกับเพื่อนผ่านแอป Activity และนอกจากนี้ยังมีฟีเจอร์พิเศษอื่น ๆ ที่ช่วยให้การใช้งาน Apple Watch สะดวกสบายมากยิ่งขึ้นสำหรับนักกีฬาและคนรักการออกกำลังกาย",18000,"11-9-2020",27,"https://media.studio7thailand.com/112634/Apple_Watch_Series_9_GPS_41mm_Starlight_Aluminum_Starlight_Sport_Band_1-square_medium.jpg"))
apple.add_product(Product(100014, watch, "Apple Watch Ultra 2", "Apple Watch Ultra 2 ที่สมบุกสมบันและมากความสามารถที่สุด โดยออกแบบมาเพื่อการผจญภัยแบบเอาท์ดอร์และการออกกำลังกายแบบเต็มพลัง พร้อมตัวเรือนไทเทเนียมน้ำหนักเบา แบตเตอรี่ที่ใช้งานได้ยาวนานเป็นพิเศษ และจอภาพที่สว่างที่สุดเท่าที่เคยมีมา อีกทั้งยังมีคำสั่งนิ้ว วิธีที่มหัศจรรย์ในการโต้ตอบกับ Apple Watch\nSiP รุ่น S9 ที่ขับเคลื่อนจอภาพที่สว่างสุด ๆ\nจอภาพ Retina แบบติดตลอดที่สว่างที่สุดของ Apple\n วิธีที่มหัศจรรย์ในการโต้ตอบกับ Apple Watch\nตัวเรือน 49 มม. ที่ทนต่อการกัดกร่อนและทนน้ำที่ระดับ 100 ม.",31900,"16-7-2023",10,"https://media.studio7thailand.com/112165/Apple_Watch_Ultra_2_LTE_49mm_Titanium_Blue_Black_Trail_Loop_1-square_medium.jpg"))
apple.add_product(Product(100015, mac, "MacBook Air", "MacBook Air เป็นโน้ตบุ๊กบุครุ่นเล็กและบางเบาของ Apple มีดีไซน์ที่บางเบาและสวยงาม มีหน้าจอ Retina ขนาด 13.3 นิ้ว (บางรุ่น) หรือ 14 นิ้ว (ตั้งแต่รุ่น MacBook Air 2021) ที่ให้ภาพคมชัดและสีสันที่สวยงาม มาพร้อมกับชิป M1 ที่ให้ประสิทธิภาพเครื่องคอมพิวเตอร์สูง และอาจมีการอัพเกรดเป็นชิป M2 ในอนาคต มีการออกแบบให้ใช้งานง่ายสะดวก มีแบตเตอรี่ที่ให้การใช้งานยาวนาน รองรับ Touch ID สำหรับการเข้าสู่ระบบและการยืนยันตัวตนอื่น ๆ มี USB-C ที่ใช้ในการชาร์จและการเชื่อมต่ออุปกรณ์อื่น ๆ อีกด้วย สำหรับการทำงานทั่วไปและการใช้งานที่ต้องการพกพาง่าย MacBook Air เป็นตัวเลือกที่ดีสำหรับผู้ใช้ทั่วไปและนักศึกษา",39900,"17-4-2021",15,"https://media.studio7thailand.com/129251/MacBook-Air-13-inch-M3-Silver-1-square_medium.jpg"))
apple.add_product(Product(100016, mac, "MacBook Pro", "MacBook Pro เป็นโน้ตบุ๊กบุคระดับมืออาชีพของ Apple มีความสามารถและประสิทธิภาพที่สูง มีหลายรุ่นให้เลือกตามความต้องการของผู้ใช้ โดยรุ่นล่าสุดจะมีการใช้ชิป M1 Pro หรือ M1 Max ที่ให้ประสิทธิภาพเครื่องคอมพิวเตอร์ที่สูงขึ้น มีหน้าจอ Retina ขนาด 14 นิ้วหรือ 16 นิ้ว ที่มีความละเอียดสูงและสีสันที่สมจริง มี Touch Bar ที่เป็นแถบสัมผัสที่ใช้งานได้หลากหลายฟังก์ชัน มีระบบเสียงที่ดีด้วยลำโพงซิสเต็ม มีการออกแบบที่สวยงามและโดดเด่น มีคีย์บอร์ดที่มีการออกแบบใหม่เพื่อความสบายในการพิมพ์ มี Touch ID สำหรับการเข้าสู่ระบบและการยืนยันตัวตน มีพอร์ต Thunderbolt ที่ใช้ในการชาร์จและการเชื่อมต่ออุปกรณ์อื่น ๆ อีกด้วย สำหรับผู้ที่ต้องการเครื่องคอมพิวเตอร์ที่มีประสิทธิภาพสูงและความสามารถมากๆ สำหรับงานออกแบบ การตัดต่อวิดีโอ หรือการพัฒนาซอฟต์แวร์ MacBook Pro เป็นตัวเลือกที่ยอดเยี่ยม",71000,"26-6-2023",14,"https://media.studio7thailand.com/118054/MacBook-Pro-M3-Space-Gray-1-square_medium.jpg"))
apple.add_product(Product(100017, mac, "imac", "iMac เป็นคอมพิวเตอร์เดสก์ท็อปของ Apple ที่มีดีไซน์ที่สวยงามและบางเบา มาพร้อมกับหน้าจอ Retina ที่มีความละเอียดสูงและสีสันที่สมจริง มีหลายรุ่นให้เลือกตามความต้องการของผู้ใช้ ตั้งแต่ขนาดหน้าจอ 21.5 นิ้ว ถึง 27 นิ้ว และมีรุ่น iMac Pro ที่มีความสามารถและประสิทธิภาพที่สูงมาก เหมาะสำหรับงานที่ต้องการประสิทธิภาพสูง เช่น งานกราฟิก วิดีโอ หรือการตัดต่อเสียง เครื่อง iMac มีชิปที่มีประสิทธิภาพสูง ระบบเสียงที่ดี มีการออกแบบให้ใช้งานง่ายสะดวก มีพอร์ตที่ใช้ในการชาร์จและการเชื่อมต่ออุปกรณ์อื่น ๆ อีกมากมาย สำหรับผู้ที่ต้องการคอมพิวเตอร์เดสก์ท็อปที่มีความสามารถและประสิทธิภาพสูง iMac เป็นตัวเลือกที่ดีในระดับมืออาชีพ",49000,"3-10-2023",17,"https://media.studio7thailand.com/117820/iMac-M3-2-ports-Pink-1-square_medium.jpg"))
apple.add_product(Product(100018,airpods,"AirPods gen 2","AirPods รุ่น 2 คือหูฟังไร้สายที่ออกแบบและผลิตโดย Apple มีลักษณะเด่นคือการเชื่อมต่อไร้สายที่สะดวกสบาย และคุณภาพเสียงที่ดี มีฟังก์ชันการใช้งานที่สะดวก เช่น การเชื่อมต่อและการเปิดใช้งานอัตโนมัติเมื่อเอาออกจากกล่อง สามารถใช้งานกับ iPhone, iPad, Apple Watch และ Mac ได้อย่างไม่มีปัญหา มีเคสชาร์จที่มาพร้อมกับการชาร์จไร้สาย และสามารถชาร์จใหม่ได้โดยวางลงบนเคสชาร์จ มีเวอร์ชันที่มีเคสชาร์จแบบไวเลสเตอร์ ทำให้ชาร์จได้เร็วขึ้น สำหรับคนที่ต้องการหูฟังไร้สายที่มีคุณภาพเสียงดีและใช้งานง่าย AirPods รุ่น 2 เป็นตัวเลือกที่ดี",6000,"22-2-2021",45,"https://store.storeimages.cdn-apple.com/8756/as-images.apple.com/is/MV7N2?wid=1144&hei=1144&fmt=jpeg&qlt=95&.v=1551489688005&fbclid=IwAR1dHZU0oO946fTUPL3pEFL-quBOhdf_YlI--eSjG3H1YRz7tTRvz95m0ZU"))
apple.add_product(Product(100019,airpods,"AirPods gen 3","AirPods รุ่น 3 คือหูฟังไร้สายที่เปิดตัวโดย Apple ในปี 2021 มาพร้อมกับการออกแบบใหม่ที่เน้นความสวยงามและความสะดวกสบาย มีการปรับปรุงเสียงให้ดีขึ้น มีการเพิ่มดอกฟังเพื่อให้ความพอดีกับหูของผู้ใช้มากยิ่งขึ้น สามารถใช้งานกับอุปกรณ์ Apple ได้แบบไร้ข้อจำกัด มีการปรับปรุงให้ชาร์จไร้สายได้ด้วย MagSafe และมีเวอร์ชันที่มาพร้อมกับเคสชาร์จแบบไวเลสเตอร์ ทำให้ชาร์จได้เร็วขึ้น ระยะเวลาการใช้งานที่เพิ่มขึ้นเมื่อใช้งานร่วมกับเคสชาร์จยังเป็นจุดเด่นของ AirPods รุ่น 3 สำหรับผู้ที่ต้องการหูฟังไร้สายที่มีคุณภาพเสียงดีและมีความสะดวกสบายในการใช้งาน AirPods รุ่น 3 เป็นตัวเลือกที่น่าสนใจ",7500,"22-2-2021",45,"https://as-images.apple.com/is/MME73?wid=1144&hei=1144&fmt=jpeg&qlt=90&.v=1632861342000&fbclid=IwAR1TEDmomQn2CbtHKMWgdqTlYdAsqmmrJiyfpEtjliT0DpfGIxXkWe6N9WA&fp=8756&origindomain=as-images.apple.com"))
apple.add_product(Product(100020,accessories ,"Apple Pencil (1st gen)","Apple Pencil (รุ่นที่ 1) ให้คุณได้ขีดเขียนลายเส้นด้วยน้ำหนักที่ต่างกัน แรเงาบางๆ และสร้างสรรค์ลวดลายศิลปะที่สวยงามได้หลากหลายเหมือนใช้ดินสอทั่วไป แต่ให้ความแม่นยำที่ลึกลงระดับพิกเซล เหมาะสำหรับผู้ที่มีใจรักด้านศิลปะ นักวาดรูป วาดๆ ขีดๆ เขียนๆ ออกแบบสร้างสรรค์ลวดลายศิลปะที่สวยงามได้หลากหลาย คุณจึงใช้งานได้อย่างเป็นธรรมชาติไม่ต่างจากดินสอจริงๆด้วย Apple Pencil (รุ่นที่ 1)",3900,"22-2-2021",105,"https://media.studio7thailand.com/3905/Apple-Acc-Apple-Pencil-01-square_medium.jpg"))

#add promotion
apple.add_promotion(Promotion(10000001, "STD10" , "ลดราคานักศึกษา 10% ", "ราคานักศึกษา", 0.1))
apple.add_promotion(Promotion(10000002, "BIRTHDAY" , "วันเกิดลด 5% ", "ลดวันเกิด", 0.05))
apple.add_promotion(Promotion(10000003, "PROMO30" , "code promo 30% ", "ลด 30 %", 0.3))

# add help
apple.add_help(Help(101,"การให้บริการแบตเตอรี่","เราสามารถเปลี่ยนแบตเตอรี่ iPhone ของคุณโดยมีค่าธรรมเนียมได้ การรับประกันของเราไม่ครอบคลุมแบตเตอรี่ที่เสื่อมสภาพจากการใช้งานตามปกติผลิตภัณฑ์ของคุณจะเข้าเกณฑ์รับการเปลี่ยนแบตเตอรี่โดยไม่มีค่าใช้จ่ายเพิ่มเติมหากคุณมี AppleCare+ และแบตเตอรี่ในผลิตภัณฑ์ของคุณเก็บประจุได้น้อยกว่า 80% ของความจุเดิม"))
apple.add_help(Help(102,"การซ่อมหน้าจอ","เราให้บริการเปลี่ยนหน้าจอที่แตกร้าวโดยมีค่าธรรมเนียม ความเสียหายจากอุบัติเหตุจะไม่ได้รับความคุ้มครองภายใต้การรับประกันของ Appleการซ่อมหน้าจอมีสิทธิรับความคุ้มครองความเสียหายจากอุบัติเหตุอันเนื่องมาจากการใช้งานภายใต้ AppleCare+ ของคุณ"))
apple.add_help(Help(103,"การรับประกัน","การรับประกันแบบจำกัดของ Apple จะคุ้มครอง iPhone และอุปกรณ์เสริมแบรนด์ Apple ที่มาในกล่องพร้อมกับผลิตภัณฑ์ของคุณจากปัญหาด้านการผลิตเป็นเวลาหนึ่งปีนับจากวันที่คุณซื้อ อุปกรณ์เสริมแบรนด์ Apple ที่ซื้อแยกต่างหากจะได้รับการคุ้มครองโดยการรับประกันแบบจำกัดของ Apple สำหรับอุปกรณ์เสริม ซึ่งได้แก่ อะแดปเตอร์ สายสำรอง ที่ชาร์จไร้สาย หรือเคสการรับประกันของเราเป็นส่วนเพิ่มเติมนอกเหนือจากสิทธิตามกฎหมายคุ้มครองผู้บริโภคคุณอาจได้รับความคุ้มครองจาก AppleCare+ ทั้งนี้ขึ้นอยู่กับปัญหา ความคุ้มครองจะเป็นไปตามข้อกำหนดและเงื่อนไข รวมถึงค่าธรรมเนียม ความพร้อมใช้งานของคุณสมบัติและตัวเลือกอาจแตกต่างกันไปในแต่ละประเทศหรือภูมิภาคหากปัญหาของคุณไม่ได้รับความคุ้มครอง คุณจะต้องจ่ายค่าธรรมเนียม หากปัญหา iPod ของคุณไม่เข้าเกณฑ์การรับบริการ คุณอาจต้องชำระค่าเปลี่ยนทดแทนเต็มจำนวน"))

# Add product to Cart
# apple.add_product_to_cart(100002,10001)
# apple.add_product_to_cart(100002,10001)
# apple.add_product_to_cart(100001,10001)



#add promotion code to Cart
# apple.use_promotion_code(10001,"STD10")
# apple.use_promotion_code(10002,"PROMO30")

#calculate amount from cart
# print(siasa.search_cart_from_status().calculates_amount())
# print(pim.search_cart_from_status().calculates_amount())

# submit to make Order (ลองorderของ10001)
# order_id = apple.submit_to_make_order(customer_id , name, phone, address)

#payment (ลองorderของ10001 ที่หดสั่งไปเมื่อกี้)
# apple.payment(10001 , order_id ,1001)

#login 
# apple.login("siasa18037@gmail.com","Sia18037")
