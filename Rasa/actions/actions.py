# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


from typing import Any, Text, Dict, List
import json
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher

class act_admision_hotline_web(Action):

    def name(self) -> Text:
        return "act_admision_hotline_web"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "postback",
            "title": "Cách tuyển sinh",
            "payload": "Cách tuyển sinh"
        }
        button1 = {
            "type": "postback",
            "title": "Gọi trực tiếp",
            "payload": "Gọi trực tiếp"
        }
        button2 = {
            "type": "web_url",
            "url": "http://dut.udn.vn/tuyensinh2022",
            "title": "Website tuyển sinh"
        }
        ret_text = "Mình có thể giúp gì cho bạn?"
        dispatcher.utter_message(text=ret_text, json_message=[button, button1, button2])

        return []

class more_infor_way1(Action):

    def name(self) -> Text:
        return "more_infor_way1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://thisinh.thithptquocgia.edu.vn/",
            "title": "Đăng ký online"
        }
        ret_text = "Đăng ký hồ sơ tại trường THPT hiện đang học\nLink đăng ký online theo hệ thống của Bộ Giáo dục và Đào tạo"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class way1(Action):

    def name(self) -> Text:
        return "way1"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Tổng hợp thông tin về cách xét tuyển bằng điểm thi Tốt nghiệp THPT",
                                image="https://scontent.fdad3-5.fna.fbcdn.net/v/t39.30808-6/240731119_4360627494022669_6290594941415128611_n.jpg?_nc_cat=106&ccb=1-5&_nc_sid=730e14&_nc_ohc=rI2mD_5VFYEAX-KfCl6&_nc_ht=scontent.fdad3-5.fna&oh=00_AT-vXjNW4I6C-zVy8clZ986z-tfaXqHEghMsdXKpoCwdag&oe=62043212")

        return []

class way2_front(Action):

    def name(self) -> Text:
        return "way2_front"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin về cách xét tuyển bằng điểm HB",
                                 image="https://tuyensinh.ute.udn.vn/Upload/2021/tuyensinh2021/dthi/dthi1.JPG")
        print('anh1')
        return []

class way2_back(Action):

    def name(self) -> Text:
        return "way2_back"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://tuyensinh.ute.udn.vn/Upload/2021/tuyensinh2021/dthi/dthi2.JPG")

        return []

class more_infor_way2(Action):

    def name(self) -> Text:
        return "more_infor_way2"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
           "type": "web_url",
            "url": "http://dut.udn.vn/tuyensinh2022",
            "title": "Thông tin tuyển sinh"
        }
        ret_text = "Cổng đăng ký xét tuyển online ĐH BK"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []        

class link_fanpage(Action):

    def name(self) -> Text:
        return "link_fanpage"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://www.facebook.com/bachkhoaDUT",
            "title": "Fanpage Đại học Bách khoa"
        }
        ret_text = "Link Fanpage chính thức về thông tin tuyển sinh ĐH DUT. Bạn có thể theo dõi fanpage để cập nhật những thông tin nhanh và chính xác nhất về tuyển sinh."
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class main_link(Action):

    def name(self) -> Text:
        return "main_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://www.dut.udn.vn/",
            "title": "Website ĐH Bách khoa"
        }
        ret_text = "Link website chính thức của trường"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class admission_link(Action):

    def name(self) -> Text:
        return "admission_link"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://dut.udn.vn/tuyensinh2022",
            "title": "Trang tuyển sinh"
        }
        ret_text = "Link trang tuyển sinh trường Đại học Bách khoa"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class more_informajor_2021mark(Action):

    def name(self) -> Text:
        return "more_informajor_2021mark"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://tuyensinh.ute.udn.vn/ChuyenMucs/Chi-tieu-tuyen-sinh_2.html",
            "title": "Thông tin chi tiết"
        }
        ret_text = "Thông tin về ngành và điểm năm 2021"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class link_register_online(Action):

    def name(self) -> Text:
        return "link_register_online"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "https://tuyensinh.ute.udn.vn/ChuyenMuc/Thong-tin-dang-ky-xet-tuyen-vao-Truong-Dai-hoc-Su-pham-Ky-thuat_19.html",
            "title": "Đăng ký online"
        }
        button1 = {
            "type": "web_url",
            "url": "https://www.facebook.com/bachkhoaDUT",
            "title": "Fanpage của trường"
        }
        ret_text = "Cổng đăng ký xét tuyển online ĐH Bách khoa.\nBạn cũng có thể theo dõi fanpage bên dưới để cập nhật thông tin liên tục."
        dispatcher.utter_message(text=ret_text, json_message=[button, button1])

        return []

class link_form_regis(Action):

    def name(self) -> Text:
        return "link_form_regis"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://ts.udn.vn/DHCD/Chinhquy/DHTbao/4569",
            "title": "Đăng ký xét tuyển"
        }
        ret_text = "Mẫu phiếu đăng ký xét tuyển ĐH DUT"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class act_admission_ways(Action):

    def name(self) -> Text:
        return "act_admission_ways"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        message = {
            "text": "Trường ĐH Bách khoa có 2 cách tuyển sinh\nCách 1: Điểm thi tốt nghiệp THPT\nCách 2: Điểm xét học bạ\nCách 3: Điểm thi đánh giá năng lực Đh quốc gia TPHCM năm 2020\nCách 4: Xét tuyển thẳng",
            "quick_replies": [
                {
                    "content_type": "text",
                    "title": "Điểm thi TN THPT",
                    "payload": "Điểm thi TN THPT",
                },
                {
                    "content_type": "text",
                    "title": "Xét tuyển thẳng",
                    "payload": "Xét tuyển thẳng",
                }
            ]
        }

        dispatcher.utter_message(json_message=message)

        return []

class act_contact_hotline(Action):

    def name(self) -> Text:
        return "act_contact_hotline"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "phone_number",
            "title": "0236 3842 308",
            "payload": "0236 3842 308"
        }
        button1 = {
            "type": "phone_number",
            "title": "0236 3842 308",
            "payload": "0236 3842 308"
        }
        ret_text = "Bạn có thể gọi điện thoại trực tiếp vào hai đầu số này"

        dispatcher.utter_message(text=ret_text, json_message=[button, button1])

        return[]

class to_roi(Action):

    def name(self) -> Text:
        return "to_roi"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin xét tuyển trường Đại học Bách khoa:",
                                 image="https://scontent.fhan5-10.fna.fbcdn.net/v/t1.6435-9/182805961_3977661562319266_6556439821610810169_n.jpg?_nc_cat=111&ccb=1-5&_nc_sid=8bfeb9&_nc_ohc=-zWGmbBtN-sAX-Zz5uC&_nc_ht=scontent.fhan5-10.fna&oh=00_AT9B5XCo2vBL1rJZINpfFgmXpCKRis5feU-NYSpB9Y659g&oe=622540A1")
        return []

class basic_infor_about_university(Action):

    def name(self) -> Text:
        return "basic_infor_about_university"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://www.dut.udn.vn",
            "title": "Trang chủ"
        }
        button1 = {
            "type": "web_url",
            "url": "http://dut.udn.vn/tuyensinh2022",
            "title": "Trang tuyển sinh"
        }
        button2 = {
            "type": "web_url",
            "url": "https://www.facebook.com/bachkhoaDUT",
            "title": "Fanpage tuyển sinh"
        }
        ret_text = "Bạn có thể xem những thông tin cơ bản về trường tại các website chính thức của trường:"
        dispatcher.utter_message(text=ret_text, json_message=[button, button1, button2])

        return []

class goodbye(Action):

    def name(self) -> Text:
        return "goodbye"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(image="https://media.tenor.com/images/e955f55bab6839ec724531e3bae3303c/tenor.gif")

        return []

class info_exam(Action):

    def name(self) -> Text:
        return "info_exam"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Thông tin về kỳ thi tốt nghiệp THPT 2021",
                                 image="https://hoigiasudanang.com/wp-content/uploads/2021/06/2.-Moc-Thoi-gian-1536x1087.jpg")

        return []

class action_fee(Action):

    def name(self) -> Text:
        return "action_fee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://sotaysinhvien.ute.udn.vn/ChuyenMucs/hoc-phi_52.html",
            "title": "Thông tin học phí"
        }
        ret_text = "ĐH Bách khoa là trường đại học công lập, học phí khoảng 5-6 triệu đồng/học kỳ. Bạn có thể tham khảo thêm thông tin về học phí tại đây"
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []

class act_have_domitory(Action):

    def name(self) -> Text:
        return "action_have_domitory"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://sotaysinhvien.ute.udn.vn/ChuyenMucs/Ky-tuc-xa_34.html",
            "title": "Các thông tin về KTX"
        }
        ret_text = "Trường có KTX ngay cạnh trường và dưới đây là thông tin về KTX của trường nha."
        dispatcher.utter_message(text=ret_text, json_message=[button])

        return []  

class action_student_support(Action):

    def name(self) -> Text:
        return "action_student_support"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        button = {
            "type": "web_url",
            "url": "http://sotaysinhvien.ute.udn.vn/ChuyenMucs/Hoc-bong_33.html",
            "title": "Thông tin học bổng"
        }
        button1 = {
            "type": "web_url",
            "url": "http://sotaysinhvien.ute.udn.vn/ChuyenMucs/Mien-giam-hoc-phi_37.html",
            "title": "Thông tin miễn giảm học phí"
        }
        ret_text = "ĐH DUT có nhiều chính sách hỗ trợ sinh viên có hoàn cảnh khó khăn và có nhiều loại học bổng khác nhau để hỗ trợ cho sinh viên khó khăn và sinh viên xuất sắc nha bạn."
        dispatcher.utter_message(text=ret_text, json_message=[button, button1])

        return []
