from app.models import db, Media


# Adds media
def seed_media():
    jamiMedia1 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FLL/JYUH/KN8W3MU5/FLLJYUHKN8W3MU5.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=2c3a9a67ad4372bba2ebfa7fe98ca5e6', recipeId=19)
    jamiMedia2 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FXH/M5OU/KN8W3QX0/FXHM5OUKN8W3QX0.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d70f5f185890ada9d14b085096a64cf2', recipeId=19)
    jamiMedia3 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F1O/HLA9/KN8W3UMO/F1OHLA9KN8W3UMO.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=4eff9057a122178afbe52218e1660cbf', recipeId=19)
    jamiMedia4 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FDD/D90A/KN8W3YLR/FDDD90AKN8W3YLR.jpg?auto=webp&frame=1&width=525&height=1024&fit=bounds&md=28ea0bb55fc079c8e2257835b193afe0', recipeId=19)
    jamiMedia5 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F9X/O3LG/KIKA4K08/F9XO3LGKIKA4K08.png?auto=webp&frame=1&width=933&fit=bounds&md=3879e9346b30b85c513038eac4c435f1', recipeId=20)
    jamiMedia6 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FZ5/JK2Q/KIKA4K02/FZ5JK2QKIKA4K02.png?auto=webp&frame=1&width=400&fit=bounds&md=6ad949a89730fcb964c195e83e2999cb', recipeId=20)
    jamiMedia7 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F4I/0CRX/KIKA4JZU/F4I0CRXKIKA4JZU.png?auto=webp&frame=1&width=400&fit=bounds&md=f6573a420a7485fed6ac71fe2ab5bf31', recipeId=20)
    jamiMedia8 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FP2/SKGJ/KIKA4JZW/FP2SKGJKIKA4JZW.png?auto=webp&frame=1&fit=bounds&md=51b3acad72f01884590f5458792684c3', recipeId=20)
    jamiMedia9 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F43/423B/KQCCFWQ0/F43423BKQCCFWQ0.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=9387b32ea6cc3167bb94156f635f46a6', recipeId=21)
    jamiMedia10 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FF6/RO6L/KQ57CO8F/FF6RO6LKQ57CO8F.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=5b34dbedeca3ba61073fbedfc57bebfe', recipeId=21)
    jamiMedia11 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FHU/76WK/KQ57CO84/FHU76WKKQ57CO84.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=860e812b91318a0b34fc16488314e65e', recipeId=21)
    jamiMedia12 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FDZ/Y6IE/KQ57CP1P/FDZY6IEKQ57CP1P.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=43b30bcaef18846b343ac68de17bf6ab', recipeId=21)
    jamiMedia13 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FG5/OBDL/KNG1B6DK/FG5OBDLKNG1B6DK.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=bb646e2bb222387898a36d947099cc9b', recipeId=22)
    jamiMedia14 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FOD/L6S3/KNG1B6DJ/FODL6S3KNG1B6DJ.jpg?auto=webp&frame=1&crop=2:3&width=467&height=1024&fit=bounds&md=affa06ff996b834e79956a78c910ad81', recipeId=22)
    jamiMedia15 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FNV/SUYD/KNG1B6DG/FNVSUYDKNG1B6DG.jpg?auto=webp&frame=1&crop=2:3&width=400&height=1024&fit=bounds&md=ed7d531f2f44634ecebec6b16e7cca4b', recipeId=22)
    jamiMedia16 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FWJ/S2R6/KNG1BIF7/FWJS2R6KNG1BIF7.jpg?auto=webp&frame=1&crop=2:3&width=400&height=1024&fit=bounds&md=ad49d9de391320122018c01b7f544461', recipeId=22)
    jamiMedia17 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F66/1C1G/KNYM1BA5/F661C1GKNYM1BA5.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=bda8ff1f44650bc1efb2027af66d0fe1', recipeId=23)
    jamiMedia18 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FCD/QBC9/KNYM0P6Y/FCDQBC9KNYM0P6Y.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=3a8170fa6b0ceb7a95393a23d13c2b77', recipeId=23)
    jamiMedia19 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FLB/3N3L/KNYM0P71/FLB3N3LKNYM0P71.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=47b1bbb12b9db4a7832ed19dcb21afcc', recipeId=23)
    jamiMedia20 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FV5/8479/KN36CAIL/FV58479KN36CAIL.jpg?auto=webp&frame=1&width=800&height=1024&fit=bounds&md=b3e17aea915e988dd7d7a5f1065ef76b', recipeId=24)
    jamiMedia21 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F8I/1LE7/KN36CAGG/F8I1LE7KN36CAGG.jpg?auto=webp&frame=1&width=400&height=1024&fit=bounds&md=a6dfd4b65d04e11b578f01a0fb7a5b06', recipeId=24)
    jamiMedia22 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FEV/28M9/KFZEJGHF/FEV28M9KFZEJGHF.png?auto=webp&frame=1&width=547&height=1024&fit=bounds&md=c1746224bc20b2e31ca2a84b15e1fc6a', recipeId=25)
    jamiMedia23 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FV4/5D0B/KFZEJGHD/FV45D0BKFZEJGHD.png?auto=webp&frame=1&width=411&fit=bounds&md=2c1239043615a1e5f3096adc6803fedf', recipeId=25)
    jamiMedia24 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FA2/L6Y4/KFZEJGH5/FA2L6Y4KFZEJGH5.png?auto=webp&frame=1&width=411&fit=bounds&md=f0b7f1b1232d02d1cb03e50c01fafe91', recipeId=25)
    jamiMedia25 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F68/6RHR/KA9N94GK/F686RHRKA9N94GK.png?auto=webp&frame=1&width=560&fit=bounds&md=0359917175c53e054ef3106313fbd758', recipeId=26)
    jamiMedia26 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FD6/3Q24/KAB2MMQG/FD63Q24KAB2MMQG.png?auto=webp&frame=1&width=525&fit=bounds&md=8ca511cabaea6ffd2ce17ad7c460eb8c', recipeId=26)
    jamiMedia27 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F55/PHJY/KQQMU1SN/F55PHJYKQQMU1SN.jpg?auto=webp&frame=1&width=1020&height=1024&fit=bounds&md=b2716a4fb8e8e8d4c6667c0ae6a9b9b1', recipeId=27)
    jamiMedia28 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FBM/QOOJ/KQQMU1R9/FBMQOOJKQQMU1R9.jpg?auto=webp&frame=1&width=822&height=1024&fit=bounds&md=73f3e5e86f9755c5eafeabd7a700c415', recipeId=27)
    jamiMedia29 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FC5/VVYH/JGGTFXAO/FC5VVYHJGGTFXAO.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=a57c985c088b7772385045d164f5a8f8', recipeId=28)
    jamiMedia30 = Media(
            mediaUrl='https://content.instructables.com/ORIG/F2O/G5JV/JGGTFXDF/F2OG5JVJGGTFXDF.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=d2bc80c1ad36b6c72ba1141c68add379', recipeId=28)
    jamiMedia31 = Media(
            mediaUrl='https://content.instructables.com/ORIG/FVB/UAMU/JGGTG035/FVBUAMUJGGTG035.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=0bc4a49bc526e42f8267571d1ca39fef', recipeId=28)


    media5011 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FB7/0ONL/IBM250KE/FB70ONLIBM250KE.jpg?auto=webp&frame=1&fit=bounds&md=6dca3a956e6504855a1600d4f77792ca', recipeId=11)


    media5021 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU9/SLP9/KUGYA4W2/FU9SLP9KUGYA4W2.jpg?auto=webp&frame=1&fit=bounds&md=897e928d97e8d6db08c6752976f56bec', recipeId=12)


    media5031 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FEB/58DH/IJRFGPLR/FEB58DHIJRFGPLR.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=b9de2f5842700d3667674a453e8c3662', recipeId=13)
    media5032 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F4P/T75K/IJRFGPO8/F4PT75KIJRFGPO8.jpg?auto=webp&frame=1&height=1024&fit=bounds&md=3e55c08b595f68e9ae2f9cdb52ca8407', recipeId=13)


    media5041 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FDN/YE2X/INPE8SN3/FDNYE2XINPE8SN3.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=05bc9656112d08859e8c3a149424db9a', recipeId=14)
    media5042 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FW8/KLNP/INPE8TH9/FW8KLNPINPE8TH9.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=3cef8bcc16caf7118b1a315de07cc78a', recipeId=14)
    media5043 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FB9/24EO/INPE8NHD/FB924EOINPE8NHD.jpg?auto=webp&frame=1&width=1024&fit=bounds&md=46841e78ff89cf32c4d2581bfc4dcecd', recipeId=14)



    media5051 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FRB/MCWS/HIGIL7PG/FRBMCWSHIGIL7PG.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=0c243477f6161af72b4b92ac875a8f5a', recipeId=15)
    media5052 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FRO/0HII/HIGFJMKR/FRO0HIIHIGFJMKR.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=03764972e37ffcec7365475e676ad92f', recipeId=15)



    media5061 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F9S/RLOZ/H7UQQYPQ/F9SRLOZH7UQQYPQ.jpg?auto=webp&frame=1&fit=bounds&md=8e966cd4b3b0f8f803b582c97e82d0ef', recipeId=16)



    media5071 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FND/AS3E/KL0VG22V/FNDAS3EKL0VG22V.jpg?auto=webp&frame=1&fit=bounds&md=0b5e6642d10fbde83fa714ed99905f1f', recipeId=17)
    media5072 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F7X/SEPT/KL0VG28U/F7XSEPTKL0VG28U.gif?format=mp4', recipeId=17)
    media5073 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F48/5C3Z/KL0VGCCF/F485C3ZKL0VGCCF.gif?format=mp4', recipeId=17)




    media5081 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F4D/3C4K/KRXX5VJC/F4D3C4KKRXX5VJC.jpg?auto=webp&frame=1&fit=bounds&md=81235b25e3d06dffcc54cc73bf63a658', recipeId=18)
    media5082 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FLB/IPG9/KRWGGLYM/FLBIPG9KRWGGLYM.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=6403e89551b25f45f62351f5d93b321a', recipeId=18)
    media5083 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FHU/GX9U/KRWGGLRK/FHUGX9UKRWGGLRK.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=b9fddf75d960858a2658829f2b577d00', recipeId=18)
    media5084 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FVX/1571/KRWGGLT4/FVX1571KRWGGLT4.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=0f2341542ab64bb276c8d94b31c9714f', recipeId=18)




    media9011 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FFH/7FOZ/KNG1CRSF/FFH7FOZKNG1CRSF.jpg?auto=webp&frame=1&fit=bounds&md=b578a9659ac76d9f6f55880c7e5b913e', recipeId=29)



    media9021 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FY8/9ZG2/HIW8L896/FY89ZG2HIW8L896.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e97535e8f044adeb5b69b523533c680a', recipeId=30)
    media9022 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FU8/RGFO/HIXPVTQ8/FU8RGFOHIXPVTQ8.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=e2e571fe971019e5635c2842457f1295', recipeId=30)
    media9023 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FPJ/R33A/HIXPVTQE/FPJR33AHIXPVTQE.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=7e77b6630845483aab0ea21fedfa076e', recipeId=30)




    media9031 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FG8/9F3Q/KQUX6UQJ/FG89F3QKQUX6UQJ.jpg?auto=webp&frame=1&fit=bounds&md=fe6b0316ec6caa3d10f037007e79ddd0', recipeId=31)
    media9032 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F91/G8WD/KQTHRAPC/F91G8WDKQTHRAPC.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=8173b49c329a784d6489b18bdd8604a5', recipeId=31)
    media9033 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F8F/NMEJ/KQTHRAOR/F8FNMEJKQTHRAOR.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=c9dee75c443e27c79d71f60e6a831933', recipeId=31)
    media9034 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FIH/Z2WQ/KQTHRANH/FIHZ2WQKQTHRANH.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=a2c727758470699008de681762165baf', recipeId=31)




    media9041 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FBZ/RK83/HSYO26UW/FBZRK83HSYO26UW.jpg?auto=webp&frame=1&fit=bounds&md=4114ec4db91bfb4795ba927c6ca4e03f', recipeId=32)





    media9051 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FPG/EA3J/HJKBZ7RW/FPGEA3JHJKBZ7RW.jpg?auto=webp&frame=1&fit=bounds&md=1b123a0c6eafa16afc5df82864365e2d', recipeId=33)



    media9061 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FVX/FIUT/KTPSX0S6/FVXFIUTKTPSX0S6.jpg?auto=webp&frame=1&fit=bounds&md=1c095448b5caafb6a4319f6885cfa71b', recipeId=34)



    media718 = Media(
        mediaUrl='https://ingestiblesapp.s3.amazonaws.com/f0ff7a6f834c42238c085fe91f3022fc.mp4', recipeId=1)
    media719 = Media(
        mediaUrl='https://ingestiblesapp.s3.amazonaws.com/f0ff7a6f834c42238c085fe91f3022fc.mp4', recipeId=4)
    media701 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FPX/23L1/KTPSYXG9/FPX23L1KTPSYXG9.jpg?auto=webp&frame=1&width=563&height=1024&fit=bounds&md=619106ddb4dd497a0a2cff236eba5b69', recipeId=1)
    media702 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FK6/1EKB/KTPSYXH4/FK61EKBKTPSYXH4.jpg?auto=webp&frame=1&width=396&height=1024&fit=bounds&md=6355eec22ad47682d075aff4d45f5959', recipeId=1)
    media703 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FK2/SID1/KR4X94WT/FK2SID1KR4X94WT.jpg?auto=webp&frame=1&width=933&height=1024&fit=bounds&md=4ff089b752e0d18edd34929c4e657e6f', recipeId=2)

    media704 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FQV/RSDM/KU5IVJLY/FQVRSDMKU5IVJLY.jpg?auto=webp&frame=1&width=674&height=1024&fit=bounds&md=c3ac97bb305aef7f3067ee77bc5d4575', recipeId=3)

    media705 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FKG/HYRL/KSUD6GJG/FKGHYRLKSUD6GJG.png?auto=webp&frame=1&width=632&height=1024&fit=bounds&md=7e2b8de316945a23b06ca1629df55cce', recipeId=4)
    media706 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FIV/SK5J/KSN82IJF/FIVSK5JKSN82IJF.jpg?auto=webp&frame=1&width=247&height=1024&fit=bounds&md=d1559835ddc029026dc950dacfa07552', recipeId=4)
    media707 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FZK/W86V/KSONIGFZ/FZKW86VKSONIGFZ.png?auto=webp&frame=1&width=247&height=1024&fit=bounds&md=e27628b316d1f2e2e0112c537ddfa5e1', recipeId=4)

    media708 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F2Y/3FF3/J1QP0HWD/F2Y3FF3J1QP0HWD.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=fa27ecd9f7aa0ac4d42873309e1abe81', recipeId=5)



    media709 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FED/DVP1/KNRGV0DF/FEDDVP1KNRGV0DF.jpg?auto=webp&frame=1&width=700&height=1024&fit=bounds&md=436c8eac45d9a98ba0f62d892127799b', recipeId=6)
    media710 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F53/AEBM/KNRGUUUB/F53AEBMKNRGUUUB.jpg?auto=webp&frame=1&width=233&height=1024&fit=bounds&md=0dc1e53a1943eb6a7a48152b195d7ffb', recipeId=6)


    media711 = Media(
        mediaUrl='https://content.instructables.com/ORIG/F0Z/U1RJ/KQGMRBUA/F0ZU1RJKQGMRBUA.jpg?auto=webp&frame=1&width=874&height=1024&fit=bounds&md=ffef0afa22a5dba342e3227016c65991', recipeId=7)
    media712 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FZI/YLMS/KQGMRBUB/FZIYLMSKQGMRBUB.jpg?auto=webp&frame=1&width=326&height=1024&fit=bounds&md=bd78d0e2e97a53b004f769473a50686b', recipeId=7)
    media713 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FMK/GEP0/KQGMRBTZ/FMKGEP0KQGMRBTZ.jpg?auto=webp&frame=1&width=326&height=1024&fit=bounds&md=6a790537b59db3b18c2f0f9f9056b50b', recipeId=7)



    media714 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FVU/8OW3/KKWL8KF3/FVU8OW3KKWL8KF3.jpg?auto=webp&frame=1&width=526&height=1024&fit=bounds&md=fe3ba40124d51f1a3cb87b46b175c900', recipeId=8)
    media715 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FD3/A29G/GD2JKDVX/FD3A29GGD2JKDVX.jpg?auto=webp&frame=1&width=1024&height=1024&fit=bounds&md=473b941f1783a0156c26dd969c6ceb9c', recipeId=9)

    media716 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FZM/A5AR/IUHMTRO5/FZMA5ARIUHMTRO5.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=91a31f58bf923808118f4b54a303dc3f', recipeId=10)
    media717 = Media(
        mediaUrl='https://content.instructables.com/ORIG/FJA/9F3T/IUHMTP3Q/FJA9F3TIUHMTP3Q.jpg?auto=webp&frame=1&width=600&height=1024&fit=bounds&md=7af9fa915eb0cb131ddc5d28b9328fca', recipeId=10)


    db.session.add(media701)
    db.session.add(media702)
    db.session.add(media703)
    db.session.add(media704)
    db.session.add(media705)
    db.session.add(media706)
    db.session.add(media707)
    db.session.add(media708)
    db.session.add(media709)
    db.session.add(media710)
    db.session.add(media711)
    db.session.add(media712)
    db.session.add(media713)
    db.session.add(media714)
    db.session.add(media715)
    db.session.add(media716)
    db.session.add(media717)

    db.session.add(media718)
    db.session.add(media719)
    db.session.add(jamiMedia1)
    db.session.add(jamiMedia2)
    db.session.add(jamiMedia3)
    db.session.add(jamiMedia4)
    db.session.add(jamiMedia5)
    db.session.add(jamiMedia6)
    db.session.add(jamiMedia7)
    db.session.add(jamiMedia8)
    db.session.add(jamiMedia9)
    db.session.add(jamiMedia10)
    db.session.add(jamiMedia11)
    db.session.add(jamiMedia12)
    db.session.add(jamiMedia13)
    db.session.add(jamiMedia14)
    db.session.add(jamiMedia15)
    db.session.add(jamiMedia16)
    db.session.add(jamiMedia17)
    db.session.add(jamiMedia18)
    db.session.add(jamiMedia19)
    db.session.add(jamiMedia20)
    db.session.add(jamiMedia21)
    db.session.add(jamiMedia22)
    db.session.add(jamiMedia23)
    db.session.add(jamiMedia24)
    db.session.add(jamiMedia25)
    db.session.add(jamiMedia26)
    db.session.add(jamiMedia27)
    db.session.add(jamiMedia28)
    db.session.add(jamiMedia29)
    db.session.add(jamiMedia30)
    db.session.add(jamiMedia31)
    db.session.add(jamiMedia14)


    db.session.add(media5011)

    db.session.add(media5021)

    db.session.add(media5031)
    db.session.add(media5032)

    db.session.add(media5041)
    db.session.add(media5042)
    db.session.add(media5043)

    db.session.add(media5051)
    db.session.add(media5052)

    db.session.add(media5061)

    db.session.add(media5071)
    db.session.add(media5072)
    db.session.add(media5073)

    db.session.add(media5081)
    db.session.add(media5082)
    db.session.add(media5083)
    db.session.add(media5084)

    db.session.add(media9011)

    db.session.add(media9021)
    db.session.add(media9022)
    db.session.add(media9023)

    db.session.add(media9031)
    db.session.add(media9032)
    db.session.add(media9033)
    db.session.add(media9034)

    db.session.add(media9041)

    db.session.add(media9051)

    db.session.add(media9061)



    db.session.commit()


# Uses a raw SQL query to TRUNCATE the users table.
# SQLAlchemy doesn't have a built in function to do this
# TRUNCATE Removes all the data from the table, and RESET IDENTITY
# resets the auto incrementing primary key, CASCADE deletes any
# dependent entities
def undo_media():
    db.session.execute('TRUNCATE media RESTART IDENTITY CASCADE;')
    db.session.commit()
