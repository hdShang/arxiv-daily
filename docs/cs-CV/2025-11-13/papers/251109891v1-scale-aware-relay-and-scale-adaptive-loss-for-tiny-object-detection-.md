---
layout: default
title: Scale-Aware Relay and Scale-Adaptive Loss for Tiny Object Detection in Aerial Images
---

# Scale-Aware Relay and Scale-Adaptive Loss for Tiny Object Detection in Aerial Images

**arXiv**: [2511.09891v1](https://arxiv.org/abs/2511.09891) | [PDF](https://arxiv.org/pdf/2511.09891.pdf)

**作者**: Jinfu Li, Yuqi Huang, Hong Song, Ting Wang, Jianghan Xia, Yucong Lin, Jingfan Fan, Jian Yang

---

## 💡 一句话要点

**提出尺度感知中继层与尺度自适应损失以解决航拍图像微小目标检测问题**

**关键词**: `微小目标检测` `航拍图像` `尺度感知` `注意力机制` `损失函数优化` `目标检测框架`

## 📋 核心要点

1. 核心问题：微小目标特征在长距离网络传播中易退化，且训练中回归惩罚不均衡
2. 方法要点：SARL通过跨尺度空间-通道注意力增强特征，SAL动态调整损失权重聚焦微小目标
3. 实验效果：在多个基准数据集上提升AP达5.5%，并在噪声数据集上实现29.0% AP

## 📄 摘要（原文）

> Recently, despite the remarkable advancements in object detection, modern detectors still struggle to detect tiny objects in aerial images. One key reason is that tiny objects carry limited features that are inevitably degraded or lost during long-distance network propagation. Another is that smaller objects receive disproportionately greater regression penalties than larger ones during training. To tackle these issues, we propose a Scale-Aware Relay Layer (SARL) and a Scale-Adaptive Loss (SAL) for tiny object detection, both of which are seamlessly compatible with the top-performing frameworks. Specifically, SARL employs a cross-scale spatial-channel attention to progressively enrich the meaningful features of each layer and strengthen the cross-layer feature sharing. SAL reshapes the vanilla IoU-based losses so as to dynamically assign lower weights to larger objects. This loss is able to focus training on tiny objects while reducing the influence on large objects. Extensive experiments are conducted on three benchmarks (\textit{i.e.,} AI-TOD, DOTA-v2.0 and VisDrone2019), and the results demonstrate that the proposed method boosts the generalization ability by 5.5\% Average Precision (AP) when embedded in YOLOv5 (anchor-based) and YOLOx (anchor-free) baselines. Moreover, it also promotes the robust performance with 29.0\% AP on the real-world noisy dataset (\textit{i.e.,} AI-TOD-v2.0).

