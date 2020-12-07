# _*_coding:utf-8 _*_

import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
import pandas as pd
from keras.models import Sequential, load_model
from keras.layers import LSTM, Dropout, Dense, Activation, CuDNNLSTM

font_location = "C:\\Windows\\Fonts\\malgun.ttf"
font_name = font_manager.FontProperties(fname=font_location).get_name()
matplotlib.rc('font', family=font_name)
matplotlib.rcParams['axes.unicode_minus'] = False

data_covid_sido = pd.read_excel('./Covid19SidoInfState.xlsx')
model_dir = './future_models'

dic_sido = {"인천": "IC", "강원": "KW", "경기": "KK", "경남": "KN", "경북": "KB", "광주": "GJ", "대구": "DG",
            "대전": "DG", "부산": "BS", "서울": "SU", "세종": "SJ", "울산": "US", "전남": "JN", "전북": "JB",
            "제주": "JJ", "충남": "CN", "충북": "CB"}

def model_create_and_run(name, cnt): #모델 정의, 데이터 전처리, 훈련
    seq_len = 50
    sequence_length = seq_len + 1

    result = []
    for index in range(len(cnt) - sequence_length):
        result.append(cnt[index: index + sequence_length])

    # 데이터 정규화
    normalized_data = []
    for window in result:
        normalized_window = [((float(p) / float(window[0])) - 1) for p in window]
        normalized_data.append(normalized_window)

    result = np.array(normalized_data)

    # train데이터와 test데이터 나누는 과정
    row = int(round(result.shape[0] * 0.9))
    train = result[:row, :]
    np.random.shuffle(train)

    x_train = train[:, :-1]
    x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
    y_train = train[:, -1]

    x_test = result[row:, :-1]
    x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1))
    y_test = result[row:, -1]

    # LSTM 모델 설계
    model = Sequential()
    model.add(CuDNNLSTM(50, return_sequences=True, input_shape=(50, 1)))
    model.add(CuDNNLSTM(64, return_sequences=False))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mse', optimizer='rmsprop')
    model.summary()

    # 모델 훈련
    model.fit(x_train, y_train,
              validation_data=(x_test, y_test),
              batch_size=10,
              epochs=50)

    # 가중치파일 저장
    model.save('{0}/{1}.h5'.format(model_dir, name))

def model_predict(name, cnt, hangeul_name):
    origin = cnt[0]

    normalized_data = []
    for window in cnt:
        normalized_window = [(float(window) / float(cnt[0]) - 1)]
        normalized_data.append(normalized_window)

    result = np.array(normalized_data)

    x_test = result[:]
    x_test = np.reshape(x_test, (1, x_test.shape[0], 1))

    model = load_model('{0}/{1}.h5'.format(model_dir, name))
    pred = model.predict(x_test)
    pred_result = (pred+1)*origin
    print("{0}'s result : ".format(hangeul_name), pred_result)
    return pred_result

# 시/도별로 데이터를 나눈 뒤 각각 배열에 저장하여 모델훈련
for list in dic_sido:   # 키값 하나씩 불러옴
    globals()['data_{}'.format(dic_sido[list])] = data_covid_sido.groupby('gubun').get_group(list)
    globals()['data_{}'.format(dic_sido[list])].drop(['seq', 'gubunCn', 'gubunEn', 'deathCnt', 'incDec', 'isolClearCnt', 'qurRate',
                                                      'isolIngCnt', 'overFlowCnt', 'localOccCnt', 'createDt', 'updateDt'],
                                                     axis='columns', inplace=True)  # 필요없는 열 제거
    globals()['data_{}'.format(dic_sido[list])] = globals()['data_{}'.format(dic_sido[list])].dropna()  # 결측데이터가 존재하는 행 제거
    defCnt = []
    # for cnt in globals()['data_{}'.format(dic_sido[list])]['defCnt']:
    #     defCnt.append(int(cnt))
    # model_create_and_run(dic_sido[list], defCnt)
    # print("{0}의 코로나 누적확진자 예측모델 훈련완료".format(list))

# 훈련된 모델을 이용하여 실제 값을 예측
# for list in dic_sido:
#     df_cnt_50 = globals()['data_{}'.format(dic_sido[list])]['defCnt'].tail(50)
#     cnt_50 = []
#     for cnt in df_cnt_50:
#         cnt_50.append(cnt)
#     model_predict(dic_sido[list], cnt_50, list)


# 더욱 먼 미래의 데이터 예측
for list in dic_sido:
    globals()['list_{}'.format(dic_sido[list])] = []
    defCnt = []
    for cnt in globals()['data_{}'.format(dic_sido[list])]['defCnt']:
        defCnt.append(int(cnt))
    df_cnt_50 = globals()['data_{}'.format(dic_sido[list])]['defCnt'].tail(50)
    cnt_50 = []
    for cnt in df_cnt_50:
        cnt_50.append(cnt)
    # 향후 12일간의 누적확진자수 예측
    for i in range(12):
        model_create_and_run(dic_sido[list], defCnt)
        pred_result = model_predict(dic_sido[list], cnt_50, list)
        defCnt.append(pred_result)
        # list_result.append(pred_result)
        globals()['list_{}'.format(dic_sido[list])].append(pred_result)
        del cnt_50[0]
        cnt_50.append(pred_result)
        print("{0}의 향후 {1}일 데이터 예측 완료".format(list, i)
    print("{0}의 12일치 데이터 예측 완료".format(list))

print(list_IC)
print(list_SU)