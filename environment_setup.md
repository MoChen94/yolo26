# YOLO 环境配置文档

## Python 环境要求
- **Python 版本**: 3.10.20

## 安装步骤

### 1. 创建虚拟环境（推荐）
```bash
python -m venv yolo_env
source yolo_env/bin/activate  # Linux/Mac
```

### 2. 安装依赖
```bash
pip install -U ultralytics
```

## 验证安装
安装完成后，运行以下命令验证环境配置：
```bash
python -c "from ultralytics import YOLO; print('YOLO 安装成功！')"
```

## 注意事项
- 建议使用虚拟环境以避免包冲突
- 确保 pip 版本为最新：`python -m pip install --upgrade pip`