import { CATEGORIES } from "./categories";

export const required104Questions = [

  
  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 1,

    question:
      "親核種よりも原子番号が1つ小さい娘核種を生成する放射壊変はどれか。1つ選べ。",

    choices: [
    "α壊変",
    "β−壊変",
    "β+壊変",
    "γ転移（核異性体転移）",
    "自発核分裂"
    ],

    answer: 2,

    explanation:
      "正答は3のβ+壊変です。β+壊変では、原子核内の陽子が中性子に変わり、陽電子などを放出するため、原子番号は1つ小さくなります。質量数はほとんど変わりません。α壊変では原子番号が2つ小さくなり、β−壊変では中性子が陽子に変わるため原子番号は1つ大きくなります。γ転移（核異性体転移）はエネルギー状態が変わるだけで原子番号は変化しません。自発核分裂は原子核が分裂して複数の核種を生じる壊変です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 2,

    question:
      "濃度未知の水酸化ナトリウム水溶液を、0.01 mol/L塩酸標準液（ファクター f = 1.020）を用いて滴定したところ、滴定終点までに6.10 mLを要した。この水酸化ナトリウム水溶液中の水酸化ナトリウムの量（μmol）として適切なのはどれか。1つ選べ。",

    choices: [
    "59.80",
    "59.8",
    "61.00",
    "62.2",
    "62.22"
    ],

    answer: 3,

    explanation:
      "NaOHとHClは 1：1 で中和するため、終点までに使ったHClの物質量がNaOHの物質量に相当します。標準液の実際の濃度は、0.01 mol/L × f ＝ 0.01 × 1.020 ＝ 0.01020 mol/Lです。したがって、0.01020 × 6.10×10^-3 L ＝ 6.222×10^-5 mol ＝ 62.22 μmol。測定値に合わせて有効数字3桁で表すと 62.2 μmol となります。よって正答は4です。3はファクターを考慮していない値、5は計算値そのままで有効数字が多すぎると考えられます。1、2はファクターの扱いを逆にした場合の値に近くなります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 3,
    hasImage: true,
    image: "/pharmacy/104/required/q3.png",

    question:
      "図は水の状態を示したものである。点Tにおけるギブスの相律の自由度（F）の値として、正しいのはどれか。1つ選べ。",

    choices: [
    "0",
    "1",
    "2",
    "3",
    "4"
    ],

    answer: 0,

    explanation:
      "点Tは水の三重点を表し、固体・液体・気体の3相が同時に平衡にある点と考える。ギブスの相律は F＝C−P＋2 で、水は1成分系なので C＝1、三重点では相の数 P＝3。したがって F＝1−3＋2＝0 となる。つまり温度と圧力は一意に決まり、自由に変えられる変数はない。なお、2相共存線上なら F＝1、1相領域なら F＝2 となるため、他の選択肢は点Tには当てはまらない。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 4,

    question:
      "強酸性陽イオン交換樹脂に最も強く結合するイオンはどれか。1つ選べ。",

    choices: [
    "塩化物イオン",
    "カルシウムイオン",
    "グリシン（双性イオン）",
    "硫酸イオン",
    "ナトリウムイオン"
    ],

    answer: 1,

    explanation:
      "強酸性陽イオン交換樹脂は、スルホン酸基などの陰性基をもち、陽イオンを交換・結合します。一般に、同じ条件では価数が大きい陽イオンほど強く結合しやすいため、Na⁺よりCa²⁺の方が強く結合します。したがって正答はカルシウムイオンです。塩化物イオンや硫酸イオンは陰イオンなので対象外です。グリシンは双性イオンですが、全体としては中性に近く、Ca²⁺ほど強く結合するとは考えにくいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 5,

    question:
      "反射波を利用する画像診断法はどれか。1つ選べ。",

    choices: [
    "X線CT",
    "MRI",
    "超音波診断法",
    "陽電子放射断層撮影法（PET）",
    "単一光子放射断層撮影法（SPECT）"
    ],

    answer: 2,

    explanation:
      "反射波を利用する画像診断法は、超音波診断法です。体内に超音波を送り、臓器や組織の境界で反射して戻ってくる波（エコー）を受信して画像化します。X線CTはX線の透過差、MRIは核磁気共鳴信号、PETは陽電子放出核種から生じる放射線、SPECTは単一光子を放出する放射性医薬品からのγ線を利用するため、反射波を利用する方法ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 6,

    question:
      "炭素原子の最外殻に収容されている電子数が7である反応中間体はどれか。1つ選べ。",

    choices: [
    "H3C−",
    "H3C+",
    "H3C・",
    "H2C:（一重項）",
    "H2C・・（三重項）"
    ],

    answer: 2,

    explanation:
      "炭素原子の最外殻電子数は、結合電子を炭素の周りの電子として数えます。H3C・（メチルラジカル）は、C–H結合3本で6個の電子に加え、不対電子1個をもつため、合計7個となります。したがって正答は3です。H3C−は結合3本＋孤立電子対で8個、H3C+は結合3本のみで6個です。H2C:（一重項カルベン）は結合2本＋孤立電子対で6個、H2C・・（三重項カルベン）も結合2本＋不対電子2個で6個と考えます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 7,
    hasImage: true,
    image: "/pharmacy/104/required/q7.png",

    question:
      "最も塩基性が強い化合物はどれか。1つ選べ。",

    choices: [
    "グアニジン",
    "アセトアミド",
    "エチルアミン",
    "インドール",
    "ピラジン"
    ],

    answer: 0,

    explanation:
      "最も塩基性が強いのはグアニジンです。グアニジンはプロトン化されるとグアニジニウムイオンとなり、正電荷が3つの窒素に共鳴で分散して安定化されるため、共役酸のpKaが高く、強い塩基性を示します。エチルアミンもアミンなので塩基性はありますが、グアニジンほどではありません。アセトアミドは窒素の非共有電子対がカルボニルと共鳴するため塩基性が弱いです。インドールは窒素の非共有電子対が芳香族性に関与するため塩基性は弱く、ピラジンも環内窒素の電子密度が低く比較的弱塩基性です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 8,
    hasImage: true,
    image: "/pharmacy/104/required/q8.png",

    question:
      "ブタンのC2-C3結合を回転させた際に生じる立体配座のうち、最も安定なのはどれか。1つ選べ。",

    choices: [
    "図示された立体配座1",
    "図示された立体配座2",
    "図示された立体配座3",
    "図示された立体配座4",
    "図示された立体配座5"
    ],

    answer: 0,

    explanation:
      "ブタンのC2-C3結合まわりの立体配座では、2つのメチル基が最も離れた位置にあるアンチ形のねじれ形配座が最も安定です。選択肢1はメチル基同士の二面角が180°となる配座で、立体反発やねじれひずみが小さいため正答です。ほかの選択肢は、メチル基が近いゴーシュ形では立体反発がやや大きく、重なり形では結合が重なることでねじれひずみが大きくなるため、選択肢1より不安定と考えられます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 9,
    hasImage: true,
    image: "/pharmacy/104/required/q9.png",

    question:
      "ヒスタミンに含まれる複素環はどれか。1つ選べ。",

    choices: [
    "図示された複素環1",
    "図示された複素環2",
    "図示された複素環3",
    "図示された複素環4",
    "図示された複素環5"
    ],

    answer: 4,

    explanation:
      "ヒスタミンは、ヒスチジンが脱炭酸してできる生体アミンで、構造中にイミダゾール環をもつのが特徴です。イミダゾール環は、5員環の中に窒素原子を2つ含む複素環です。したがって、イミダゾール環を示す5が正答です。他の選択肢は、窒素原子の数や位置、環の大きさなどがイミダゾール環と異なるため、ヒスタミンに含まれる複素環としては適切ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 10,

    question:
      "ショウガの根茎に含まれる辛味成分はどれか。1つ選べ。",

    choices: [
    "カプサイシン",
    "[6]-ギンゲロール",
    "α-サンショオール",
    "シンナムアルデヒド",
    "ピペリン"
    ],

    answer: 1,

    explanation:
      "ショウガの根茎に含まれる代表的な辛味成分は[6]-ギンゲロールです。加熱や乾燥によりショウガオール類に変化することもあります。カプサイシンはトウガラシ、α-サンショオールはサンショウ、シンナムアルデヒドはケイヒ、ピペリンはコショウの辛味・芳香成分として整理しておくとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 11,
    hasImage: true,
    image: "/pharmacy/104/required/q11.png",

    question:
      "図は聴覚器の断面の模式図である。1〜5のうち、鼓膜はどれか。1つ選べ。",

    choices: [
    "1",
    "2",
    "3",
    "4",
    "5"
    ],

    answer: 4,

    explanation:
      "鼓膜は、外耳道の奥にあり、外耳と中耳を隔てる薄い膜です。音の振動を受けて振動し、耳小骨へ伝えます。図ではこの位置にある5が鼓膜に相当します。1〜4は、鼓膜そのものではなく、耳小骨や内耳などの周辺構造を示していると考えられるため、正答は5です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 12,

    question:
      "末梢組織から肝臓へのコレステロールの輸送を主として担う血漿リポタンパク質はどれか。1つ選べ。",

    choices: [
    "キロミクロン",
    "超低密度リポタンパク質（VLDL）",
    "中間密度リポタンパク質（IDL）",
    "低密度リポタンパク質（LDL）",
    "高密度リポタンパク質（HDL）"
    ],

    answer: 4,

    explanation:
      "末梢組織にたまったコレステロールを回収し、肝臓へ運ぶ働きは「コレステロール逆転送」と呼ばれ、主にHDLが担います。そのため正答は5です。キロミクロンは食事由来の脂質を小腸から末梢へ運び、VLDLは肝臓で合成されたトリグリセリドを末梢へ運びます。IDLはVLDLの代謝途中の粒子、LDLは主にコレステロールを肝臓から末梢組織へ運ぶため、今回の「末梢から肝臓へ」とは逆方向です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 13,
    hasImage: true,
    image: "/pharmacy/104/required/q13.png",

    question:
      "RNAを構成するD-リボースはどれか。1つ選べ。",

    choices: [
    "構造式1",
    "構造式2",
    "構造式3",
    "構造式4",
    "構造式5"
    ],

    answer: 3,

    explanation:
      "RNAを構成する糖はD-リボースで、5炭糖（アルドペントース）です。鎖状構造で考えると、アルデヒド基をもち、C2・C3・C4のOHがすべて右側にあるものがD-リボースに相当します。選択肢では構造式4がこれに当たります。ほかの構造式は、炭素数が異なる、ケトースである、またはOHの立体配置がD-リボースと異なるため該当しません。なお、DNAでは2位のOHがない2-デオキシD-リボースが用いられる点も区別しておきましょう。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 14,

    question:
      "ヒト染色体において、ヌクレオソームを形成する際に、DNAが巻きつくタンパク質はどれか。1つ選べ。",

    choices: [
    "アクチン",
    "ケラチン",
    "コラーゲン",
    "チューブリン",
    "ヒストン"
    ],

    answer: 4,

    explanation:
      "ヌクレオソームは、DNAがヒストンタンパク質に巻きついて形成される構造です。ヒストンは塩基性タンパク質で、負に帯電したDNAと結合しやすい性質があります。したがって正答は5のヒストンです。アクチンやチューブリンは細胞骨格、ケラチンは中間径フィラメント、コラーゲンは細胞外基質の主要タンパク質であり、DNAが巻きつくタンパク質ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 15,

    question:
      "母乳中で二量体として存在し、乳児の感染防御を担う免疫グロブリンはどれか。1つ選べ。",

    choices: [
    "IgA",
    "IgD",
    "IgE",
    "IgG",
    "IgM"
    ],

    answer: 0,

    explanation:
      "正答は1のIgAです。IgAは分泌型IgAとして唾液・涙・母乳などの外分泌液中に多く存在し、二量体を形成して粘膜面での感染防御に関与します。母乳中のIgAは乳児の腸管などで病原体の侵入を防ぐ働きが重要です。IgGは胎盤を通過して胎児に移行する免疫グロブリン、IgMは主に初期免疫で働く五量体、IgEはアレルギーや寄生虫感染に関与します。IgDは主にB細胞表面に存在するため、母乳中の二量体としての感染防御とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 16,

    question:
      "次のうち、食品に含まれる硝酸塩と第二級アミンから、消化の過程で胃内において生成する発がん物質はどれか。1つ選べ。",

    choices: [
    "ジメチルニトロソアミン",
    "Trp-P-1",
    "アフラトキシンB1",
    "サイカシン",
    "プタキロシド"
    ],

    answer: 0,

    explanation:
      "食品中の硝酸塩は体内で亜硝酸塩となり、胃内の酸性条件下で第二級アミンと反応してN-ニトロソアミンを生じます。代表例がジメチルニトロソアミンで、発がん性が問題となります。Trp-P-1は肉や魚の焦げなどで生じるヘテロサイクリックアミン、アフラトキシンB1はカビ毒、サイカシンはソテツ類、プタキロシドはワラビに含まれる発がん関連物質なので、本問の生成物とは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 17,

    question:
      "感染型食中毒の原因となる細菌はどれか。1つ選べ。",

    choices: [
    "Staphylococcus aureus",
    "Clostridium botulinum",
    "Aspergillus flavus",
    "Kudoa septempunctata",
    "Campylobacter jejuni"
    ],

    answer: 4,

    explanation:
      "感染型食中毒は、食品中の細菌が体内に入り、腸管内で増殖して発症するタイプです。Campylobacter jejuniは少量の菌でも感染し、下痢・腹痛・発熱などを起こす代表的な感染型食中毒菌です。Staphylococcus aureusは食品中で産生されたエンテロトキシンによる毒素型、Clostridium botulinumはボツリヌス毒素による毒素型です。Aspergillus flavusはカビでアフラトキシン産生が問題となり、Kudoa septempunctataは寄生虫で、細菌ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 18,

    question:
      "原虫を病原体とする再興感染症はどれか。1つ選べ。",

    choices: [
    "クリプトスポリジウム症",
    "マラリア",
    "重症急性呼吸器症候群（SARS）",
    "中東呼吸器症候群（MERS）",
    "コレラ"
    ],

    answer: 1,

    explanation:
      "マラリアは、原虫であるマラリア原虫（Plasmodium）を病原体とし、いったん減少しても地域によって再び問題となる再興感染症として扱われます。したがって正答は2です。クリプトスポリジウム症も原虫が原因ですが、国家試験では主に新興感染症・水系感染症として整理されることが多いです。SARS、MERSはコロナウイルスによる感染症で、原虫ではありません。コレラはコレラ菌による細菌感染症です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 19,

    question:
      "ロコモティブシンドローム（運動器症候群）の主な要因となる疾患として、最も適切なのはどれか。1つ選べ。",

    choices: [
    "脂質異常症",
    "COPD",
    "高血圧症",
    "骨粗しょう症",
    "逆流性食道炎"
    ],

    answer: 3,

    explanation:
      "ロコモティブシンドロームは、骨・関節・筋肉などの運動器の障害により、移動機能が低下した状態を指します。骨粗しょう症では骨折を起こしやすく、特に大腿骨近位部骨折や椎体骨折は歩行能力の低下につながるため、主な要因として重要です。脂質異常症や高血圧症は生活習慣病、COPDは呼吸器疾患、逆流性食道炎は消化器疾患であり、いずれもロコモの主因となる運動器疾患とは考えにくいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 20,

    question:
      "ある地域の1年間の人口動態を調べる際、必要でないのはどれか。1つ選べ。",

    choices: [
    "出生数",
    "死亡数",
    "老年人口",
    "婚姻数",
    "離婚数"
    ],

    answer: 2,

    explanation:
      "人口動態は、一定期間に発生した出生・死亡・婚姻・離婚などの「人口の動き」を把握するものです。そのため、出生数、死亡数、婚姻数、離婚数は必要な項目に含まれます。一方、老年人口はある時点での年齢別人口構成を示す「人口静態」に関する指標であり、1年間の人口動態を調べるために必須とはいえません。したがって、必要でないものは3です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 21,

    question:
      "次のうち、地球温暖化係数は最も小さいが、地球温暖化への寄与度が最も大きいのはどれか。1つ選べ。",

    choices: [
    "メタン",
    "二酸化炭素",
    "一酸化二窒素",
    "ハイドロフルオロカーボン",
    "六フッ化硫黄"
    ],

    answer: 1,

    explanation:
      "地球温暖化係数（GWP）は、二酸化炭素を基準にして温室効果の強さを表す指標で、二酸化炭素のGWPは1とされています。選択肢の中では最も小さいですが、大気中への排出量が非常に多く、地球温暖化への寄与度は最も大きいと考えられます。メタン、一酸化二窒素、ハイドロフルオロカーボン、六フッ化硫黄はいずれも二酸化炭素よりGWPは大きいものの、排出量や大気中濃度の点から、寄与度は二酸化炭素ほど大きくありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 22,

    question:
      "化学物質の審査及び製造等の規制に関する法律（化審法）で定める第一種特定化学物質はどれか。1つ選べ。",

    choices: [
    "クロロホルム",
    "四塩化炭素",
    "ポリ塩化ビフェニル",
    "2,3,7,8-テトラクロロジベンゾ-p-ジオキシン",
    "スクラロース"
    ],

    answer: 2,

    explanation:
      "第一種特定化学物質は、難分解性・高蓄積性があり、長期毒性のおそれがあるものとして、製造・輸入などが厳しく規制されます。代表例としてポリ塩化ビフェニル（PCB）があり、正答は3です。クロロホルムや四塩化炭素は有害な化学物質ですが、化審法の第一種特定化学物質の代表例としては扱いません。2,3,7,8-テトラクロロジベンゾ-p-ジオキシンは強毒性で重要ですが、主にダイオキシン類対策特別措置法で押さえます。スクラロースは甘味料であり該当しません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 23,

    question:
      "湖沼の富栄養化の進行に伴い、アオコを形成する藍藻類が産生し、肝毒性を示す物質はどれか。1つ選べ。",

    choices: [
    "ペンタクロロフェノール",
    "ジクロラミン",
    "ミクロシスチン",
    "ジェオスミン",
    "2-メチルイソボルネオール"
    ],

    answer: 2,

    explanation:
      "湖沼の富栄養化が進むと、藍藻類（シアノバクテリア）が増殖してアオコを形成します。この藍藻類の一部が産生する代表的な肝毒性物質がミクロシスチンです。したがって正答は3です。ペンタクロロフェノールは防腐剤などに関連する化学物質、ジクロラミンは消毒副生成物の一種です。ジェオスミンと2-メチルイソボルネオールは、カビ臭などの異臭味原因物質として重要ですが、肝毒性物質として問われるものではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 24,

    question:
      "体内組織の酸素欠乏を起こしやすく、建築物環境衛生管理基準が10 ppm 以下となっている室内汚染物質はどれか。1つ選べ。",

    choices: [
    "一酸化炭素",
    "二酸化炭素",
    "アンモニア",
    "二酸化窒素",
    "二酸化硫黄"
    ],

    answer: 0,

    explanation:
      "正答は1の一酸化炭素です。一酸化炭素（CO）はヘモグロビンと強く結合して酸素運搬を妨げるため、体内組織の酸素欠乏を起こしやすい物質です。建築物環境衛生管理基準でも、室内の一酸化炭素濃度は10 ppm以下とされています。2の二酸化炭素は換気状態の指標で、基準はおおむね1000 ppm以下です。3のアンモニア、4の二酸化窒素、5の二酸化硫黄は主に刺激性や呼吸器への影響が問題となりますが、本問の「酸素欠乏」と「10 ppm以下」に該当するのは一酸化炭素です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 25,

    question:
      "水域における生活環境の保全に関する環境基準において、河川にのみ定められている項目はどれか。1つ選べ。",

    choices: [
    "水素イオン濃度（pH）",
    "生物化学的酸素要求量（BOD）",
    "化学的酸素要求量（COD）",
    "浮遊物質量（SS）",
    "溶存酸素量（DO）"
    ],

    answer: 1,

    explanation:
      "河川の生活環境項目では、有機汚濁の指標として主にBOD（生物化学的酸素要求量）が用いられます。したがって、河川にのみ定められている項目としてはBODが該当します。CODは主に湖沼・海域で用いられる指標です。pH、SS、DOは河川以外の水域にも基準が定められているため、「河川にのみ」には当たりません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 26,

    question:
      "アゴニストの用量-反応曲線が低用量側にあるほど値が大きいのはどれか。1つ選べ。",

    choices: [
    "ED₅₀",
    "LD₅₀",
    "Kᴅ",
    "pA₂",
    "pD₂"
    ],

    answer: 4,

    explanation:
      "用量-反応曲線が低用量側（左側）にあるほど、少ない用量で効果が出るため効力が高いと考えます。pD₂は、50％効果を示す濃度（ED₅₀またはEC₅₀）の負の対数で表されるため、ED₅₀が小さいほどpD₂は大きくなります。したがって正答は5です。1のED₅₀は左にあるほど小さくなります。2のLD₅₀は致死量に関する指標です。3のKᴅは受容体との親和性の指標で、用量-反応曲線の位置そのものを表す指標ではありません。4のpA₂は拮抗薬の強さを表す指標です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 27,

    question:
      "ムスカリン性アセチルコリン受容体を選択的に刺激することで、消化管や膀胱の運動を亢進するのはどれか。1つ選べ。",

    choices: [
    "ベタネコール",
    "オキシブチニン",
    "チオトロピウム",
    "ネオスチグミン",
    "ピレンゼピン"
    ],

    answer: 0,

    explanation:
      "ベタネコールは、ムスカリン性アセチルコリン受容体を比較的選択的に刺激するコリン作動薬で、消化管運動や膀胱平滑筋の収縮を促進します。そのため、術後の腸管麻痺や尿閉などで用いられることがあります。オキシブチニンは抗ムスカリン薬で過活動膀胱に用いられ、膀胱収縮を抑えます。チオトロピウムも抗ムスカリン薬で、主にCOPDなどで気管支拡張に用いられます。ネオスチグミンはコリンエステラーゼ阻害薬で、間接的にアセチルコリン作用を増強しますが、受容体を選択的に直接刺激する薬ではありません。ピレンゼピンはM1受容体遮断薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 28,

    question:
      "自律神経節を遮断した時、交感神経節後線維の神経終末からのアセチルコリンの遊離が低下する効果器として、最も適切なのはどれか。1つ選べ。",

    choices: [
    "心臓",
    "汗腺",
    "毛様体",
    "消化管",
    "瞳孔"
    ],

    answer: 1,

    explanation:
      "自律神経節遮断薬は、節前線維から節後線維への伝達を遮断するため、節後線維終末からの伝達物質放出が低下します。交感神経節後線維は多くの場合ノルアドレナリンを放出しますが、例外的に汗腺ではアセチルコリンを放出します。したがって、該当する効果器は汗腺です。心臓や瞳孔散大筋などの交感神経支配では主にノルアドレナリンが関与します。毛様体や消化管でのアセチルコリンは主に副交感神経の作用として考えます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 29,

    question:
      "メラトニン受容体を刺激することで不眠症における入眠困難を改善するのはどれか。1つ選べ。",

    choices: [
    "ブロモバレリル尿素",
    "ゾルピデム",
    "スボレキサント",
    "リルマザホン",
    "ラメルテオン"
    ],

    answer: 4,

    explanation:
      "ラメルテオンは、メラトニンMT1・MT2受容体を刺激し、体内時計に関わる睡眠リズムを整えることで、主に入眠困難を改善する薬です。したがって正答は5です。ゾルピデムはベンゾジアゼピン受容体（ω1）に作用する非ベンゾジアゼピン系睡眠薬、リルマザホンはベンゾジアゼピン系睡眠薬に分類されます。スボレキサントはオレキシン受容体拮抗薬で、覚醒を抑えることで睡眠を促します。ブロモバレリル尿素は古いタイプの催眠鎮静薬で、メラトニン受容体刺激薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 30,

    question:
      "主に電位依存性Na+チャネルを遮断することで抗てんかん作用を示すのはどれか。1つ選べ。",

    choices: [
    "エトスクシミド",
    "ジアゼパム",
    "ラモトリギン",
    "ガバペンチン",
    "フェノバルビタール"
    ],

    answer: 2,

    explanation:
      "ラモトリギンは、主に電位依存性Na+チャネルを遮断し、神経細胞の過剰な興奮やグルタミン酸放出を抑えることで抗てんかん作用を示すため、正答は3です。エトスクシミドは主にT型Ca2+チャネル抑制、ジアゼパムとフェノバルビタールはGABAA受容体を介した抑制性神経伝達の増強が中心です。ガバペンチンはCa2+チャネルのα2δサブユニットに作用するとされ、Na+チャネル遮断が主作用ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 31,

    question:
      "Ca2+チャネルを遮断することで抗不整脈作用を示すのはどれか。1つ選べ。",

    choices: [
    "アテノロール",
    "フレカイニド",
    "リドカイン",
    "ソタロール",
    "ベラパミル"
    ],

    answer: 4,

    explanation:
      "ベラパミルは非ジヒドロピリジン系Ca2+チャネル遮断薬で、主に房室結節の伝導を抑えることで抗不整脈作用を示します。特に上室性頻脈などで重要です。アテノロールはβ1遮断薬、フレカイニドはNa+チャネル遮断薬（Ic群）、リドカインはNa+チャネル遮断薬（Ib群）、ソタロールは主にK+チャネル遮断作用に加えてβ遮断作用をもつ薬です。したがって、Ca2+チャネル遮断による抗不整脈薬はベラパミルです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 32,

    question:
      "γ-アミノ酪酸 GABA_A 受容体のベンゾジアゼピン結合部位に結合し、ベンゾジアゼピン系薬による呼吸抑制を改善するのはどれか。1つ選べ。",

    choices: [
    "デキストロメトルファン",
    "アセチルシステイン",
    "ドキサプラム",
    "フルマゼニル",
    "イプラトロピウム"
    ],

    answer: 3,

    explanation:
      "正答は4のフルマゼニルです。フルマゼニルはGABA_A受容体のベンゾジアゼピン結合部位に競合的に結合し、ベンゾジアゼピン系薬の作用を拮抗するため、過量投与時の鎮静や呼吸抑制の改善に用いられます。1のデキストロメトルファンは鎮咳薬、2のアセチルシステインは去痰薬・アセトアミノフェン中毒の解毒薬、3のドキサプラムは呼吸中枢刺激薬ですがベンゾジアゼピン受容体拮抗薬ではありません。5のイプラトロピウムは抗コリン作用をもつ気管支拡張薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 33,

    question:
      "モサプリドによる消化管運動亢進の作用機序はどれか。1つ選べ。",

    choices: [
    "セロトニン 5-HT_3 受容体遮断",
    "セロトニン 5-HT_4 受容体刺激",
    "オピオイド μ 受容体刺激",
    "アセチルコリンエステラーゼ阻害",
    "ムスカリン性アセチルコリン M_3 受容体刺激"
    ],

    answer: 1,

    explanation:
      "モサプリドは、消化管のセロトニン5-HT4受容体を刺激することで、アセチルコリンの遊離を促進し、消化管運動を亢進させる薬です。したがって正答は2です。1の5-HT3受容体遮断は制吐薬などで重要な作用です。3のオピオイドμ受容体刺激は一般に腸管運動を抑制し、便秘の原因になります。4のアセチルコリンエステラーゼ阻害はネオスチグミンなどの作用、5のM3受容体刺激は直接的なコリン作動薬のイメージであり、モサプリドの主作用ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 34,

    question:
      "カモスタットの急性膵炎治療効果に関わる作用機序はどれか。1つ選べ。",

    choices: [
    "H^+, K^+-ATPase 阻害",
    "セロトニン 5-HT_3 受容体遮断",
    "ヒスタミン H_2 受容体遮断",
    "タンパク質分解酵素阻害",
    "シクロオキシゲナーゼ阻害"
    ],

    answer: 3,

    explanation:
      "カモスタットはメシル酸カモスタットとして用いられるタンパク質分解酵素阻害薬です。トリプシンなどの膵酵素の働きを抑え、膵臓の自己消化や炎症の進行を抑えることが膵炎治療に関わります。したがって正答は4です。1のH+,K+-ATPase阻害はプロトンポンプ阻害薬、2の5-HT3受容体遮断は制吐薬、3のH2受容体遮断は胃酸分泌抑制薬、5のシクロオキシゲナーゼ阻害はNSAIDsの作用であり、カモスタットの主作用ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 35,

    question:
      "キサンチンオキシダーゼを選択的に阻害するのはどれか。1つ選べ。",

    choices: [
    "ベンズブロマロン",
    "アロプリノール",
    "コルヒチン",
    "ラスブリカーゼ",
    "プロベネシド"
    ],

    answer: 1,

    explanation:
      "アロプリノールは、体内でオキシプリノールとなり、キサンチンオキシダーゼを阻害して尿酸産生を低下させる薬です。そのため正答は2です。ベンズブロマロンとプロベネシドは尿酸排泄促進薬で、主に尿細管での尿酸再吸収を抑えます。コルヒチンは痛風発作時の炎症を抑える薬で、尿酸値を直接下げる薬ではありません。ラスブリカーゼは尿酸を分解する酵素製剤で、キサンチンオキシダーゼ阻害薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 36,

    question:
      "サルポグレラートによる血小板凝集抑制の作用機序はどれか。1つ選べ。",

    choices: [
    "プロスタノイド IP 受容体刺激",
    "セロトニン 5-HT2 受容体遮断",
    "シクロオキシゲナーゼ阻害",
    "ホスホジエステラーゼⅢ阻害",
    "トロンボキサン合成酵素阻害"
    ],

    answer: 1,

    explanation:
      "サルポグレラートは、血小板や血管平滑筋にあるセロトニン5-HT2受容体を遮断し、セロトニンによる血小板凝集や血管収縮を抑える薬です。したがって正答は2です。1のIP受容体刺激はベラプロストなど、3のシクロオキシゲナーゼ阻害はアスピリン、4のホスホジエステラーゼⅢ阻害はシロスタゾール、5のトロンボキサン合成酵素阻害はオザグレルの作用機序として整理しておくとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 37,

    question:
      "TNF-αに特異的に結合することで、TNF-αとその受容体の結合を阻害するのはどれか。1つ選べ。",

    choices: [
    "インフリキシマブ",
    "プレドニゾロン",
    "トシリズマブ",
    "アバタセプト",
    "トファシチニブ"
    ],

    answer: 0,

    explanation:
      "インフリキシマブは抗TNF-αモノクローナル抗体で、TNF-αに特異的に結合し、TNF受容体への結合を阻害します。関節リウマチなどの炎症性疾患で用いられます。プレドニゾロンは副腎皮質ステロイド、トシリズマブは抗IL-6受容体抗体、アバタセプトはT細胞の共刺激を抑える薬、トファシチニブはJAK阻害薬であり、いずれもTNF-αに直接結合する薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 38,

    question:
      "プロスタノイド TP 受容体を遮断することで、抗アレルギー作用を示すのはどれか。1つ選べ。",

    choices: [
    "プランルカスト",
    "オザグレル",
    "セラトロダスト",
    "クロモグリク酸",
    "メキタジン"
    ],

    answer: 2,

    explanation:
      "正答は3のセラトロダストです。セラトロダストは、トロンボキサンA2などが作用するプロスタノイドTP受容体を遮断し、気道収縮や炎症反応を抑えることで抗アレルギー作用を示します。1のプランルカストはロイコトリエン受容体拮抗薬、2のオザグレルはトロンボキサンA2合成酵素阻害薬で、TP受容体遮断ではありません。4のクロモグリク酸は肥満細胞からの化学伝達物質遊離を抑制し、5のメキタジンはH1受容体遮断薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 39,

    question:
      "アンピシリンによる抗菌作用の標的はどれか。1つ選べ。",

    choices: [
    "細胞膜リン脂質",
    "DNA 依存性 RNA ポリメラーゼ",
    "リボソーム 30S サブユニット",
    "リボソーム 50S サブユニット",
    "トランスペプチダーゼ"
    ],

    answer: 4,

    explanation:
      "アンピシリンはβ-ラクタム系抗菌薬で、細菌の細胞壁合成に関わるトランスペプチダーゼ（PBP）を阻害します。その結果、ペプチドグリカンの架橋形成が妨げられ、抗菌作用を示します。したがって正答は5です。1の細胞膜リン脂質はポリミキシン系など、2のDNA依存性RNAポリメラーゼはリファンピシン、3の30Sサブユニットはアミノグリコシド系・テトラサイクリン系、4の50Sサブユニットはマクロライド系などの標的として整理します。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 40,
    hasImage: true,
    image: "/pharmacy/104/required/q40.png",

    question:
      "以下に示す化学構造の薬物が結合し、鎮痛作用を引き起こす作用点はどれか。1つ選べ。",

    choices: [
    "γ-アミノ酪酸 GABA_A 受容体-Cl^-チャネル複合体",
    "ドパミン D_2 受容体",
    "オピオイド μ 受容体",
    "ムスカリン性アセチルコリン受容体",
    "シクロオキシゲナーゼ"
    ],

    answer: 2,

    explanation:
      "示された構造は、モルヒネ様のオピオイド鎮痛薬に特徴的な構造と考えられます。オピオイド鎮痛薬は主にオピオイド μ 受容体に結合し、痛みの伝達を抑制して鎮痛作用を示します。したがって正答は3です。1のGABA_A受容体はベンゾジアゼピン系など、2のD2受容体は抗精神病薬など、4のムスカリン受容体は副交感神経系の薬物、5のシクロオキシゲナーゼはNSAIDsの主な作用点として押さえます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 41,

    question:
      "経口投与された薬物のバイオアベイラビリティを表す式はどれか。1つ選べ。ただし、消化管管腔内からの吸収率を Fa、消化管及び肝臓での消失を免れた割合をそれぞれ Fg 及び Fh とする。",

    choices: [
    "Fa・Fg/Fh",
    "Fa・Fg・Fh",
    "Fa・Fg・(1−Fh)",
    "Fa・(Fg＋Fh)",
    "Fa＋Fg＋Fh"
    ],

    answer: 1,

    explanation:
      "経口投与後に全身循環へ到達する割合（バイオアベイラビリティ）は、①消化管から吸収される割合 Fa、②消化管で消失を免れる割合 Fg、③肝臓で初回通過効果を免れる割合 Fh をすべて通過した分として考えるため、F＝Fa・Fg・Fh となります。よって正答は2です。1はFhで割っており不適切、3の(1−Fh)は肝臓で消失した割合を表す方向になります。4、5のように加算して求めるものではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 42,

    question:
      "一次性能動輸送担体はどれか。1つ選べ。",

    choices: [
    "グルコーストランスポーター GLUT1",
    "P-糖タンパク質 MDR1",
    "有機アニオントランスポーター OAT1",
    "H+/ペプチド共輸送体 PEPT1",
    "Na+/グルコース共輸送体 SGLT2"
    ],

    answer: 1,

    explanation:
      "一次性能動輸送担体は、ATPの加水分解エネルギーを直接利用して物質を輸送する担体です。P-糖タンパク質（MDR1）はABCトランスポーターの一種で、ATPを利用して薬物などを細胞外へ排出するため、一次性能動輸送担体に該当します。GLUT1は濃度勾配に従う促進拡散、OAT1はイオン勾配を利用する二次性能動輸送、PEPT1はH+勾配、SGLT2はNa+勾配を利用する二次性能動輸送として整理されます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 43,

    question:
      "母体から胎児への移行性が最も低いのはどれか。1つ選べ。",

    choices: [
    "インスリン",
    "エタノール",
    "グルコース",
    "チオペンタール",
    "バルプロ酸"
    ],

    answer: 0,

    explanation:
      "母体から胎児への移行性は、一般に分子量が小さく脂溶性が高い薬物ほど高くなります。インスリンはペプチド性ホルモンで分子量が大きく、胎盤を通過しにくいため、胎児への移行性は最も低いと考えられます。エタノールは小分子で胎盤を通過しやすく、グルコースは胎児の栄養源として輸送体を介して移行します。チオペンタールは脂溶性が高く胎盤移行しやすい薬物です。バルプロ酸も胎盤を通過し、催奇形性が問題となるため、インスリンとは異なります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 44,

    question:
      "体内からの消失が主に CYP1A2 による代謝である薬物はどれか。1つ選べ。",

    choices: [
    "テオフィリン",
    "デキストロメトルファン",
    "ファモチジン",
    "フェロジピン",
    "ワルファリン"
    ],

    answer: 0,

    explanation:
      "テオフィリンは、主に肝臓の CYP1A2 により代謝されて消失する薬物として重要です。喫煙により CYP1A2 が誘導され、血中濃度が低下しやすい点も国家試験でよく問われます。デキストロメトルファンは主に CYP2D6、フェロジピンは主に CYP3A4、ワルファリンは特に S体が CYP2C9 で代謝されます。ファモチジンは代謝よりも腎排泄の寄与が大きい薬物です。したがって、正答はテオフィリンです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 45,

    question:
      "ネフロンでの能動的な薬物の分泌を行う主要な部位はどれか。1つ選べ。",

    choices: [
    "遠位尿細管",
    "近位尿細管",
    "糸球体",
    "ヘンレ係蹄上行脚",
    "ボーマン嚢"
    ],

    answer: 1,

    explanation:
      "能動的な薬物分泌の主要部位は近位尿細管です。近位尿細管には有機アニオン輸送系や有機カチオン輸送系などのトランスポーターがあり、ペニシリンなど多くの薬物を血液側から尿細管腔内へ分泌します。糸球体は主にろ過、ボーマン嚢はろ過された原尿を受ける部位です。遠位尿細管やヘンレ係蹄上行脚も水・電解質調節に関与しますが、薬物の能動的分泌の中心ではないと考えます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 46,

    question:
      "体内動態が線形1-コンパートメントモデルに従う薬物100 mgを急速静脈内投与したとき、投与直後の血中濃度が2 mg/L、消失速度定数が0.1 hr−1であった。この薬物の全身クリアランス（L/hr）はどれか。1つ選べ。",

    choices: [
    "0.2",
    "2",
    "5",
    "7",
    "20"
    ],

    answer: 2,

    explanation:
      "急速静脈内投与の1-コンパートメントモデルでは、投与直後濃度 C0 から分布容積 Vd を求め、全身クリアランス CL＝消失速度定数 k × Vd で計算します。Vd＝投与量/C0＝100 mg ÷ 2 mg/L＝50 L。したがって、CL＝0.1 hr−1 × 50 L＝5 L/hr となり、正答は3です。ほかの選択肢は、投与量・濃度・消失速度定数の組合せを誤って計算した値と考えられます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 47,
    hasImage: true,
    image: "/pharmacy/104/required/q47.png",

    question:
      "体内動態が線形1-コンパートメントモデルに従う薬物を静脈内定速注入したとき、血中濃度は下図のような推移を示した。この薬物の消失半減期（hr）に最も近い値はどれか。1つ選べ。",

    choices: [
    "2",
    "4",
    "6",
    "8",
    "10"
    ],

    answer: 0,

    explanation:
      "静脈内定速注入では、血中濃度は定常状態濃度（Css）に指数関数的に近づきます。1-コンパートメントモデルでは、注入開始から1半減期でCssの約50％、2半減期で約75％、3半減期で約87.5％に達します。図では、定常状態濃度の約半分に達する時刻が約2時間と読み取れるため、消失半減期は約2 hrと考えられます。したがって正答は1です。4、6、8、10 hrでは、Cssの50％に達する時刻がもっと遅くなるため、図の推移とは合いにくいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 48,

    question:
      "治療薬物モニタリング（TDM）の実施が推奨される薬物はどれか。1つ選べ。",

    choices: [
    "イトラコナゾール",
    "オメプラゾール",
    "バンコマイシン",
    "ベラパミル",
    "モルヒネ"
    ],

    answer: 2,

    explanation:
      "TDMは、有効域と中毒域が近い薬物や、血中濃度の個人差が大きい薬物で特に重要です。バンコマイシンは腎機能により血中濃度が変動しやすく、腎障害などの副作用を避けつつ有効性を確保するため、TDMが推奨されます。イトラコナゾールは場合により濃度確認が行われることはありますが、国家試験で代表的なTDM対象薬としてはバンコマイシンが基本です。オメプラゾール、ベラパミル、モルヒネは通常、血中濃度を日常的に測定して投与量を調節する薬物としては扱われません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 49,

    question:
      "日本薬局方に基づき、溶液の濃度を（1→10）で表したときの意味として正しいのはどれか。1つ選べ。",

    choices: [
    "固形の薬品1 gを溶媒10 mLに溶かす。",
    "液状の薬品1 gを溶媒10 mLに溶かす。",
    "固形の薬品1 gを溶媒に溶かして全量を10 gにする。",
    "液状の薬品1 gを溶媒に溶かして全量を10 gにする。",
    "固形の薬品1 gを溶媒に溶かして全量を10 mLにする。"
    ],

    answer: 4,

    explanation:
      "日本薬局方で濃度を（1→10）と表す場合、固形の薬品では「薬品1 gを溶媒に溶かして全量を10 mLにする」という意味です。したがって正答は5です。1は溶媒を10 mL加えるという意味で、最終容量が10 mLとは限らないため異なります。2、4は液状薬品を1 gとしており、通常は液状では体積を用いる点で不適切です。3は全量を10 gにしており、質量ではなく容量で表す点が違います。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 50,

    question:
      "点眼剤の保存剤として利用される陽イオン性界面活性剤はどれか。1つ選べ。",

    choices: [
    "ラウリル硫酸ナトリウム",
    "レシチン",
    "タウロコール酸",
    "ベンザルコニウム塩化物",
    "ラウロマクロゴール"
    ],

    answer: 3,

    explanation:
      "点眼剤の保存剤としてよく用いられる陽イオン性界面活性剤は、ベンザルコニウム塩化物です。陽イオン性界面活性剤は殺菌作用を示すものがあり、ベンザルコニウム塩化物は点眼剤の防腐・保存目的で頻出です。1のラウリル硫酸ナトリウムは陰イオン性界面活性剤、2のレシチンは両性界面活性剤、3のタウロコール酸は胆汁酸系の陰イオン性界面活性剤、5のラウロマクロゴールは非イオン性界面活性剤に分類されます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 51,

    question:
      "せん断応力の増加に伴い、みかけ粘度が増大するのはどれか。1つ選べ。",

    choices: [
    "ビンガム流動",
    "準塑性流動",
    "ダイラタント流動",
    "準粘性流動",
    "ニュートン流動"
    ],

    answer: 2,

    explanation:
      "せん断応力（またはせん断速度）が大きくなるほど、みかけ粘度が増大する流動はダイラタント流動です。濃厚な懸濁液などでみられ、力を加えるほど流れにくくなる「せん断増粘」と考えると覚えやすいです。準塑性流動は逆に、せん断によりみかけ粘度が低下します。ニュートン流動では粘度は一定です。ビンガム流動は降伏値を超えると流動し、みかけ粘度が単純に増大するタイプではありません。準粘性流動も本問の特徴には該当しません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 52,

    question:
      "皮膚に適用する液剤はどれか。1つ選べ。",

    choices: [
    "エリキシル剤",
    "シロップ剤",
    "パップ剤",
    "リニメント剤",
    "リモナーデ剤"
    ],

    answer: 3,

    explanation:
      "正答は4のリニメント剤です。リニメント剤は、皮膚に塗擦して用いる液状または半固形状の外用剤で、皮膚適用の液剤に分類されます。1のエリキシル剤、2のシロップ剤、5のリモナーデ剤はいずれも主に内用の液剤です。3のパップ剤は有効成分を含む基剤を布などに展延した貼付剤であり、液剤ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 53,

    question:
      "日本薬局方に規定されている全ての注射剤の安全性の確保に必須なのはどれか。1つ選べ。",

    choices: [
    "等張化剤の添加",
    "着色剤の添加",
    "保存剤の添加",
    "エンドトキシンの除去",
    "無菌性の保証"
    ],

    answer: 4,

    explanation:
      "注射剤は体内に直接投与されるため、感染を防ぐうえで「無菌性の保証」が全ての注射剤に必須と考えられます。したがって正答は5です。1の等張化剤は必要に応じて添加されますが、全ての注射剤に必須ではありません。2の着色剤は通常、注射剤では使用が制限されます。3の保存剤も単回使用製剤などでは不要で、むしろ添加できない場合があります。4のエンドトキシン対策は重要ですが、「除去」が全ての注射剤に必須という表現ではなく、試験や管理により安全性を確保します。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 54,

    question:
      "日本薬局方の溶出試験法が適用されるのはどれか。1つ選べ。",

    choices: [
    "透析用剤",
    "坐剤",
    "軟膏剤",
    "点耳剤",
    "散剤"
    ],

    answer: 4,

    explanation:
      "日本薬局方の溶出試験法は、主に経口固形製剤から有効成分がどの程度溶け出すかを確認する試験です。散剤は経口固形製剤に含まれるため、適用対象となります。透析用剤や点耳剤は液状製剤、坐剤は直腸などに適用する製剤、軟膏剤は半固形製剤であり、通常この溶出試験法の対象とは考えません。したがって、正答は5の散剤です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 55,

    question:
      "消化管吸収後、体内でCYP2A6によって代謝され、抗悪性腫瘍作用を示すプロドラッグはどれか。1つ選べ。",

    choices: [
    "テガフール",
    "イリノテカン",
    "ドキシフルリジン",
    "サラゾスルファピリジン",
    "アラセプリル"
    ],

    answer: 0,

    explanation:
      "正答は1のテガフールです。テガフールは消化管から吸収された後、主に肝臓のCYP2A6により代謝され、活性本体である5-FUとなって抗悪性腫瘍作用を示すプロドラッグです。イリノテカンはカルボキシルエステラーゼでSN-38に変換されます。ドキシフルリジンも5-FU系プロドラッグですが、主にピリミジンヌクレオシドホスホリラーゼで変換されます。サラゾスルファピリジンは腸内細菌で分解される抗炎症薬、アラセプリルはACE阻害薬のプロドラッグであり、抗悪性腫瘍薬ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 56,

    question:
      "腎機能の低下などにより尿量が減少する症候はどれか。1つ選べ。",

    choices: [
    "残尿",
    "尿失禁",
    "乏尿",
    "尿閉",
    "血尿"
    ],

    answer: 2,

    explanation:
      "腎機能の低下や脱水、循環血液量の低下などにより尿の産生量が減少する状態は「乏尿」です。一般に1日尿量が少ない状態を指し、腎機能低下の症候として重要です。残尿は排尿後に膀胱内に尿が残ること、尿失禁は意思に反して尿が漏れること、尿閉は尿が作られていても排出できない状態、血尿は尿中に血液が混じる状態をいいます。したがって正答は3です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 57,

    question:
      "肝硬変で高値を示す検査値はどれか。1つ選べ。",

    choices: [
    "血小板数",
    "血清アルブミン濃度",
    "血清総コレステロール濃度",
    "血清γ-グロブリン濃度",
    "血清コリンエステラーゼ活性"
    ],

    answer: 3,

    explanation:
      "肝硬変では、慢性炎症や免疫反応の亢進により血清γ-グロブリン濃度が高値を示しやすいため、正答は4です。一方、肝臓の合成能が低下するため、血清アルブミン濃度、血清総コレステロール濃度、血清コリンエステラーゼ活性は低下しやすいです。また、門脈圧亢進による脾機能亢進などで血小板数も低下しやすくなります。肝硬変では「γ-グロブリン上昇、アルブミン・コリンエステラーゼ・血小板低下」と整理しておくとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 58,
    hasImage: true,
    image: "/pharmacy/104/required/q58.png",

    question:
      "第Ⅱ誘導により得られた心電図（下図）において、QT間隔に当たるのはどれか。1つ選べ。",

    choices: [
    "a～d間",
    "a～e間",
    "b～d間",
    "b～e間",
    "c～d間"
    ],

    answer: 1,

    explanation:
      "QT間隔は、心室の興奮開始から再分極終了までの時間を表し、心電図ではQRS波の始まりからT波の終わりまでを指します。この図では、QRS波の開始がa、T波の終了がeに相当するため、a～e間がQT間隔です。a～d間はT波の終わりまで含まず、b～e間やb～d間はQRS波の開始を含みません。c～d間は主にST～T波の一部であり、QT間隔とはいえません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 59,

    question:
      "食道がんの腫瘍マーカーとして有用なのはどれか。1つ選べ。",

    choices: [
    "AFP",
    "NSE",
    "SCC抗原",
    "PIVKA-II",
    "CA 15-3"
    ],

    answer: 2,

    explanation:
      "食道がんは、日本では扁平上皮がんが多く、扁平上皮がんの腫瘍マーカーとしてSCC抗原が用いられるため、正答は3です。AFPとPIVKA-IIは主に肝細胞がん、NSEは小細胞肺がんや神経内分泌腫瘍、CA 15-3は乳がんで参考にされる腫瘍マーカーです。腫瘍マーカーは診断の決め手というより、治療効果判定や経過観察に使われる点も押さえておきましょう。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 60,

    question:
      "右心不全を伴わない左心不全の主な症状に該当しないのはどれか。1つ選べ。",

    choices: [
    "急性肺水腫",
    "下肢浮腫",
    "呼吸困難",
    "血圧低下",
    "尿量減少"
    ],

    answer: 1,

    explanation:
      "左心不全では、左心系のポンプ機能低下により肺うっ血が起こりやすく、呼吸困難や急性肺水腫が主な症状としてみられます。また、心拍出量の低下により血圧低下や腎血流低下による尿量減少も起こり得ます。一方、下肢浮腫は主に右心不全で体静脈うっ血が生じたときにみられる症状です。したがって、右心不全を伴わない左心不全の主な症状に該当しないものは下肢浮腫です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 61,

    question:
      "てんかん発作のうち、意識障害を伴わないのはどれか。1つ選べ。",

    choices: [
    "脱力発作",
    "単純部分発作",
    "欠神発作",
    "複雑部分発作",
    "強直間代発作"
    ],

    answer: 1,

    explanation:
      "意識障害を伴わない発作として代表的なのは、単純部分発作です。部分発作のうち、意識が保たれるものを単純部分発作、意識障害を伴うものを複雑部分発作と考えると整理しやすいです。欠神発作は短時間の意識消失が特徴で、強直間代発作も意識消失を伴うことが多いです。脱力発作は突然筋緊張が低下して倒れる発作で、意識障害を伴う場合があります。したがって、正答は2です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 62,

    question:
      "客観的な危険が存在しないのに、急な不安に襲われ、動悸、呼吸困難、めまいなどの自律神経症状を伴い、通常30分以内に症状が改善する不安神経症はどれか。1つ選べ。",

    choices: [
    "全般性不安障害",
    "外傷後ストレス障害",
    "強迫性障害",
    "パニック障害",
    "解離性障害"
    ],

    answer: 3,

    explanation:
      "正答は4のパニック障害です。パニック障害では、明らかな危険がない状況で突然強い不安（パニック発作）が起こり、動悸、息苦しさ、めまい、発汗などの自律神経症状を伴います。発作は比較的短時間でピークに達し、多くは30分以内に軽快する点が特徴です。1の全般性不安障害は、日常のさまざまなことへの過度な不安が長期間続く状態です。2の外傷後ストレス障害は、強い心的外傷体験後の再体験や回避が中心です。3の強迫性障害は、強迫観念や強迫行為がみられます。5の解離性障害は、記憶や意識、自己同一性のまとまりが障害される状態です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 63,

    question:
      "細菌感染が原因となる皮膚疾患はどれか。1つ選べ。",

    choices: [
    "蜂窩織炎",
    "アトピー性皮膚炎",
    "尋常性乾癬",
    "帯状疱疹",
    "じん麻疹"
    ],

    answer: 0,

    explanation:
      "蜂窩織炎は、主に黄色ブドウ球菌や溶血性レンサ球菌などの細菌が皮膚の深部に感染して起こる皮膚疾患であり、正答は1です。発赤、腫脹、疼痛、熱感などがみられます。アトピー性皮膚炎はアレルギー素因や皮膚バリア機能異常、尋常性乾癬は免疫異常が関与する慢性炎症性疾患です。帯状疱疹は水痘・帯状疱疹ウイルスによる疾患、じん麻疹はヒスタミンなどによる一過性の膨疹が特徴で、いずれも細菌感染が主因ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 64,

    question:
      "免疫複合体が組織に沈着することによって引き起こされるアレルギー反応の型はどれか。1つ選べ。",

    choices: [
    "Ⅰ型",
    "Ⅱ型",
    "Ⅲ型",
    "Ⅳ型",
    "Ⅰ型とⅡ型の複合型"
    ],

    answer: 2,

    explanation:
      "免疫複合体（抗原抗体複合体）が血管壁や腎糸球体などの組織に沈着し、補体活性化や炎症を起こす反応はⅢ型アレルギーです。代表例として、血清病、全身性エリテマトーデス（SLE）、糸球体腎炎などが挙げられます。Ⅰ型はIgEが関与する即時型反応、Ⅱ型は細胞表面抗原に対する抗体による細胞障害、Ⅳ型はT細胞が関与する遅延型反応です。したがって、正答は3のⅢ型です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 65,

    question:
      "がんに伴う疼痛のうち、プレガバリンが最も有効なのはどれか。1つ選べ。",

    choices: [
    "神経障害による痛み",
    "臓器へのがん浸潤による痛み",
    "術後の創部の痛み",
    "消化管閉塞による痛み",
    "骨転移による痛み"
    ],

    answer: 0,

    explanation:
      "プレガバリンは、電位依存性Ca2＋チャネルのα2δサブユニットに結合し、神経伝達物質の放出を抑えることで鎮痛効果を示します。特に、しびれ・灼熱感・電撃痛などを伴う神経障害性疼痛に用いられるため、最も有効なのは「神経障害による痛み」です。臓器浸潤や消化管閉塞による痛みは内臓痛、術後創部や骨転移による痛みは主に侵害受容性疼痛であり、NSAIDsやオピオイドなどが中心となるため、プレガバリンが第一に選ばれる痛みとはいえません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 66,

    question:
      "菌交代現象による偽膜性大腸炎の代表的な起因菌はどれか。1つ選べ。",

    choices: [
    "Streptococcus pneumoniae",
    "Clostridium difficile",
    "Mycobacterium tuberculosis",
    "Salmonella typhi",
    "Vibrio cholerae"
    ],

    answer: 1,

    explanation:
      "偽膜性大腸炎は、抗菌薬の使用により腸内細菌叢が乱れ、菌交代現象としてClostridium difficileが増殖することで起こる代表的な疾患です。C. difficileは毒素を産生し、大腸炎や下痢の原因となります。1のStreptococcus pneumoniaeは主に肺炎や髄膜炎、3のMycobacterium tuberculosisは結核、4のSalmonella typhiは腸チフス、5のVibrio choleraeはコレラの原因菌であり、偽膜性大腸炎の代表的起因菌ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 67,

    question:
      "要指導医薬品及び一般用医薬品の添付文書への記載項目に該当しないのはどれか。1つ選べ。",

    choices: [
    "製品の特徴",
    "使用上の注意",
    "効能又は効果",
    "臨床成績",
    "用法及び用量"
    ],

    answer: 3,

    explanation:
      "要指導医薬品・一般用医薬品の添付文書には、使用者が適正に使えるように「製品の特徴」「使用上の注意」「効能又は効果」「用法及び用量」などが記載されます。一方、「臨床成績」は主に医療用医薬品の添付文書などで扱われる内容であり、要指導医薬品・一般用医薬品の添付文書の記載項目としては通常該当しません。したがって、正答は4です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 68,

    question:
      "学術論文収載雑誌の評価指標で、掲載された研究論文の被引用数に基づいて算出される値はどれか。1つ選べ。",

    choices: [
    "リスクファクター",
    "インパクトファクター",
    "国際標準図書番号（ISBN）",
    "デジタルオブジェクト識別子（DOI）",
    "フェイススケール"
    ],

    answer: 1,

    explanation:
      "正答は2のインパクトファクターです。インパクトファクターは、学術雑誌に掲載された論文が一定期間にどれだけ引用されたかをもとに算出される指標で、雑誌の影響度を評価する際に用いられます。1のリスクファクターは疾患などの危険因子、3のISBNは書籍を識別する番号、4のDOIは論文などの電子資料を一意に識別する記号です。5のフェイススケールは痛みなどを表情で評価する尺度であり、雑誌評価の指標ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 69,

    question:
      "気管支喘息の発作治療薬（リリーバー）として用いられる薬物はどれか。1つ選べ。",

    choices: [
    "フルチカゾンプロピオン酸エステル",
    "カルテオロール塩酸塩",
    "アゼラスチン塩酸塩",
    "モンテルカストナトリウム",
    "プロカテロール塩酸塩水和物"
    ],

    answer: 4,

    explanation:
      "発作治療薬（リリーバー）は、喘息発作時に気管支を速やかに拡張して症状を改善する薬です。プロカテロール塩酸塩水和物はβ2受容体刺激薬で、気管支平滑筋を弛緩させるため、発作時の治療に用いられます。フルチカゾンは吸入ステロイドで長期管理薬、モンテルカストはロイコトリエン受容体拮抗薬で予防・維持療法に用いられます。アゼラスチンは抗アレルギー薬、カルテオロールはβ遮断薬であり、喘息発作治療薬としては適しません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 70,

    question:
      "問題志向型システム（POS）による問題解決の過程として、該当しないのはどれか。1つ選べ。",

    choices: [
    "患者情報の収集",
    "情報の公開",
    "問題の明確化",
    "初期計画の立案",
    "計画の実施"
    ],

    answer: 1,

    explanation:
      "POS（問題志向型システム）は、患者の問題点に基づいて医療を進める考え方です。一般的な流れは、①患者情報の収集、②問題の明確化（問題リスト作成）、③初期計画の立案、④計画の実施・評価です。したがって、1、3、4、5はPOSによる問題解決の過程に含まれます。一方、情報の公開はPOSの過程そのものではなく、患者情報は守秘義務のもと適切に管理されるべきものです。よって、該当しないのは2です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 71,

    question:
      "薬剤師に関する記述のうち、正しいのはどれか。1つ選べ。",

    choices: [
    "薬剤師の免許の効力は、薬剤師国家試験に合格した時から生じる。",
    "薬剤師以外の者が調剤を行うことは、例外なく禁止されている。",
    "薬剤師名簿への登録を行えば、自動的に保険薬剤師として登録される。",
    "薬剤師でなければ、薬剤師又はこれにまぎらわしい名称を用いてはならない。",
    "薬剤師の品位を損するような行為を行っても、免許を取り消されることはない。"
    ],

    answer: 3,

    explanation:
      "正答は4です。薬剤師法では、薬剤師でない者が「薬剤師」またはこれに紛らわしい名称を用いることは禁止されています。 1は、国家試験に合格しただけでは免許の効力は生じず、薬剤師名簿に登録されて初めて薬剤師となります。2は、調剤は原則として薬剤師の業務ですが、医師等による一定の例外があるため「例外なく」は不適切です。3は、保険薬剤師の登録は別途必要で、薬剤師名簿への登録だけで自動的にはなりません。5は、薬剤師としての品位を損する行為は、免許取消し等の処分対象となることがあります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 72,

    question:
      "店舗販売業において販売できないのはどれか。1つ選べ。",

    choices: [
    "要指導医薬品",
    "第一類医薬品",
    "第二類医薬品",
    "第三類医薬品",
    "処方箋医薬品"
    ],

    answer: 4,

    explanation:
      "店舗販売業で販売できるのは、要指導医薬品および一般用医薬品（第一類・第二類・第三類）です。したがって、1〜4はいずれも店舗販売業で取り扱える医薬品に含まれます。一方、処方箋医薬品は医師等の処方箋に基づいて薬局で調剤・販売される医薬品であり、店舗販売業では販売できません。よって正答は5です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 73,

    question:
      "特定生物由来製品について、直接の容器又は直接の被包に記載しなければならない「特生物」の表示方法はどれか。1つ選べ。",

    choices: [
    "白地に赤枠、赤字",
    "白地に赤枠、黒字",
    "白地に黒枠、黒字",
    "白地に黒枠、赤字",
    "赤地に白字（枠なし）"
    ],

    answer: 2,

    explanation:
      "特定生物由来製品では、直接の容器または直接の被包に「特生物」と表示する必要があり、その表示は「白地に黒枠、黒字」とされています。したがって正答は3です。赤枠や赤字を用いる表示は、毒薬・劇薬など他の表示と混同しやすいため、本問では該当しません。赤地に白字も特定生物由来製品の表示方法ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 74,

    question:
      "医療の担い手が医療を提供するに当たり、適切な説明を行い、医療を受ける者の理解を得るよう努めることを求めているのはどれか。1つ選べ。",

    choices: [
    "医薬品医療機器等法",
    "医師法",
    "健康保険法",
    "医療法",
    "薬剤師法"
    ],

    answer: 3,

    explanation:
      "正答は4の医療法です。医療法では、医師・歯科医師・薬剤師などの医療の担い手が、医療を提供する際に適切な説明を行い、医療を受ける者の理解を得るよう努めることが定められています。いわゆるインフォームド・コンセントに関係する内容として押さえます。1の医薬品医療機器等法は医薬品等の品質・有効性・安全性の確保、2の医師法は医師の資格や業務、3の健康保険法は医療保険制度、5の薬剤師法は薬剤師の資格や業務に関する法律であり、本問の一般的な説明義務を定めるものとしては医療法が適切です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 75,

    question:
      "都道府県知事の免許を受けることが必要なのはどれか。1つ選べ。",

    choices: [
    "麻薬製剤業者",
    "麻薬輸出業者",
    "麻薬輸入業者",
    "麻薬小売業者",
    "麻薬製造業者"
    ],

    answer: 3,

    explanation:
      "麻薬小売業者は、薬局などで麻薬を譲り渡す業務を行う者で、都道府県知事の免許が必要です。国家試験では「地域での取扱いに関わる麻薬小売業者は知事免許」と整理するとよいです。一方、麻薬輸入業者・輸出業者・製造業者・製剤業者は、より広域的・製造流通上の管理が必要なため、厚生労働大臣の免許を受けるものとされています。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 76,

    question:
      "製造物責任法の対象にならないのはどれか。1つ選べ。ただし、免責事由はないものとする。",

    choices: [
    "一般用医薬品",
    "血液製剤",
    "要指導医薬品",
    "薬局製造販売医薬品",
    "調剤された薬剤"
    ],

    answer: 4,

    explanation:
      "製造物責任法（PL法）は、製造・加工された動産の欠陥により損害が生じた場合に、製造業者等の責任を問う法律です。一般用医薬品、血液製剤、要指導医薬品、薬局製造販売医薬品はいずれも製造・販売される医薬品であり、PL法の対象となり得ます。一方、調剤された薬剤は、処方せんに基づく薬剤師の調剤行為によって患者ごとに交付されるもので、一般にPL法上の「製造物」としては扱われにくいため、対象にならないものとして整理されます。したがって正答は5です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 77,

    question:
      "地域における薬局の役割に該当しないのはどれか。1つ選べ。",

    choices: [
    "在宅医療への参画",
    "地域住民の健康診断",
    "医薬品の販売・調剤",
    "生活習慣病等の健康相談応需",
    "薬物乱用防止活動"
    ],

    answer: 1,

    explanation:
      "薬局の地域における役割としては、医薬品の販売・調剤に加え、在宅医療への参画、生活習慣病などの健康相談、薬物乱用防止の啓発活動などが挙げられます。一方、地域住民の健康診断は、主に医療機関や自治体などが実施するものであり、薬局の基本的な役割としては位置づけにくいため、該当しないものは2です。1、3、4、5はいずれも地域包括ケアやセルフメディケーション支援の中で薬局に期待される役割です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 78,

    question:
      "医薬品の GLP の説明として正しいのはどれか。1つ選べ。",

    choices: [
    "医薬品の製造管理及び品質管理の基準",
    "医薬品の臨床試験の実施の基準",
    "医薬品の安全性に関する非臨床試験の実施の基準",
    "医薬品の製造販売後安全管理の基準",
    "医薬品の適正な流通管理の基準"
    ],

    answer: 2,

    explanation:
      "GLP（Good Laboratory Practice）は、医薬品の安全性に関する非臨床試験が適正に実施され、データの信頼性が確保されるための基準です。したがって正答は3です。1はGMP（製造管理・品質管理）、2はGCP（臨床試験）、4はGVP（製造販売後安全管理）、5はGDP（適正流通管理）に対応します。GLPは「非臨床・安全性試験」と結びつけて覚えるとよいです。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 79,

    question:
      "生命倫理の四原則に含まれないのはどれか。1つ選べ。",

    choices: [
    "善行原則",
    "正義原則",
    "自律尊重原則",
    "優生原則",
    "無危害原則"
    ],

    answer: 3,

    explanation:
      "生命倫理の四原則は、一般に「自律尊重原則」「善行原則」「無危害原則」「正義原則」の4つです。したがって、含まれないのは4の優生原則です。優生原則は、遺伝的に望ましい形質を重視する考え方に関係しますが、生命倫理の四原則には含まれません。1の善行原則は患者の利益になる行為を行うこと、2の正義原則は公平・公正な扱い、3の自律尊重原則は患者の自己決定の尊重、5の無危害原則は害を与えないことを指すため、いずれも四原則に含まれます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 80,

    question:
      "コミュニケーションにおける言語メッセージはどれか。1つ選べ。",

    choices: [
    "手話",
    "対人距離",
    "声の調子",
    "姿勢",
    "表情"
    ],

    answer: 0,

    explanation:
      "言語メッセージとは、言葉や記号など一定の意味をもつ言語体系を用いて伝える情報を指します。手話は音声ではありませんが、語彙や文法をもつ言語として用いられるため、言語メッセージに含まれます。対人距離、姿勢、表情は非言語メッセージです。声の調子は話し方に関する情報であり、言葉の内容そのものではないため、一般に非言語的要素として扱われます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 81,

    question:
      "7日間連日服用できないのはどれか。1つ選べ。",

    choices: [
    "アトルバスタチンカルシウム水和物",
    "アムロジピンベシル酸塩",
    "葉酸",
    "メトトレキサート",
    "メトホルミン塩酸塩"
    ],

    answer: 3,

    explanation:
      "メトトレキサートは、関節リウマチなどでは通常、1週間に1〜2日服用し、残りの日は休薬する投与法が用いられます。7日間連日服用すると、骨髄抑制や口内炎、肝障害などの副作用リスクが高まるため、連日服用できない薬として注意が必要です。アトルバスタチン、アムロジピン、葉酸、メトホルミンはいずれも、用法に従って連日服用されることがある薬です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 82,

    question:
      "臨床試験を遂行するに当たり、公開してはいけないのはどれか。1つ選べ。",

    choices: [
    "利益相反",
    "被験者個人情報",
    "研究資金源",
    "主要評価項目",
    "倫理的配慮"
    ],

    answer: 1,

    explanation:
      "臨床試験では、被験者のプライバシー保護が重要であり、氏名や住所など個人を特定できる情報は公開してはいけません。したがって、正答は2です。一方、利益相反、研究資金源、主要評価項目、倫理的配慮は、研究の透明性や信頼性を確保するために、原則として公開・明示されるべき情報です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 83,

    question:
      "以下の薬物を主薬とする注射剤のうち、一般病棟での病棟在庫の医薬品として適切でないのはどれか。1つ選べ。",

    choices: [
    "ヒドロコルチゾンコハク酸エステルナトリウム",
    "インスリン ヒト（遺伝子組換え）",
    "クロルフェニラミンマレイン酸塩",
    "塩化カリウム",
    "アトロピン硫酸塩水和物"
    ],

    answer: 3,

    explanation:
      "正答は4の塩化カリウムです。塩化カリウム注射液は、急速静注や原液投与により致死的な高カリウム血症や心停止を起こすおそれがあるため、特に厳重な管理が必要な医薬品です。そのため、一般病棟の病棟在庫として置くのは適切でないと考えます。1のヒドロコルチゾン、3のクロルフェニラミン、5のアトロピンは、アレルギー対応や救急時に使用されることがあり、病棟在庫として扱われることがあります。2のインスリンも注意が必要な薬ですが、血糖管理で使用頻度が高く、適切な管理下で病棟に置かれる場合があります。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 84,

    question:
      "次亜塩素酸ナトリウムを含む洗剤と混ぜた時に有毒ガスが発生するのはどれか。1つ選べ。",

    choices: [
    "アルカノイルオキシベンゼンスルホン酸ナトリウムを含むアルカリ性洗剤",
    "過酸化水素を含む酸性洗剤",
    "塩酸を含む酸性洗剤",
    "アルキルスルホン酸ナトリウムを含む酸性洗剤",
    "イソチアゾリン系抗菌剤を含む中性洗剤"
    ],

    answer: 2,

    explanation:
      "次亜塩素酸ナトリウムは、塩酸などの強い酸と混ざると塩素ガスを発生しやすく、「まぜるな危険」の代表例です。したがって正答は3です。1のアルカリ性洗剤では酸性化しにくく、塩素ガス発生の典型ではありません。2の過酸化水素では主に酸素発生が問題となります。4は界面活性剤、5は抗菌剤が中心で、塩酸との組合せほど塩素ガス発生の代表例ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 85,

    question:
      "処方箋には先発医薬品が記載されていたが、患者が後発医薬品を希望した。そこで、後発医薬品の分割調剤1回目として7日分の調剤を行った。次回、残りをこの後発医薬品で調剤する場合に必要な最大錠数はどれか。1つ選べ。なお、処方箋には変更不可の記載はない。 （処方） ムコダイン®錠250mg 1回2錠（1日6錠） 1日3回 朝昼夕食後 28日分 （分割調剤1回目） L-カルボシステイン錠500mg 1回1錠（1日3錠） 1日3回 朝昼夕食後 7日分",

    choices: [
    "21錠",
    "42錠",
    "63錠",
    "84錠",
    "126錠"
    ],

    answer: 2,

    explanation:
      "先発品ムコダイン®錠250mgは1回2錠なので、1回量は500mgです。後発品のL-カルボシステイン錠500mgでは1回1錠で同じ量になります。処方は28日分で、1回目に7日分調剤しているため、残りは21日分です。後発品は1日3錠なので、21日分では3錠×21日＝63錠となります。1の21錠は7日分、2の42錠は14日分、4の84錠は日数や規格の換算が合わず、5の126錠は250mg錠を1日6錠で21日分と考えた場合の数です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 86,

    question:
      "Common Terminology Criteria for Adverse Events（CTCAE）は、米国 National Cancer Institute（NCI）が主導し世界共通で使用されることを意図して作成された A に関しての共通用語規準である。Aに入る語句として正しいのはどれか。1つ選べ。",

    choices: [
    "効果発現",
    "有害事象",
    "予後予測",
    "製品回収",
    "品質管理"
    ],

    answer: 1,

    explanation:
      "CTCAEは「Common Terminology Criteria for Adverse Events」の略で、がん治療などで生じる有害事象（副作用を含む好ましくない医療上のできごと）を共通の基準で評価・記録するための用語規準です。米国NCIが作成し、重症度をGradeで分類する点も重要です。したがってAは「有害事象」です。効果発現や予後予測を評価する基準ではなく、製品回収や品質管理に関する規準でもありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 87,
    hasImage: true,
    image: "/pharmacy/104/required/q87.png",

    question:
      "下記の処方に従って薬剤調製した後の鑑査で指摘すべき項目はどれか。1つ選べ。なお、投薬びんと処方薬剤は無色透明である。 （処方） アンブロキソール塩酸塩シロップ0.3% 1回2 mL（1日6 mL） 1日3回 朝昼夕食後 8日分",

    choices: [
    "遮光の必要性",
    "薬剤の総量",
    "計量カップの必要性",
    "薬札（ラベル）の必要性",
    "投薬びんにおける服用量の目盛の必要性"
    ],

    answer: 3,

    explanation:
      "正答は4です。水剤を投薬びんで交付する場合、患者が薬剤名や用法・用量を確認できるよう、薬札（ラベル）の貼付が必要です。特に今回は投薬びんも薬剤も無色透明であり、見た目だけでは薬と分かりにくいため、鑑査で指摘すべき項目となります。総量は1日6 mL×8日＝48 mLで問題ありません。アンブロキソール塩酸塩シロップは通常、遮光が必須とは考えにくいです。計量カップや服用量の目盛は、服用量確認に有用な場合はありますが、本問で最も指摘すべき必須項目は薬札です。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 88,

    question:
      "廃棄時に麻薬取締員又は保健所職員の立会いが必要なのはどれか。1つ選べ。",

    choices: [
    "有効期限切れとなった在庫麻薬",
    "調剤済みで返却された麻薬",
    "手術室で施用後に残った麻薬",
    "患者が床に落下させた麻薬",
    "入院時に持参して不用になった麻薬"
    ],

    answer: 0,

    explanation:
      "正答は1です。有効期限切れとなった在庫麻薬を廃棄する場合は、事前に麻薬廃棄届を提出し、麻薬取締員又は保健所職員などの立会いのもとで廃棄します。2の調剤済みで返却された麻薬や、5の患者持参で不用になった麻薬は、調剤済麻薬として廃棄後に届出を行う扱いで、原則としてこの立会いは不要です。3の施用後の残液、4の落下などで使用できない麻薬も、在庫麻薬の通常廃棄とは扱いが異なり、設問の立会いが必要なものとしては1を選びます。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 89,

    question:
      "薬剤服用歴管理記録の記述法の1つとしてSOAPがある。このうち、「O」の表現として正しいのはどれか。1つ選べ。",

    choices: [
    "Objective data",
    "Optimal data",
    "Outbreak data",
    "Outcome data",
    "Outstanding data"
    ],

    answer: 0,

    explanation:
      "SOAP形式では、S＝Subjective data（患者の訴えなど主観的情報）、O＝Objective data（検査値・バイタル・処方内容など客観的情報）、A＝Assessment（評価）、P＝Plan（計画）を表します。したがって「O」はObjective dataであり、1が正答です。Optimal data（最適なデータ）、Outbreak data（発生データ）、Outcome data（結果データ）、Outstanding data（未解決・顕著なデータ）はSOAPの「O」を表す用語ではありません。"
  },


  {
    subject: "pharmacy",
    category: CATEGORIES.REQUIRED,

    sourceType: "past_exam",
    examNumber: 104,
    sourceNumber: 90,

    question:
      "副作用として特にCK（クレアチニンキナーゼ）上昇に注意するのはどれか。1つ選べ。",

    choices: [
    "アセトアミノフェン",
    "ゲフィチニブ",
    "プラバスタチンナトリウム",
    "チクロピジン塩酸塩",
    "ジゴキシン"
    ],

    answer: 2,

    explanation:
      "CK（クレアチニンキナーゼ）上昇に特に注意する薬は、3のプラバスタチンナトリウムです。プラバスタチンはスタチン系薬で、まれに横紋筋融解症を起こすことがあり、筋肉痛・脱力感とともにCK上昇が重要な検査所見になります。1のアセトアミノフェンは主に肝障害、2のゲフィチニブは間質性肺炎や肝障害、4のチクロピジンは血栓性血小板減少性紫斑病（TTP）や無顆粒球症、肝障害、5のジゴキシンは不整脈や消化器症状などの中毒症状に注意します。したがって、CK上昇に注意するものとしてはプラバスタチンが適切です。"
  },

  // AI_QUESTION_INSERT_HERE
];
