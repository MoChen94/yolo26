import cv2
from ultralytics import YOLO

# ==========================================
# 配置部分
# ==========================================
# 1. 你的 best.pt 模型路径
# 如果 best.pt 和此脚本在同一个文件夹，直接写文件名即可。
# 如果不在，请使用绝对路径，例如: r"E:\Project\PycharmProjects\yolo26\runs\detect\train\weights\best.pt"
model_path = r"" 

# 2. USB 摄像头索引
# 通常内置摄像头是 0，外部 USB 摄像头可能是 1, 2 等。
# 如果调用失败，尝试修改这个数字。
camera_index = 1 

# 3. 置信度阈值 (0.0 - 1.0)
# 只有模型认为可能性高于这个值的目标才会被显示出来。
conf_threshold = 0.5 
# ==========================================


def run_realtime_detection():
    # 1. 加载训练好的 YOLOv8 模型
    try:
        print(f"正在加载模型: {model_path} ...")
        model = YOLO(model_path)
        print("模型加载成功！")
    except Exception as e:
        print(f"加载模型失败，请检查路径是否正确。错误信息: {e}")
        return

    # 2. 打开 USB 摄像头
    print(f"正在打开摄像头 (索引: {camera_index}) ...")
    cap = cv2.VideoCapture(camera_index)

    # 检查摄像头是否成功打开
    if not cap.isOpened():
        print(f"错误: 无法打开摄像头 (索引: {camera_index})。")
        print("尝试更换 camera_index (例如改为 1)。")
        return

    # 设置摄像头分辨率 (可选，如果觉得卡顿可以调小)
    # cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    # cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    print("开始实时检测。按下 'q' 键退出...")

    # 3. 循环读取摄像头帧
    while True:
        # 读取一帧图像
        # ret: 布尔值，表示是否成功读取
        # frame: 读取到的图像矩阵 (BGR格式)
        ret, frame = cap.read()

        if not ret:
            print("错误: 无法从摄像头读取图像。")
            break

        # 4. 使用模型对当前帧进行推理
        # stream=True: 使用流式模式，更节省内存，适合实时处理
        results = model.predict(source=frame, conf=conf_threshold, stream=True)

        # 5. 处理推理结果并绘制到图像上
        # YOLO 的 predict 方法在 stream=True 时返回一个生成器
        for result in results:
            # result.plot() 会返回一个绘制了边界框和标签的 BGR 图像
            annotated_frame = result.plot()

            # 6. 显示带有检测结果的画面
            cv2.imshow("YOLOv8 USB Camera Detection", annotated_frame)

        # 7. 监听键盘输入
        # 等待 1 毫秒，如果按下 'q' 键，则退出循环
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # ==========================================
    # 清理部分
    # ==========================================
    # 释放摄像头资源
    cap.release()
    # 关闭所有 OpenCV 窗口
    cv2.destroyAllWindows()
    print("实时检测结束。")

if __name__ == "__main__":
    run_realtime_detection()