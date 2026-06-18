import { CATEGORIES } from "./categories";

export const commonExtraQuestions = [

      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に天候が悪化しそうな場合、操縦者の対応として最も適切なものはどれか？",
        choices: [
          "予定通り最後まで飛行を続ける",
          "安全を優先し、帰還または緊急着陸を判断する",
          "自動操縦に切り替えれば天候の影響は考慮しなくてよい"
        ],
        answer: 1,
        explanation:
          "飛行中に天候が悪化するおそれがある場合は、安全を優先して帰還や緊急着陸を判断する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "補助者を配置する場合の対応として、適切なものはどれか？",
        choices: [
          "役割や連絡手段を事前に確認する",
          "補助者がいれば操縦者は周囲を監視しなくてよい",
          "補助者の配置場所は飛行中に決めればよい"
        ],
        answer: 0,
        explanation:
          "補助者を配置する場合は、役割、担当範囲、操縦者との連絡手段を事前に確認することが重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行前点検として、最も適切なものはどれか？",
        choices: [
          "前回問題なく飛行できた場合は省略できる",
          "機体、プロペラ、バッテリーなどに異常がないか確認する",
          "飛行後にまとめて確認すればよい"
        ],
        answer: 1,
        explanation:
          "飛行前には、機体、プロペラ、バッテリー、通信状態などを確認し、異常があれば整備してから飛行します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
        
        question:
          "飛行日誌について、適切なものはどれか？",
        choices: [
          "特定飛行を行う場合などは飛行日誌の作成・管理が必要となる",
          "趣味目的であれば必ず不要である",
          "事故が起きた場合だけ作成すればよい"
        ],
        answer: 0,
        explanation:
          "特定飛行を行う場合などには、飛行日誌の作成や管理が求められます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "濃霧が発生している状況での飛行判断として、最も適切なものはどれか？",
        choices: [
          "視認性が低下するため、延期または中止を検討する",
          "自動操縦なら問題なく飛行できる",
          "低高度なら安全に飛行できる"
        ],
        answer: 0,
        explanation:
          "濃霧では視認性が低下し、周囲の障害物や航空機との安全確認が難しくなるため、延期や中止を検討します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
        
        question:
          "低温時のバッテリーについて、適切なものはどれか？",
        choices: [
          "低温時は飛行可能時間が長くなる",
          "低温時はバッテリー性能が低下し、飛行可能時間が短くなることがある",
          "低温時でもバッテリーへの影響はない"
        ],
        answer: 1,
        explanation:
          "低温時はバッテリーの性能が低下し、通常より飛行可能時間が短くなる可能性があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行中の周囲監視について、適切なものはどれか？",
        choices: [
          "衝突防止装置があれば周囲監視は不要である",
          "周囲の航空機、建物、電線、樹木などを継続して監視する",
          "自動操縦中は監視を省略できる"
        ],
        answer: 1,
        explanation:
          "衝突防止装置を過信せず、航空機、建物、電線、樹木、鳥など周囲の状況を継続して監視することが重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "無人航空機の事故が発生した場合の責任について、正しいものはどれか？",
        choices: [
          "操縦者が刑事責任、民事責任、行政処分の対象となる場合がある",
          "機体メーカーだけが責任を負う",
          "補助者がいれば操縦者は責任を負わない"
        ],
        answer: 0,
        explanation:
          "事故の内容によっては、操縦者が刑事責任、民事責任、行政処分等の対象となる場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "地域情報の収集として、適切なものはどれか？",
        choices: [
          "航空法だけ確認すれば十分である",
          "条例、立入禁止区域、飛行自粛要請空域なども確認する",
          "過去に飛ばした場所なら確認は不要である"
        ],
        answer: 1,
        explanation:
          "地域によっては条例や立入禁止区域、飛行自粛要請空域などがあるため、事前に地域情報を確認します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "安全な飛行計画として、適切なものはどれか？",
        choices: [
          "操縦者の経験だけを基準に計画する",
          "機体性能、操縦者や補助者の能力、飛行環境を考慮して無理のない計画を立てる",
          "飛行中に状況を見ながら計画を決める"
        ],
        answer: 1,
        explanation:
          "飛行計画は、機体性能、操縦者・補助者の経験や能力、飛行環境を考慮して無理のない内容にする必要があります。"
      }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "無人航空機の操縦者が飛行前に行うべき事項として最も適切なものはどれか？",
        choices: [
          "飛行前点検を実施する",
          "飛行後にまとめて点検する",
          "過去に飛行実績があれば点検は不要である"
        ],
        answer: 0,
        explanation:
          "飛行前には機体やバッテリー等の点検を実施する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "無人航空機を飛行させる際の気象確認について適切なものはどれか？",
        choices: [
          "飛行前に風速や降雨予報を確認する",
          "晴れていれば気象確認は不要",
          "飛行開始後に確認すればよい"
        ],
        answer: 0,
        explanation:
          "飛行前に風速や降雨などの気象条件を確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行中に異常振動が発生した場合の対応として最も適切なものはどれか？",
        choices: [
          "安全な場所へ着陸させる",
          "飛行を継続する",
          "速度を上げて飛行する"
        ],
        answer: 0,
        explanation:
          "異常振動は機体故障の可能性があるため安全な場所へ着陸します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "操縦者の健康状態について適切なものはどれか？",
        choices: [
          "体調不良時は飛行を見合わせる",
          "軽い体調不良なら問題ない",
          "補助者がいれば体調は関係ない"
        ],
        answer: 0,
        explanation:
          "安全な飛行のため操縦者の健康状態は重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行計画の作成目的として最も適切なものはどれか？",
        choices: [
          "飛行の安全確保",
          "飛行時間を長くするため",
          "機体性能を向上させるため"
        ],
        answer: 0,
        explanation:
          "飛行計画は安全な運航を実現するために作成します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "第三者との接触リスクを減らす方法として適切なものはどれか？",
        choices: [
          "立入管理措置を講じる",
          "高度を上げるだけでよい",
          "飛行速度を上げる"
        ],
        answer: 0,
        explanation:
          "第三者を飛行区域へ立ち入らせない管理措置が重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行中に通信品質が悪化した場合の対応として適切なものはどれか？",
        choices: [
          "事前に定めた手順に従う",
          "そのまま飛行する",
          "通信断を無視する"
        ],
        answer: 0,
        explanation:
          "通信異常時は事前に定めた手順に従って対応します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行日誌を作成する目的として最も適切なものはどれか？",
        choices: [
          "飛行記録を管理するため",
          "機体を大型化するため",
          "バッテリー寿命を延ばすため"
        ],
        answer: 0,
        explanation:
          "飛行日誌は飛行記録や整備履歴を管理するために用います。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行区域の確認として適切なものはどれか？",
        choices: [
          "障害物や第三者の有無を確認する",
          "離陸地点だけ確認する",
          "飛行後に確認する"
        ],
        answer: 0,
        explanation:
          "飛行区域全体の安全確認が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "飛行前ブリーフィングの目的として最も適切なものはどれか？",
        choices: [
          "関係者間で情報共有する",
          "飛行時間を短縮する",
          "機体重量を減らす"
        ],
        answer: 0,
        explanation:
          "関係者間で飛行内容や緊急時対応を共有することが重要です。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RISK,
        
        question:
          "無人航空機の飛行場所に関するルールとして、最も適切なものはどれか？",
        choices: [
          "飛行場所ごとのルールや遵守事項を確認する",
          "航空法だけ守れば地域のルールは確認不要である",
          "人が少なければどこでも自由に飛行できる"
        ],
        answer: 0,
        explanation:
          "飛行場所によっては条例、施設管理者のルール、立入禁止区域などがあるため、事前確認が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機の騒音に関する配慮として、適切なものはどれか？",
        choices: [
          "周囲への騒音影響を考慮して飛行する",
          "無人航空機の騒音は避けられないため配慮不要である",
          "昼間であれば騒音への配慮は不要である"
        ],
        answer: 0,
        explanation:
          "無人航空機の飛行では、周囲への騒音影響にも配慮する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "特定飛行を行う際に携行すべきものとして、適切なものはどれか？",
        choices: [
          "必要に応じて許可書・承認書、技能証明書、飛行日誌など",
          "機体の販売カタログのみ",
          "操縦者の任意のメモだけ"
        ],
        answer: 0,
        explanation:
          "特定飛行では、許可書・承認書、技能証明書、飛行日誌などを携行する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機の飛行で、航空機と接近するおそれがある場合の対応として適切なものはどれか？",
        choices: [
          "無人航空機側が回避する",
          "高度が低ければそのまま飛行を続ける",
          "航空機が必ず回避するため対応不要である"
        ],
        answer: 0,
        explanation:
          "航空機の安全を確保するため、無人航空機側が回避行動を取る必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "飛行自粛要請空域が設定されている可能性がある場合、操縦者の対応として適切なものはどれか？",
        choices: [
          "国土交通省などが公表する情報を確認し、要請内容に応じて対応する",
          "法令ではないため確認する必要はない",
          "飛行後に確認すればよい"
        ],
        answer: 0,
        explanation:
          "飛行自粛要請空域は国土交通省のホームページ等で公示されるため、飛行前に確認し適切に対応します。"
      },
        
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "無人航空機の登録を受けられない可能性がある機体として、適切なものはどれか？",
        choices: [
          "安全性に問題があり、国土交通大臣が登録できないものとして指定した機体",
          "遠隔操作しかできない機体",
          "外観の色が派手な機体"
        ],
        answer: 0,
        explanation:
          "安全性に問題がある機体や、飛行制御が著しく困難な機体などは登録を受けられない場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "物件投下に関する説明として、適切なものはどれか？",
        choices: [
          "液体や霧状のものを散布する行為も物件投下に含まれる",
          "水であれば散布しても物件投下には含まれない",
          "水面に物を置く行為は必ず物件投下に該当する"
        ],
        answer: 0,
        explanation:
          "物件投下には、水や農薬などの液体・霧状のものの散布も含まれます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
          "小型無人機等飛行禁止法に関する説明として、適切なものはどれか？",
        choices: [
          "対象施設の敷地・区域の上空や周辺おおむね300mの上空が規制対象となる場合がある",
          "空港は航空法で規制されているため対象施設にならない",
          "対象施設は一時的に追加されることはない"
        ],
        answer: 0,
        explanation:
          "重要施設やその周辺おおむね300mの上空は規制対象となることがあり、対象施設が一時的に追加される場合もあります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "技能証明と登録講習機関に関する説明として、適切なものはどれか？",
        choices: [
          "登録講習機関の講習を修了しても、学科試験は原則として免除されない",
          "登録講習機関を修了すれば学科試験も実地試験もすべて免除される",
          "技能証明は機体登録をすれば自動的に取得できる"
        ],
        answer: 0,
        explanation:
          "登録講習機関の講習を修了した場合、実地試験の免除対象になりますが、学科試験は原則として免除されません。"
      }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "DIPS 2.0の主な目的として最も適切なものはどれか？",
        choices: [
          "飛行許可・承認申請や飛行計画通報等をオンラインで管理するため",
          "無人航空機の速度を制御するため",
          "バッテリー管理を行うため"
        ],
        answer: 0,
        explanation:
          "DIPS 2.0は飛行許可・承認申請や飛行計画通報などを行うためのシステムです。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "機体登録制度の目的として最も適切なものはどれか？",
        choices: [
          "事故発生時の所有者特定や安全管理を行うため",
          "飛行性能を向上させるため",
          "操縦技能を評価するため"
        ],
        answer: 0,
        explanation:
          "機体登録制度は所有者の把握や安全管理を目的としています。"
      },
        
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "飛行計画通報制度の目的として最も適切なものはどれか？",
        choices: [
          "他の空域利用者との安全確保",
          "バッテリー寿命の延長",
          "操縦技能向上"
        ],
        answer: 0,
        explanation:
          "飛行計画を共有することで空域利用者間の安全確保を図ります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "飛行ログを保存する理由として適切なものはどれか？",
        choices: [
          "運航記録やトラブル分析に活用するため",
          "機体重量を管理するため",
          "通信品質を改善するため"
        ],
        answer: 0,
        explanation:
          "飛行ログは運航記録や事故調査等に利用されます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSSの役割として最も適切なものはどれか？",
        choices: [
          "位置情報を取得する",
          "映像伝送を行う",
          "バッテリー残量を測定する"
        ],
        answer: 0,
        explanation:
          "GNSSは衛星を利用して位置情報を取得します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "フェールセーフ機能の説明として適切なものはどれか？",
        choices: [
          "異常発生時に安全側へ移行する機能",
          "飛行速度を向上させる機能",
          "映像品質を改善する機能"
        ],
        answer: 0,
        explanation:
          "フェールセーフは異常時の安全確保を目的とした機能です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "RTH（Return To Home）の役割として適切なものはどれか？",
        choices: [
          "自動的に離陸地点付近へ帰還する",
          "飛行速度を自動調整する",
          "カメラ映像を保存する"
        ],
        answer: 0,
        explanation:
          "RTHは自動帰還機能です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "飛行前にファームウェア更新を確認する理由として適切なものはどれか？",
        choices: [
          "安全性や不具合修正の反映状況を確認するため",
          "飛行時間を長くするため",
          "重量を軽くするため"
        ],
        answer: 0,
        explanation:
          "ファームウェア更新には安全性向上や不具合修正が含まれることがあります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "バッテリー管理で重要な事項として適切なものはどれか？",
        choices: [
          "劣化状況や充電状態を確認する",
          "満充電なら点検不要である",
          "飛行後だけ確認すればよい"
        ],
        answer: 0,
        explanation:
          "飛行前後にバッテリー状態を確認することが重要です。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "飛行計画通報を行う主な目的として適切なものはどれか？",
        choices: [
          "他の空域利用者との安全確保",
          "機体性能向上",
          "飛行時間延長"
        ],
        answer: 0,
        explanation:
          "飛行計画を共有することで他の空域利用者との安全確保を図ります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "リモートID機能が正常に動作しているか確認するタイミングとして適切なものはどれか？",
        choices: [
          "飛行前",
          "飛行終了後のみ",
          "確認不要"
        ],
        answer: 0,
        explanation:
          "リモートIDの正常動作確認は飛行前に実施する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSS信号の受信状態が悪化した場合のリスクとして適切なものはどれか？",
        choices: [
          "位置精度低下",
          "バッテリー容量増加",
          "機体重量増加"
        ],
        answer: 0,
        explanation:
          "GNSS信号が不安定になると位置精度が低下する可能性があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "通信リンクが途絶した場合に備える機能として適切なものはどれか？",
        choices: [
          "フェールセーフ",
          "電子調速機",
          "ジンバル"
        ],
        answer: 0,
        explanation:
          "通信断に備えてフェールセーフ機能を設定しておくことが重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "飛行ログの確認で把握できる内容として適切なものはどれか？",
        choices: [
          "飛行経路や異常履歴",
          "操縦者の資格更新日",
          "気温予報"
        ],
        answer: 0,
        explanation:
          "飛行ログから飛行経路や異常発生状況などを確認できます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "自動帰還機能を利用する際に事前設定が必要な項目として適切なものはどれか？",
        choices: [
          "帰還高度",
          "機体色",
          "送信機のストラップ長"
        ],
        answer: 0,
        explanation:
          "障害物回避のため帰還高度を適切に設定する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "冗長化設計の目的として適切なものはどれか？",
        choices: [
          "故障時の安全性向上",
          "飛行速度向上",
          "重量削減"
        ],
        answer: 0,
        explanation:
          "冗長化は一部故障時にも安全性を維持するために行います。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "飛行前に確認するバッテリー情報として適切なものはどれか？",
        choices: [
          "残量やセル異常の有無",
          "製造国のみ",
          "外箱のデザイン"
        ],
        answer: 0,
        explanation:
          "残量やセル異常の有無は飛行安全に直結します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "機体ソフトウェア更新後に行うべき事項として適切なものはどれか？",
        choices: [
          "動作確認",
          "即飛行",
          "確認不要"
        ],
        answer: 0,
        explanation:
          "更新後は正常動作を確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に異常警告が表示された場合の対応として適切なものはどれか？",
        choices: [
          "内容を確認し安全側の判断を行う",
          "無視して飛行継続",
          "警告を消して飛行継続"
        ],
        answer: 0,
        explanation:
          "異常警告は安全運航に関わるため内容確認と対応が必要です。"
    }
    
        ,
    {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を飛行させる前に、飛行場所の管理者がいる場合の対応として最も適切なものはどれか？",
        choices: [
          "管理者の許可や利用ルールを確認する",
          "航空法上の許可があれば管理者確認は不要である",
          "飛行後に報告すればよい"
        ],
        answer: 0,
        explanation:
          "飛行場所に管理者がいる場合は、施設や土地の利用ルール、管理者の許可などを事前に確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に第三者が飛行区域へ接近してきた場合の対応として最も適切なものはどれか？",
        choices: [
          "安全を優先して飛行を中断または着陸させる",
          "高度を上げればよいので飛行を継続する",
          "第三者が離れるまで上空で待機すれば必ず安全である"
        ],
        answer: 0,
        explanation:
          "第三者が飛行区域へ接近した場合は、衝突や墜落時の被害を避けるため、安全を優先して中断や着陸を判断します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機の操縦者が飛行前に確認すべき周辺環境として適切なものはどれか？",
        choices: [
          "電線、建物、樹木、人や車両の動き",
          "機体の色だけ",
          "操縦者の服装だけ"
        ],
        answer: 0,
        explanation:
          "飛行前には、電線、建物、樹木などの障害物や、人・車両の通行状況を確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に強風が発生した場合の対応として最も適切なものはどれか？",
        choices: [
          "機体の制御が困難になる前に安全な場所へ着陸させる",
          "風上へ全速で飛行すれば必ず回復できる",
          "自動操縦中であれば強風の影響は受けない"
        ],
        answer: 0,
        explanation:
          "強風により機体の制御が困難になるおそれがあるため、安全な場所への着陸や飛行中止を判断します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を飛行させる際のプライバシーへの配慮として適切なものはどれか？",
        choices: [
          "住宅や人を撮影する可能性がある場合は、撮影範囲や利用目的に配慮する",
          "上空からの撮影であればプライバシーを考慮しなくてよい",
          "飛行許可があれば撮影内容は自由に扱える"
        ],
        answer: 0,
        explanation:
          "無人航空機の撮影では、住宅や人物が写り込む可能性があるため、プライバシーや肖像権への配慮が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前に補助者と確認しておく事項として最も適切なものはどれか？",
        choices: [
          "監視範囲、合図、緊急時の連絡方法",
          "補助者の好きな機体メーカー",
          "飛行後の片付けだけ"
        ],
        answer: 0,
        explanation:
          "補助者を配置する場合は、監視範囲、合図、連絡方法、緊急時対応などを事前に共有します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機の飛行における安全管理として最も適切なものはどれか？",
        choices: [
          "飛行前、飛行中、飛行後の各段階で安全確認を行う",
          "飛行前だけ確認すれば十分である",
          "飛行後だけ記録を残せばよい"
        ],
        answer: 0,
        explanation:
          "安全管理は飛行前点検、飛行中の監視、飛行後の記録や点検まで継続して行う必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を人口が多い地域の近くで飛行させる場合の考え方として適切なものはどれか？",
        choices: [
          "第三者へのリスクを低減するため、飛行経路や時間帯を検討する",
          "人が多い地域でも高度を上げればリスクはなくなる",
          "短時間であれば第三者リスクは考慮しなくてよい"
        ],
        answer: 0,
        explanation:
          "人口が多い地域の近くでは、第三者への接近や墜落時被害を考慮し、経路や時間帯を工夫する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に機体を見失った場合の対応として最も適切なものはどれか？",
        choices: [
          "安全を確保できる手順に従い、必要に応じて帰還または着陸させる",
          "見えるまでそのまま飛行を続ける",
          "高度を上げれば必ず見つかるため上昇させる"
        ],
        answer: 0,
        explanation:
          "機体を見失った場合は、衝突や逸脱の危険があるため、事前に定めた手順に従い安全確保を優先します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前に緊急着陸場所を確認する理由として最も適切なものはどれか？",
        choices: [
          "異常時に第三者への被害を避けて安全に着陸させるため",
          "飛行時間を延ばすため",
          "操縦者の負担を増やすため"
        ],
        answer: 0,
        explanation:
          "緊急着陸場所を事前に確認しておくことで、異常時に第三者への被害を避けながら安全に着陸できます。"
      }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "航空法において無人航空機とは、一般に何kg未満の機体を除くものとして定義されているか。",
        choices: [
          "100g未満",
          "200g未満",
          "250g未満"
        ],
        answer: 0,
        explanation:
          "航空法上の無人航空機は100g以上の機体が対象です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を飛行させる際、飛行前に確認すべき事項として最も適切なものはどれか。",
        choices: [
          "機体の状態と周辺環境",
          "操縦者の服装のみ",
          "飛行後の予定のみ"
        ],
        answer: 0,
        explanation:
          "飛行前には機体点検と周辺環境の確認が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "人口集中地区（DID）上空で飛行する場合に必要となるものはどれか。",
        choices: [
          "国土交通大臣の許可",
          "市役所への届出",
          "警察署への届出"
        ],
        answer: 0,
        explanation:
          "人口集中地区での飛行には国土交通大臣の許可が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "夜間飛行を行う場合に必要となるものはどれか。",
        choices: [
          "国土交通大臣の承認",
          "都道府県知事の承認",
          "警察署長の承認"
        ],
        answer: 0,
        explanation:
          "夜間飛行は承認対象飛行です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "目視外飛行を行う場合に必要となるものはどれか。",
        choices: [
          "国土交通大臣の承認",
          "飛行日誌のみ",
          "補助者のみ"
        ],
        answer: 0,
        explanation:
          "目視外飛行は承認対象飛行です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "第三者または第三者の物件から確保しなければならない距離はどれか。",
        choices: [
          "30m",
          "20m",
          "10m"
        ],
        answer: 0,
        explanation:
          "第三者および第三者物件とは30m以上の距離を確保します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "催し場所上空で飛行する場合に必要となるものはどれか。",
        choices: [
          "国土交通大臣の承認",
          "市町村長の承認",
          "消防署長の承認"
        ],
        answer: 0,
        explanation:
          "催し場所上空の飛行は承認対象です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "アルコールまたは薬物の影響下で無人航空機を飛行させてはならない。この規定の目的として最も適切なものはどれか。",
        choices: [
          "安全運航の確保",
          "騒音対策",
          "飛行時間短縮"
        ],
        answer: 0,
        explanation:
          "判断力や操作能力の低下を防ぎ安全運航を確保します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に異常を認めた場合の対応として最も適切なものはどれか。",
        choices: [
          "安全を確保し飛行を中止する",
          "飛行を継続する",
          "異常を記録しない"
        ],
        answer: 0,
        explanation:
          "異常発生時は安全確保を優先します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前の気象確認として最も重要なものはどれか。",
        choices: [
          "風向・風速",
          "月齢",
          "潮位"
        ],
        answer: 0,
        explanation:
          "風向・風速は飛行安全に直接影響します。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "航空法上、飛行の方法として禁止されているものはどれか。",
        choices: [
          "アルコールまたは薬物の影響下で飛行させること",
          "昼間に目視内で飛行させること",
          "風速を確認してから飛行させること"
        ],
        answer: 0,
        explanation:
          "アルコールまたは薬物の影響により正常な飛行ができないおそれがある状態での飛行は禁止されています。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を飛行させる者が、飛行前に確認しなければならない事項として適切なものはどれか。",
        choices: [
          "無人航空機の状況、飛行空域、気象その他飛行に必要な事項",
          "操縦者の服装と飛行後の予定",
          "機体の購入価格のみ"
        ],
        answer: 0,
        explanation:
          "飛行前には機体状態、空域、気象、周辺環境など飛行に必要な事項を確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "航空法上、飛行中に他の航空機との衝突のおそれがある場合、無人航空機の操縦者が取るべき対応として適切なものはどれか。",
        choices: [
          "地上に降下させるなど衝突を予防する措置を講じる",
          "有人航空機が回避するためそのまま飛行する",
          "高度を維持して様子を見る"
        ],
        answer: 0,
        explanation:
          "他の航空機との衝突のおそれがある場合は、地上に降下させるなど衝突を予防する措置が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "航空法上、飛行中に他人に迷惑を及ぼすような方法で飛行させることについて、適切な説明はどれか。",
        choices: [
          "禁止されている",
          "夜間のみ禁止されている",
          "人口集中地区のみ禁止されている"
        ],
        answer: 0,
        explanation:
          "航空法では、他人に迷惑を及ぼすような方法で無人航空機を飛行させることは禁止されています。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "航空法上、無人航空機の飛行禁止空域に該当するものはどれか。",
        choices: [
          "空港等の周辺空域",
          "すべての河川上空",
          "すべての私有地上空"
        ],
        answer: 0,
        explanation:
          "空港等の周辺空域、緊急用務空域、150m以上の空域、人口集中地区上空などは飛行禁止空域に該当します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "緊急用務空域に関する説明として適切なものはどれか。",
        choices: [
          "災害時などに捜索救助等の航空機の安全を確保するため指定される空域である",
          "趣味飛行のみ自由に飛行できる空域である",
          "無人航空機の練習飛行専用空域である"
        ],
        answer: 0,
        explanation:
          "緊急用務空域は、災害時等に警察・消防・自衛隊等の航空機の活動を妨げないために指定されます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "150m以上の空域で飛行する場合に必要となるものとして適切なものはどれか。",
        choices: [
          "国土交通大臣の許可",
          "市町村長の承認",
          "土地所有者の承認のみ"
        ],
        answer: 0,
        explanation:
          "地表または水面から150m以上の空域で飛行する場合は、国土交通大臣の許可が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "危険物の輸送に関する説明として適切なものはどれか。",
        choices: [
          "無人航空機で危険物を輸送する場合は承認が必要となる",
          "少量であれば常に自由に輸送できる",
          "夜間でなければ制限されない"
        ],
        answer: 0,
        explanation:
          "無人航空機による危険物輸送は承認対象となります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "物件投下に関する説明として適切なものはどれか。",
        choices: [
          "無人航空機から物件を投下する場合は承認が必要となる",
          "水や農薬の散布は物件投下に含まれない",
          "高度30m未満なら自由に投下できる"
        ],
        answer: 0,
        explanation:
          "物件投下は承認対象です。水や農薬など液体の散布も物件投下に含まれる場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "人または物件との距離を30m以上確保できない飛行を行う場合、必要となるものはどれか。",
        choices: [
          "国土交通大臣の承認",
          "警察署への届出のみ",
          "補助者の同意のみ"
        ],
        answer: 0,
        explanation:
          "第三者や第三者物件から30m未満で飛行する場合は承認が必要です。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "無人航空機の登録制度の目的として最も適切なものはどれか。",
        choices: [
          "事故発生時の所有者特定や安全管理のため",
          "機体価格を管理するため",
          "飛行時間を制限するため"
        ],
        answer: 0,
        explanation:
          "登録制度は所有者の把握と安全管理を目的としています。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "登録が必要となる無人航空機について正しいものはどれか。",
        choices: [
          "100g以上の無人航空機",
          "200g以上の無人航空機",
          "250g以上の無人航空機"
        ],
        answer: 0,
        explanation:
          "100g以上の無人航空機は登録が必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
        question:
          "登録記号の表示について正しいものはどれか。",
        choices: [
          "機体へ見やすい方法で表示する",
          "操縦者のみが知っていればよい",
          "飛行計画にだけ記載すればよい"
        ],
        answer: 0,
        explanation:
          "登録記号は機体へ表示しなければなりません。"
      },
        
      {
        subject: "drone",
        category: CATEGORIES.RULE,
        
        question:
          "機体認証制度の目的として最も適切なものはどれか。",
        choices: [
          "機体の安全性を確認するため",
          "機体価格を統一するため",
          "操縦者の技能を評価するため"
        ],
        answer: 0,
        explanation:
          "機体認証は無人航空機の安全性確認を目的としています。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "技能証明制度の目的として最も適切なものはどれか。",
        choices: [
          "操縦者の知識と技能を証明するため",
          "機体の製造年を証明するため",
          "飛行回数を管理するため"
        ],
        answer: 0,
        explanation:
          "技能証明制度は操縦者の知識と技能を証明する制度です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.FIRST,
    
        question:
          "一等無人航空機操縦士について正しいものはどれか。",
        choices: [
          "高いレベルの運航を行うための国家資格である",
          "趣味飛行専用資格である",
          "機体整備専用資格である"
        ],
        answer: 0,
        explanation:
          "一等操縦士は高度な運航を行うための国家資格です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "二等無人航空機操縦士について正しいものはどれか。",
        choices: [
          "一定の条件下での運航を想定した国家資格である",
          "機体開発者専用資格である",
          "空港管理者専用資格である"
        ],
        answer: 0,
        explanation:
          "二等操縦士は一定条件下での運航を想定した国家資格です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "登録された無人航空機の所有者が変更になった場合の対応として適切なものはどれか。",
        choices: [
          "登録情報の変更手続きを行う",
          "何もする必要はない",
          "登録を削除するだけでよい"
        ],
        answer: 0,
        explanation:
          "所有者変更時は登録情報の変更手続きが必要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "登録の有効期間に関する説明として適切なものはどれか。",
        choices: [
          "更新手続きが必要である",
          "一度登録すれば永久に有効である",
          "飛行ごとに再登録する"
        ],
        answer: 0,
        explanation:
          "無人航空機登録には有効期間があり更新が必要です。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSSの主な役割として最も適切なものはどれか。",
        choices: [
          "機体の位置を測位する",
          "モーター回転数を制御する",
          "バッテリー温度を測定する"
        ],
        answer: 0,
        explanation:
          "GNSSは衛星を利用して機体の位置を測位します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "IMU（慣性計測装置）に含まれる代表的なセンサはどれか。",
        choices: [
          "ジャイロセンサと加速度センサ",
          "気圧センサと温度センサ",
          "カメラとGNSS"
        ],
        answer: 0,
        explanation:
          "IMUは主にジャイロセンサと加速度センサで構成されます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
        
        question:
          "ジャイロセンサの役割として最も適切なものはどれか。",
        choices: [
          "角速度を測定する",
          "高度を測定する",
          "位置を測定する"
        ],
        answer: 0,
        explanation:
          "ジャイロセンサは機体の回転速度（角速度）を測定します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "加速度センサの役割として最も適切なものはどれか。",
        choices: [
          "加速度を測定する",
          "磁北を測定する",
          "バッテリー残量を測定する"
        ],
        answer: 0,
        explanation:
          "加速度センサは機体に加わる加速度を測定します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "地磁気センサの役割として最も適切なものはどれか。",
        choices: [
          "機体の方位を測定する",
          "機体速度を測定する",
          "電流を測定する"
        ],
        answer: 0,
        explanation:
          "地磁気センサは地球磁場を利用して方位を求めます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "気圧センサの主な用途として最も適切なものはどれか。",
        choices: [
          "高度推定",
          "位置測位",
          "映像伝送"
        ],
        answer: 0,
        explanation:
          "気圧の変化から高度を推定します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ESCの役割として最も適切なものはどれか。",
        choices: [
          "モーター回転数を制御する",
          "衛星信号を受信する",
          "映像を記録する"
        ],
        answer: 0,
        explanation:
          "ESCはElectronic Speed Controllerの略でモーター回転数を制御します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ブラシレスモーターの特徴として最も適切なものはどれか。",
        choices: [
          "高効率で摩耗が少ない",
          "必ずブラシが必要である",
          "回転制御ができない"
        ],
        answer: 0,
        explanation:
          "ブラシレスモーターは高効率でメンテナンス性に優れています。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "フライトコントローラの役割として最も適切なものはどれか。",
        choices: [
          "各センサ情報を統合し機体姿勢を制御する",
          "映像のみを記録する",
          "機体重量を測定する"
        ],
        answer: 0,
        explanation:
          "フライトコントローラは飛行制御の中枢です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSS信号を受信できなくなった場合に発生しやすい事象として最も適切なものはどれか。",
        choices: [
          "位置保持性能の低下",
          "モーター停止",
          "バッテリー容量増加"
        ],
        answer: 0,
        explanation:
          "GNSS喪失時は位置保持精度が低下する可能性があります。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "フェールセーフ機能の目的として最も適切なものはどれか。",
        choices: [
          "異常発生時に安全側へ移行する",
          "飛行速度を向上させる",
          "飛行時間を延長する"
        ],
        answer: 0,
        explanation:
          "フェールセーフは異常発生時に安全を確保するための機能です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "RTH（Return To Home）の説明として最も適切なものはどれか。",
        choices: [
          "離陸地点へ自動帰還する機能",
          "モーター停止機能",
          "バッテリー充電機能"
        ],
        answer: 0,
        explanation:
          "RTHは設定されたホームポイントへ自動帰還する機能です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "通信断が発生した場合の対応として最も一般的なものはどれか。",
        choices: [
          "フェールセーフまたはRTHが作動する",
          "必ずその場で着陸する",
          "モーターが停止する"
        ],
        answer: 0,
        explanation:
          "通信断時は機体設定に応じてフェールセーフやRTHが作動します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ホームポイントとして通常記録される位置はどれか。",
        choices: [
          "離陸地点",
          "飛行終了地点",
          "操縦者の自宅"
        ],
        answer: 0,
        explanation:
          "ホームポイントは通常離陸時に記録されます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "リチウムポリマーバッテリーの特徴として最も適切なものはどれか。",
        choices: [
          "高エネルギー密度を持つ",
          "絶対に発熱しない",
          "劣化しない"
        ],
        answer: 0,
        explanation:
          "LiPoバッテリーは高エネルギー密度が特徴です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "リチウムポリマーバッテリーの保管方法として適切なものはどれか。",
        choices: [
          "高温を避け適切な保管電圧で保管する",
          "満充電で数年間放置する",
          "直射日光下に保管する"
        ],
        answer: 0,
        explanation:
          "LiPoバッテリーは適切な電圧で保管します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "バッテリー残量低下時に発生しやすい事象として最も適切なものはどれか。",
        choices: [
          "出力低下やフェールセーフ作動",
          "機体重量増加",
          "GNSS受信感度向上"
        ],
        answer: 0,
        explanation:
          "残量低下により出力低下や自動帰還が発生することがあります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "映像伝送用の電波と操縦用電波について正しいものはどれか。",
        choices: [
          "別系統で運用される場合がある",
          "必ず同じ周波数を使用する",
          "映像伝送のみで操縦できる"
        ],
        answer: 0,
        explanation:
          "映像伝送系と操縦系は別系統の場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "通信品質が低下した場合のリスクとして最も適切なものはどれか。",
        choices: [
          "操縦遅延や通信断",
          "機体重量減少",
          "バッテリー容量増加"
        ],
        answer: 0,
        explanation:
          "通信品質低下は操縦遅延や通信断につながります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "RTH高度の設定目的として最も適切なものはどれか。",
        choices: [
          "障害物との衝突回避",
          "飛行速度向上",
          "通信速度向上"
        ],
        answer: 0,
        explanation:
          "RTH高度は帰還時に障害物を回避するため設定します。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSSの測位精度が低下する要因として最も適切なものはどれか。",
        choices: [
          "建物や地形による電波反射",
          "モーター回転数の増加",
          "プロペラサイズの変更"
        ],
        answer: 0,
        explanation:
          "マルチパスなどの電波反射により測位精度が低下することがあります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチパスとは何か。",
        choices: [
          "衛星信号が反射して受信される現象",
          "複数のモーターを搭載する方式",
          "複数のバッテリーを接続する方式"
        ],
        answer: 0,
        explanation:
          "GNSS信号が建物などで反射し誤差の原因となる現象です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "コンパスキャリブレーションの目的として最も適切なものはどれか。",
        choices: [
          "方位測定精度を向上させる",
          "飛行速度を向上させる",
          "バッテリー寿命を延ばす"
        ],
        answer: 0,
        explanation:
          "地磁気センサの誤差補正を行い方位精度を向上させます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "コンパス異常が発生した場合に起こりやすい現象はどれか。",
        choices: [
          "方位制御の不安定化",
          "映像画質向上",
          "飛行時間延長"
        ],
        answer: 0,
        explanation:
          "機体方位を誤認し飛行制御へ影響する場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSSとIMUを組み合わせて使用する主な理由はどれか。",
        choices: [
          "互いの弱点を補い安定した位置推定を行うため",
          "バッテリー消費をゼロにするため",
          "通信距離を延ばすため"
        ],
        answer: 0,
        explanation:
          "GNSSとIMUを組み合わせることで位置推定精度を向上できます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "2.4GHz帯の電波に関する説明として適切なものはどれか。",
        choices: [
          "Wi-Fiなどでも利用される",
          "無人航空機専用周波数である",
          "屋内では利用できない"
        ],
        answer: 0,
        explanation:
          "2.4GHz帯はWi-Fiなどでも利用される周波数帯です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "電波干渉が発生した場合に起こりやすい事象として適切なものはどれか。",
        choices: [
          "通信品質低下",
          "機体重量増加",
          "飛行時間増加"
        ],
        answer: 0,
        explanation:
          "電波干渉により通信品質が低下する場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSS衛星数が少ない場合に発生しやすい問題として適切なものはどれか。",
        choices: [
          "測位精度低下",
          "モーター停止",
          "プロペラ破損"
        ],
        answer: 0,
        explanation:
          "利用可能衛星数が少ないと測位精度が低下します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "機体近くに強い磁性体が存在する場合に起こりやすい現象はどれか。",
        choices: [
          "コンパス異常",
          "バッテリー容量増加",
          "GNSS感度向上"
        ],
        answer: 0,
        explanation:
          "磁性体は地磁気センサへ影響を与える場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "通信品質確認を飛行前に行う主な目的はどれか。",
        choices: [
          "通信断リスク低減",
          "飛行速度向上",
          "機体重量低減"
        ],
        answer: 0,
        explanation:
          "飛行前に通信品質を確認し安全性を高めます。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GPSモードの特徴として最も適切なものはどれか。",
        choices: [
          "GNSSを利用して位置保持を行う",
          "GNSSを使用しない",
          "必ず手動操縦になる"
        ],
        answer: 0,
        explanation:
          "GPSモードではGNSSを利用して位置保持を行います。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ATTIモードの特徴として最も適切なものはどれか。",
        choices: [
          "位置保持を行わず風で流されることがある",
          "常にRTHが作動する",
          "GNSSが必須である"
        ],
        answer: 0,
        explanation:
          "ATTIモードでは位置保持が行われないため風の影響を受けやすくなります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ATTIモードへ移行する原因として最も適切なものはどれか。",
        choices: [
          "GNSS受信不良",
          "バッテリー満充電",
          "気温上昇"
        ],
        answer: 0,
        explanation:
          "GNSS受信不良などによりATTIモードへ移行する場合があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "冗長化の目的として最も適切なものはどれか。",
        choices: [
          "一部故障時でも安全性を維持する",
          "飛行速度を向上させる",
          "機体重量を増やす"
        ],
        answer: 0,
        explanation:
          "冗長化は故障時の安全性向上を目的とします。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "プロペラの損傷を放置した場合のリスクとして最も適切なものはどれか。",
        choices: [
          "振動増加や飛行性能低下",
          "GNSS精度向上",
          "飛行時間延長"
        ],
        answer: 0,
        explanation:
          "損傷したプロペラは振動や揚力低下の原因になります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチコプターにおいて対角線上のモーターが同じ回転方向を持つ主な理由はどれか。",
        choices: [
          "反トルクを打ち消すため",
          "騒音を増加させるため",
          "バッテリー消費を増やすため"
        ],
        answer: 0,
        explanation:
          "反トルクを相殺し安定飛行を実現します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "セルバランスが崩れたバッテリーに起こりやすい問題として適切なものはどれか。",
        choices: [
          "性能低下や劣化促進",
          "飛行時間延長",
          "重量低下"
        ],
        answer: 0,
        explanation:
          "セルバランス異常はバッテリー性能低下の原因になります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ファームウェアの主な役割として最も適切なものはどれか。",
        choices: [
          "機体や送信機の制御プログラム",
          "バッテリーそのもの",
          "GNSS衛星"
        ],
        answer: 0,
        explanation:
          "ファームウェアは機体制御を行うソフトウェアです。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ファームウェア更新時に注意すべき事項として適切なものはどれか。",
        choices: [
          "更新後の動作確認を行う",
          "更新後は確認不要",
          "飛行中に更新する"
        ],
        answer: 0,
        explanation:
          "更新後は必ず動作確認を行います。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "フライトログを保存する主な目的として最も適切なものはどれか。",
        choices: [
          "飛行状況や異常の分析",
          "機体重量の削減",
          "映像品質向上"
        ],
        answer: 0,
        explanation:
          "フライトログは飛行記録やトラブル解析に利用されます。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前点検の目的として最も適切なものはどれか。",
        choices: [
          "機体異常を発見し事故を防止する",
          "飛行時間を延ばす",
          "映像品質を向上させる"
        ],
        answer: 0,
        explanation:
          "飛行前点検は異常を発見し事故を未然に防ぐために行います。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前にバッテリーを確認する主な理由として最も適切なものはどれか。",
        choices: [
          "飛行中の電力不足を防ぐため",
          "機体重量を増やすため",
          "GNSS感度を上げるため"
        ],
        answer: 0,
        explanation:
          "バッテリー残量や状態を確認し安全運航を確保します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "補助者を配置する主な目的として最も適切なものはどれか。",
        choices: [
          "周囲監視や安全確保を支援するため",
          "飛行速度を向上させるため",
          "映像編集を行うため"
        ],
        answer: 0,
        explanation:
          "補助者は周囲監視や安全確保を支援します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に予期しない強風が発生した場合の対応として最も適切なものはどれか。",
        choices: [
          "安全な場所へ着陸または飛行中止を検討する",
          "そのまま飛行を継続する",
          "高度を最大まで上げる"
        ],
        answer: 0,
        explanation:
          "強風時は安全確保を優先し飛行継続可否を判断します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行日誌を記録する主な目的として最も適切なものはどれか。",
        choices: [
          "飛行実績や異常の記録を残すため",
          "機体を軽量化するため",
          "通信距離を伸ばすため"
        ],
        answer: 0,
        explanation:
          "飛行日誌は飛行記録や安全管理に利用されます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "離陸前ブリーフィングの目的として最も適切なものはどれか。",
        choices: [
          "関係者間で飛行計画や役割を共有する",
          "機体価格を確認する",
          "飛行後の予定を決める"
        ],
        answer: 0,
        explanation:
          "飛行計画や役割分担を共有することが目的です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "緊急着陸地点を事前に決める主な理由として最も適切なものはどれか。",
        choices: [
          "異常発生時に迅速に安全確保するため",
          "飛行速度を上げるため",
          "映像品質を向上させるため"
        ],
        answer: 0,
        explanation:
          "緊急時に安全な着陸場所を確保するためです。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に第三者が飛行区域へ侵入した場合の対応として最も適切なものはどれか。",
        choices: [
          "飛行を中断し安全確保を優先する",
          "飛行を継続する",
          "速度を上げて飛行する"
        ],
        answer: 0,
        explanation:
          "第三者の安全確保を最優先します。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前にNOTAMや空域情報を確認する目的として最も適切なものはどれか。",
        choices: [
          "空域制限や危険情報を把握するため",
          "機体重量を確認するため",
          "飛行速度を確認するため"
        ],
        answer: 0,
        explanation:
          "空域制限や危険情報の確認は安全運航に重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行後点検の目的として最も適切なものはどれか。",
        choices: [
          "損傷や異常の有無を確認するため",
          "GNSS精度を向上させるため",
          "飛行時間を延ばすため"
        ],
        answer: 0,
        explanation:
          "飛行後に機体状態を確認し次回飛行へ備えます。"
    }
    
    ,
    {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "CRM（Crew Resource Management）の目的として最も適切なものはどれか。",
        choices: [
          "人的要因による事故を防止する",
          "飛行速度を向上させる",
          "機体重量を軽くする"
        ],
        answer: 0,
        explanation:
          "CRMは人的要因による事故防止を目的とした考え方です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "CRMにおいて重要な要素として適切なものはどれか。",
        choices: [
          "コミュニケーション",
          "機体価格",
          "飛行回数"
        ],
        answer: 0,
        explanation:
          "CRMでは適切なコミュニケーションが重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "補助者から危険の指摘を受けた場合の対応として最も適切なものはどれか。",
        choices: [
          "内容を確認し安全を優先して判断する",
          "無視して飛行を継続する",
          "補助者を交代させる"
        ],
        answer: 0,
        explanation:
          "安全に関する指摘は真摯に確認する必要があります。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "ヒューマンエラーの発生要因として最も適切なものはどれか。",
        choices: [
          "疲労や思い込み",
          "GNSS受信",
          "プロペラ回転"
        ],
        answer: 0,
        explanation:
          "疲労や思い込みは代表的なヒューマンエラー要因です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "疲労が蓄積した状態での飛行について適切なものはどれか。",
        choices: [
          "判断力低下の原因となるため避けるべき",
          "問題なく飛行できる",
          "飛行性能が向上する"
        ],
        answer: 0,
        explanation:
          "疲労は判断力や注意力を低下させます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "思い込みによる事故を防ぐ方法として適切なものはどれか。",
        choices: [
          "チェックリストを活用する",
          "確認を省略する",
          "経験だけで判断する"
        ],
        answer: 0,
        explanation:
          "チェックリストは思い込み防止に有効です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "安全文化の説明として最も適切なものはどれか。",
        choices: [
          "組織全体で安全を重視する考え方",
          "飛行速度向上を目指す考え方",
          "コスト削減を優先する考え方"
        ],
        answer: 0,
        explanation:
          "安全文化とは安全を最優先に考える組織風土です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行前のダブルチェックの主な目的はどれか。",
        choices: [
          "見落とし防止",
          "飛行時間延長",
          "通信距離向上"
        ],
        answer: 0,
        explanation:
          "複数人で確認することで見落としを減らせます。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "飛行中に想定外の事象が発生した場合の対応として適切なものはどれか。",
        choices: [
          "落ち着いて状況把握を行う",
          "慌てて操作する",
          "確認せず飛行継続する"
        ],
        answer: 0,
        explanation:
          "状況把握と冷静な判断が重要です。"
      },
    
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "安全管理においてインシデント報告を行う目的として適切なものはどれか。",
        choices: [
          "再発防止",
          "責任追及のみ",
          "飛行時間延長"
        ],
        answer: 0,
        explanation:
          "インシデント報告は再発防止に活用されます。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.FIRST,
    
        question:
          "第三者上空を飛行するカテゴリーⅢ飛行について、最も適切なものを選べ。",
        choices: [
          "一等無人航空機操縦士資格と第一種機体認証が必要である",
          "二等無人航空機操縦士資格があれば飛行できる",
          "機体認証は不要である"
        ],
        answer: 0,
        explanation:
          "カテゴリーⅢ飛行には一等無人航空機操縦士資格及び第一種機体認証機が必要である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "カテゴリーⅡB飛行について正しいものを選べ。",
        choices: [
          "技能証明と機体認証があれば許可承認なしで飛行できる場合がある",
          "必ずカテゴリーⅢ飛行として扱われる",
          "飛行マニュアルは不要である"
        ],
        answer: 0,
        explanation:
          "カテゴリーⅡB飛行は技能証明者が認証機を使用し、飛行マニュアルを遵守することで許可承認不要となる場合がある。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "第三者上空を飛行しない特定飛行は、原則としてどのカテゴリーに分類されるか。",
        choices: [
          "カテゴリーⅡ",
          "カテゴリーⅢ",
          "カテゴリーⅠ"
        ],
        answer: 0,
        explanation:
          "第三者上空を飛行しない特定飛行はカテゴリーⅡに分類される。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "カテゴリーⅠ飛行として最も適切なものを選べ。",
        choices: [
          "特定飛行に該当しない飛行",
          "第三者上空飛行",
          "夜間の目視外飛行"
        ],
        answer: 0,
        explanation:
          "特定飛行に該当しない飛行はカテゴリーⅠ飛行である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "カテゴリーⅡA飛行について正しいものを選べ。",
        choices: [
          "認証機と技能証明があっても許可承認が必要である",
          "必ず許可承認不要である",
          "第三者上空飛行のみを指す"
        ],
        answer: 0,
        explanation:
          "カテゴリーⅡA飛行は認証機及び技能証明があっても運航管理の審査と許可承認が必要である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "技能証明の種類として正しいものを選べ。",
        choices: [
          "一等無人航空機操縦士と二等無人航空機操縦士",
          "上級操縦士と一般操縦士",
          "業務用操縦士と趣味用操縦士"
        ],
        answer: 0,
        explanation:
          "技能証明は一等無人航空機操縦士及び二等無人航空機操縦士に区分される。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "登録講習機関を修了した場合に免除されるものとして正しいものを選べ。",
        choices: [
          "実地試験",
          "学科試験",
          "身体検査"
        ],
        answer: 0,
        explanation:
          "登録講習機関修了者は指定試験機関の実地試験が免除される。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "技能証明を受けた者の義務として正しいものを選べ。",
        choices: [
          "限定された範囲内で特定飛行を行う",
          "全ての特定飛行を自由に実施できる",
          "許可承認が不要になる"
        ],
        answer: 0,
        explanation:
          "技能証明者は限定事項及び条件の範囲内で飛行しなければならない。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "技能証明の取消し又は効力停止の対象となる可能性があるものを選べ。",
        choices: [
          "航空法違反や重大な過失",
          "機体の色を変更した",
          "飛行記録を保存した"
        ],
        answer: 0,
        explanation:
          "航空法違反や重大な過失などは技能証明の取消し又は効力停止の対象となる。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "カテゴリーⅢ飛行に必要な機体認証はどれか。",
        choices: [
          "第一種機体認証",
          "第二種機体認証",
          "認証不要"
        ],
        answer: 0,
        explanation:
          "カテゴリーⅢ飛行には第一種機体認証が必要である。"
    },
          
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "機体認証制度の目的として最も適切なものを選べ。",
        choices: [
          "無人航空機の安全性を確認するため",
          "操縦者の技能を評価するため",
          "飛行時間を記録するため"
        ],
        answer: 0,
        explanation:
          "機体認証制度は無人航空機の安全性を確認する制度である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "第二種機体認証について正しいものを選べ。",
        choices: [
          "カテゴリーⅡ飛行で活用される認証である",
          "カテゴリーⅢ飛行専用である",
          "模型航空機に必要である"
        ],
        answer: 0,
        explanation:
          "第二種機体認証は主にカテゴリーⅡ飛行において活用される。"
    },
    
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "リモートID機器について正しいものを選べ。",
        choices: [
          "内蔵型と外付型が存在する",
          "必ず機体内部に組み込まれていなければならない",
          "飛行中のみ発信される"
        ],
        answer: 0,
        explanation:
          "リモートID機器には内蔵型と外付型が存在する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "高度150メートル以上の飛行禁止空域について正しいものを選べ。",
        choices: [
          "直下の地表又は水面から150m以上の高度差を指す",
          "海抜150m以上を指す",
          "標高150m以上の山は全て飛行禁止となる"
        ],
        answer: 0,
        explanation:
          "高度150mとは海抜ではなく、直下の地表又は水面からの高度差を指す。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "空港周辺空域について正しいものを選べ。",
        choices: [
          "制限表面や進入経路の安全確保のため規制されている",
          "空港から5km以上離れていれば自由に飛行できる",
          "夜間のみ規制される"
        ],
        answer: 0,
        explanation:
          "空港周辺空域は航空機の安全な離着陸のため規制されている。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "緊急用務空域について正しいものを選べ。",
        choices: [
          "災害等の状況に応じて国土交通省が指定する",
          "全国で常時設定されている",
          "100g未満の模型航空機は飛行可能である"
        ],
        answer: 0,
        explanation:
          "緊急用務空域は災害等に応じて指定され、模型航空機を含め飛行が制限される。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "小型無人機等飛行禁止法におけるイエローゾーンについて正しいものを選べ。",
        choices: [
          "対象施設周辺おおむね300mの範囲",
          "対象施設周辺おおむね150mの範囲",
          "対象施設内部のみ"
        ],
        answer: 0,
        explanation:
          "イエローゾーンは対象施設周辺おおむね300mの範囲を指す。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "小型無人機等飛行禁止法の対象施設として正しいものを選べ。",
        choices: [
          "国会議事堂",
          "一般病院",
          "市立図書館"
        ],
        answer: 0,
        explanation:
          "国会議事堂は対象施設であり、その周辺には飛行制限がある。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.RULE,
    
        question:
          "対象施設上空のレッドゾーンで無許可飛行を行った場合について正しいものを選べ。",
        choices: [
          "罰則の対象となる可能性がある",
          "注意のみで終了する",
          "レクリエーション飛行なら問題ない"
        ],
        answer: 0,
        explanation:
          "レッドゾーンでの無許可飛行は懲役又は罰金の対象となる可能性がある。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSSによる位置測位について正しいものを選べ。",
        choices: [
          "最低4個以上の衛星から同時に信号を受信する必要がある",
          "最低2個以上の衛星から信号を受信すれば測位できる",
          "衛星は1個でも測位可能である"
        ],
        answer: 0,
        explanation:
          "GNSSは最低4個以上の人工衛星から同時に信号を受信することで位置を算出する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "GNSSの測位精度に影響を与える要因として適切なものを選べ。",
        choices: [
          "建物によるマルチパス",
          "機体の色",
          "送信機の重量"
        ],
        answer: 0,
        explanation:
          "建物などによる電波反射（マルチパス）はGNSS測位精度を低下させる。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチパス現象について正しいものを選べ。",
        choices: [
          "電波が複数経路で到達する現象",
          "バッテリー電圧が低下する現象",
          "プロペラの振動現象"
        ],
        answer: 0,
        explanation:
          "マルチパスは電波が建物や地面で反射し複数経路で受信される現象である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチパスによる通信不安定が発生した場合の対応として適切なものを選べ。",
        choices: [
          "送信機を高い位置に持ちアンテナ方向を調整する",
          "送信機の電源を切る",
          "バッテリーを交換する"
        ],
        answer: 0,
        explanation:
          "マルチパス時は送信機を高い位置に移動しアンテナ方向を調整する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "地磁気センサの役割として正しいものを選べ。",
        choices: [
          "機体の向いている方角を検出する",
          "高度を測定する",
          "気温を測定する"
        ],
        answer: 0,
        explanation:
          "地磁気センサは地球磁場を利用して方位を検出する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ジャイロセンサの役割として正しいものを選べ。",
        choices: [
          "機体の回転角速度を検出する",
          "位置情報を取得する",
          "バッテリー残量を計測する"
        ],
        answer: 0,
        explanation:
          "ジャイロセンサは機体の回転運動を検出する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "加速度センサの役割として正しいものを選べ。",
        choices: [
          "速度変化や加速度を検出する",
          "方位を測定する",
          "通信距離を測定する"
        ],
        answer: 0,
        explanation:
          "加速度センサは機体の加速度や速度変化を検出する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "LiDARの説明として正しいものを選べ。",
        choices: [
          "レーザー光の反射時間から距離を測定する",
          "超音波の反射で方位を測定する",
          "磁力線から高度を測定する"
        ],
        answer: 0,
        explanation:
          "LiDARはレーザー光の往復時間から距離や高度を測定する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチローターが上昇する条件として正しいものを選べ。",
        choices: [
          "全ローターの推力が機体重量を上回る",
          "前方ローターのみ回転数を上げる",
          "ラダー操作を行う"
        ],
        answer: 0,
        explanation:
          "総揚力が機体重量を上回ると機体は上昇する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチローターが前進する仕組みとして正しいものを選べ。",
        choices: [
          "機体を前方へ傾け推力の一部を前方成分にする",
          "全ローターを同時停止する",
          "ラダーのみ操作する"
        ],
        answer: 0,
        explanation:
          "機体を前傾させることで推力の一部が前方へ働く。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチローターのヨー制御について正しいものを選べ。",
        choices: [
          "反トルクのバランスを崩して機体を回転させる",
          "全ローターを停止する",
          "機首を上下させる"
        ],
        answer: 0,
        explanation:
          "ヨーは反トルクのバランス変化により発生する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチローターのブレードについて正しいものを選べ。",
        choices: [
          "通常は固定ピッチで回転数制御を行う",
          "飛行中に可変ピッチ制御を行う",
          "揚力は発生しない"
        ],
        answer: 0,
        explanation:
          "一般的なマルチローターは固定ピッチで回転数を変化させて制御する。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "送信機アンテナについて正しいものを選べ。",
        choices: [
          "電波強度は方向によって異なる",
          "どの方向でも同じ強度である",
          "アンテナ角度は関係ない"
        ],
        answer: 0,
        explanation:
          "アンテナには指向性があり方向によって電波強度が異なる。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "通信状態を改善する方法として適切なものを選べ。",
        choices: [
          "アンテナ方向を調整する",
          "プロペラを交換する",
          "機体色を変更する"
        ],
        answer: 0,
        explanation:
          "通信不良時はアンテナ方向の調整が有効である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "ESCの役割として正しいものを選べ。",
        choices: [
          "モーター回転数を制御する",
          "GNSS信号を受信する",
          "方位を検出する"
        ],
        answer: 0,
        explanation:
          "ESCはモーター回転数を制御する装置である。"
    },
    
    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,
    
        question:
          "マルチローターの飛行制御におけるESCの働きとして正しいものを選べ。",
        choices: [
          "各モーター回転数を変化させ姿勢制御を行う",
          "衛星信号を増幅する",
          "バッテリー容量を増加させる"
        ],
        answer: 0,
        explanation:
          "ESCは各モーター回転数を個別制御し機体姿勢を安定させる。"
    },
    
      
      {
        subject: "drone",
        category: CATEGORIES.RISK,
    
        question:
          "無人航空機を飛行させる前に、補助者と確認しておくべき事項として最も適切なものはどれか？",
    
        choices: [
          "監視範囲、合図、緊急時の連絡方法を確認する",
          "補助者の好きな機体メーカーを確認する",
          "飛行後の片付けだけ確認する"
        ],
    
        answer: 0,
    
        explanation:
          "補助者を配置する場合は、監視範囲、合図、緊急時の連絡方法などを事前に共有しておく必要があります。"
      },

    {  
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "空港周辺の制限表面について、最も適切なものはどれか？",
        choices: [
        "進入表面、水平表面、転移表面は、航空機の離着陸や空港周辺の低空飛行の安全を確保するために設定される制限表面である",
        "水平表面は、無人航空機が水平飛行するために設定される区域であり、有人航空機の離着陸とは直接関係しない",
        "転移表面は、空港から十分に離れた山岳地帯の高度制限を示すものであり、進入表面や水平表面とは別の制度である"
        ],
        answer: 0,
        explanation:
        "進入表面、水平表面、転移表面は、航空機の安全な離着陸や空港周辺での飛行安全を確保するために設定される制限表面です。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "空港等の周辺の空域で無人航空機を飛行させる場合の考え方として、最も適切なものはどれか？",
        choices: [
        "空港周辺では、進入表面、転移表面、水平表面等の上空が飛行禁止空域となる場合があり、場所によっては制限高以下でも確認が必要となる",
        "空港から5km以上離れていれば、制限表面や告示空域を確認しなくても常に自由に飛行できる",
        "空港周辺の規制は有人航空機だけを対象とするため、100g以上の無人航空機であっても低高度なら確認は不要である"
        ],
        answer: 0,
        explanation:
        "空港等の周辺では、制限表面や告示空域などにより飛行が制限されます。単純な距離だけで判断せず、飛行場所の空域情報を確認する必要があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "リモートID機能により発信される情報について、最も適切なものはどれか？",
        choices: [
        "製造番号や登録記号などの静的情報に加え、位置、速度、高度、時刻などの動的情報が含まれるが、所有者や使用者の個人情報は含まれない",
        "事故発生時の所有者特定を目的としているため、所有者の氏名、住所、電話番号も周囲に発信される",
        "プライバシー保護のため、発信される情報は登録記号のみであり、位置や高度などの動的情報は含まれない"
        ],
        answer: 0,
        explanation:
        "リモートIDでは、製造番号、登録記号、位置、速度、高度、時刻などが発信されますが、所有者や使用者の情報は含まれません。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "小型無人機等飛行禁止法に関する説明として、最も適切なものはどれか？",
        choices: [
        "重要施設の敷地・区域の上空だけでなく、その周辺おおむね300mの上空も規制対象となる場合があり、対象施設が一時的に追加されることもある",
        "航空法で空港周辺が規制されているため、小型無人機等飛行禁止法では空港が対象施設に含まれることはない",
        "小型無人機等飛行禁止法は100g以上の無人航空機だけを対象とし、100g未満の小型機や模型航空機には一切関係しない"
        ],
        answer: 0,
        explanation:
        "小型無人機等飛行禁止法では、対象施設の敷地・区域の上空や周辺おおむね300mが規制対象となる場合があります。対象施設が一時的に追加される場合もあります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "高度150m以上の飛行禁止空域について、最も注意すべきものはどれか？",
        choices: [
        "山岳地など地形が起伏している場所では、海抜高度ではなく、無人航空機の直下の地表又は水面からの高度差で150m以上かを判断する必要がある",
        "標高150m以上の土地では、地表から1mでも上昇すれば必ず高度150m以上の飛行禁止空域に該当する",
        "海抜高度が150m未満であれば、直下の地表又は水面からの高度差が150mを超えていても許可は不要である"
        ],
        answer: 0,
        explanation:
        "高度150m以上とは、海抜高度ではなく、無人航空機の直下の地表又は水面からの高度差で判断します。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "飛行自粛要請空域について、最も適切な説明はどれか？",
        choices: [
        "国土交通省が飛行自粛を要請することがあり、操縦者は飛行前に該当空域の有無を確認し、要請内容に応じて適切に対応する必要がある",
        "飛行自粛要請は航空法上の許可制度と同じであり、違反した場合は常に直ちに罰金刑となる",
        "飛行自粛要請は報道機関だけを対象とする情報であり、一般の無人航空機操縦者が確認する必要はない"
        ],
        answer: 0,
        explanation:
        "飛行自粛要請空域が設定される場合があるため、操縦者は飛行前に情報を確認し、要請内容に基づいて対応する必要があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "回転翼航空機であるヘリコプターの特徴として、最も適切なものはどれか？",
        choices: [
        "ヘリコプターは主に1組の大きなローターで揚力を発生させるため、ローター直径が大きくなりやすく、マルチローターとは異なる可変ピッチ機構などを備える",
        "ヘリコプターはマルチローターと同じく、複数の固定ピッチプロペラの回転数だけを変化させてピッチ、ロール、ヨーを制御する",
        "ヘリコプターは固定翼機と同じく、主翼だけで揚力を発生させるため、ホバリングや垂直離着陸は原理上できない"
        ],
        answer: 0,
        explanation:
        "ヘリコプターは1組の大きなローターで揚力を発生させ、ローター面やピッチ角を変化させる機構を持ちます。マルチローターの固定ピッチ・回転数制御とは異なります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "ヘリコプター型の回転翼航空機におけるスワッシュプレートの役割として、最も適切なものはどれか？",
        choices: [
        "メインローターの回転面を傾けたり、ローターピッチ角を変化させたりするために用いられる機構である",
        "GNSS信号を増幅して位置保持精度を高めるために用いられる電子部品である",
        "テールローターの代わりに反トルクを完全に打ち消すため、全てのヘリコプターに不要となる装置である"
        ],
        answer: 0,
        explanation:
        "スワッシュプレートは、ヘリコプターのローター面やローターピッチ角を変化させるための機構です。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "ヘリコプターのテールローターについて、最も適切なものはどれか？",
        choices: [
        "メインローターの反トルクを打ち消したり、機体の向きであるヨー方向の制御に用いられる",
        "機体の上下移動だけを担当する装置であり、ヨー方向の制御とは関係しない",
        "固定翼機にも必ず装備され、主翼の揚力を増加させるために使用される"
        ],
        answer: 0,
        explanation:
        "テールローターは、メインローターの反トルクを打ち消す役割や、ヨー方向の制御に用いられます。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "飛行機、回転翼航空機、パワードリフト機の特徴として、最も適切なものはどれか？",
        choices: [
        "飛行機は速度やエネルギー効率に優れ長距離・長時間飛行に向き、回転翼航空機は垂直離着陸やホバリングが可能で、パワードリフト機は両者の特徴を組み合わせた機体である",
        "回転翼航空機は固定翼機より常に長距離飛行に向き、飛行機は垂直離着陸とホバリングが可能で、パワードリフト機は水上専用機である",
        "飛行機、回転翼航空機、パワードリフト機はいずれも同じ飛行原理であり、操縦や運航リスクに違いはない"
        ],
        answer: 0,
        explanation:
        "飛行機は速度と効率に優れ、回転翼航空機は垂直離着陸やホバリングが可能です。パワードリフト機は両者の特徴を組み合わせた機体です。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "高度を計測するセンサの説明として、適切ではないものはどれか？",
        choices: [
        "LiDARはレーザー光の反射時間ではなく、レーザー光を照射したときの出力値そのものから高度を計測する",
        "超音波センサは、音波を発射して対象物から反射して戻るまでの時間を利用して距離や高度を推定する",
        "気圧センサは、気圧の変化を利用して高度を推定するため、機体の高度推定に利用されることがある"
        ],
        answer: 0,
        explanation:
        "LiDARはレーザー光の反射時間を利用して距離や高度を測定します。出力値そのものだけで高度を測るという説明は不適切です。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "リチウムポリマーバッテリーの取り扱いとして、適切ではないものはどれか？",
        choices: [
        "複数セルのバッテリーでは、効率的な放電のためにセル間の電圧差を意図的に大きくして充電することが望ましい",
        "バランスコネクタを備えるバッテリーでは、充電時に各セルの充電量のバランスを補正することが重要である",
        "リチウムポリマーバッテリーは高エネルギー密度である一方、取り扱いを誤ると発熱や劣化などのリスクがあるため管理が必要である"
        ],
        answer: 0,
        explanation:
        "複数セルのバッテリーでは、セル間の電圧差を大きくするのではなく、バランスを保つことが重要です。"
  },

{
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "空港周辺の制限表面に関する説明として、適切ではないものはどれか？",
        choices: [
        "進入表面、水平表面、転移表面は、すべての空港で同じ形状・同じ範囲として一律に設定される",
        "進入表面は、航空機が滑走路へ進入又は離陸する際の安全を確保するために設定される",
        "転移表面は、進入表面や滑走路周辺の空域と関連して航空機の安全を確保するための制限表面である"
        ],
        answer: 0,
        explanation:
        "制限表面は空港の種類や滑走路の条件などに応じて設定されます。すべての空港で同じ形状・同じ範囲とは限りません。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "空港等の周辺で制限高以下の高度で飛行する場合の考え方として、最も適切なものはどれか？",
        choices: [
        "制限高以下であっても、告示空域や地理院地図等で示される範囲など、別途確認が必要な場合がある",
        "制限高以下であれば、空港周辺であってもDIPSや空域情報を確認する必要は一切ない",
        "空港から一定距離以上離れていれば、進入表面や水平表面の影響を受けることは絶対にない"
        ],
        answer: 0,
        explanation:
        "空港周辺では、制限表面や告示空域などを確認する必要があります。単純に距離や高度だけで判断しないことが重要です。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "模型航空機に対する規制として、最も適切なものはどれか？",
        choices: [
        "100g未満であっても、航空機の飛行に影響を及ぼすおそれがある空域では、航空法上の規制対象となる場合がある",
        "100g未満であれば、緊急用務空域や空港周辺であっても航空法上の規制を一切受けない",
        "模型航空機は無人航空機ではないため、高度や空港周辺に関する規制は常に適用されない"
        ],
        answer: 0,
        explanation:
        "100g未満の模型航空機であっても、航空機の飛行に影響を及ぼすおそれがある空域では規制対象となる場合があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "カテゴリーⅡA飛行とカテゴリーⅡB飛行の説明として、最も適切なものはどれか？",
        choices: [
        "カテゴリーⅡB飛行は一定の条件下で許可・承認が不要となる場合があるが、カテゴリーⅡA飛行はリスクが高く、許可・承認が必要となる場合がある",
        "カテゴリーⅡA飛行もカテゴリーⅡB飛行も、技能証明と機体認証があれば飛行マニュアルの作成や遵守は不要である",
        "カテゴリーⅡA飛行は第三者上空を飛行するため、常にカテゴリーⅢ飛行と同じ扱いになる"
        ],
        answer: 0,
        explanation:
        "カテゴリーⅡB飛行は一定の条件を満たすと許可・承認が不要となる場合があります。一方、カテゴリーⅡA飛行はよりリスクが高く、許可・承認が必要となる場合があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "物件投下に関する説明として、適切ではないものはどれか？",
        choices: [
        "農薬や水などの液体を散布する行為は、危険性が低い場合には物件投下に含まれない",
        "無人航空機から液体や霧状のものを散布する行為は、物件投下に含まれる場合がある",
        "輸送した物件を地表に落下させずに置く行為は、物件投下とは区別される場合がある"
        ],
        answer: 0,
        explanation:
        "水や農薬などの液体・霧状のものを散布する行為も、物件投下に含まれます。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
        "技能証明と登録講習機関に関する説明として、最も適切なものはどれか？",
        choices: [
        "登録講習機関の講習を修了し修了審査に合格した場合、指定試験機関の実地試験が免除されるが、学科試験は原則として免除されない",
        "登録講習機関を修了すれば、学科試験、実地試験、身体検査のすべてが免除される",
        "技能証明は機体登録を完了した時点で自動的に付与され、別途試験や身体検査は不要である"
        ],
        answer: 0,
        explanation:
        "登録講習機関を修了した場合、指定試験機関の実地試験が免除されますが、学科試験は原則として免除されません。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "ヘリコプターのメインローターとマルチローターのブレード制御の違いとして、最も適切なものはどれか？",
        choices: [
        "ヘリコプターはローターブレードのピッチ角を変化させて制御するが、一般的なマルチローターは固定ピッチのプロペラ回転数を変化させて制御する",
        "ヘリコプターもマルチローターも、すべてのブレード角を固定したまま、常に同じ回転数で飛行する",
        "マルチローターはスワッシュプレートでローター面を傾けるが、ヘリコプターは各モーター回転数だけで姿勢を制御する"
        ],
        answer: 0,
        explanation:
        "ヘリコプターは可変ピッチ機構を持ち、マルチローターは一般に固定ピッチのプロペラ回転数を変化させて制御します。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "大型の回転翼航空機、特に最大離陸重量25kg以上のマルチローターの特徴として、適切ではないものはどれか？",
        choices: [
        "機体やローターが大きくなるため慣性が増し、上昇・降下や加減速に必要な時間と距離が短くなる",
        "機体の対角寸法やローターサイズ、モーターパワーが大きくなり、飛行中の慣性力も増加する",
        "小型機に比べて騒音が大きくなり、周囲への影響範囲も広くなる可能性がある"
        ],
        answer: 0,
        explanation:
        "大型機は慣性力が増えるため、上昇・降下や加減速に要する時間と距離が長くなる傾向があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "ビジョンセンサーを利用した安全機能について、最も適切なものはどれか？",
        choices: [
        "カメラ画像を利用するため、夜間や暗所などでは衝突回避や姿勢安定機能が十分に働かない可能性がある",
        "ビジョンセンサーはGNSS衛星からの信号を直接受信するため、暗所や夜間ほど精度が高くなる",
        "ビジョンセンサーが搭載されていれば、夜間飛行の承認や灯火の確認は不要となる"
        ],
        answer: 0,
        explanation:
        "ビジョンセンサーは画像を利用するため、夜間や暗所では十分に機能しない場合があります。夜間飛行の承認や灯火の確認とは別に考える必要があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "無人航空機に使用される電波の周波数帯に関する説明として、適切ではないものはどれか？",
        choices: [
        "通信可能距離は、周波数帯や出力、アンテナ特性、変調方式、伝送速度に関係なく一定である",
        "無人航空機では2.4GHz帯や5.7GHz帯など、複数の周波数帯が利用されることがある",
        "169MHz帯は、無人移動体画像伝送システムの無線局のバックアップ回線として利用される場合がある"
        ],
        answer: 0,
        explanation:
        "通信可能距離は、周波数帯、出力、アンテナ特性、変調方式、伝送速度などにより変動します。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "リチウムポリマーバッテリーの特性として、適切ではないものはどれか？",
        choices: [
        "電解質は不燃物であり、衝撃や高温環境でも発火や劣化のリスクはほとんどない",
        "エネルギー密度が高く、無人航空機の電源として多く利用されている",
        "自己放電が少なく、メモリ効果が小さい一方で、取り扱いには注意が必要である"
        ],
        answer: 0,
        explanation:
        "リチウムポリマーバッテリーは高エネルギー密度などの利点がありますが、電解質は可燃物であり、取り扱いには注意が必要です。"
    },

    {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
        "物件投下装置を搭載した無人航空機の運用として、最も適切なものはどれか？",
        choices: [
        "投下装置の搭載位置や対象物、吊り下げ時の揺れ、投下前後の重心変化を考慮して運用する",
        "物件投下装置は対象物が揺れない構造であるため、飛行中の重心移動を考慮する必要はない",
        "ウインチ機構で物件を吊り下げる場合は、必ず飛行禁止となり、装置の特性を理解しても運用できない"
        ],
        answer: 0,
        explanation:
        "物件投下装置を使用する場合は、装置の特性、搭載位置、対象物の揺れ、投下前後の重心変化を考慮する必要があります。"
    },

    {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "空港等周辺空域に関する説明として最も適切なものはどれか。",

        choices: [
            "航空機の離着陸の安全を確保するため飛行が制限される空域である",
            "空港から5km以上離れていれば必ず飛行可能である",
            "夜間のみ規制される空域である"
        ],

        answer: 0,

        explanation:
            "空港等周辺空域は航空機の安全な離着陸を確保するために設定されている。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "カテゴリーⅡB飛行について最も適切なものはどれか。",

        choices: [
            "認証機と技能証明を前提に許可承認不要となる場合がある",
            "常に国土交通大臣の承認が必要である",
            "第三者上空飛行のみを指す"
        ],

        answer: 0,

        explanation:
            "カテゴリーⅡB飛行は一定条件を満たすことで許可承認不要となる場合がある。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "登録講習機関を修了した者について正しいものはどれか。",

        choices: [
            "指定試験機関の実地試験が免除される",
            "学科試験が免除される",
            "身体検査が免除される"
        ],

        answer: 0,

        explanation:
            "登録講習機関修了者は実地試験の免除対象となる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "技能証明の効力停止処分を受ける可能性があるものはどれか。",

        choices: [
            "航空法違反や重大な過失",
            "機体色の変更",
            "飛行日誌の作成"
        ],

        answer: 0,

        explanation:
            "航空法違反や重大な過失は行政処分対象となる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "模型航空機について最も適切なものはどれか。",

        choices: [
            "100g未満であっても飛行場所によっては規制対象となる",
            "航空法の適用を一切受けない",
            "空港周辺空域でも自由に飛行できる"
        ],

        answer: 0,

        explanation:
            "模型航空機であっても飛行場所によっては規制対象となる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "飛行自粛要請空域について正しいものはどれか。",

        choices: [
            "国や自治体が公表する情報を飛行前に確認する必要がある",
            "航空法に規定されていないため無視してよい",
            "災害時のみ設定される"
        ],

        answer: 0,

        explanation:
            "飛行自粛要請空域は飛行前に確認することが重要である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "高度150m以上の飛行禁止空域に関する説明として最も適切なものはどれか。",

        choices: [
            "直下の地表又は水面から150m以上で判断する",
            "海抜150m以上で判断する",
            "標高150m以上の山は飛行禁止となる"
        ],

        answer: 0,

        explanation:
            "高度150m以上とは海抜ではなく直下地表からの高度差である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "小型無人機等飛行禁止法における対象施設として適切なものはどれか。",

        choices: [
            "国会議事堂",
            "一般公園",
            "市民体育館"
        ],

        answer: 0,

        explanation:
            "国会議事堂は対象施設に指定されている。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "シングルローターヘリコプターにおいてテールローターが必要な主な理由はどれか。",

        choices: [
            "主回転翼による反トルクを打ち消すため",
            "高度を測定するため",
            "GNSS信号を受信するため"
        ],

        answer: 0,

        explanation:
            "テールローターは主回転翼の反トルクを打ち消すために用いられる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "スワッシュプレートの役割として最も適切なものはどれか。",

        choices: [
            "回転するローターブレードへ操縦入力を伝達する",
            "バッテリー電圧を調整する",
            "GNSS信号を増幅する"
        ],

        answer: 0,

        explanation:
            "スワッシュプレートは回転翼機の操縦入力伝達装置である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "固定翼機が飛行を維持するために必要なものとして最も適切なものはどれか。",

        choices: [
            "前進速度",
            "GNSS信号",
            "RTH機能"
        ],

        answer: 0,

        explanation:
            "固定翼機は翼に気流を受けて揚力を発生させる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "マルチローターと比較した固定翼機の特徴として適切なものはどれか。",

        choices: [
            "一般的に長距離飛行に適している",
            "その場で静止しやすい",
            "離着陸に広い場所を必要としない"
        ],

        answer: 0,

        explanation:
            "固定翼機は効率が良く長距離飛行に適している。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "LiDARが利用される主な目的として最も適切なものはどれか。",

        choices: [
            "距離や地形情報の取得",
            "バッテリー残量測定",
            "映像圧縮"
        ],

        answer: 0,

        explanation:
            "LiDARはレーザーを用いて距離を測定する。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "ATTIモード飛行中に強風を受けた場合に起こりやすい現象はどれか。",

        choices: [
            "機体が風に流される",
            "GNSS精度が向上する",
            "飛行時間が延びる"
        ],

        answer: 0,

        explanation:
            "ATTIモードでは位置保持を行わないため風の影響を受けやすい。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "ビジョンセンサーが正常に機能しにくい環境として最も適切なものはどれか。",

        choices: [
            "暗所や模様の少ない地面",
            "十分な照度がある場所",
            "コントラストが高い地面"
        ],

        answer: 0,

        explanation:
            "ビジョンセンサーは照度や地表模様の影響を受ける。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "ESC故障時に発生する可能性が高い事象はどれか。",

        choices: [
            "モーター回転制御異常",
            "GNSS測位精度向上",
            "バッテリー容量増加"
        ],

        answer: 0,

        explanation:
            "ESCはモーター回転数を制御している。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "飛行計画を立案する際に最も重要な考え方はどれか。",

        choices: [
            "危険な状況にならないよう事前に回避する",
            "異常発生後に対応すればよい",
            "飛行時間を最優先する"
        ],

        answer: 0,

        explanation:
            "リスク管理では危険発生前の予防が重要である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "CRMの考え方として最も適切なものはどれか。",

        choices: [
            "利用可能な人的資源を活用して安全を高める",
            "操縦者だけで全て判断する",
            "補助者の意見は考慮しない"
        ],

        answer: 0,

        explanation:
            "CRMはチーム全体で安全性を向上させる考え方である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "飛行経験のある場所で飛行する場合について最も適切なものはどれか。",

        choices: [
            "経験の有無に関係なく飛行計画を作成する",
            "経験があれば事前確認は不要である",
            "経験があれば気象確認は不要である"
        ],

        answer: 0,

        explanation:
            "教則では経験のある場所でも飛行計画作成を求めている。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "飛行中に天候悪化の兆候を確認した場合として最も適切な対応はどれか。",

        choices: [
            "帰還または緊急着陸を判断する",
            "予定終了まで飛行を継続する",
            "自動操縦に任せる"
        ],

        answer: 0,

        explanation:
            "危険な状況になる前に飛行を終了する判断が重要である。"
},

{
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "空港等周辺空域に設定される『水平表面』について最も適切なものはどれか。",

        choices: [
            "空港周辺の一定高度以下の空域を保護するため設定される",
            "空港滑走路上空のみを対象とする",
            "夜間のみ適用される"
        ],

        answer: 0,

        explanation:
            "水平表面は航空機の離着陸の安全確保を目的として設定される制限表面の一つである。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "転移表面の説明として最も適切なものはどれか。",

        choices: [
            "滑走路周辺の制限表面と水平表面をつなぐ傾斜した空域である",
            "空港外周300mの区域である",
            "航空機が駐機する区域である"
        ],

        answer: 0,

        explanation:
            "転移表面は制限表面の一つであり、側方の安全確保を目的としている。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "円錐表面について正しいものはどれか。",

        choices: [
            "水平表面の外側に広がる上向きの傾斜面である",
            "滑走路中心線のみを保護する",
            "空港内地上部分のみを指す"
        ],

        answer: 0,

        explanation:
            "円錐表面は水平表面外側に設けられる制限表面である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "進入表面が設定される主な理由として最も適切なものはどれか。",

        choices: [
            "航空機の進入経路を保護するため",
            "騒音を抑制するため",
            "GNSS精度を向上させるため"
        ],

        answer: 0,

        explanation:
            "進入表面は着陸進入経路の安全確保を目的として設定される。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "カテゴリーⅡA飛行について最も適切なものはどれか。",

        choices: [
            "技能証明や認証機があっても許可承認が必要となる飛行が含まれる",
            "常に許可承認不要である",
            "第三者上空飛行のみを指す"
        ],

        answer: 0,

        explanation:
            "カテゴリーⅡA飛行は運航管理等について審査を受ける必要がある。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "カテゴリーⅡB飛行について最も適切なものはどれか。",

        choices: [
            "認証機及び技能証明により許可承認不要となる場合がある",
            "必ずカテゴリーⅢ飛行である",
            "飛行マニュアル遵守は不要である"
        ],

        answer: 0,

        explanation:
            "カテゴリーⅡB飛行は一定条件を満たした場合に許可承認不要となる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "第一種機体認証について正しいものはどれか。",

        choices: [
            "カテゴリーⅢ飛行で必要となる認証である",
            "模型航空機専用認証である",
            "技能証明の代替となる制度である"
        ],

        answer: 0,

        explanation:
            "カテゴリーⅢ飛行では第一種機体認証機が必要となる。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "第三者上空飛行について最も適切なものはどれか。",

        choices: [
            "立入管理措置を講じていない第三者の上空を飛行すること",
            "補助者の上空を飛行すること",
            "操縦者の上空を飛行すること"
        ],

        answer: 0,

        explanation:
            "第三者上空飛行はカテゴリーⅢ飛行に該当する。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "カテゴリーⅢ飛行を実施するために必要な組み合わせとして最も適切なものはどれか。",

        choices: [
            "一等無人航空機操縦士＋第一種機体認証",
            "二等無人航空機操縦士＋第二種機体認証",
            "機体登録のみ"
        ],

        answer: 0,

        explanation:
            "カテゴリーⅢ飛行では一等資格及び第一種機体認証が必要である。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "技能証明の効力停止処分について最も適切なものはどれか。",

        choices: [
            "航空法違反等により行政処分として行われる場合がある",
            "本人が希望すればいつでも停止される",
            "機体故障のみで自動停止される"
        ],

        answer: 0,

        explanation:
            "重大な法令違反等では技能証明の効力停止処分が行われる場合がある。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "第三者上空飛行が厳しく規制されている主な理由として最も適切なものはどれか。",

        choices: [
            "墜落時に第三者へ直接危害を及ぼす危険性が高いため",
            "騒音が大きいため",
            "飛行時間が短くなるため"
        ],

        answer: 0,

        explanation:
            "第三者上空飛行は人的被害リスクが高いため厳格に規制されている。"
},

{
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "カテゴリーⅡB飛行に関する説明として、最も適切なものはどれか。",

        choices: [
            "技能証明を受けた操縦者が認証機を使用し、定められた飛行マニュアル等を遵守することで、許可・承認を要しない場合がある飛行である",
            "技能証明を受けた操縦者が操縦する飛行であれば、機体認証の有無に関係なく常に許可・承認が不要となる飛行である",
            "認証機を使用していれば、操縦者が技能証明を保有していなくても許可・承認が不要となる飛行である"
        ],

        answer: 0,

        explanation:
            "カテゴリーⅡB飛行では技能証明、認証機、飛行マニュアル遵守等の条件を満たす必要があります。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "高度150m以上の空域について、最も適切な説明はどれか。",

        choices: [
            "無人航空機直下の地表又は水面から150m以上の高度差がある空域を指し、海抜高度とは異なる考え方で判断される",
            "海抜150m以上の空域を指し、山岳地帯では地表からの高度差は考慮しない",
            "標高150m以上の場所において飛行する場合は、高度に関係なく飛行禁止空域として扱われる"
        ],

        answer: 0,

        explanation:
            "高度150m以上は海抜ではなく直下地表等からの高度差で判断します。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "登録講習機関を修了した者について、最も適切な説明はどれか。",

        choices: [
            "指定試験機関が実施する実地試験の全部又は一部が免除されるが、学科試験や身体検査は原則として免除されない",
            "学科試験、実地試験及び身体検査の全てが免除されるため、そのまま技能証明を取得できる",
            "登録講習機関を修了した場合は、技能証明を受けなくても特定飛行を自由に行うことができる"
        ],

        answer: 0,

        explanation:
            "登録講習機関修了による主なメリットは実地試験の免除です。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "第三者上空飛行について、最も適切な説明はどれか。",

        choices: [
            "立入管理措置を講じていない第三者の上空を飛行するものであり、高い安全性が求められるカテゴリーⅢ飛行に該当する",
            "操縦者及び補助者の上空を飛行するものであり、カテゴリーⅠ飛行に分類される",
            "第三者から30m以上離れていれば上空飛行に該当せず、カテゴリー区分とは無関係である"
        ],

        answer: 0,

        explanation:
            "第三者上空飛行はカテゴリーⅢ飛行に該当します。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "GNSSとIMUを併用する主な理由として、最も適切なものはどれか。",

        choices: [
            "GNSSによる位置情報とIMUによる姿勢・加速度情報を組み合わせることで、より安定した位置推定を行うため",
            "GNSSだけでは位置測位ができないため、IMUが代わりに衛星信号を受信するため",
            "IMUが取得した情報をGNSS衛星へ送信することで測位精度を向上させるため"
        ],

        answer: 0,

        explanation:
            "GNSSとIMUは互いの弱点を補完する目的で使用されます。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "スワッシュプレートの役割として、最も適切なものはどれか。",

        choices: [
            "操縦者の入力を回転中のメインローターブレードへ伝達し、機体姿勢や進行方向を制御するために用いられる",
            "モーター回転数を制御し、マルチローターの各ローターへ電力を供給するために用いられる",
            "GNSS信号を受信し、機体位置を算出するために用いられる"
        ],

        answer: 0,

        explanation:
            "スワッシュプレートは回転翼機特有の操縦機構です。"
        },

        {
        subject: "drone",
        category: CATEGORIES.SYSTEM,

        question:
            "ATTIモードに移行した場合の飛行特性として、最も適切なものはどれか。",

        choices: [
            "GNSSによる位置保持が行われなくなるため、風の影響を受けて機体が流されやすくなる",
            "自動的にRTHが作動するため、操縦者による操作は一切不要となる",
            "通常のGPSモードより位置保持性能が向上し、風の影響を受けにくくなる"
        ],

        answer: 0,

        explanation:
            "ATTIモードでは位置保持が行われません。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "CRM（Crew Resource Management）の考え方として、最も適切なものはどれか。",

        choices: [
            "操縦者だけでなく補助者や関係者も含めた人的資源を有効活用し、安全性向上を図る考え方である",
            "操縦者の経験を最優先とし、補助者からの助言は原則として受けない考え方である",
            "機体性能を最大限発揮することを目的として飛行効率を高める考え方である"
        ],

        answer: 0,

        explanation:
            "CRMは人的資源を活用して安全性向上を図る考え方です。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RISK,

        question:
            "飛行経験のある場所で飛行する場合の考え方として、最も適切なものはどれか。",

        choices: [
            "過去に飛行実績がある場所であっても、周辺環境や気象条件の変化を考慮して飛行前確認を実施する必要がある",
            "飛行経験がある場所であれば周辺環境確認は不要であり、機体点検のみで飛行できる",
            "飛行経験がある場所であれば飛行計画の作成やリスク評価は省略してよい"
        ],

        answer: 0,

        explanation:
            "同じ場所でも環境は変化するため事前確認が必要です。"
        },

        {
        subject: "drone",
        category: CATEGORIES.RULE,

        question:
            "小型無人機等飛行禁止法の対象施設周辺で飛行する場合について、最も適切なものはどれか。",

        choices: [
            "対象施設及びその周辺空域では飛行が制限されており、無許可飛行は罰則の対象となる場合がある",
            "航空法上の許可を受けていれば、小型無人機等飛行禁止法による制限は受けない",
            "対象施設の敷地外であれば距離に関係なく自由に飛行することができる"
        ],

        answer: 0,

        explanation:
            "航空法とは別に小型無人機等飛行禁止法の規制を受けます。"
},


  // AI_COMMON_EXTRA_INSERT_HERE

];