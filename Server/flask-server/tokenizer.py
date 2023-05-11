from eunjeon import Mecab
import os
from dotenv import load_dotenv

load_dotenv()

stopwords = ['라', '공동으로', '형식', '사람', '대로', '사람들', '생각', '좋아', '기준으로', '알겠는가', '동시에', '일', '의', '같은', '말하면', '오자마자', '누구', '하기는한데', '아', '할때', '그렇', '두', '어떠', '되', '아래', '여기', '아이야', '로써', '막론하고', '여', '한', '육', '하나', '이런', '저', '어쩔수', '천', '구', '요만한', '때문에', '시키', '지', '틀림없다', '물론', '알았어', '미치다', '다면', '근거', '하지만', '해', '비길수', '여러분', '왜냐하면', '응', '그리하여', '일곱', '많', '조차', '이러한', '인하여', '인', '기점', '우리들', '까닭으로', '잠깐', '그중에서', '이르다', '입각하여', '불구하고', '오히려', '까닭', '할수있어', '관해서', '아이고', '그러한즉', '윗', '비슷하다', '참', '하고', '아이쿠', '형식으로', '일반적으로', '할줄알다', '이천칠', '여전히', '관계없이', '김에', '되는', '모른다', '만약에', '조차도', '공동', '자기', '하기만', '그렇지만', '정도', '따라서', '보면', '타인', '영', '그러니', '서술', '예를', '하기보다는', '버금', '아무도', '서술한바와같이', '와', '이번', '몰', '그만', '지경', '서', '오로지', '라면', '두번째로', '기타', '정도에', '뿐이다', '뿐만', '다음으로', '전부', '하도다', '랏다', '않는다면', '만이', '이리하여', '뿐만아니라', '남', '전후', '도착하다', '누가', '예하면', '근거하여', '의거하여', '일때', '으로서', '아이', '아이구', '이와', '얼마', '인하', '면', '엉엉', '나', '만약', '대해', '하지', '어찌하여', '아무거나', '어떻게', '부터', '자', '이러', '붕붕', '이천팔', '잠시', '연관', '보다', '된다', '이렇게말하자면', '위에서', '듯하', '종합한것과같이', '놀라다', '기준', '그렇게', '삐걱', '이르', '을', '그럼에도', '한데', '여섯', '으로써', '예컨대', '휘익', '종합', '면서', '그러니까', '결론', '바', '그러면', '에서', '이로', '따름', '할', '려고', '소생', '못하다', '다시', '까닭에', '임에', '까지도', '않으면', '예', '둥둥', '에', '쾅쾅', '차라리', '첫', '하면', '가', '아울러', '구나', '이렇게되면', '아니', '도달', '요만', '만은', '앞에서', '집', '뿐', '으로', '많은', '있', '안된다', '고', '관해서는', '때문', '봐라', '그런', '위하', '도착', '도', '그러', '다른', '쉿', '어', '하는것도', '그러므로', '하구나', '은', '여부', '나머지는', '혼자', '줄은', '앞', '겸사겸사', '한다면', '만', '입각', '총적으로', '반드시', '들', '상대', '한켠으로는', '오', '는다면', '이유만으로', '어찌하든지', '해서', '관계', '이러이러하다', '든지', '놀라', '칠', '견지', '중에서', '그리고', '틀림없', '남들', '않기', '한항목', '았', '보는데서', '게', '어찌됏어', '어째서', '이만큼', '둘', '그치', '아니라면', '알', '관계가', '함으로써', '셋', '이러이러', '견지에서', '않다', '겠', '이것', '때', '로', '흐흐', '막론', '만일', '우에', '다섯', '아래윗', '쿵', '한하다', '자기집', '적', '마치', '보', '그런데', '못', '줄은모른다', '김', '단지', '이쪽', '운운', '하기에', '관련이', '어떻해', '어떻', '없', '하지마라', '그러나', '소인', '으면', '해야', '어느', '우선', '너', '몰랏다', '시각', '거나', '같다', '안', '지경이다', '생각이다', '오호', '정도의', '또한', '연관되다', '일반', '기', '무엇때문에', '결론을', '한마디', '네', '저희', '부류', '근거로', '어떤것들', '따라', '본대로', '들자면', '하지마', '봐', '본', '위', '상대적으로', '동안', '이렇게', '좋', '도달하다', '데', '이때', '아니다', '중', '말', '그리', '참나', '그', '이라면', '넷', '이천육', '도다', '심지어', '는가', '일단', '아무', '하는바', '전자', '되다', '요만큼', '무렵', '아니라', '같', '입장에서', '비길', '무슨', '하기', '것', '한하', '었', '와아', '외', '어떤', '의거', '다음', '령', '하다', '줄', '까지', '해야한다', '일것이다', '의해', '할수있다', '를', '않도록', '말하자면', '번', '어떠한', '따위', '듯하다', '낫', '그치지', '그렇지', '반대로', '다음에', '너희', '자면', '동시', '이럴', '하면서', '이럴정도로', '지만', '과', '마', '이', '중의하나', '몰라도', '미치', '팔', '이렇', '이와같다면', '에게', '입장', '따름이다', '없다', '총적', '아니면', '이렇구나', '같이', '윙윙', '달려', '오직', '그런즉', '여덟', '기에', '휴', '해서는', '수', '그들', '그만이다', '너희들', '시간', '것과', '위해서', '부류의', '무엇', '임', '야', '어쩔', '이르기까지', '그래서', '째', '항목', '결과', '후', '하느니', '아니었다면', '앞의것', '니', '관련', '도록', '위하여', '나머지', '삼', '하는', '외에도', '할수록', '낼', '지말고', '불구', '하든지', '아하', '켠', '있다', '사', '것들', '함', '자신', '않다면', '륙', '어떤것', '어쨋든', '다시말하면', '이유는', '이곳', '이유', '하려고하다', '어찌', '낫다', '자마자', '결과에', '느니', '탕탕', '한다', '기점으로', '첫번째로', '비슷', '반대', '아홉', '쓰여', '이천구', '다', '끼익', '하도록시키다', '는', '않', '어때', '우리', '하여금', '들면', '하', '됏', '편이', '의해되다']

# NNG: 일반 명사, NNP: 고유 명사, VV: 동사, VA: 형용사
def tokenizer(raw, pos=["NNG", "NNP", "VV", "VA"], stopword=stopwords):
    m = Mecab(dicpath=os.getenv("DICT_PATH"))
    return [word for word, tag in m.pos(raw) if len(word) > 1 and tag in pos and word not in stopword]