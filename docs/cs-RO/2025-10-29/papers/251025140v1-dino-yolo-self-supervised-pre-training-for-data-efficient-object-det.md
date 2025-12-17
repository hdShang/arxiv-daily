---
layout: default
title: DINO-YOLO: Self-Supervised Pre-training for Data-Efficient Object Detection in Civil Engineering Applications
---

# DINO-YOLO: Self-Supervised Pre-training for Data-Efficient Object Detection in Civil Engineering Applications

**arXiv**: [2510.25140v1](https://arxiv.org/abs/2510.25140) | [PDF](https://arxiv.org/pdf/2510.25140.pdf)

**作者**: Malaisree P, Youwai S, Kitkobsin T, Janrungautai S, Amorndechaphon D, Rojanavasu P

---

## 💡 一句话要点

**提出DINO-YOLO混合架构以解决土木工程中数据稀缺的目标检测问题**

**关键词**: `目标检测` `自监督学习` `土木工程应用` `混合架构` `实时推理`

## 📋 核心要点

1. 土木工程目标检测受限于专业领域标注数据不足
2. 结合YOLOv12与DINOv3自监督视觉变换器，在输入和骨干网中集成特征
3. 实验显示在多个数据集上mAP显著提升，保持实时推理速度

## 📄 摘要（原文）

> Object detection in civil engineering applications is constrained by limited
> annotated data in specialized domains. We introduce DINO-YOLO, a hybrid
> architecture combining YOLOv12 with DINOv3 self-supervised vision transformers
> for data-efficient detection. DINOv3 features are strategically integrated at
> two locations: input preprocessing (P0) and mid-backbone enhancement (P3).
> Experimental validation demonstrates substantial improvements: Tunnel Segment
> Crack detection (648 images) achieves 12.4% improvement, Construction PPE (1K
> images) gains 13.7%, and KITTI (7K images) shows 88.6% improvement, while
> maintaining real-time inference (30-47 FPS). Systematic ablation across five
> YOLO scales and nine DINOv3 variants reveals that Medium-scale architectures
> achieve optimal performance with DualP0P3 integration (55.77% mAP@0.5), while
> Small-scale requires Triple Integration (53.63%). The 2-4x inference overhead
> (21-33ms versus 8-16ms baseline) remains acceptable for field deployment on
> NVIDIA RTX 5090. DINO-YOLO establishes state-of-the-art performance for civil
> engineering datasets (<10K images) while preserving computational efficiency,
> providing practical solutions for construction safety monitoring and
> infrastructure inspection in data-constrained environments.

