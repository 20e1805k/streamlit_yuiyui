# -*- coding: utf-8 -*-
"""
Created on Thu Nov 18 16:58:18 2021

@author: iwanaga yuika
"""
import streamlit as st
from pytube import YouTube
import datetime
import streamlit as st
import time
import pandas as pd
st.title('*music for you')
st.write('こんにちは！')
st.write('当てはまる項目を選んでください！')
st.write('私からあなたへおすすめしたい音楽を紹介させていただきます！')
st.write('ぜひ聞いてみてください♪')

genre = st.radio('1.【あなたの今の気分は？】',('noselect','楽しい', '悲しい', '盛り上がりたい', 'イライラ'))
if genre == '楽しい':
    st.write('あなたは「楽しい」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/EusUvmUi2Xk')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','1で「楽しい」を選択したときの歌詞', '1で「楽しい」を選択したときのこのアーティストの他の曲'))
    if option == "1で「楽しい」を選択したときの歌詞":
        st.write('朝 始まりの朝 2番出口から見えた空サイダーみたいな音立てて 並木道が手招きしている「前髪短すぎたかな?」気にする声 弾んでる誰もが胸躍らせる 4月のビートに遅れないようにスピード上げて走れ走れ 花びらを追い抜いて新しいスニーカーが希望の歌を歌っている走れ 走れ 冬の怠惰を振り切って高ぶった心を風に乗せて駆けよう8時半のチャイムが響いて僕らの春が始まる朝 いつもの朝 万事悩み絶えず上の空ミュージックは知らないふりで「課題曲 3番」リピートし続ける急いでものんびりしてても上手くいかずに崩れてく見つけなきゃいけないのは空白のモンスター出来るまで何度も繰り返す、繰り返す走れ 走れ 花びらを追い抜いて新しいスニーカーが希望の歌を歌っている走れ 走れ 冬の怠惰を振り切って 高ぶった心を風に乗せて駆けよう結末がどんなに転んでもやがて春が始まる朝 始まりの朝 かすかに震える指先たち並木道や 2番出口の空 浮かんでく走れ 走れ 花びらを追い抜いて新しいスニーカーが希望の歌を歌っている走れ 走れ 冬の怠惰を振り切って高ぶった心を風に乗せて駆けよう位置についてライトが灯ったなら僕らの春が春が春が始まる春が春が春が始まる朝 始まりの朝')
    if option == '1で「楽しい」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/Vho5jBUfR28')

elif genre == '悲しい':
    st.write('あなたは「悲しい」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/z80Eu4z44go')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','1で「悲しい」を選択したときの歌詞', '1で「悲しい」を選択したときのこのアーティストの他の曲'))
    if option == "1で「悲しい」を選択したときの歌詞":
        st.write('涙を流した君にしか　浮かべられない笑顔があるそのままの君で大丈夫　こぼれおちた分だけ強くなる変わりたいのに　変われない日々本当の気持ちから　毎日少しずつ逃げた見えないフリや　聞こえないフリで綺麗事ならべても　自分は騙しきれなくて負けそうな心　抱えても　僕らは笑う　無理して笑うけどきっと涙を流した君にしか　浮かべられない笑顔があるたまには泣いても大丈夫　素直になっても大丈夫生きていくだけで人は皆　数えきれぬほど乗り越える強がらなくても大丈夫　こぼれおちた分だけ強くなる　強くなる　強くなれる　大丈夫誰かの理想になろうとしすぎて　越えられないボーダーライン気がつけば　引いてしまってる自分で選んだ道なんだからって　誰にも頼れずに一人ぼっちで戦ってるプライドや夢を守るため　僕らは笑う　無理して笑うけどでもね涙を流した君にしか　迎えられない明日がある見守ってるから大丈夫　焦らなくたって大丈夫生きていくなかで人は皆　幾千もの自分に出会うそうして大人になっていく　見つけられた分だけ　強くなる世界は涙じゃ変わらない　でも君は変わってゆけるさそう僕も　ちっぽけでも　踏み出していくよ胸を張って　君だけじゃない　僕ら　一人じゃないそうさ涙を流した君にしか　浮かべられない笑顔がある転んで泣いても大丈夫　素直になっても大丈夫生きていくだけで人は皆　数えきれないほど　乗り越えるだから大丈夫　こぼれおちた分だけ強くなる　強くなる　強くなれる　大丈夫')
    if option == '1で「悲しい」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/szFhwZ52NyY')
    
elif genre == '盛り上がりたい':
    st.write('あなたは「盛り上がりたい」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/UM9XNpgrqVk')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','1で「盛り上がりたい」を選択したときの歌詞', '1で「盛り上がりたい」を選択したときのこのアーティストの他の曲'))
    if option == "1で「盛り上がりたい」を選択したときの歌詞":
        st.write('思い出すのは君の歌会話よりも鮮明だどこに行ってしまったのいつも探すんだよ思い出すのは君の歌歌い笑う顔が鮮明だ君に似合うんだよずっと見ていたいよでも最後に見たいのはきっともう君の夢の中もう一度また聞かせてくれよ聞きたいんだもっと騒げ怪獣の歌まだ消えない夢の歌唱えて君がいつも歌う怪獣の歌まだ消えない口ずさんでしまうよ思い出すのは君がいたギター持ってる君がいた忘れられないんだよだから僕が歌うよでも最後に見たいのはきっともう君の夢の中もう一度また聞かせてくれよ聞きたいんだもっと騒げ怪獣の歌まだ消えない夢の歌唱えて君がいつも歌う怪獣の歌まだ消えない口ずさんでしまうよ落ちてく過去は鮮明で見せたい未来は繊細ですぎてく日々には鈍感な君へねぇ、もっと騒げ怪獣の歌まだ消えない夢の歌唱えて君がいつも歌う怪獣の歌まだ消えない口ずさんでしまうよねぇ、僕ら眠れない夜に手を伸ばして眠らない夜をまた伸ばして眠くないまだねそんな日々でいたいのにな懲りずに眠れない夜に手を伸ばして眠らない夜をまた伸ばして眠くないまだねそんな夜に歌う怪獣の歌')
    if option == '1で「盛り上がりたい」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/b3H5RvRHiYs')
    
elif genre == 'イライラ':
    st.write('あなたは「イライラ」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/A2k6ZO6B0A8')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','1で「イライラ」を選択したときの歌詞', '1で「イライラ」を選択したときのこのアーティストの他の曲'))
    if option == "1で「イライラ」を選択したときの歌詞":
        st.write('OH OH OH OH OH…HEY！HEY！OH OH OH OH OH…HEY！HEY！川面(かわも)に映る自分の姿に吠えなくなってしまった犬は餌もらうために尻尾振って飼い慣らされたんだろう(BOWWOW)噛みつきたい気持ちを殺して聞き分けいいふりをするなよ上目遣いで媚びるために生まれて来たのか？(HOUND DOG)今あるしあわせにどうしてしがみつくんだ？閉じ込められた見えない檻から抜け出せよRock you！目の前のガラスを割れ！握りしめた拳で Oh！Oh！やりたいこと　やってみせろよおまえはもっと自由でいい　騒げ！(OH OH OH OH OH…)邪魔するもの　ぶち壊せ！夢見るなら愚かになれ他人(ひと)を見ても吠えないように躾(しつけ)けられた悲しい犬よ鼻を鳴らしすり寄ったら誰かに撫でられるか？(BOWWOW)リードで繋がれなくてもどこへも走り出そうとしない日和見(ひよりみ)主義のその群れに紛れていいのか？(HOUND DOG)すべて失っても手に入れたいものがあるがむしゃらになってどこまでも追い求めるだろうRock you！抑圧のガラスを割れ！怒り込めた拳で Oh！Oh！風通しをよくしたいんだ俺たちはもう犬じゃない　叫べ！(OH OH OH OH OH…）偉い奴らに怯(ひる)むなよ！闘うなら孤独になれ群れてるだけじゃ始まらないよ目の前のガラスを割れ！握りしめた拳で Oh！Oh！やりたいこと　やってみせろよおまえはもっと自由でいい　騒げ！(OH OH OH OH OH…)邪魔するもの　ぶち壊せ！夢見るなら愚かになれ傷つかなくちゃ本物じゃないよ')
    if option == '1で「イライラ」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/Ko_P7puwo1Q')
st.write('―――――――――――――――――――――――――――♡――――――――――――――――――――――――――')
genre = st.radio('2.【あなたの現在の状況は？】',('noselect','片思い', '失恋した', 'なにかに努力している', '実家に向かっている・実家に帰省している'))
if genre == '片思い':
    st.write('あなたは「片思い」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/gLWWXhMVuQs')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','2で「片思い」を選択したときの歌詞', '2で「片思い」を選択したときのこのアーティストの他の曲'))
    if option == "2で「片思い」を選択したときの歌詞":
        st.write('「好き」なんて言えない あなたしか見えないよ瞳(め)があうたび 声を聞くたび 愛しくなる 切なくなる「好き」だけど苦しい 今の私 どう映ってるの誰かを見る 横顔は ふり向かない ふり向かせたいもしも二人で 寄り添いあってキスしたらなんて思っても叶わないのに 叶わないのにあなたに恋していいですか?私じゃダメかな?もうどうしようもないくらい想い止まらないのああずっとずっと一緒にいれたらいいのに･･･本気なんです 本気で好きなんです好きだから伝えたい 私だけ見て欲しい意識するたび 顔見れずに 困らせちゃう 嫌われちゃうイヤ こんな私 泣いてばかり 情けなくなる心配してくれるけど 期待なんてさせないでよなんで夜になると あなたのことばかり考えてしまうんだろう叶わないのに 叶わないのにあなたに恋したせいですか?心が痛いよもっと知りたい 触れたい 膨らんでく想いあぁ 風船みたいにとばせたならいいのに･･･ 本気なんです 本気で好きなんですどこにいたって誰といたって気になっちゃって離れなくなってお願い勇気をください あなたに会って景色だって輝いて見えて忘れない 消えない 優しい ぬくもり全部 そっと包んでゆくあなたに恋していいですか?私じゃダメかな?もうどうしようもないくらい想い止まらないのああ ずっとずっと一緒にいれたらいいのに･･･本気なんです 本気で好きなんです')
    if option == '2で「片思い」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/Ko_P7puwo1Q')
    
elif genre == '失恋した':
    st.write('あなたは「失恋した」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/0mtHh0k6sVg')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','2で「失恋した」を選択したときの歌詞', '2で「失恋した」を選択したときのこのアーティストの他の曲'))
    if option == "2で「失恋した」を選択したときの歌詞":
        st.write('思い違いは空のかなたさよならだけの人生かほんの少しだけの未来は見えたのにさよならなんだ昔　住んでた小さな部屋は今は他人が住んでんだ君に言われた　ひどい言葉も無駄な気がした毎日もあの時こうしてれば　あの日に戻れればあの頃の僕にはもう　戻れないよたとえばゆるい幸せがだらっと続いたとするきっと悪い種が芽を出してもう　さよならなんだ寒い冬の冷えた缶コーヒーと虹色の長いマフラーと小走りで路地裏を抜けて思い出してみるたとえばゆるい幸せがだらっと続いたとするきっと悪い種が芽を出してもう　さよならなんださよなら　それもいいさどこかで元気でやれよ僕もどーにかやるさそうするよ')
    if option == '2で「失恋した」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/uRluqu6yFe4')
    
elif genre == 'なにかに努力している':
    st.write('あなたは「なにかに努力している」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/249YdrcCL0Y')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','2で「なにかに努力している」を選択したときの歌詞', '2で「なにかに努力している」を選択したときのこのアーティストの他の曲'))
    if option == "2で「なにかに努力している」を選択したときの歌詞":
        st.write('ドアの閉まる音　カレンダーの印部屋から聞こえる　君の泣き声逃げる事の方が怖いと君は夢を追い続けてきた努力が報われず　不安になって珍しく僕に当たったりしてここで諦めたら今までの自分が可哀想だと君は泣いた夢を追う君へ思い出して　つまずいたならいつだって物語の主人公は笑われる方だ人を笑う方じゃないと僕は思うんだよ誰よりも転んで　誰よりも泣いて誰よりも君は　立ち上がってきた僕は知ってるよ誰よりも君が一番輝いてる瞬間を夢を追う君へ思い出して　くじけそうならいつだって物語の主人公が立ち上がる限り物語は続くんだ嬉しいのに涙が溢れるのは君が歩んできた道のりを知っているから夢を追う君へ思い出して　つまずいたならいつだって物語の主人公は笑われる方だ人を笑う方じゃない君ならきっと')
    if option == '2で「なにかに努力している」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/O2YIMvyAIm4')
    
elif genre == '実家に向かっている・実家に帰省している':
    st.write('あなたは「実家に向かっている・実家に帰省している」を選択しました。こちらをクリック！')
    st.write('https://youtu.be/woRV5VxJDkU')
    option = st.selectbox(
    '☆詳しくはこちら',
   ('noselect','2で「実家に向かっている・実家に帰省している」を選択したときの歌詞', '2で「実家に向かっている・実家に帰省している」を選択したときのこのアーティストの他の曲'))
    if option == "2で「実家に向かっている・実家に帰省している」を選択したときの歌詞":
        st.write('嬉しい事があった時に誰かに言いたくなるのは自分よりも喜んでくれる人に育ててもらったからなんだろうな身体がだるくなった時は確か生姜とハチミツで口うるさくて嫌でも思い出すよ離れていても守られているんだあなたはずっと手を振って笑ってくれた帰り道迷わないようにもし前を向けなくなった時も振り返ればいつも見えるように愛されている事にちゃんと気付いている事いつか歌にしよう思い上がって街を出て思い知った挙句　途方に暮れて追い越していく人を恨んでみたりしてそれでもいつか自分の事誇れるように　そしてその時は誇らしく思ってもらえるように膝すりむいて帰った日はなぜか僕より痛そうでそんな記憶が形を変え今も離れていても守られているんだあなたはずっと手を振って笑ってくれた帰り道迷わないようにもし前を向けなくなった時も振り返ればいつも見えるように愛されている事にちゃんと気付いている事いつか歌にしようちゃんと返したい事いつか歌にしよう')
    if option == '2で「実家に向かっている・実家に帰省している」を選択したときのこのアーティストの他の曲':
        st.write('☆https://youtu.be/meZPD28Y7xE')
st.write('―――――――――――――――――――――――――――♡――――――――――――――――――――――――――')
option = st.selectbox(
     '3.【好きなジブリ作品を選んでください！】',
     ('noselect','耳を澄ませば', '千と千尋の神隠し', '猫の恩返し','ゲド戦記','もののけ姫'))
if option == '耳を澄ませば':
    st.write('あなたは「耳を澄ませば」を選択しました。こちらをクリック!')
    st.write('https://youtu.be/G4FUjD_N8YU')
    st.write('［歌詞］カントリー・ロードこの道　ずっとゆけばあの街に　つづいてる気がする　カントリー・ロードひとりぼっち　おそれずに生きようと　夢　みてたさみしさ　押し込めて強い自分を　守っていこカントリー・ロードこの道　ずっとゆけばあの街に　つづいてる気がする　カントリー・ロード歩き疲れ　たたずむと浮かんで来る　故郷(ふるさと)の街丘をまく　坂の道そんな僕を　叱っているカントリー・ロードこの道　ずっとゆけばあの街に　つづいてる気がする　カントリー・ロードどんな挫(くじ)けそうな時だって決して　涙は見せないで心なしか　歩調が速くなっていく思い出　消すためカントリー・ロードこの道　故郷(ふるさと)へつづいても僕は　行かないさ　カントリー・ロードカントリー・ロード明日は　いつもの僕さ帰りたい　帰れないさよなら　カントリー・ロード')
if option == '千と千尋の神隠し':
    st.write('あなたは「千と千尋の神隠し」を選択しました。こちらをクリック!')
    st.write('https://youtu.be/WOZE40v1iok')
    st.write('［歌詞］青空に線を引く　ひこうき雲の白さは　ずっとどこまでも　ずっと続いていく　明日を知ってたみたい　胸で浅く息をしてた　熱い頬　さました風も　おぼえてる　未来の前にすくむ手足は　静かな声にほどかれて　叫びたいほど　なつかしいのは　ひとつのいのち　真夏の光　あなたの肩に　揺れてた木漏れ日　つぶれた白いボール風が散らした花びらふたつを浮かべて 見えない川は歌いながら流れてく秘密も 嘘も 喜びも宇宙を生んだ神さまの 子供たち未来の前に すくむ心がいつか名前を 思い出す叫びたいほど いとおしいのはひとつのいのち 帰り着く場所わたしの指に 消えない 夏の日')
if option == '猫の恩返し':
    st.write('あなたは「猫の恩返し」を選択しました。こちらをクリック!')
    st.write('https://youtu.be/lHWVOfC41L4')
    st.write('［歌詞］忘れていた目を閉じて 取り戻せ恋のうた青空に隠れている 手を伸ばしてもう一度忘れないですぐそばに 僕がいるいつの日も星空を眺めている 一人きりの夜明けもたった一つの心 悲しみに暮れないで君のためいきなんて 春風に変えてやる陽のあたる坂道を 自転車で駆けのぼる君と失くした 想い出乗せて行くよララララ 口ずさむ くちびるを染めて行く君と見つけた しあわせ 花のように忘れていた窓開けて 走り出せ恋のうた青空に託している 手をかざしてもう一度忘れないよすぐそばに 君がいるいつの日も星空に輝いてる 涙揺れる明日もたった一つの言葉 この胸に抱きしめて君のため僕は今 春風に吹かれてる陽のあたる坂道を 自転車で駆けのぼる君と誓った約束 乗せて行くよララララ 口ずさむ くちびるを染めて行く君と出会えた しあわせ 祈るように陽のあたる坂道を 自転車で駆けのぼる君と誓った約束 乗せて行くよララララ 口ずさむ くちびるを染めて行く君と出会えた しあわせ 祈るように君と出会えた しあわせ 祈るように')
if option == 'ゲド戦記':
    st.write('あなたは「ゲド戦記」を選択しました。こちらをクリック!')
    st.write('https://youtu.be/zQHYlBbzA1c')
    st.write('［歌詞］夕闇迫る雲の上いつも一羽で飛んでいる鷹はきっと悲しかろう音も途絶えた風の中空を掴んだその翼休めることはできなくて心を何にたとえよう鷹のようなこの心心を何にたとえよう空を舞うよな悲しさを雨のそぼ降る岩陰にいつも小さく咲いている花はきっと切なかろう色も霞んだ雨の中薄桃色の花びらを愛でてくれる手もなくて心を何にたとえよう花のようなこの心心を何にたとえよう雨に打たれる切なさを人影絶えた野の道を私とともに歩んでるあなたもきっと寂しかろう虫の囁く草原をともに道行く人だけど絶えて物言うこともなく心を何にたとえよう一人道行くこの心心を何にたとえよう一人ぼっちの寂しさを')
if option == 'もののけ姫':
    st.write('あなたは「もののけ姫」を選択しました。こちらをクリック!')
    st.write('https://youtu.be/c9DHaTaJsbg')
    st.write('［歌詞］はりつめた弓の ふるえる弦よ月の光にざわめく おまえの心とぎすまされた刃の美しいそのきっさきによく似た そなたの横顔悲しみと怒りにひそむ まことの心を知るは森の精 もののけ達だけ もののけ達だけUh… Uh… Uh… Uh… Uh…Ah… Ah… Ah… Ah… Ah…')
st.write('―――――――――――――――――――――――――――♡――――――――――――――――――――――――――')
st.subheader('おまけ')
st.write('勉強中のあなたにぴったりなクラシックを紹介します！')
st.write('ラ・カンパネラ👇')
st.write('https://youtu.be/8EaXf6fOFnA')
st.write('華麗なる大円舞曲👇')
st.write('https://youtu.be/QOLnMXMJ-ng')
st.write('子犬のワルツ👇')
st.write('https://youtu.be/Q9JALr8mEHU')






