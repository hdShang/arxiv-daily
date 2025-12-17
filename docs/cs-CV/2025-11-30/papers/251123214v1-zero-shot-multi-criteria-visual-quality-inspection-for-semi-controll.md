---
layout: default
title: Zero-Shot Multi-Criteria Visual Quality Inspection for Semi-Controlled Industrial Environments via Real-Time 3D Digital Twin Simulation
---

# Zero-Shot Multi-Criteria Visual Quality Inspection for Semi-Controlled Industrial Environments via Real-Time 3D Digital Twin Simulation

**arXiv**: [2511.23214v1](https://arxiv.org/abs/2511.23214) | [PDF](https://arxiv.org/pdf/2511.23214.pdf)

**作者**: Jose Moises Araya-Martinez, Gautham Mohan, Kenichi Hayakawa Bolaños, Roberto Mendieta, Sarvenaz Sardari, Jens Lambrecht, Jörg Krüger

---

## 💡 一句话要点

**提出基于实时3D数字孪生的零样本多标准视觉质量检测框架，用于半控制工业环境。**

**关键词**: `零样本学习` `数字孪生` `视觉质量检测` `工业自动化` `多标准缺陷检测`

## 📋 核心要点

1. 核心问题：半控制工业环境中视觉质量检测系统复杂且数据需求高，阻碍广泛应用。
2. 方法要点：通过对象检测和姿态估计，在RGB-D空间实时比较真实场景与数字孪生，实现零样本检测。
3. 实验或效果：在汽车轴向磁通电机案例中，IoU最高达63.3%，验证了框架的有效性。

## 📄 摘要（原文）

> Early-stage visual quality inspection is vital for achieving Zero-Defect Manufacturing and minimizing production waste in modern industrial environments. However, the complexity of robust visual inspection systems and their extensive data requirements hinder widespread adoption in semi-controlled industrial settings. In this context, we propose a pose-agnostic, zero-shot quality inspection framework that compares real scenes against real-time Digital Twins (DT) in the RGB-D space. Our approach enables efficient real-time DT rendering by semantically describing industrial scenes through object detection and pose estimation of known Computer-Aided Design models. We benchmark tools for real-time, multimodal RGB-D DT creation while tracking consumption of computational resources. Additionally, we provide an extensible and hierarchical annotation strategy for multi-criteria defect detection, unifying pose labelling with logical and structural defect annotations. Based on an automotive use case featuring the quality inspection of an axial flux motor, we demonstrate the effectiveness of our framework. Our results demonstrate detection performace, achieving intersection-over-union (IoU) scores of up to 63.3% compared to ground-truth masks, even if using simple distance measurements under semi-controlled industrial conditions. Our findings lay the groundwork for future research on generalizable, low-data defect detection methods in dynamic manufacturing settings.

