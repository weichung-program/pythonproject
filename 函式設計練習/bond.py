def bond(coupon_rate,market_rate,face_value,years):
    #先計算每年票面利息
    annual_interest=coupon_rate*face_value
    #把發行價格設定為0
    issue_price=0
    #計算發行價格（即債券的現值）
    for t in range (1,years+1):
        issue_price += annual_interest / ((1+market_rate) ** t )
    issue_price += face_value / ((1+market_rate) ** years )
    book_value=issue_price
    #判斷折溢價
    if coupon_rate>market_rate:
        print("溢價發行")
    elif coupon_rate<market_rate:
        print("折價發行")
    else:
        print("平價發行")
    print("發行類型",end="")
    print(f"初始帳面價格:{book_value:.2f}")
    print(f"每年要付的利息:{annual_interest:.2f}")
    print("---------------------------------------")
    for year in  range ( 1, years+1):
        利息費用=face_value*market_rate
        攤銷費用=利息費用-annual_interest
        帳面價格=book_value+攤銷費用
        print("期數",year)
        print(f"利息費用:{利息費用:.2f}")
        print(f"攤銷費用:{攤銷費用:.2f}")
        print(f"帳面價格:{帳面價格:.2f}")
        print("-------------------------")

print(bond(0.12,0.1,45000,5))


