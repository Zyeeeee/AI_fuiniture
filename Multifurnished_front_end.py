import streamlit as st
import requests
from openai import OpenAI

# 初始化 OpenAI 客户端
client = OpenAI(base_url='https://external.api.recraft.ai/v1',
                api_key="FagaDqBYGg321WFIEUmnMG4IPa57QvpTNjP6on8huMWCC1NZeMCgyINn3p6lqepC")


# 功能二：用户自定义Prompt
def get_user_prompt():
    return st.text_input('请输入自定义的Prompt:', '我想把这个置物架变成森林风格的，上面放了很多看起来很好吃的果子')


def get_user_prompt2():
    return st.text_input('请输入自定义的Prompt:', '我想把这个床变成赛博风格的，上面摆了个高达')

# 功能三：处理图片并显示结果


def process_image(image_path, user_prompt):
    # 发送图像转换请求
    response1 = client.post(
        path='/images/imageToImage',
        cast_to=object,
        options={'headers': {'Content-Type': 'multipart/form-data'}},
        files={'image': open(image_path, 'rb')},
        body={'prompt': user_prompt, 'style': 'digital_illustration', 'strength': 0.3},  # default 0.3
    )
    # 获取转换后的图片URL
    image_to_image_result = response1['data'][0]['url']

    # 获取转换后的图片内容
    image_to_image_content = requests.get(image_to_image_result).content

    # 去除背景请求
    response2 = client.post(
        path='/images/removeBackground',
        cast_to=object,
        options={'headers': {'Content-Type': 'multipart/form-data'}},
        files={'file': ('filename.png', image_to_image_content)},
    )
    remove_background_result = response2['image']['url']

    # 返回生成后的图片URL
    return remove_background_result


def process_image2(image_path, user_prompt):
    # 发送图像转换请求
    response1 = client.post(
        path='/images/imageToImage',
        cast_to=object,
        options={'headers': {'Content-Type': 'multipart/form-data'}},
        files={'image': open(image_path, 'rb')},
        body={'prompt': user_prompt, 'style': 'digital_illustration', 'strength': 0.2},  # default 0.2
    )
    # 获取转换后的图片URL
    image_to_image_result = response1['data'][0]['url']

    # 获取转换后的图片内容
    image_to_image_content = requests.get(image_to_image_result).content

    # 去除背景请求
    response2 = client.post(
        path='/images/removeBackground',
        cast_to=object,
        options={'headers': {'Content-Type': 'multipart/form-data'}},
        files={'file': ('filename.png', image_to_image_content)},
    )
    remove_background_result = response2['image']['url']

    # 返回生成后的图片URL
    return remove_background_result


# 主函数
def main():
    st.title("AI自定义家具🤩")

    # 1. 展示置物架原图
    st.header("预览置物架")
    image_path1 = "shelf1.png"
    col1, col2 = st.columns(2)
    with col1:
        st.image(image_path1, caption="原始置物架")
    bookshelf_new = col2.empty()

    # 2. 用户自定义Prompt
    user_prompt = get_user_prompt()

    # 3. 用户点击按钮后进行图片处理
    if st.button('生成转换后的置物架'):
        if user_prompt:
            # 处理图片并获取生成的结果
            image_to_image_result = process_image(image_path1, user_prompt)

            # 第二列：显示生成后的图片（如果有的话）
            bookshelf_new.image(image_to_image_result, caption="宁的自定义置物架")
        else:
            st.warning("请先输入Prompt！")
    # 1. 展示置物架原图
    st.header("预览床")
    image_path2 = "bed1.png"
    col3, col4 = st.columns(2)
    with col3:
        st.image(image_path2, caption="原始床")
    bed_new = col4.empty()

    # 2. 用户自定义Prompt
    user_prompt2 = get_user_prompt2()

    # 3. 用户点击按钮后进行图片处理
    if st.button('生成转换后的床'):
        if user_prompt2:
            # 处理图片并获取生成的结果
            image_to_image_result = process_image2(image_path2, user_prompt2)

            # 第二列：显示生成后的图片（如果有的话）
            bed_new.image(image_to_image_result, caption="宁的自定义床")
        else:
            st.warning("请先输入Prompt！")


if __name__ == "__main__":
    main()

