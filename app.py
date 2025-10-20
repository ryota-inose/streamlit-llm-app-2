from dotenv import load_dotenv

load_dotenv()

import os
import streamlit as st
from openai import OpenAI

st.title("なんでも相談アプリ")

st.write("##### 健康についての相談 ")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、健康に関する相談ができます。")
st.write("##### 服装についての相談")
st.write("入力フォームにテキストを入力し、「実行」ボタンを押すことで、服装に関する相談ができます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["健康についての相談", "服装についての相談"]
)

st.divider()

input_message = st.text_input(label="相談内容を入力してください。")
text_count = len(input_message)

if st.button("実行"):
    st.divider()

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("OPENAI_API_KEY が設定されていません。")
    else:
        client = OpenAI(api_key=api_key)

        if selected_item == "健康についての相談":
            system_prompt = "あなたは健康に関するアドバイザーです。安全なアドバイスを提供してください。"
        else:
            system_prompt = "あなたは服装に関するアドバイザーです。安全なアドバイスを提供してください。"

        first_completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": input_message}
            ],
            temperature=0.5
        )

        # show the assistant response in the Streamlit app
        response_text = first_completion.choices[0].message.content
        st.write(response_text)