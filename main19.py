import streamlit as st
import pandas as pd
from io import BytesIO

st.set_page_config(
    page_title="Nhà hàng Góc Phố",
    page_icon="🍽️",
    layout="wide"
)


def tao_file_excel(df):
    output = BytesIO()

    with pd.ExcelWriter(output, engine="openpyxl") as writer:
        df.to_excel(writer, index=False, sheet_name="HoaDon")

    processed_data = output.getvalue()
    return processed_data


st.title("🍕 Nhà hàng Góc Phố")
st.write("✨ Chào mừng bạn đến với nhà hàng Góc Phố✨")

st.image(
    "https://th.bing.com/th/id/OIP.wcVpMmkQ4P8IFyM2NlMy2gHaEc?r=0&o=7rm=3&rs=1&pid=ImgDetMain&o=7&rm=3",
    use_container_width=True
)

menu = {
    "Món khai vị": [
        {
            "ten": "🍟 Khoai tây chiên",
            "gia": 35000,
            "img": "https://tse2.mm.bing.net/th/id/OIP._5wkud0zUQwwf0bCi970MwHaHa"
        },
        {
            "ten": "🥗 Salad",
            "gia": 30000,
            "img": "https://images.unsplash.com/photo-1546069901-ba9599a7e63c"
        }
    ],

    "Món chính": [
        {
            "ten": "🍕 Pizza",
            "gia": 120000,
            "img": "https://tse1.mm.bing.net/th/id/OIP.DiACdB0h_8mIG7J0y4YZmAHaEJ"
        },
        {
            "ten": "🍜 Phở",
            "gia": 50000,
            "img": "https://th.bing.com/th/id/R.3c91759485e0457b4ea680f77dffbf76?rik=LAwqZXA4wSRssg&pid=ImgRaw&r=0"
        },
        {
            "ten": "🍔 Hamburger",
            "gia": 80000,
            "img": "https://tse1.mm.bing.net/th/id/OIP.YUtaWrsnUetCh02NNveI_AAAAA?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        {
            "ten": "🍝 Mì Ý",
            "gia": 90000,
            "img": "https://tse4.mm.bing.net/th/id/OIP.0zwDZnL2C84DI2cfDXZPIgHaEK?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        }
    ],

    "Tráng miệng": [
        {
            "ten": "🍰 Bánh ngọt",
            "gia": 20000,
            "img": "https://tse2.mm.bing.net/th/id/OIP.oYJD0sMEGoPt6HPo7sd2rgHaE8"
        },
        {
            "ten": "🍉 Trái cây",
            "gia": 15000,
            "img": "https://images.unsplash.com/photo-1619566636858-adf3ef46400b"
        },
        {
            "ten": "🍦 Kem",
            "gia": 25000,
            "img": "https://tse1.explicit.bing.net/th/id/OIP.dsE3MIoDVe6D9JBehZj8UgHaE6?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        },
        {
            "ten": "🧋 Trà sữa",
            "gia": 35000,
            "img": "https://tse4.mm.bing.net/th/id/OIP.rY4mhTClRb3FceXizY0UyAHaE8?r=0&rs=1&pid=ImgDetMain&o=7&rm=3"
        }
    ]
}

so_luong = {}

for nhom, ds_mon in menu.items():

    st.divider()
    st.header(nhom)

    cols = st.columns(2)

    for i, mon in enumerate(ds_mon):
        with cols[i % 2]:
            with st.container(border=True):
                st.image(mon["img"], width=250)
                st.subheader(mon["ten"])
                st.write(f'{mon["gia"]:,} VNĐ')

                so_luong[mon["ten"]] = st.number_input(
                    f'Số lượng {mon["ten"]}',
                    min_value=0,
                    step=1,
                    key=mon["ten"]
                )

if st.button("💳 Xác nhận & Thanh toán"):

    tong_mon = sum(so_luong.values())

    if tong_mon == 0:
        st.error("⚠️ Bạn chưa chọn món nào!")
        st.stop()

    tong = 0
    hoa_don = []

    for nhom, ds_mon in menu.items():
        for mon in ds_mon:

            sl = so_luong[mon["ten"]]

            if sl > 0:
                thanh_tien_mon = sl * mon["gia"]
                tong += thanh_tien_mon

                hoa_don.append({
                    "Tên món": mon["ten"],
                    "Số lượng": sl,
                    "Đơn giá": mon["gia"],
                    "Thành tiền": thanh_tien_mon
                })

    giam = 0

    if tong >= 300000:
        giam = tong * 0.1

    thanh_tien = tong - giam

    st.success("✅ Thanh toán thành công!")

    st.header("🧾 Hóa đơn")

    for item in hoa_don:
        st.write(
            f'{item["Tên món"]}: '
            f'{item["Số lượng"]} x '
            f'{item["Đơn giá"]:,} = '
            f'{item["Thành tiền"]:,} VNĐ'
        )

    st.divider()

    st.write(f'💵 Tổng tiền: {tong:,} VNĐ')

    if giam > 0:
        st.write(f'🎁 Giảm giá: -{giam:,.0f} VNĐ')

    st.subheader(f'💰 Thành tiền: {thanh_tien:,.0f} VNĐ')

    df = pd.DataFrame(hoa_don)

    tong_df = pd.DataFrame([
        {
            "Tên món": "TỔNG",
            "Số lượng": "",
            "Đơn giá": "",
            "Thành tiền": thanh_tien
        }
    ])

    df = pd.concat([df, tong_df], ignore_index=True)

    excel_file = tao_file_excel(df)

    st.download_button(
        label="📥 Tải hóa đơn Excel",
        data=excel_file,
        file_name="hoa_don_nha_hang.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )