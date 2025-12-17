---
layout: default
title: Proto-Former: Unified Facial Landmark Detection by Prototype Transformer
---

# Proto-Former: Unified Facial Landmark Detection by Prototype Transformer

**arXiv**: [2510.15338v1](https://arxiv.org/abs/2510.15338) | [PDF](https://arxiv.org/pdf/2510.15338.pdf)

**作者**: Shengkai Hu, Haozhe Qi, Jun Wan, Jiaxing Huang, Lefei Zhang, Hang Sun, Dacheng Tao

---

## 💡 一句话要点

**提出Proto-Former以解决多数据集面部关键点检测的统一建模问题**

**关键词**: `面部关键点检测` `原型变换器` `多数据集训练` `自适应特征提取` `原型感知损失`

## 📋 核心要点

1. 核心问题：现有面部关键点检测方法难以统一处理不同数据集定义的多样关键点数量
2. 方法要点：通过原型变换器学习自适应原型表示，结合编码器-解码器架构和原型感知损失
3. 实验或效果：在多个基准数据集上验证，性能优于现有先进方法，代码已开源

## 📄 摘要（原文）

> Recent advances in deep learning have significantly improved facial landmark
> detection. However, existing facial landmark detection datasets often define
> different numbers of landmarks, and most mainstream methods can only be trained
> on a single dataset. This limits the model generalization to different datasets
> and hinders the development of a unified model. To address this issue, we
> propose Proto-Former, a unified, adaptive, end-to-end facial landmark detection
> framework that explicitly enhances dataset-specific facial structural
> representations (i.e., prototype). Proto-Former overcomes the limitations of
> single-dataset training by enabling joint training across multiple datasets
> within a unified architecture. Specifically, Proto-Former comprises two key
> components: an Adaptive Prototype-Aware Encoder (APAE) that performs adaptive
> feature extraction and learns prototype representations, and a Progressive
> Prototype-Aware Decoder (PPAD) that refines these prototypes to generate
> prompts that guide the model's attention to key facial regions. Furthermore, we
> introduce a novel Prototype-Aware (PA) loss, which achieves optimal path
> finding by constraining the selection weights of prototype experts. This loss
> function effectively resolves the problem of prototype expert addressing
> instability during multi-dataset training, alleviates gradient conflicts, and
> enables the extraction of more accurate facial structure features. Extensive
> experiments on widely used benchmark datasets demonstrate that our Proto-Former
> achieves superior performance compared to existing state-of-the-art methods.
> The code is publicly available at: https://github.com/Husk021118/Proto-Former.

