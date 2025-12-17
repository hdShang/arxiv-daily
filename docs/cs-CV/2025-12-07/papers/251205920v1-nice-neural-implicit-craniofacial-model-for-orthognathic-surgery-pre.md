---
layout: default
title: NICE: Neural Implicit Craniofacial Model for Orthognathic Surgery Prediction
---

# NICE: Neural Implicit Craniofacial Model for Orthognathic Surgery Prediction

**arXiv**: [2512.05920v1](https://arxiv.org/abs/2512.05920) | [PDF](https://arxiv.org/pdf/2512.05920.pdf)

**作者**: Jiawen Yang, Yihui Cao, Xuanyu Tian, Yuyao Zhang, Hongjiang Wei

---

## 💡 一句话要点

**提出NICE神经隐式颅面模型，用于正颌手术预测，以解决骨骼运动与软组织复杂非线性交互建模难题。**

**关键词**: `神经隐式表示` `正颌手术预测` `颅面建模` `生物力学响应` `深度学习`

## 📋 核心要点

1. 核心问题：正颌手术后面部外观预测因骨骼运动与软组织复杂非线性交互而具挑战性。
2. 方法要点：采用区域特定隐式SDF解码器重建面部结构，结合共享手术潜码驱动变形解码器建模非线性生物力学响应。
3. 实验或效果：在关键面部区域如唇部和下巴提升预测准确性，优于现有方法，保持解剖完整性。

## 📄 摘要（原文）

> Orthognathic surgery is a crucial intervention for correcting dentofacial skeletal deformities to enhance occlusal functionality and facial aesthetics. Accurate postoperative facial appearance prediction remains challenging due to the complex nonlinear interactions between skeletal movements and facial soft tissue. Existing biomechanical, parametric models and deep-learning approaches either lack computational efficiency or fail to fully capture these intricate interactions. To address these limitations, we propose Neural Implicit Craniofacial Model (NICE) which employs implicit neural representations for accurate anatomical reconstruction and surgical outcome prediction. NICE comprises a shape module, which employs region-specific implicit Signed Distance Function (SDF) decoders to reconstruct the facial surface, maxilla, and mandible, and a surgery module, which employs region-specific deformation decoders. These deformation decoders are driven by a shared surgical latent code to effectively model the complex, nonlinear biomechanical response of the facial surface to skeletal movements, incorporating anatomical prior knowledge. The deformation decoders output point-wise displacement fields, enabling precise modeling of surgical outcomes. Extensive experiments demonstrate that NICE outperforms current state-of-the-art methods, notably improving prediction accuracy in critical facial regions such as lips and chin, while robustly preserving anatomical integrity. This work provides a clinically viable tool for enhanced surgical planning and patient consultation in orthognathic procedures.

