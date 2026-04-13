from ultralytics import YOLO

# 加载预训练模型（推荐，迁移学习收敛更快）
model = YOLO("yolo26n.pt")

# 开始训练
results = model.train(
    data="train_data/data.yaml",   # 数据集配置文件路径
    epochs=100,                  # 训练轮数
    imgsz=640,                   # 输入图片尺寸
    batch=16,                    # 批次大小
    # device=0,                    # GPU 设备（0 表示第一块 GPU）
    project="runs/train",       # 输出目录
    name="my_yolo26_exp",       # 实验名称
)