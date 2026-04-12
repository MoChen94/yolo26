# YOLO26 - 目标检测模型训练框架

![YOLO Logo](https://img.alicdn.com/imgextra/i2/O1CN01vYr7xG1XpF3GfJ0uT_!!6000000002971-2-tps-160-160.png)

YOLO26 是一个基于 YOLO（You Only Look Once）算法的目标检测模型训练框架，提供快速、准确的目标检测解决方案。

## 🚀 功能特点

- **高效的目标检测**：基于 YOLO 算法，实现实时目标检测
- **模型训练支持**：完整的训练流程，支持自定义数据集
- **预训练模型**：内置 YOLO 预训练模型，开箱即用
- **易于扩展**：模块化设计，便于添加新的检测任务和模型

## 📋 环境要求

- **Python**: 3.10.20 或更高版本
- **依赖库**: Ultralytics YOLO 框架
- **硬件**: 推荐使用 GPU 进行模型训练

## 🛠️ 安装步骤

1. **克隆仓库**
   ```bash
   git clone https://github.com/MoChen94/yolo26.git
   cd yolo26
   ```

2. **安装依赖**
   ```bash
   pip install -U ultralytics
   ```

3. **验证安装**
   ```bash
   python -c "from ultralytics import YOLO; print('YOLO 安装成功！')"
   ```

## 💻 使用示例

```python
from ultralytics import YOLO

# 加载预训练模型
model = YOLO('yolo26n.pt')

# 进行目标检测
results = model('input_image.jpg')

# 显示结果
results.show()
```

## 📁 项目结构

```
yolo26/
├── main.py                 # 主程序入口
├── yolo26n.pt             # YOLO 预训练模型
├── environment_setup.md   # 环境配置文档
├── ultralytics/           # YOLO 库
└── ultralytics-main/      # YOLO 主代码库
```

## 🤝 贡献指南

欢迎提交 Issue 和 Pull Request 来改进这个项目！

## 📄 许可证

本项目基于 MIT 许可证开源。

## 📞 联系方式

如有问题或建议，欢迎通过 GitHub Issues 与我们联系。

---

**YOLO26** - 让目标检测变得更简单！