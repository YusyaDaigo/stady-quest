import { CATEGORIES } from "./categories";

export const required97Questions = [

  
  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 1,

    question:
      "希薄溶液の束一的性質でないのはどれか。1つ選べ。",

    choices: [
    "蒸気圧降下",
    "凝固点降下",
    "沸点上昇",
    "表面張力低下",
    "浸透圧"
    ],

    answer: 3,

    explanation:
      "希薄溶液の束一的性質とは、溶質の種類ではなく、溶液中の粒子数に主に依存して現れる性質です。代表例は、蒸気圧降下、凝固点降下、沸点上昇、浸透圧です。したがって、1、2、3、5はいずれも束一的性質に含まれます。一方、表面張力低下は界面での分子の性質や溶質の種類、例えば界面活性剤の作用などに大きく関係するため、束一的性質とは扱いません。よって正答は4です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 2,

    question:
      "ある化合物の25℃における分解が、半減期3日の一次反応に従うとする。この化合物100 mgを6日間、25℃で保存したときの残存量として、正しいのはどれか。1つ選べ。",

    choices: [
    "17 mg",
    "25 mg",
    "33 mg",
    "50 mg",
    "75 mg"
    ],

    answer: 1,

    explanation:
      "一次反応では、半減期ごとに量が1/2になります。半減期が3日なので、6日間は半減期2回分です。したがって、100 mg → 50 mg → 25 mgとなり、残存量は25 mgです。よって正答は2です。1の17 mgや3の33 mgは半減期からの単純な1/2減少に合いません。4の50 mgは3日後の量、5の75 mgは一次反応の半減期の考え方とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 3,

    question:
      "Ag2CrO4の溶解度がS（mol/L）であるとき、溶解度積（Ksp）と溶解度の関係式として、正しいのはどれか。1つ選べ。",

    choices: [
    "Ksp = 2S",
    "Ksp = S^2",
    "Ksp = 2S^2",
    "Ksp = 2S^3",
    "Ksp = 4S^3"
    ],

    answer: 4,

    explanation:
      "Ag2CrO4は水中で Ag2CrO4 ⇄ 2Ag+ ＋ CrO4^2− のように溶けます。溶解度をS mol/Lとすると、[CrO4^2−]＝S、[Ag+]＝2Sです。したがって、溶解度積は Ksp＝[Ag+]^2[CrO4^2−]＝(2S)^2×S＝4S^3 となり、正答は5です。1〜4は、Ag+が2倍生成することや、Kspで[Ag+]を2乗する点を正しく反映できていません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 4,

    question:
      "電気泳動において、イオン性物質の移動速度と比例するのはどれか。1つ選べ。",

    choices: [
    "イオン性物質の半径",
    "イオン性物質の電荷",
    "溶液の粘度",
    "溶液のpH",
    "電極間の距離"
    ],

    answer: 1,

    explanation:
      "電気泳動での移動速度は、電場中で受ける力に関係し、イオン性物質の電荷が大きいほど速く移動しやすくなります。式では概ね、移動速度は電荷に比例し、粒子の半径や溶液の粘度には反比例します。したがって正答は2です。1の半径は大きいほど抵抗が増えるため速くなるとはいえません。3の粘度も高いほど移動しにくくなります。4のpHは物質の電離状態を変えて影響することはありますが、移動速度に直接比例する因子ではありません。5の電極間距離は電場の強さに関係しますが、距離そのものに比例するわけではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 5,

    question:
      "紫外可視吸光度測定法において、吸光度と比例するのはどれか。1つ選べ。",

    choices: [
    "透過度",
    "透過率",
    "試料の濃度",
    "比吸光度の対数",
    "モル吸光係数の対数"
    ],

    answer: 2,

    explanation:
      "紫外可視吸光度測定法では、ランベルト・ベールの法則 A＝εcl により、吸光度 A は試料の濃度 c に比例します。したがって正答は「試料の濃度」です。透過率や透過度は吸光度と対数関係にあり、A＝−logT で表されるため比例しません。比吸光度やモル吸光係数は物質に固有の値として扱われ、これらの対数が吸光度と比例するわけではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 6,
    hasImage: true,
    image: "/pharmacy/97/required/q6.png",

    question:
      "以下の反応はどれに分類されるか。1つ選べ。",

    choices: [
    "置換反応",
    "脱離反応",
    "付加反応",
    "転位反応"
    ],

    answer: 1,

    explanation:
      "この反応は、分子内から原子や原子団（例：Hとハロゲン、HとOHなど）が抜けて、新たに二重結合などが形成されるタイプと考えられるため、脱離反応に分類されます。国家試験では「小分子が抜ける」「不飽和結合ができる」が脱離反応の目印です。置換反応はある原子団が別の原子団に入れ替わる反応、付加反応は二重結合などに原子や原子団が加わる反応、転位反応は分子内で原子団の位置が移動する反応なので、本問の分類とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 7,
    hasImage: true,
    image: "/pharmacy/97/required/q7.png",

    question:
      "ベンゾジアゼピン骨格を持つのはどれか。1つ選べ。",

    choices: [
    "構造式1",
    "構造式2",
    "構造式3",
    "構造式4",
    "構造式5"
    ],

    answer: 2,

    explanation:
      "ベンゾジアゼピン骨格は、ベンゼン環に7員環のジアゼピン環が縮合し、その環内に窒素原子を2個もつ構造が特徴です。構造式3はこの特徴を満たしているため、ベンゾジアゼピン骨格をもつと判断できます。ほかの構造式は、ベンゼン環とジアゼピン環の縮合構造がない、または7員環中の窒素原子数などが一致しないため該当しません。国家試験では「ベンゼン環＋7員環＋Nが2個」を目印に確認するとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 8,
    hasImage: true,
    image: "/pharmacy/97/required/q8.png",

    question:
      "以下の化合物のうち、光学活性を示さないのはどれか。1つ選べ。",

    choices: [
    "フィッシャー投影式：上COOH、下COOH、上側不斉炭素は左H・右OH、下側不斉炭素は左OH・右H",
    "フィッシャー投影式：上COOH、下COOH、上側不斉炭素は左OH・右H、下側不斉炭素は左H・右OH",
    "フィッシャー投影式：上COOH、下COOH、上側不斉炭素は左H・右OH、下側不斉炭素は左H・右OH",
    "フィッシャー投影式：上COOH、下COOH、上側不斉炭素は左H・右H、下側不斉炭素は左H・右OH"
    ],

    answer: 2,

    explanation:
      "この問題は、フィッシャー投影式からメソ体を見抜く問題です。上下に同じ COOH をもつ酒石酸型の構造では、2つの不斉炭素の配置が互いに逆（R,S）になると分子内に対称性をもち、光学活性を示しません。選択肢3は上下の不斉炭素が R,S の関係となるメソ体に相当するため、正答です。選択肢1と2はそれぞれ R,R/S,S の関係で互いに鏡像異性体となり、通常は光学活性を示します。選択肢4は一方が H を2つもつため不斉炭素ではありませんが、もう一方に不斉中心が残る構造として考えられ、光学活性を示し得ます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 9,

    question:
      "窒素の酸化数が最も大きいのはどれか。1つ選べ。",

    choices: [
    "一酸化二窒素",
    "一酸化窒素",
    "二酸化窒素",
    "亜硝酸",
    "硝酸"
    ],

    answer: 4,

    explanation:
      "酸化数は、Hを＋1、Oを－2として全体の電荷が0になるように考えます。硝酸 HNO3 では、＋1＋N＋3×(－2)=0 より、N＝＋5となり最も大きいです。一酸化二窒素 N2O のNは平均＋1、一酸化窒素 NO は＋2、二酸化窒素 NO2 は＋4、亜硝酸 HNO2 は＋3です。したがって、窒素の酸化数が最も大きいのは硝酸です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 10,
    hasImage: true,
    image: "/pharmacy/97/required/q10.png",

    question:
      "ヒドロキシ基（OH基）を持つ3つの化合物について、酸性の強いものから弱いものへ並べた正しい順番はどれか。1つ選べ。A：ベンゼン環-CH2OH、B：ベンゼン環-COOH、C：ベンゼン環-OH",

    choices: [
    "A > B > C",
    "A > C > B",
    "B > A > C",
    "B > C > A",
    "C > A > B",
    "C > B > A"
    ],

    answer: 3,

    explanation:
      "酸性の強さは、H⁺が外れた後の共役塩基がどれだけ安定かで考える。B（安息香酸）はカルボキシラートイオンが共鳴で強く安定化されるため最も酸性が強い。C（フェノール）はフェノキシドイオンがベンゼン環と共鳴できるため、通常のアルコールよりは酸性が強い。A（ベンジルアルコール）はOHの隣にCH₂があり、アルコキシドイオンがベンゼン環と直接共鳴できないため最も酸性が弱い。したがって、強い順に B ＞ C ＞ A となる。他の選択肢は、AをCより強い、またはCをBより強いとしている点が不適切。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 11,

    question:
      "ホルモンとその作用との対応のうち、誤っているのはどれか。1つ選べ。",

    choices: [
    "ガストリン — 胃酸分泌の抑制",
    "セクレチン — HCO3−を多く含む膵液の分泌促進",
    "カルシトニン — 血中Ca2+の減少",
    "インスリン — 血中グルコースの減少",
    "アルドステロン — 腎臓におけるNa+及びCl−の再吸収促進"
    ],

    answer: 0,

    explanation:
      "誤っているのは1です。ガストリンは胃のG細胞から分泌され、胃酸分泌を促進するホルモンとして押さえます。「抑制」ではありません。2のセクレチンは、十二指腸に酸性内容物が入ると分泌され、HCO3−を多く含む膵液分泌を促進します。3のカルシトニンは血中Ca2+を低下させます。4のインスリンは血中グルコースを低下させます。5のアルドステロンは腎臓でNa+再吸収を促進し、Cl−もそれに伴って再吸収されやすくなるため正しい対応です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 12,

    question:
      "原核生物はどれか。1つ選べ。",

    choices: [
    "赤痢アメーバ",
    "黄色ブドウ球菌",
    "インフルエンザウイルス",
    "皮膚糸状菌",
    "マラリア原虫"
    ],

    answer: 1,

    explanation:
      "原核生物は、核膜で囲まれた核をもたない生物で、代表例は細菌です。黄色ブドウ球菌は細菌なので、原核生物に分類されます。赤痢アメーバやマラリア原虫は原虫、皮膚糸状菌は真菌で、いずれも真核生物です。インフルエンザウイルスは細胞構造をもたないため、原核生物にも真核生物にも分類されません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 13,

    question:
      "DNAの構造について、正しいのはどれか。1つ選べ。",

    choices: [
    "構成塩基は、アデニン、グアニン、シトシン及びウラシルである。",
    "アデニンと対をなす塩基はグアニンである。",
    "構成糖としてD-リボースを含む。",
    "ヒトの染色体DNAは環状構造をとる。",
    "生理的条件下では主に右巻きらせん構造をとる。"
    ],

    answer: 4,

    explanation:
      "DNAは生理的条件下で主にB型DNAとして存在し、右巻き二重らせん構造をとるため、5が正しいです。1：DNAの塩基はアデニン、グアニン、シトシン、チミンであり、ウラシルは主にRNAに含まれます。2：アデニンはチミンと相補的に塩基対を作り、グアニンはシトシンと対を作ります。3：DNAの糖はD-2-デオキシリボースで、D-リボースはRNAの構成糖です。4：ヒトの染色体DNAは基本的に線状であり、環状DNAは細菌やミトコンドリアDNAなどでみられます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 14,

    question:
      "セロトニンの生合成の前駆体はどれか。1つ選べ。",

    choices: [
    "アラキドン酸",
    "L-チロシン",
    "コリン",
    "L-トリプトファン",
    "L-ヒスチジン"
    ],

    answer: 3,

    explanation:
      "セロトニンは、必須アミノ酸であるL-トリプトファンから合成されます。L-トリプトファンが水酸化・脱炭酸されてセロトニンになるため、正答は4です。アラキドン酸はプロスタグランジンなどの前駆体、L-チロシンはドパミン・ノルアドレナリンなどカテコールアミンの前駆体、コリンはアセチルコリンの前駆体、L-ヒスチジンはヒスタミンの前駆体として押さえておくと整理しやすいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 15,

    question:
      "抗原抗体反応を利用した測定法でないのはどれか。1つ選べ。",

    choices: [
    "ラジオイムノアッセイ（RIA）によるホルモンの定量",
    "酵素免疫測定法（ELISA）によるサイトカインの定量",
    "赤血球凝集反応による血液型判定",
    "ポリメラーゼ連鎖反応（PCR）法によるDNAの検出",
    "ウエスタンブロット法によるタンパク質の検出"
    ],

    answer: 3,

    explanation:
      "正答は4です。PCR法は、DNAを特異的に増幅して検出する方法であり、抗原抗体反応を利用する測定法ではありません。1のRIAは放射性標識を用いた免疫測定法、2のELISAは酵素標識抗体を用いる免疫測定法です。3の赤血球凝集反応は、赤血球表面抗原と抗体の反応を利用します。5のウエスタンブロット法も、目的タンパク質を抗体で検出するため抗原抗体反応を利用します。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 16,

    question:
      "過剰に摂取すると、悪心、嘔吐、頭痛などを主症状とする急性中毒を起こすのはどれか。1つ選べ。",

    choices: [
    "ビタミンA",
    "ビタミンB12",
    "ビタミンD",
    "ビタミンE",
    "ビタミンK"
    ],

    answer: 0,

    explanation:
      "過剰摂取により、悪心・嘔吐・頭痛などを主症状とする急性中毒を起こしやすいのはビタミンAです。ビタミンAは脂溶性で体内に蓄積しやすく、大量摂取で頭蓋内圧亢進に関連した症状などがみられることがあります。ビタミンB12は水溶性で過剰症は比較的起こりにくいです。ビタミンD過剰では高カルシウム血症による食欲不振、腎障害などが問題になります。ビタミンE過剰では出血傾向、ビタミンKは通常の摂取では過剰症は起こりにくいとされます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 17,

    question:
      "2005年以降の年齢階級別死亡率において、20歳～29歳の死因の第1位はどれか。1つ選べ。",

    choices: [
    "悪性新生物",
    "心疾患",
    "脳血管疾患",
    "自殺",
    "不慮の事故"
    ],

    answer: 3,

    explanation:
      "2005年以降の年齢階級別死亡率では、20〜29歳の死因第1位は「自殺」とされます。若年層では悪性新生物や心疾患、脳血管疾患などの生活習慣病・加齢に関連する死因よりも、自殺の割合が高い点が特徴です。不慮の事故も若年層で重要な死因ですが、第1位として問われる場合は自殺を選びます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 18,

    question:
      "疾病の二次予防に該当するのはどれか。1つ選べ。",

    choices: [
    "健康教室",
    "予防接種",
    "集団検診",
    "在宅機能訓練",
    "職場環境の改善"
    ],

    answer: 2,

    explanation:
      "二次予防は、疾病を早期に発見し、早期治療につなげて重症化を防ぐ段階です。集団検診は、症状がない人も含めて病気を早く見つける目的で行われるため、二次予防に該当します。健康教室、予防接種、職場環境の改善は、病気の発生を防ぐ一次予防に分類されます。在宅機能訓練は、病後の機能回復や社会復帰を目指す三次予防にあたります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 19,

    question:
      "VDT（visual display terminal）作業従事者に多くみられる健康障害はどれか。1つ選べ。",

    choices: [
    "熱中症",
    "職業性レイノー症候群",
    "頸肩腕症候群",
    "難聴",
    "潜函病"
    ],

    answer: 2,

    explanation:
      "VDT作業は、パソコン画面を見ながら長時間同じ姿勢でキーボードやマウス操作を行う作業です。そのため、首・肩・腕に負担がかかりやすく、肩こり、腕のだるさ、しびれなどを伴う頸肩腕症候群が多くみられます。1の熱中症は高温環境、2の職業性レイノー症候群は振動工具の使用、4の難聴は騒音作業、5の潜函病は高気圧環境下の作業で問題となる健康障害です。したがって、VDT作業に関連が深いのは3です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 20,

    question:
      "異物代謝において、メルカプツール酸生成に関与する酵素はどれか。1つ選べ。",

    choices: [
    "カテコール O-メチルトランスフェラーゼ",
    "グルタチオン S-トランスフェラーゼ",
    "スルホトランスフェラーゼ",
    "ロダネーゼ",
    "UDP-グルクロノシルトランスフェラーゼ"
    ],

    answer: 1,

    explanation:
      "メルカプツール酸は、異物がまずグルタチオン抱合を受け、その後代謝されてN-アセチルシステイン抱合体となったものです。この最初のグルタチオン抱合に関与する代表的酵素がグルタチオン S-トランスフェラーゼなので、正答は2です。1のカテコールO-メチルトランスフェラーゼはカテコール構造のメチル化、3のスルホトランスフェラーゼは硫酸抱合、4のロダネーゼはシアン化物の解毒、5のUDP-グルクロノシルトランスフェラーゼはグルクロン酸抱合に関与します。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 21,

    question:
      "癌抑制遺伝子はどれか。1つ選べ。",

    choices: [
    "src",
    "fos",
    "kit",
    "H-ras",
    "p53"
    ],

    answer: 4,

    explanation:
      "癌抑制遺伝子は、細胞増殖を抑えたり、DNA損傷時に細胞周期を停止・アポトーシスを誘導したりして、がん化を防ぐ遺伝子です。p53は代表的な癌抑制遺伝子であり、変異により多くのがんで機能低下がみられます。したがって正答は5です。src、fos、kit、H-rasはいずれも細胞増殖シグナルに関わる癌原遺伝子（プロトオンコジーン）として覚えるとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 22,

    question:
      "メタロチオネインの構成アミノ酸のうち、約1/3を占めるのはどれか。1つ選べ。",

    choices: [
    "グリシン",
    "メチオニン",
    "トリプトファン",
    "システイン",
    "アルギニン"
    ],

    answer: 3,

    explanation:
      "メタロチオネインは、亜鉛やカドミウムなどの金属イオンと結合する低分子タンパク質です。構成アミノ酸の約1/3をシステインが占め、システインのチオール基（−SH）が金属イオンとの結合に関与します。したがって正答は4です。グリシン、メチオニン、トリプトファン、アルギニンはメタロチオネインの主要な特徴である高いシステイン含量とは一致しません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 23,

    question:
      "ジエチル-p-フェニレンジアミン（DPD）法による水道水中の残留塩素の測定において、DPDと速やかに反応して赤色を呈するのはどれか。1つ選べ。",

    choices: [
    "HClO",
    "NH₂Cl",
    "NHCl₂",
    "NCl₃",
    "CHCl₃"
    ],

    answer: 0,

    explanation:
      "DPD法では、遊離残留塩素がDPDを酸化して速やかに赤色を呈します。水道水中の遊離残留塩素の主な形は次亜塩素酸（HClO）や次亜塩素酸イオンであるため、正答は1です。NH₂Cl、NHCl₂、NCl₃はクロラミン類で、結合残留塩素に分類され、DPDとの反応は遊離残留塩素ほど速やかではありません。CHCl₃はクロロホルムで、消毒副生成物の一つであり、残留塩素としてDPDを赤色にするものではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 24,

    question:
      "大気汚染に係る環境基準の項目として、設定されていないのはどれか。1つ選べ。",

    choices: [
    "一酸化炭素",
    "二酸化硫黄",
    "浮遊粒子状物質",
    "二酸化窒素",
    "二酸化炭素"
    ],

    answer: 4,

    explanation:
      "大気汚染に係る環境基準は、人の健康を保護する目的で設定されており、代表的な項目に一酸化炭素、二酸化硫黄、浮遊粒子状物質、二酸化窒素などがあります。一方、二酸化炭素は地球温暖化に関係する温室効果ガスですが、一般的な大気汚染に係る環境基準の項目としては設定されていません。したがって、正答は5です。1〜4はいずれも大気汚染に係る環境基準の項目として扱われます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 25,

    question:
      "医療機関より廃棄される“血液の付着したガーゼ（未滅菌）”が該当する区分として、最も適切なのはどれか。1つ選べ。",

    choices: [
    "産業廃棄物",
    "特別管理産業廃棄物",
    "事業系一般廃棄物",
    "家庭系一般廃棄物",
    "特別管理一般廃棄物"
    ],

    answer: 4,

    explanation:
      "血液の付着した未滅菌ガーゼは、感染のおそれがある「感染性廃棄物」と考える。ガーゼは医療機関から出ても、産業廃棄物の品目に該当しにくいため、一般廃棄物に分類され、感染性があるので「特別管理一般廃棄物」となる。1の産業廃棄物は感染性への特別な管理を含まない。2の特別管理産業廃棄物は、感染性のある産業廃棄物（例：血液そのもの、注射針など）で考える。3は感染性がない事業系一般廃棄物、4は家庭から出る一般廃棄物であり不適切。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 26,

    question:
      "薬物の安全域の計算式はどれか。1つ選べ。",

    choices: [
    "LD50 − ED50",
    "ED50 − LD50",
    "LD50 × ED50",
    "ED50 ÷ LD50",
    "LD50 ÷ ED50"
    ],

    answer: 4,

    explanation:
      "薬物の安全域（治療係数）は、一般に LD50 ÷ ED50 で表されます。LD50は50％の個体が死亡する量、ED50は50％の個体に有効作用を示す量であり、この値が大きいほど有効量と致死量の差が大きく、比較的安全性が高いと考えられます。したがって正答は5です。1や2のような差、3の積、4のED50÷LD50は安全域の計算式としては用いません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 27,
    hasImage: true,
    image: "/pharmacy/97/required/q27.png",

    question:
      "競合的アンタゴニストを加えることによりアゴニストの用量-反応曲線が矢印のように変化した。正しいのはどれか。1つ選べ。",

    choices: [
    "1：最大反応は変化せず、用量-反応曲線が右方へ移動する図",
    "2：最大反応は変化せず、用量-反応曲線が左方へ移動する図",
    "3：最大反応が低下する図",
    "4：最大反応が増加する図",
    "5：最大反応が低下し、用量-反応曲線が右方へ移動する図"
    ],

    answer: 0,

    explanation:
      "競合的アンタゴニストは、アゴニストと同じ受容体部位に可逆的に競合して結合します。そのため、アゴニスト濃度を高くすれば作用を打ち消せるため、最大反応（Emax）は基本的に変化しません。一方、同じ反応を得るにはより多くのアゴニストが必要となるので、用量-反応曲線は右方へ移動します。したがって正答は1です。2の左方移動はアゴニストの作用増強を示す変化です。3や5のような最大反応の低下は、非競合的アンタゴニストや不可逆的拮抗でみられやすい変化です。4の最大反応増加も競合的アンタゴニストの典型ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 28,

    question:
      "アトロピンの薬理作用として、正しいのはどれか。1つ選べ。",

    choices: [
    "瞳孔括約筋収縮",
    "唾液分泌抑制",
    "消化管運動促進",
    "胃酸分泌促進",
    "子宮平滑筋収縮"
    ],

    answer: 1,

    explanation:
      "アトロピンはムスカリン受容体を遮断する抗コリン薬です。副交感神経作用を抑えるため、唾液腺からの分泌が低下し、口渇が起こりやすくなります。したがって、正答は2です。1の瞳孔括約筋収縮は副交感神経刺激で起こる作用で、アトロピンでは散瞳がみられます。3の消化管運動促進、4の胃酸分泌促進も副交感神経作用であり、アトロピンではむしろ抑制傾向です。5の子宮平滑筋収縮はアトロピンの代表的作用ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 29,

    question:
      "終板の持続的脱分極により骨格筋弛緩作用を示すのはどれか。1つ選べ。",

    choices: [
    "パンクロニウム",
    "ベクロニウム",
    "ダントロレン",
    "スキサメトニウム",
    "A型ボツリヌス毒素"
    ],

    answer: 3,

    explanation:
      "終板の持続的脱分極により筋弛緩を起こす代表薬はスキサメトニウムです。ニコチン性アセチルコリン受容体を刺激して一過性に脱分極させ、その状態が持続することで再興奮できなくなり、骨格筋弛緩を示します。パンクロニウム、ベクロニウムは非脱分極性筋弛緩薬で、受容体を競合的に遮断します。ダントロレンは筋小胞体からのCa2＋遊離を抑制します。A型ボツリヌス毒素はアセチルコリン放出を抑制するため、作用機序が異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 30,

    question:
      "フェンタニルの鎮痛作用発現に関わる作用点はどれか。1つ選べ。",

    choices: [
    "GABA_A受容体",
    "グルタミン酸NMDA受容体",
    "オピオイドμ受容体",
    "ドパミンD_2受容体",
    "電位依存性Na^+チャネル"
    ],

    answer: 2,

    explanation:
      "フェンタニルは強力なオピオイド鎮痛薬で、主にオピオイドμ受容体を刺激することで鎮痛作用を示します。μ受容体の活性化により痛みの伝達が抑えられるため、正答は3です。GABA_A受容体はベンゾジアゼピン系など、NMDA受容体はケタミンなど、ドパミンD2受容体は抗精神病薬などの作用点として重要です。電位依存性Na+チャネルは局所麻酔薬などが関与します。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 31,

    question:
      "GABAトランスアミナーゼ阻害作用を有する抗てんかん薬はどれか。1つ選べ。",

    choices: [
    "カルバマゼピン",
    "フェニトイン",
    "ジアゼパム",
    "エトスクシミド",
    "バルプロ酸"
    ],

    answer: 4,

    explanation:
      "バルプロ酸は、GABAトランスアミナーゼを阻害してGABAの分解を抑え、脳内GABA濃度を高める作用をもつ抗てんかん薬です。また、Na＋チャネル抑制作用なども関与します。カルバマゼピンとフェニトインは主に電位依存性Na＋チャネルを抑制します。ジアゼパムはベンゾジアゼピン系でGABAA受容体の作用を増強します。エトスクシミドは主にT型Ca2＋チャネルを抑制し、欠神発作に用いられます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 32,

    question:
      "ドブタミンの強心作用発現に関わる作用点はどれか。1つ選べ。",

    choices: [
    "アドレナリンβ1受容体",
    "アセチルコリンM2受容体",
    "アデニル酸シクラーゼ",
    "プロテインキナーゼA",
    "ホスホジエステラーゼ"
    ],

    answer: 0,

    explanation:
      "ドブタミンは主に心筋のアドレナリンβ1受容体を刺激し、心収縮力を高める強心薬です。β1受容体刺激により、結果としてアデニル酸シクラーゼ活性化、cAMP増加、プロテインキナーゼA活性化が起こりますが、薬物が直接作用する主な作用点としてはβ1受容体を選びます。M2受容体は副交感神経系で心機能を抑える方向に働きます。ホスホジエステラーゼはcAMP分解酵素で、阻害薬（ミルリノンなど）の作用点です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 33,

    question:
      "L型Ca2+チャネルを遮断することにより冠動脈拡張作用を示すのはどれか。1つ選べ。",

    choices: [
    "ニトログリセリン",
    "ジピリダモール",
    "アルプレノロール",
    "ジルチアゼム",
    "硝酸イソソルビド"
    ],

    answer: 3,

    explanation:
      "ジルチアゼムはCa拮抗薬で、L型Ca2+チャネルを遮断し、血管平滑筋へのCa2+流入を抑えることで冠動脈を拡張します。したがって正答は4です。ニトログリセリンや硝酸イソソルビドは硝酸薬で、NOを介して血管を拡張します。ジピリダモールはアデノシン増加などにより冠血管拡張作用を示します。アルプレノロールはβ遮断薬であり、L型Ca2+チャネル遮断薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 34,

    question:
      "Na+-K+-2Cl−共輸送系の抑制により利尿作用を示すのはどれか。1つ選べ。",

    choices: [
    "チアジド系利尿薬",
    "ループ利尿薬",
    "カリウム保持性利尿薬",
    "浸透圧利尿薬",
    "炭酸脱水酵素阻害薬"
    ],

    answer: 1,

    explanation:
      "Na+-K+-2Cl−共輸送系（NKCC2）は、ヘンレ係蹄上行脚太い部に存在します。これを抑制してNaClの再吸収を阻害し、強い利尿作用を示す代表がループ利尿薬（フロセミドなど）です。チアジド系利尿薬は遠位尿細管のNa+-Cl−共輸送系を阻害します。カリウム保持性利尿薬は集合管でアルドステロン作用やNa+チャネルを抑えます。浸透圧利尿薬は尿細管内の浸透圧を高めて水の再吸収を抑制します。炭酸脱水酵素阻害薬は近位尿細管でHCO3−再吸収を抑える薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 35,

    question:
      "ムコタンパク質のジスルフィド結合（−S−S−）を切断して低分子化し、喀痰の粘度を低下させるのはどれか。1つ選べ。",

    choices: [
    "アンブロキソール",
    "ジヒドロコデイン",
    "アセチルシステイン",
    "ジモルホラミン",
    "ノスカピン"
    ],

    answer: 2,

    explanation:
      "アセチルシステインは、喀痰中のムコタンパク質のジスルフィド結合（−S−S−）を切断し、低分子化することで痰の粘度を下げる去痰薬です。したがって正答は3です。アンブロキソールは肺サーファクタント分泌促進などにより痰を出しやすくする薬で、S−S結合を切断する作用ではありません。ジヒドロコデイン、ノスカピンは鎮咳薬、ジモルホラミンは呼吸興奮薬であり、喀痰の粘度を低下させる薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 36,

    question:
      "ヒスタミンH₂受容体遮断作用を示すのはどれか。1つ選べ。",

    choices: [
    "メトクロプラミド",
    "ファモチジン",
    "モサプリド",
    "スルピリド",
    "プログルミド"
    ],

    answer: 1,

    explanation:
      "ヒスタミンH₂受容体遮断薬は、胃壁細胞のH₂受容体を遮断して胃酸分泌を抑える薬です。ファモチジンは代表的なH₂受容体遮断薬であり、正答です。メトクロプラミドはD₂受容体遮断作用などにより消化管運動を促進し、制吐作用も示します。モサプリドは5-HT₄受容体刺激薬で、消化管運動改善薬です。スルピリドはD₂受容体遮断薬で、精神神経系や消化器症状に用いられます。プログルミドはガストリン受容体遮断作用をもつ薬として整理されます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 37,

    question:
      "甲状腺ホルモン産生阻害作用を示すのはどれか。1つ選べ。",

    choices: [
    "チアマゾール",
    "オキシトシン",
    "プロチレリン",
    "クロミフェン",
    "ソマトレリン"
    ],

    answer: 0,

    explanation:
      "チアマゾールは抗甲状腺薬で、甲状腺ペルオキシダーゼを阻害し、ヨウ素の有機化やカップリング反応を抑えることで甲状腺ホルモンの産生を低下させます。したがって正答は1です。オキシトシンは子宮収縮・乳汁射出に関わるホルモン、プロチレリンはTRH製剤でTSH分泌を促す薬、クロミフェンは排卵誘発薬、ソマトレリンは成長ホルモン分泌を促すGHRH製剤であり、いずれも甲状腺ホルモン産生阻害作用は示しません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 38,

    question:
      "ヒスタミンH₁受容体遮断作用を持たないケミカルメディエーター遊離抑制薬はどれか。1つ選べ。",

    choices: [
    "クロルフェニラミン",
    "プロメタジン",
    "クロモグリク酸",
    "ジフェンヒドラミン",
    "ケトチフェン"
    ],

    answer: 2,

    explanation:
      "正答は3のクロモグリク酸です。クロモグリク酸は肥満細胞からのヒスタミンなどのケミカルメディエーター遊離を抑制する薬ですが、ヒスタミンH₁受容体遮断作用は基本的に持ちません。1のクロルフェニラミン、2のプロメタジン、4のジフェンヒドラミンはいずれもH₁受容体遮断薬です。5のケトチフェンはケミカルメディエーター遊離抑制作用に加えてH₁受容体遮断作用も持つため、本問の条件には当てはまりません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 39,

    question:
      "セファゾリンの抗菌作用の機序はどれか。1つ選べ。",

    choices: [
    "RNA合成阻害",
    "DNA複製阻害",
    "タンパク質合成阻害",
    "細胞膜合成阻害",
    "細胞壁合成阻害"
    ],

    answer: 4,

    explanation:
      "セファゾリンはセフェム系（β-ラクタム系）抗菌薬で、細菌の細胞壁を構成するペプチドグリカンの架橋形成を阻害します。そのため、抗菌作用の機序は「細胞壁合成阻害」です。RNA合成阻害はリファンピシン、DNA複製阻害はキノロン系、タンパク質合成阻害はアミノグリコシド系やマクロライド系などでみられます。細胞膜に作用する薬もありますが、セファゾリンの主作用ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 40,

    question:
      "DNAトポイソメラーゼⅠを阻害して抗悪性腫瘍作用を示すのはどれか。1つ選べ。",

    choices: [
    "ネダプラチン",
    "ブレオマイシン",
    "メルカプトプリン",
    "イリノテカン",
    "マイトマイシンC"
    ],

    answer: 3,

    explanation:
      "イリノテカンは体内で活性代謝物SN-38となり、DNAトポイソメラーゼⅠを阻害してDNA複製を妨げるため、抗悪性腫瘍作用を示します。したがって正答は4です。 ネダプラチンは白金製剤でDNA鎖内・鎖間架橋を形成します。ブレオマイシンはDNA鎖を切断します。メルカプトプリンはプリン代謝拮抗薬です。マイトマイシンCはアルキル化様作用によりDNA架橋を形成するため、トポイソメラーゼⅠ阻害薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 41,

    question:
      "経口投与された薬物が吸収される過程はどれか。１つ選べ。",

    choices: [
    "小腸→全身循環系→肝臓→門脈",
    "小腸→門脈→肝臓→全身循環系",
    "小腸→肝臓→門脈→全身循環系",
    "小腸→全身循環系→門脈→肝臓",
    "小腸→門脈→全身循環系→肝臓",
    "小腸→肝臓→全身循環系→門脈"
    ],

    answer: 1,

    explanation:
      "経口投与された薬物は、主に小腸で吸収された後、門脈を通って肝臓へ運ばれます。肝臓で代謝を受けた後、全身循環系に入るため、正答は「小腸→門脈→肝臓→全身循環系」です。この肝臓での代謝は初回通過効果として重要です。ほかの選択肢は、全身循環系に入った後に肝臓や門脈へ向かう流れになっていたり、門脈を経ずに肝臓へ行く順序になっているため、経口吸収後の基本的な流れとしては適切ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 42,

    question:
      "薬物の生体膜透過機構のうち、トランスポーターを介するが、ATP の加水分解で産生されるエネルギーを必要としないのはどれか。１つ選べ。",

    choices: [
    "単純拡散",
    "促進拡散",
    "一次性能動輸送",
    "二次性能動輸送",
    "膜動輸送"
    ],

    answer: 1,

    explanation:
      "トランスポーターを介するが、ATP加水分解のエネルギーを直接必要としない代表は促進拡散です。促進拡散は濃度勾配に従って物質が移動するため、エネルギーは不要です。単純拡散はエネルギー不要ですが、トランスポーターを介しません。一次性能動輸送はATP加水分解のエネルギーを直接利用します。二次性能動輸送はATPを直接使わない場合もありますが、イオン勾配などのエネルギーを利用して濃度勾配に逆らって輸送します。膜動輸送はエンドサイトーシスなどで、ATPなどのエネルギーを必要とします。したがって、正答は2です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 43,

    question:
      "薬物の血漿タンパク結合の測定に際し、非結合形薬物を分離する方法として、一般的なのはどれか。１つ選べ。",

    choices: [
    "溶媒抽出法",
    "塩析法",
    "再結晶法",
    "逆浸透法",
    "限外ろ過法"
    ],

    answer: 4,

    explanation:
      "血漿タンパク結合を測定する際は、タンパクに結合していない非結合形薬物を分離する方法として、限外ろ過法がよく用いられます。限外ろ過膜により、タンパク質は通過しにくく、非結合形薬物はろ液側へ移動するため、遊離薬物濃度を測定できます。溶媒抽出法は成分の抽出、塩析法はタンパク質の沈殿、再結晶法は精製、逆浸透法は水処理などで用いられる方法であり、血漿タンパク結合の非結合形薬物の分離法として一般的とはいえません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 44,

    question:
      "ヒトの肝臓において、薬物の酸化、還元、加水分解、抱合の全ての代謝反応が行われる細胞内小器官はどれか。1つ選べ。",

    choices: [
    "核",
    "ゴルジ体",
    "小胞体",
    "ミトコンドリア",
    "リソソーム"
    ],

    answer: 2,

    explanation:
      "正答は3の小胞体です。肝細胞の小胞体、とくに滑面小胞体には、CYP（シトクロムP450）などによる酸化反応、還元反応、エステラーゼなどによる加水分解反応、さらにグルクロン酸抱合などの抱合反応に関わる酵素が存在します。そのため、薬物代謝の主要な場として重要です。核は遺伝情報の保持、ゴルジ体はタンパク質の修飾・輸送、ミトコンドリアは一部の酸化反応に関与しますが全ての代謝反応の中心ではありません。リソソームは主に細胞内物質の分解に関わります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 45,

    question:
      "主として未変化体のまま体内から尿中に排泄されるのはどれか。1つ選べ。",

    choices: [
    "ゲンタマイシン",
    "テオフィリン",
    "ニフェジピン",
    "フェニトイン",
    "リドカイン"
    ],

    answer: 0,

    explanation:
      "正答は1のゲンタマイシンです。ゲンタマイシンはアミノグリコシド系抗菌薬で、水溶性が高く、ほとんど代謝されずに主として未変化体のまま腎から尿中排泄されます。そのため腎機能低下時には血中濃度上昇に注意が必要です。テオフィリンは主に肝代謝、ニフェジピンも主に肝臓でCYP3Aにより代謝されます。フェニトインは主に肝代謝され、代謝能が飽和しやすい薬物です。リドカインも主に肝代謝を受けるため、未変化体の尿中排泄が主体ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 46,

    question:
      "水酸化アルミニウムを含む制酸剤とともに経口投与すると、キレートを形成して吸収が低下するのはどれか。1つ選べ。",

    choices: [
    "オメプラゾール",
    "ノルフロキサシン",
    "フェノバルビタール",
    "リボフラビン",
    "ワルファリン"
    ],

    answer: 1,

    explanation:
      "正答は2のノルフロキサシンです。ノルフロキサシンはニューキノロン系抗菌薬で、アルミニウムやマグネシウムなどの多価金属イオンを含む制酸剤と併用すると、消化管内でキレートを形成し、吸収が低下することがあります。そのため、服用間隔をあける必要があります。オメプラゾールは胃酸分泌抑制薬、フェノバルビタールはバルビツール酸系薬、リボフラビンはビタミンB2、ワルファリンは抗凝固薬であり、アルミニウム含有制酸剤とのキレート形成による吸収低下が典型的に問題となる薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 47,

    question:
      "薬物を除去する能力を表すパラメーターで、血流速度と同じ単位を持つのはどれか。1つ選べ。",

    choices: [
    "分布容積",
    "消失半減期",
    "消失速度定数",
    "血中濃度－時間曲線下面積",
    "クリアランス"
    ],

    answer: 4,

    explanation:
      "クリアランスは、単位時間あたりに薬物が除去される血漿（血液）の見かけの体積を表すパラメーターで、単位は L/h や mL/min などです。これは血流量（血流速度）と同じ「体積/時間」の単位を持つため、正答は5です。分布容積は L などの体積、消失半減期は時間、消失速度定数は 1/時間、AUCは濃度×時間を表すため、血流速度と同じ単位ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 48,

    question:
      "Fick の第一法則に従う膜透過において、薬物の透過速度と反比例するのはどれか。1つ選べ。",

    choices: [
    "ドナー側（高濃度側）の薬物濃度",
    "レシーバー側（低濃度側）の薬物濃度",
    "薬物の拡散係数",
    "膜の厚さ",
    "薬物の膜への分配係数"
    ],

    answer: 3,

    explanation:
      "Fick の第一法則では、膜透過速度は概ね J＝(D・K・A/h)(C_d−C_r) で表されます。Dは拡散係数、Kは膜への分配係数、hは膜の厚さです。この式より、透過速度は膜の厚さ h に反比例するため、正答は4です。ドナー側濃度が高いほど濃度差が大きくなり透過は速くなります。レシーバー側濃度が高くなると濃度差は小さくなりますが、単純に反比例する項ではありません。拡散係数や分配係数は大きいほど透過速度が大きくなるため、反比例ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 49,

    question:
      "o/w 型エマルションの性質として、正しいのはどれか。1つ選べ。",

    choices: [
    "水に滴下したとき、水表面で容易に広がる。",
    "スダンIIIを少量添加すると全体が着色される。",
    "w/o 型エマルションよりも電気伝導度が小さい。",
    "半透膜を透過する。",
    "水を加えると粘度が増加する。"
    ],

    answer: 0,

    explanation:
      "o/w型エマルションは、油滴が水中に分散し、水が外相（連続相）となっている乳剤です。そのため水となじみやすく、水に滴下すると表面で容易に広がるので、1が正しいと考えられます。2のスダンIIIは油溶性色素で、o/w型では分散している油滴が主に着色され、全体が一様に着色されるとはいえません。3は水が外相であるo/w型の方が、w/o型より電気伝導度は大きくなりやすいです。4はエマルションの粒子は半透膜を通過しにくいです。5はo/w型に水を加えると一般に希釈され、粘度は低下しやすいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 50,

    question:
      "沈降法によって粒子径を求めるときに用いる式はどれか。1つ選べ。",

    choices: [
    "コゼニーカーマン式",
    "ラングミュアー式",
    "BET 式",
    "ストークス式",
    "ブラック式"
    ],

    answer: 3,

    explanation:
      "沈降法で粒子径を求めるときは、粒子が液体中を沈降する速度と粒子径の関係を表すストークス式を用います。ストークス式では、粒子径が大きいほど沈降速度が大きくなることを利用して粒子径を求めます。1のコゼニーカーマン式は粉体層の比表面積や透過性、2のラングミュアー式と3のBET式は吸着に関する式、5のブラック式は主に分解・安定性評価で扱われる式であり、沈降法による粒子径測定には通常用いません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 51,

    question:
      "直接打錠用の結合剤はどれか。1つ選べ。",

    choices: [
    "結晶セルロース",
    "ヒプロメロース",
    "ショ糖",
    "ポビドン",
    "ヒプロメロースフタル酸エステル"
    ],

    answer: 0,

    explanation:
      "直接打錠では、粉末をそのまま圧縮して錠剤にするため、流動性や圧縮成形性に優れた添加剤が必要です。結晶セルロースは、直接打錠用の賦形剤・結合剤としてよく用いられるため、正答は1です。ヒプロメロース、ショ糖、ポビドンは結合剤として用いられることがありますが、主に造粒時の結合剤として扱われます。ヒプロメロースフタル酸エステルは腸溶性コーティング剤として用いられるため、直接打錠用の結合剤とはいえません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 52,

    question:
      "空気で吹き上げた原料粉体に結合液を噴霧して造粒する方法はどれか。1つ選べ。",

    choices: [
    "噴霧乾燥造粒法",
    "撹拌造粒法",
    "流動層造粒法",
    "押出し造粒法",
    "乾式造粒法"
    ],

    answer: 2,

    explanation:
      "空気で原料粉体を吹き上げて流動化させ、その中に結合液を噴霧して粒子同士を付着・成長させる方法は、流動層造粒法です。乾燥も同じ装置内で行いやすいのが特徴です。噴霧乾燥造粒法は薬液や懸濁液を熱風中に噴霧して乾燥・造粒する方法、撹拌造粒法は撹拌羽根で混合しながら結合液を加える方法です。押出し造粒法は湿った練合物をスクリーンなどから押し出す方法、乾式造粒法は結合液を用いず圧縮などで造粒する方法です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 53,

    question:
      "点眼剤に適用される日本薬局方一般試験法はどれか。1つ選べ。",

    choices: [
    "アルコール数測定法",
    "製剤均一性試験法",
    "エンドトキシン試験法",
    "発熱性物質試験法",
    "無菌試験法"
    ],

    answer: 4,

    explanation:
      "点眼剤は眼に直接適用する製剤であり、微生物による汚染を避ける必要があるため、日本薬局方では無菌であることが求められます。その確認に用いられる一般試験法が無菌試験法です。したがって正答は5です。アルコール数測定法はアルコール含有製剤など、製剤均一性試験法は主に投与量の均一性確認、エンドトキシン試験法や発熱性物質試験法は主に注射剤などで問題となる発熱性物質の確認に関する試験であり、点眼剤に適用される代表的な試験としては無菌試験法を押さえます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 54,

    question:
      "薬物の経口徐放性製剤化の目的として、誤っているのはどれか。1つ選べ。",

    choices: [
    "薬効の持続",
    "コンプライアンスの改善",
    "副作用の軽減",
    "肝初回通過効果の回避",
    "血中濃度の急激な上昇の回避"
    ],

    answer: 3,

    explanation:
      "経口徐放性製剤は、有効成分をゆっくり放出して血中濃度の変動を小さくすることを目的とします。そのため、薬効の持続、服用回数の減少によるコンプライアンスの改善、急激な血中濃度上昇の回避、それに伴う副作用の軽減が期待されます。一方、経口投与である以上、吸収後に門脈を経て肝臓に入るため、肝初回通過効果を回避することは基本的にできません。したがって、誤っているのは4です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 55,

    question:
      "脂質二分子膜から成る微粒子はどれか。1つ選べ。",

    choices: [
    "リピッドマイクロスフェア",
    "リポソーム",
    "高分子ミセル",
    "デンドリマー",
    "シクロデキストリン"
    ],

    answer: 1,

    explanation:
      "脂質二分子膜から成る微粒子として代表的なのはリポソームです。リポソームはリン脂質などが水中で自己集合し、脂質二分子膜で水相を包み込んだ小胞を形成します。1のリピッドマイクロスフェアは脂質粒子ですが、油滴を界面活性剤などで安定化した製剤であり、脂質二分子膜構造とは異なります。3の高分子ミセルは両親媒性高分子が形成するミセル、4のデンドリマーは樹枝状高分子、5のシクロデキストリンは環状オリゴ糖で、いずれも脂質二分子膜から成る微粒子ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 56,

    question:
      "肝細胞癌の腫瘍マーカーとして、最も適切なのはどれか。1つ選べ。",

    choices: [
    "AFP（α-fetoprotein）",
    "CA 19-9（carbohydrate antigen 19-9）",
    "PSA（prostate specific antigen）",
    "CYFRA 21-1（cytokeratin 19 fragment）",
    "SCC（squamous cell carcinoma related antigen）"
    ],

    answer: 0,

    explanation:
      "肝細胞癌の代表的な腫瘍マーカーはAFP（α-fetoprotein）です。AFPは胎児期に産生されるタンパク質ですが、肝細胞癌などで上昇することがあり、診断補助や経過観察に用いられます。CA19-9は主に膵癌・胆道癌、PSAは前立腺癌、CYFRA21-1は肺扁平上皮癌など、SCCは扁平上皮癌で用いられることが多いマーカーです。したがって、最も適切なのは1です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 57,

    question:
      "高LDLコレステロール血症に関する記述のうち、正しいのはどれか。1つ選べ。",

    choices: [
    "食事直後に血清LDLコレステロール値が上昇する。",
    "血清がクリーム状である。",
    "LDL受容体機能不全が原因となる。",
    "冠動脈疾患の危険因子とはならない。",
    "甲状腺機能亢進症に合併する。"
    ],

    answer: 2,

    explanation:
      "高LDLコレステロール血症では、LDLの肝臓への取り込み低下などにより血中LDLが増加します。特に家族性高コレステロール血症では、LDL受容体の機能不全が原因となるため、3が正しいと考えられます。1の食後に上がりやすいのは主に中性脂肪（カイロミクロン）です。2の血清がクリーム状になるのも高度の中性脂肪増加でみられます。4は誤りで、LDL高値は冠動脈疾患の重要な危険因子です。5は甲状腺機能低下症でLDLが上昇しやすく、亢進症では一般に低下しやすいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 58,

    question:
      "インフルエンザの薬物治療に関する記述のうち、正しいのはどれか。1つ選べ。",

    choices: [
    "ザナミビル水和物は、B型の患者に有効である。",
    "アスピリンは、小児の解熱薬として推奨される。",
    "アマンタジン塩酸塩は、B型の患者に有効である。",
    "ニューキノロン系抗菌薬が第一選択薬である。",
    "オセルタミビルリン酸塩は、症状発現直後の使用では有効性がない。"
    ],

    answer: 0,

    explanation:
      "正答は1です。ザナミビル水和物はノイラミニダーゼ阻害薬で、インフルエンザA型・B型のいずれにも効果が期待されます。2のアスピリンは、小児ではライ症候群のリスクがあるため解熱薬としては通常推奨されません。3のアマンタジンはA型に作用しますが、B型には無効です。4のニューキノロン系抗菌薬は細菌に対する薬であり、ウイルス感染であるインフルエンザの第一選択にはなりません。5のオセルタミビルは、症状発現後できるだけ早期、一般に48時間以内の使用で有効性が期待されます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 59,

    question:
      "アルツハイマー病の病態として、最も適切なのはどれか。1つ選べ。",

    choices: [
    "急激に発症する。",
    "安静時振戦が現れる。",
    "まだら認知症を呈する。",
    "幻視がみられる。",
    "初期には短期記憶が障害される。"
    ],

    answer: 4,

    explanation:
      "アルツハイマー病では、海馬を中心とした障害により、初期から近時記憶（短期記憶）の低下が目立ちます。そのため、同じことを何度も聞く、物忘れが増えるなどが典型的です。1の急激な発症はせん妄や脳血管障害などでみられやすく、アルツハイマー病は一般に緩徐に進行します。2の安静時振戦はパーキンソン病で特徴的です。3のまだら認知症は脳血管性認知症でみられやすい所見です。4の幻視はレビー小体型認知症で特徴的です。したがって、最も適切なのは5です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 60,

    question:
      "次の抗うつ薬のうち、緑内障を合併している患者に使用できるのはどれか。1つ選べ。",

    choices: [
    "イミプラミン塩酸塩",
    "アミトリプチリン塩酸塩",
    "フルボキサミンマレイン酸塩",
    "アモキサピン",
    "マプロチリン塩酸塩"
    ],

    answer: 2,

    explanation:
      "緑内障では、抗コリン作用により眼圧上昇を起こしやすい薬は避けるのが基本です。イミプラミン、アミトリプチリン、アモキサピン、マプロチリンはいずれも三環系または四環系抗うつ薬で、抗コリン作用を示すため緑内障では使用しにくい薬です。フルボキサミンはSSRIで、これらに比べて抗コリン作用が弱いため、緑内障を合併する患者にも比較的使用しやすいと考えます。したがって正答は3です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 61,

    question:
      "関節リウマチの治療薬はどれか。1つ選べ。",

    choices: [
    "セツキシマブ",
    "インフリキシマブ",
    "トラスツズマブ",
    "ベバシズマブ",
    "ゲフィチニブ"
    ],

    answer: 1,

    explanation:
      "関節リウマチでは、炎症性サイトカインであるTNF-αを標的とする生物学的製剤が用いられます。インフリキシマブは抗TNF-α抗体で、関節リウマチの治療薬として使用されるため正答です。セツキシマブは抗EGFR抗体、トラスツズマブは抗HER2抗体、ベバシズマブは抗VEGF抗体で、主に悪性腫瘍に用いられます。ゲフィチニブはEGFRチロシンキナーゼ阻害薬で、肺がんなどに用いられる薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 62,

    question:
      "統合失調症の陽性症状はどれか。1つ選べ。",

    choices: [
    "思考の貧困",
    "自閉",
    "妄想",
    "意欲の低下",
    "感情の平板化"
    ],

    answer: 2,

    explanation:
      "統合失調症の陽性症状は、幻覚や妄想など、本来ないはずの精神症状が現れるものです。したがって、3の妄想が正答です。1の思考の貧困、4の意欲の低下、5の感情の平板化は陰性症状に分類されます。2の自閉も周囲との関わりが乏しくなる症状で、陰性症状として考えられます。陽性症状＝幻覚・妄想、陰性症状＝意欲低下・感情平板化・思考の貧困、と整理しておくとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 63,

    question:
      "糖尿病患者で心不全を併発した場合に禁忌となる医薬品はどれか。1つ選べ。",

    choices: [
    "グリメピリド",
    "ナテグリニド",
    "ボグリボース",
    "ピオグリタゾン塩酸塩",
    "アログリプチン安息香酸塩"
    ],

    answer: 3,

    explanation:
      "正答は4のピオグリタゾン塩酸塩です。ピオグリタゾンはチアゾリジン薬で、インスリン抵抗性を改善しますが、体液貯留や浮腫を起こしやすく、心不全を悪化させるおそれがあるため、心不全患者では禁忌とされます。1のグリメピリドはSU薬、2のナテグリニドは速効型インスリン分泌促進薬で、主な注意点は低血糖です。3のボグリボースはα-グルコシダーゼ阻害薬で、腹部膨満などが問題になります。5のアログリプチンはDPP-4阻害薬で、心不全では注意が必要な場合がありますが、典型的な禁忌として問われるのはピオグリタゾンです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 64,

    question:
      "糖尿病の三大合併症に該当するのはどれか。1つ選べ。",

    choices: [
    "結膜炎",
    "角膜炎",
    "黄斑変性症",
    "網膜症",
    "緑内障"
    ],

    answer: 3,

    explanation:
      "糖尿病の三大合併症は、糖尿病性網膜症、糖尿病性腎症、糖尿病性神経障害です。したがって、該当するのは4の網膜症です。糖尿病では高血糖により細小血管が障害され、網膜の血管障害から視力低下などにつながることがあります。結膜炎・角膜炎は主に感染や外傷など、黄斑変性症は加齢などが関与しやすい疾患です。緑内障も糖尿病と関連することはありますが、三大合併症には含まれません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 65,

    question:
      "癌化学療法において、制吐に用いられる医薬品として、適切なのはどれか。1つ選べ。",

    choices: [
    "ブロモクリプチンメシル酸塩",
    "ランソプラゾール",
    "ラニチジン塩酸塩",
    "スクラルファート水和物",
    "アプレピタント"
    ],

    answer: 4,

    explanation:
      "癌化学療法による悪心・嘔吐には、セロトニン5-HT3受容体拮抗薬、NK1受容体拮抗薬、ステロイドなどが用いられます。アプレピタントはNK1受容体拮抗薬で、サブスタンスPの作用を抑え、特に遅発性嘔吐の予防に有用とされるため正答です。ブロモクリプチンはドパミン受容体作動薬、ランソプラゾールはプロトンポンプ阻害薬、ラニチジンはH2受容体拮抗薬、スクラルファートは胃粘膜保護薬であり、いずれも癌化学療法時の制吐薬としては適切とはいえません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 66,

    question:
      "医薬品の妊婦に対する投与の可否を検討する資料として、最も適切なのはどれか。1つ選べ。",

    choices: [
    "Index Medicus",
    "Drug Interaction Facts",
    "Drugs in Pregnancy and Lactation",
    "Meyler’s Side Effects of Drugs",
    "Goodman & Gilman’s The Pharmacological Basis of Therapeutics"
    ],

    answer: 2,

    explanation:
      "妊婦への投与可否を検討する資料として最も適切なのは、3の『Drugs in Pregnancy and Lactation』です。薬物の妊娠中・授乳中の安全性、胎児への影響などを調べるための代表的な資料です。 1のIndex Medicusは医学文献の索引、2のDrug Interaction Factsは薬物相互作用、4のMeyler’s Side Effects of Drugsは副作用情報、5のGoodman & Gilman’sは薬理学の標準的教科書であり、妊婦投与の可否を調べる目的では3が最も適しています。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 67,

    question:
      "医薬品の安全性に関して最も詳細な情報が得られるのはどれか。1つ選べ。",

    choices: [
    "医療用医薬品添付文書",
    "Drug Safety Update",
    "医療用医薬品製品情報概要",
    "医薬品・医療機器等安全性情報",
    "医薬品インタビューフォーム"
    ],

    answer: 4,

    explanation:
      "医薬品インタビューフォーム（IF）は、添付文書を補完する目的で作成され、有効性・安全性・薬物動態・製剤情報などが比較的詳細にまとめられています。そのため、安全性について最も詳しい情報を得たい場合に適しています。添付文書は重要事項を簡潔に示す基本情報、Drug Safety Updateや医薬品・医療機器等安全性情報は安全性に関する新たな情報や注意喚起が中心です。製品情報概要は主に医薬品の特徴を説明する資料であり、IFほど詳細ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 68,

    question:
      "問題志向型システム（POS）の説明として、適切なのはどれか。1つ選べ。",

    choices: [
    "処方設計支援システムの一部である。",
    "EBMで問題点を定式化する際の手法の1つである。",
    "服薬遵守のための方法論である。",
    "患者の抱える医療上の問題に焦点をあてる問題解決法である。",
    "臨床研究の計画を決定するために必要な手法である。"
    ],

    answer: 3,

    explanation:
      "POS（Problem Oriented System：問題志向型システム）は、患者が抱える医療上の問題点を明確にし、その問題ごとに情報収集・評価・計画を行う問題解決型の考え方です。したがって、正答は4です。1の処方設計支援システムとは別の概念です。2はEBMで疑問を整理するPICOなどに関する説明です。3は服薬遵守を高める方法そのものではありません。5は臨床研究計画の手法というより、日常の医療・薬学的ケアで用いられる考え方です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 69,

    question:
      "遺伝子多型がワルファリンの薬効に最も影響する薬物代謝酵素はどれか。1つ選べ。",

    choices: [
    "CYP1A2",
    "CYP2C9",
    "CYP2C19",
    "CYP2D6",
    "CYP3A4"
    ],

    answer: 1,

    explanation:
      "ワルファリンの薬効に影響しやすい代謝酵素として重要なのはCYP2C9です。特に薬効の強いS-ワルファリンを主に代謝するため、CYP2C9の遺伝子多型により代謝が低下すると、作用が強く出て出血リスクが高まることがあります。CYP1A2やCYP3A4も一部代謝に関与しますが、影響はCYP2C9ほど大きくありません。CYP2C19は主にプロトンポンプ阻害薬など、CYP2D6は抗不整脈薬や抗うつ薬などで重要です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 70,

    question:
      "加齢に伴い増大するのはどれか。1つ選べ。",

    choices: [
    "肺活量",
    "体脂肪率",
    "腎血漿流量",
    "胃酸分泌量",
    "血漿中アルブミン濃度"
    ],

    answer: 1,

    explanation:
      "加齢に伴い、一般に筋肉量や体内水分量は減少し、相対的に体脂肪率は増加しやすくなります。したがって正答は2です。肺活量は呼吸筋や肺の弾性の低下により低下しやすく、腎血漿流量も腎機能低下に伴い減少します。胃酸分泌量は低下傾向とされ、血漿中アルブミン濃度も栄養状態などの影響で低下しやすいため、いずれも「増大する」とは考えにくいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 71,

    question:
      "薬剤師が倫理的に配慮すべき事項として、ふさわしくないのはどれか。1つ選べ。",

    choices: [
    "職務上知り得た患者の秘密を守る。",
    "薬剤師職能間の相互協調に努める。",
    "医薬品の安全性の確保に努める。",
    "地域医療の向上のための施策に協力する。",
    "社会全体の医薬品消費量の増加を促す。"
    ],

    answer: 4,

    explanation:
      "薬剤師が倫理的に配慮すべき事項としてふさわしくないのは5です。薬剤師は、医薬品の適正使用を推進し、必要な人に必要な薬物療法が行われるよう支援する立場であり、社会全体の医薬品消費量を増やすこと自体を目的とするものではありません。1の守秘義務、2の薬剤師間の協調、3の医薬品の安全性確保、4の地域医療への協力はいずれも薬剤師の倫理・職能として重要な事項です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 72,

    question:
      "薬剤師のみが資格要件を満たすのはどれか。1つ選べ。",

    choices: [
    "薬局の管理者",
    "店舗販売業の店舗管理者",
    "医薬部外品製造販売業の総括製造販売責任者",
    "生物由来製品の製造管理者",
    "麻薬管理者"
    ],

    answer: 0,

    explanation:
      "正答は1です。薬局の管理者は、原則として薬剤師であることが求められるため、「薬剤師のみ」が該当します。 2の店舗販売業の店舗管理者は、薬剤師だけでなく、一定の要件を満たす登録販売者もなることができます。3の医薬部外品製造販売業の総括製造販売責任者は、薬剤師以外にも所定の学歴・経験を満たす者が認められます。4の生物由来製品の製造管理者も、薬剤師に限られません。5の麻薬管理者は、薬剤師のほか、医師・歯科医師・獣医師も該当する場合があります。したがって、薬剤師のみが資格要件となるのは薬局の管理者です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 73,

    question:
      "薬剤師免許の絶対的欠格事由に該当するのはどれか。1つ選べ。",

    choices: [
    "成年被後見人",
    "視覚障害者",
    "精神機能障害者",
    "麻薬中毒者",
    "罰金以上の刑に処せられた者"
    ],

    answer: 0,

    explanation:
      "絶対的欠格事由は、該当すると薬剤師免許が与えられない事由です。本問では「成年被後見人」がこれに該当します。視覚障害者や精神機能障害者は、業務を適正に行えるかなどを個別に判断する相対的欠格事由として扱われます。麻薬中毒者、罰金以上の刑に処せられた者も、免許を与えないことがある相対的欠格事由であり、絶対的欠格事由ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 74,

    question:
      "医療法に基づく医療の基本理念に含まれていないのはどれか。1つ選べ。",

    choices: [
    "生命の尊重",
    "個人の尊厳の保持",
    "相互信頼",
    "包括医療",
    "安楽死"
    ],

    answer: 4,

    explanation:
      "医療法の基本理念では、医療は「生命の尊重」と「個人の尊厳の保持」を旨とし、医療従事者と患者との「信頼関係」に基づいて行われるものとされています。また、治療だけでなく、予防やリハビリテーションを含む良質かつ適切な医療、いわゆる包括的な医療の考え方も含まれます。一方、「安楽死」は医療法に基づく医療の基本理念には含まれていません。したがって、正答は5です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 75,

    question:
      "医療法に規定される病院の病床の種別に該当しないのはどれか。1つ選べ。",

    choices: [
    "精神病床",
    "感染症病床",
    "救急病床",
    "療養病床",
    "一般病床"
    ],

    answer: 2,

    explanation:
      "医療法で定められる病院の病床の種別は、精神病床、感染症病床、結核病床、療養病床、一般病床です。したがって、該当しないのは3の救急病床です。救急医療は救急病院・救急診療体制などとして扱われますが、医療法上の病床種別ではありません。1、2、4、5はいずれも病床の種別として規定されています。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 76,

    question:
      "サリドマイドによって引き起こされた薬害で問題となった有害事象はどれか。1つ選べ。",

    choices: [
    "アザラシ肢症",
    "亜急性脊髄視神経症",
    "劇症肝炎",
    "無顆粒球症",
    "アナフィラキシーショック"
    ],

    answer: 0,

    explanation:
      "サリドマイドは、妊娠初期に服用した場合の催奇形性が問題となり、胎児に四肢の形成異常であるアザラシ肢症を起こした薬害として知られています。したがって正答は1です。2の亜急性脊髄視神経症（SMON）は主にキノホルム、3の劇症肝炎、4の無顆粒球症、5のアナフィラキシーショックはサリドマイド薬害の代表的な有害事象とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 77,

    question:
      "地域保険はどれか。1つ選べ。",

    choices: [
    "組合管掌健康保険",
    "国民健康保険",
    "国家公務員共済組合",
    "船員保険",
    "全国健康保険協会管掌健康保険"
    ],

    answer: 1,

    explanation:
      "地域保険とは、職業に関係なく地域住民を対象とする医療保険で、代表例は国民健康保険です。自営業者、退職者、無職の人などが主な対象となるため、正答は2です。1の組合管掌健康保険、5の全国健康保険協会管掌健康保険は主に会社員などを対象とする職域保険です。3の国家公務員共済組合は公務員、4の船員保険は船員を対象とする職域保険に分類されます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 78,

    question:
      "地域薬局の役割に該当しないのはどれか。1つ選べ。",

    choices: [
    "セルフメディケーションの支援",
    "医薬品の販売",
    "調剤",
    "地域住民の健康診断",
    "在宅医療への参画"
    ],

    answer: 3,

    explanation:
      "地域薬局の主な役割には、処方箋に基づく調剤、医薬品の販売、セルフメディケーションの支援、在宅医療への参画などがあります。一方、地域住民の健康診断は、一般に医療機関や自治体などが実施するものであり、薬局の基本的な役割としては該当しにくいため、4が正答です。1〜3、5はいずれも地域薬局に求められる代表的な役割です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 79,

    question:
      "治験審査委員会に必須の構成員はどれか。1つ選べ。",

    choices: [
    "治験実施医療機関の長",
    "治験責任医師",
    "治験依頼者の代表",
    "医学・薬学等の専門的知識を有する者以外の者",
    "治験薬管理者"
    ],

    answer: 3,

    explanation:
      "治験審査委員会（IRB）は、治験の倫理性・科学性を中立的に審査するため、医学・薬学等の専門家だけでなく、「専門的知識を有する者以外の者」を含めることが求められます。したがって正答は4です。医療機関の長、治験責任医師、治験依頼者の代表は、審査の独立性の観点から必須構成員ではありません。治験薬管理者も治験薬の管理を担う役割であり、IRBの必須構成員とはされていません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 80,

    question:
      "インフォームド・コンセントの目的として、適切でないのはどれか。1つ選べ。",

    choices: [
    "医療過誤の責任を回避する。",
    "提供する医療について患者の同意を得る。",
    "提供される医療について患者が理解する。",
    "患者の自己決定権を尊重する。",
    "患者の知る権利を尊重する。"
    ],

    answer: 0,

    explanation:
      "インフォームド・コンセントは、医療者が治療内容・効果・リスク・代替案などを説明し、患者が理解したうえで自ら同意・選択できるようにするためのものです。したがって、患者の同意を得る、理解を促す、自己決定権や知る権利を尊重することは目的に含まれます。一方で、医療過誤の責任を回避することが目的ではありません。説明と同意があっても、医療過誤の責任が免除されるわけではないため、1が適切でない選択肢です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 81,

    question:
      "文中の□に入る適切な語句はどれか。1つ選べ。 世界保健機関（WHO）は、「ファーマシューティカルケアとは、薬剤師の活動の中心に□を据える行動哲学である。ファーマシューティカルケアは、患者の保健及び生活の質の向上のため、明確な治療効果を達成するとの目標をもって、薬物療法を施す際の、薬剤師の姿勢、行動、関与、倫理、機能、知識、責務ならびに技能に焦点を当てるものである」と定めている。",

    choices: [
    "国民医療の経済性",
    "国際保健への貢献",
    "無報酬での奉仕",
    "薬剤師の権利",
    "患者の利益"
    ],

    answer: 4,

    explanation:
      "WHOの定義では、ファーマシューティカルケアは薬剤師の活動の中心に「患者の利益」を据える考え方とされています。薬物療法を通じて、治療効果の達成や患者のQOL向上を目指す点が重要です。1の医療経済性や2の国際保健も医療上の課題ですが、定義の中心ではありません。3の無報酬での奉仕、4の薬剤師の権利もファーマシューティカルケアの趣旨とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 82,

    question:
      "文中の□に入る適切な語句はどれか。1つ選べ。 チーム医療とは「多種多様な医療スタッフが、□を前提に、目的と情報を共有し、業務を分担しつつも互いに連携・補完し合い、患者の状況に的確に対応した医療を提供すること」と一般的に理解されている。",

    choices: [
    "業務負担の軽減",
    "医師への依存",
    "人件費の削減",
    "各々の高い専門性",
    "医行為の規制緩和"
    ],

    answer: 3,

    explanation:
      "チーム医療では、医師、薬剤師、看護師など多職種がそれぞれの専門性を発揮し、情報共有と連携により患者に適した医療を提供することが重要です。そのため、□には「各々の高い専門性」が入ります。1の業務負担軽減は結果として期待されることはありますが前提ではありません。2の医師への依存はチーム医療の考え方と逆です。3の人件費削減、5の医行為の規制緩和も主目的・前提としては不適切です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 83,

    question:
      "腎機能が低下した患者へ投与する際、減量の必要性が少ないのはどれか。1つ選べ。",

    choices: [
    "アルベカシン硫酸塩",
    "メロペネム水和物",
    "レボフロキサシン水和物",
    "セファゾリンナトリウム水和物",
    "アジスロマイシン水和物"
    ],

    answer: 4,

    explanation:
      "腎機能低下時に減量の必要性が少ない薬は、主に腎排泄ではない薬です。アジスロマイシンはマクロライド系抗菌薬で、胆汁中排泄・糞中排泄の寄与が大きく、腎機能低下時でも比較的用量調節の必要性が少ないと考えます。したがって正答は5です。アルベカシンはアミノグリコシド系で腎排泄性が高く、腎障害時は血中濃度上昇や腎毒性に注意します。メロペネム、レボフロキサシン、セファゾリンも腎排泄の寄与が大きく、腎機能に応じた減量・投与間隔調節が必要になりやすい薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 84,

    question:
      "保険薬局において、調剤を行う上で疑義照会が不要な場合はどれか。1つ選べ。",

    choices: [
    "賦形剤の使用が必要と考えられた。",
    "医薬品の規格が特定できなかった。",
    "併用禁忌の組合せを発見した。",
    "医薬品名が略号で記載されていた。",
    "用量の記載が抜けていた。"
    ],

    answer: 0,

    explanation:
      "疑義照会は、処方内容に不明点や医学的な疑いがあり、そのまま調剤すると適切性が確認できない場合に行います。賦形剤の使用は、散剤などを調剤しやすくするための調剤上の工夫であり、通常は処方内容そのものを変更するものではないため、疑義照会が不要な場合と考えられます。したがって正答は1です。2の規格不明、4の略号記載、5の用量抜けは処方内容が特定できず疑義照会が必要です。3の併用禁忌は安全性に関わるため、当然確認が必要です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 85,

    question:
      "横紋筋融解症が現れやすくなるので、シンバスタチンとの併用が禁忌とされているのはどれか。1つ選べ。",

    choices: [
    "コレスチラミン",
    "ハロペリドール",
    "イトラコナゾール",
    "プロプラノロール塩酸塩",
    "葛根湯"
    ],

    answer: 2,

    explanation:
      "正答は3のイトラコナゾールです。シンバスタチンは主にCYP3A4で代謝されます。イトラコナゾールはCYP3A4を強く阻害するため、シンバスタチンの血中濃度が上昇し、横紋筋融解症などの重篤な筋障害が起こりやすくなるため併用禁忌です。コレスチラミンは薬物の吸収を低下させることがあり、服用間隔に注意しますが併用禁忌ではありません。ハロペリドール、プロプラノロール塩酸塩、葛根湯は、シンバスタチンとの併用で横紋筋融解症リスク増大により禁忌とされる代表薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 86,

    question:
      "文中の□に入る適切な語句はどれか。1つ選べ。患者から医薬品を使用後に重篤な副作用が現れたとの訴えがあった。添付文書に記載されていない症状であったため、□に基づき薬剤師から厚生労働大臣に状況を報告した。",

    choices: [
    "日本薬局方",
    "再審査制度",
    "医薬品の臨床試験の実施に関する基準（GCP）",
    "医薬品・医療機器等安全性情報報告制度",
    "プレアボイド報告"
    ],

    answer: 3,

    explanation:
      "重篤な副作用が疑われ、添付文書に記載のない症状であっても、薬剤師などの医療関係者は「医薬品・医療機器等安全性情報報告制度」に基づき、厚生労働大臣へ報告することが求められます。これは市販後の安全対策に重要な制度です。日本薬局方は医薬品の規格基準、再審査制度は承認後一定期間の有効性・安全性の再確認、GCPは治験の基準です。プレアボイド報告は薬剤師の介入により副作用などを回避・軽減した事例の報告であり、本問の制度とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 87,

    question:
      "病院の薬剤部門を構成する各セクション（室）の中で、薬剤管理指導料の施設基準として、必要なのはどれか。1つ選べ。",

    choices: [
    "調剤室",
    "製剤室",
    "医薬品情報管理室",
    "薬務室",
    "試験室"
    ],

    answer: 2,

    explanation:
      "薬剤管理指導料では、入院患者への服薬指導だけでなく、医薬品情報を収集・評価し、医療スタッフへ提供できる体制が求められます。そのため、施設基準として必要なセクションは医薬品情報管理室（DI室）です。調剤室は薬剤部門の基本的な機能ですが、この施設基準として問われる代表的なものではありません。製剤室、薬務室、試験室も病院によって設置されることはありますが、薬剤管理指導料の施設基準として必須とされるものではないため、正答は3です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 88,

    question:
      "病院において使用記録を20年間保存しなければならないのはどれか。1つ選べ。",

    choices: [
    "麻薬",
    "腫瘍用薬",
    "放射性医薬品",
    "血液製剤類",
    "ワクチン類"
    ],

    answer: 3,

    explanation:
      "正答は4の血液製剤類です。血液製剤などの特定生物由来製品は、感染症などが後から判明した場合に使用患者を追跡できるよう、医療機関で使用記録を20年間保存する必要があります。1の麻薬は帳簿の保存期間が原則2年、3の放射性医薬品も20年保存の対象として問われるものではありません。2の腫瘍用薬、5のワクチン類も一般に「使用記録を20年間保存」として覚える対象ではなく、国家試験では血液製剤類＝20年保存と整理しておくとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 89,

    question:
      "医薬品の保存条件や使用期限に関して、誤っているのはどれか。1つ選べ。",

    choices: [
    "冷所は、特に規定がなければ1～15℃を示す。",
    "常温は、15～30℃を示す。",
    "室温は、1～30℃を示す。",
    "使用期限は、適切な保存条件下で未開封での期限を示す。",
    "医薬品の保存にふさわしい相対湿度は、45～55%程度とされている。"
    ],

    answer: 1,

    explanation:
      "誤っているのは2です。日本薬局方などで用いられる温度の目安では、常温は15～25℃を指すため、15～30℃ではありません。1の冷所は1～15℃、3の室温は1～30℃で正しい内容です。4の使用期限は、通常、適切な保存条件で未開封の場合に品質が保たれる期限を示します。5の相対湿度45～55％程度も、医薬品の保存に適した湿度の目安として扱われます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 97,
    sourceNumber: 90,

    question:
      "一般用医薬品の第1類医薬品の取扱いとして、誤っているのはどれか。1つ選べ。",

    choices: [
    "第2類医薬品と区別して陳列した。",
    "医薬品を購入しようとする人の手が直接触れられない場所に陳列した。",
    "医薬品を購入しようとする人からの相談に薬剤師が対応した。",
    "医薬品を購入しようとする人に、その医薬品の情報を記載した書面を用いずに説明した。",
    "現在使用している医療用医薬品との重複がないか確認した。"
    ],

    answer: 3,

    explanation:
      "第1類医薬品は、薬剤師が購入者に対して必要な情報提供を行う必要があり、原則としてその医薬品の情報を記載した書面を用いて説明します。したがって、書面を用いずに説明した選択肢4が誤りです。1は第1類医薬品を他の区分と区別して陳列する対応として適切です。2も購入者が直接手に取れない場所に陳列する扱いとして適切です。3のように相談対応は薬剤師が行います。5の併用薬や重複の確認も、適正使用のために重要な対応です。"
  },

  // AI_QUESTION_INSERT_HERE
];
