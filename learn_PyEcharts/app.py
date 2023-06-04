from flask import Flask, render_template
from PIL import Image, ImageDraw, ImageFont

app = Flask(__name__)

# 设置字体
font = ImageFont.truetype("arial.ttf", 36)

# 初始化订单金额
total_amount = 0

@app.route("/")
def index():
    global total_amount
    # 更新订单金额
    total_amount += 10

    # 创建图像
    img = Image.new('RGB', (400, 200), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    d.text((50, 50), "Total Amount: $" + str(total_amount), fill=(0, 0, 0), font=font)

    # 保存图像
    img.save("static/img.png")

    # 渲染模板
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
