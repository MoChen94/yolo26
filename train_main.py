from ultralytics import YOLO

def train():
    # 加载预训练模型
    model = YOLO("yolo26n.pt")

    # 开始训练
    results = model.train(
        data="train_data/data.yaml",   # 数据集配置文件路径
        epochs=300,                   # 训练轮数
        imgsz=640,                    # 输入图片尺寸
        batch=16,                     # 批次大小
        device=0,                     # GPU 设备
        project="runs/train",         # 输出目录
        name="my_yolo26_exp",         # 实验名称
    )

if __name__ == '__main__':
    train()