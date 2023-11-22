from flask import Flask, render_template
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import BytesIO
import base64

app = Flask(__name__)

# 사용할 데이터 파일 경로 지정
data_path = "C:\\Users\\218\\Desktop\\1122\\data\\compas_dataset.csv"

# 데이터 로드
df = pd.read_csv(data_path)

# 재범 여부와 성별 간의 상관관계 그래프 생성 함수
def plot_recid_gender():
    plt.figure(figsize=(12, 5))

    # 그래프 1: 재범 여부와 성별
    plt.subplot(1, 2, 1)
    sns.countplot(x='is_recid', hue='sex', data=df)
    plt.title('Correlation between Recidivism and Gender')
    plt.xlabel('Recidivism')
    plt.ylabel('Count')
    plt.legend(title='Gender', loc='upper right')

    # 그래프 2: 나이 그룹에 따른 재범 여부
    plt.subplot(1, 2, 2)
    sns.histplot(x='age', hue='is_recid', multiple='stack', data=df, bins=20, kde=True)
    plt.title('Correlation between Recidivism and Age Group')
    plt.xlabel('Age')
    plt.ylabel('Count')
    plt.legend(title='Recidivism', loc='upper right')

    plt.tight_layout()

# 웹페이지 라우트
@app.route('/')
def index():
    # 그래프 생성
    plot_recid_gender()

    # 그래프를 이미지로 변환
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plot_url = base64.b64encode(img.getvalue()).decode('utf8')

    # HTML 템플릿 렌더링
    return render_template('index.html', plot_url=plot_url)

if __name__ == '__main__':
    app.run(debug=True)
'''감사합니다'''
