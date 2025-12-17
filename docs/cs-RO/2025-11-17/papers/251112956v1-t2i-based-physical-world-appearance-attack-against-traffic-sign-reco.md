---
layout: default
title: T2I-Based Physical-World Appearance Attack against Traffic Sign Recognition Systems in Autonomous Driving
---

# T2I-Based Physical-World Appearance Attack against Traffic Sign Recognition Systems in Autonomous Driving

**arXiv**: [2511.12956v1](https://arxiv.org/abs/2511.12956) | [PDF](https://arxiv.org/pdf/2511.12956.pdf)

**作者**: Chen Ma, Ningfei Wang, Junhao Zheng, Qing Guo, Qian Wang, Qi Alfred Chen, Chao Shen

---

## 💡 一句话要点

**提出DiffSign框架以生成针对自动驾驶交通标志识别系统的物理世界外观攻击**

**关键词**: `交通标志识别` `物理世界攻击` `文本到图像模型` `对抗样本` `自动驾驶安全`

## 📋 核心要点

1. 现有物理世界外观攻击存在隐蔽性差和泛化能力弱的问题
2. 采用CLIP损失和掩码提示改进攻击聚焦与可控性
3. 在多种真实条件下平均攻击成功率达83.3%

## 📄 摘要（原文）

> Traffic Sign Recognition (TSR) systems play a critical role in Autonomous Driving (AD) systems, enabling real-time detection of road signs, such as STOP and speed limit signs. While these systems are increasingly integrated into commercial vehicles, recent research has exposed their vulnerability to physical-world adversarial appearance attacks. In such attacks, carefully crafted visual patterns are misinterpreted by TSR models as legitimate traffic signs, while remaining inconspicuous or benign to human observers. However, existing adversarial appearance attacks suffer from notable limitations. Pixel-level perturbation-based methods often lack stealthiness and tend to overfit to specific surrogate models, resulting in poor transferability to real-world TSR systems. On the other hand, text-to-image (T2I) diffusion model-based approaches demonstrate limited effectiveness and poor generalization to out-of-distribution sign types.
>   In this paper, we present DiffSign, a novel T2I-based appearance attack framework designed to generate physically robust, highly effective, transferable, practical, and stealthy appearance attacks against TSR systems. To overcome the limitations of prior approaches, we propose a carefully designed attack pipeline that integrates CLIP-based loss and masked prompts to improve attack focus and controllability. We also propose two novel style customization methods to guide visual appearance and improve out-of-domain traffic sign attack generalization and attack stealthiness. We conduct extensive evaluations of DiffSign under varied real-world conditions, including different distances, angles, light conditions, and sign categories. Our method achieves an average physical-world attack success rate of 83.3%, leveraging DiffSign's high effectiveness in attack transferability.

