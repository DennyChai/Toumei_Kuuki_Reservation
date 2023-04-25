import traceback
import Provider
import Service


def send_msg(msg=""):
    sys_log = traceback.format_exc()
    print("開發測試:", sys_log + msg)


def main():
    try:
        #! 先輸入好資訊
        book_info = {
            "date": "2023-05-10",  # 要訂的日期
            "time": "15:00",  # 要訂的時間
            "adults": "3",  # 大人人數
            "childrens": "0",  # 小孩人數
            "name": "王曉明",  # 訂位名子
            "contact_number": "0912345678",  # 手機號碼
            "sex": "男生",  # 輸入男生或女生
            "email": "123@gmail.com",  # 信箱
        }
        provider = Provider.Provider(send_msg)
        inputs = {
            "send_msg": send_msg,
            "provider": provider,
            "book_info": book_info,
        }
        Service.Service(inputs).flow_service()
    except:
        print(f"Main Error: {traceback.format_exc()}")


if __name__ == "__main__":
    main()
