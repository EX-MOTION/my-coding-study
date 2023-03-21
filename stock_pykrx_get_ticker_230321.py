# from pykrx import stock
# from pykrx import bond
# import pandas as pd
# import datetime

# # ticker 정보 가져오기

# tickers = stock.get_market_ticker_list("20230320", market="KOSPI")


# print(tickers)

# for ticker in stock.get_market_ticker_list("20230320", market="KOSPI"):
#         종목 = stock.get_market_ticker_name(ticker)
#         print(종목)

# # 데이터프레임 생성
# df = pd.DataFrame({'ticker': tickers})

# # 현재 시간에서 년, 월, 일 정보 추출
# now = datetime.datetime.now()
# date_string = now.strftime("%y%m%d")

# # CSV 파일로 저장
# filename = f'tickers_{date_string}.csv'
# df.to_csv(filename, index=False)


# from pykrx import stock
# import pandas as pd
# import datetime
# import os 


# # ticker 정보 가져오기
# tickers = stock.get_market_ticker_list("20230320", market="KOSPI")

# # 종목명 정보 가져오기
# names = [stock.get_market_ticker_name(ticker) for ticker in tickers]

# # 데이터프레임 생성
# df = pd.DataFrame({'ticker': [str(t) for t in tickers], '종목': names})

# # # CSV 파일로 저장
# # now = datetime.datetime.now()
# # date_string = now.strftime("%y%m%d")
# # filename = f"ticker_list_{date_string}.csv"
# # df.to_csv(filename, index=False, encoding='utf-8-sig')


# def save_to_csv(df, file_path):
#     # CSV 파일로 저장
#     now = datetime.datetime.now()
#     date_string = now.strftime("%y%m%d")
#     filename = f"ticker_list_{date_string}.csv"
#     df.to_csv(file_path + '\\' + filename, index=False, encoding='utf-8-sig')

# # 파일 경로
# file_path = 'C:\coding_230321\stock_230321'

# # 파일이 존재하는 경우, 파일 열기
# if os.path.exists(file_path):
#     print(f"{filename}이(가) 정상적으로 저장되었습니다!")
#     os.startfile(file_path)
# else:
#     print('파일을 찾을 수 없습니다.')
    
    
    
    
from pykrx import stock
import pandas as pd
import datetime
import os 

def save_to_csv(df, file_path):
    # CSV 파일로 저장
    now = datetime.datetime.now()
    date_string = now.strftime("%y%m%d")
    filename = f"ticker_list_{date_string}.csv"
    df.to_csv(file_path + '\\' + filename, index=False, encoding='utf-8-sig')
    return filename

# ticker 정보 가져오기
tickers = stock.get_market_ticker_list("20230320", market="KOSPI")

# 종목명 정보 가져오기
names = [stock.get_market_ticker_name(ticker) for ticker in tickers]

# 데이터프레임 생성
df = pd.DataFrame({'ticker': [str(t) for t in tickers], '종목': names})

# 파일 경로
file_path = 'C:\coding_230321\stock_230321'

# 파일이 존재하는 경우, 파일 저장
if os.path.exists(file_path):
    filename = save_to_csv(df, file_path)
    print(f"{filename}이(가) 정상적으로 저장되었습니다!")
    os.startfile(file_path + '\\' + filename)
else:
    print('파일을 찾을 수 없습니다.')