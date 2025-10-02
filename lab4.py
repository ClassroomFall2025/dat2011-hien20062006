# Code lab 4 bài 1 ở đây
def tinh_tien_nuoc(so_nuoc):
    gia_ban_nuoc = (7500,8800,12000,24000)
    if so_nuoc <= 10 and so_nuoc >= 0:
        tien_nuoc_thang = so_nuoc*gia_ban_nuoc[0]
    elif so_nuoc <= 20:
        tinh_nuoc_thang = 10 * gia_ban_nuoc[0] * (so_nuoc - 10) * gia_ban_nuoc[1]
    elif so_nuoc <= 30:
        tinh_nuoc_thang = 10 * gia_ban_nuoc[0] * 10* gia_ban_nuoc[1] + (so_nuoc - 20)* gia_ban_nuoc[2]
    elif so_nuoc <= 40:
         tinh_nuoc_thang = 10 * gia_ban_nuoc[0] + 10* gia_ban_nuoc[1] + 10 *gia_ban_nuoc[2] +(so_nuoc -30)* gia_ban_nuoc[3]
         return tien_nuoc_thang
    


    # Code lab 4  bài 2 ở đây
def tinh_nguyen_lieu(sl_bdx,sl_btc,sl_db):
    banh_dau_xanh ={"duong":0.04,"dau":0.07}
    banh_thap_cam ={"duong":0.06,"dau":0}
    banh_deo ={"duong":0.05,"dau":0.02}
    duong_hop_banh = sl_bdx * banh_dau_xanh["duong"] + sl_btc * banh_thap_cam["duong"] + sl_db * banh_deo["duong"]
    dau_hop_banh = sl_bdx * banh_dau_xanh["dau"] +sl_btc * banh_thap_cam["dau"] + sl_db * banh_deo["dau"]
    nguyen_lieu["duong"] = dau_hop_banh
    nguyen_lieu["dau"] = dau_hop_banh
    return nguyen_lieu




# code lab 4 bài 4 ở đây
menu = {
    "1" : "Tinh tien nuoc"
    "2" : "Tính nguyên liệu"
    "3" : "Thoát"
}
while True:
    print("=="*10 + "MENU" + "=="*10)
    print("Lua chon chhuc nang chuong trinh ")
    lua_chon = imput("nhap chuc nang chuong trinh")
    if lua_chon == "3":
        print("kết thúc chương trình")
        break
    elif lua_chon == "1"
        so_nuoc float(imput("Số nước: "))
        print(f"Tiền nước: ")

    
    