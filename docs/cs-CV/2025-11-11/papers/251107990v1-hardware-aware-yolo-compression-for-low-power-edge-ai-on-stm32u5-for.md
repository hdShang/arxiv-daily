---
layout: default
title: Hardware-Aware YOLO Compression for Low-Power Edge AI on STM32U5 for Weeds Detection in Digital Agriculture
---

# Hardware-Aware YOLO Compression for Low-Power Edge AI on STM32U5 for Weeds Detection in Digital Agriculture

**arXiv**: [2511.07990v1](https://arxiv.org/abs/2511.07990) | [PDF](https://arxiv.org/pdf/2511.07990.pdf)

**作者**: Charalampos S. Kouzinopoulos, Yuri Manna

---

## 💡 一句话要点

**提出硬件感知YOLO压缩方法，用于STM32U5低功耗杂草检测以解决农业边缘AI能效问题**

**关键词**: `杂草检测` `YOLO压缩` `边缘AI` `低功耗优化` `STM32微控制器` `数字农业`

## 📋 核心要点

1. 杂草降低作物产量，传统除草方法有环境风险，需低功耗精准检测方案
2. 应用结构化剪枝、整数量化和输入缩放压缩YOLOv8n，适配STM32U5微控制器
3. 在CropAndWeed数据集评估，实现51.8mJ/推理的低能耗，平衡检测精度与效率

## 📄 摘要（原文）

> Weeds significantly reduce crop yields worldwide and pose major challenges to sustainable agriculture. Traditional weed management methods, primarily relying on chemical herbicides, risk environmental contamination and lead to the emergence of herbicide-resistant species. Precision weeding, leveraging computer vision and machine learning methods, offers a promising eco-friendly alternative but is often limited by reliance on high-power computational platforms. This work presents an optimized, low-power edge AI system for weeds detection based on the YOLOv8n object detector deployed on the STM32U575ZI microcontroller. Several compression techniques are applied to the detection model, including structured pruning, integer quantization and input image resolution scaling in order to meet strict hardware constraints. The model is trained and evaluated on the CropAndWeed dataset with 74 plant species, achieving a balanced trade-off between detection accuracy and efficiency. Our system supports real-time, in-situ weeds detection with a minimal energy consumption of 51.8mJ per inference, enabling scalable deployment in power-constrained agricultural environments.

