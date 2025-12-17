---
layout: default
title: MUSE: Multi-Scale Dense Self-Distillation for Nucleus Detection and Classification
---

# MUSE: Multi-Scale Dense Self-Distillation for Nucleus Detection and Classification

**arXiv**: [2511.05170v1](https://arxiv.org/abs/2511.05170) | [PDF](https://arxiv.org/pdf/2511.05170.pdf)

**作者**: Zijiang Yang, Hanqing Chao, Bokai Zhao, Yelin Yang, Yunshuo Zhang, Dongmei Fu, Junping Zhang, Le Lu, Ke Yan, Dakai Jin, Minfeng Xu, Yun Bian, Hui Jiang

---

## 💡 一句话要点

**提出MUSE多尺度密集自蒸馏方法以解决组织病理学中细胞核检测与分类的标注依赖问题**

**关键词**: `细胞核检测与分类` `自监督学习` `多尺度蒸馏` `组织病理学分析` `局部自蒸馏` `半监督微调`

## 📋 核心要点

1. 核心问题：现有方法依赖大量细胞核级标注，难以利用未标记数据学习判别性表示
2. 方法要点：引入NuLo坐标引导机制，实现灵活局部自蒸馏，支持跨尺度对齐
3. 实验或效果：在三个基准测试中超越监督基线和通用病理基础模型

## 📄 摘要（原文）

> Nucleus detection and classification (NDC) in histopathology analysis is a
> fundamental task that underpins a wide range of high-level pathology
> applications. However, existing methods heavily rely on labor-intensive
> nucleus-level annotations and struggle to fully exploit large-scale unlabeled
> data for learning discriminative nucleus representations. In this work, we
> propose MUSE (MUlti-scale denSE self-distillation), a novel self-supervised
> learning method tailored for NDC. At its core is NuLo (Nucleus-based Local
> self-distillation), a coordinate-guided mechanism that enables flexible local
> self-distillation based on predicted nucleus positions. By removing the need
> for strict spatial alignment between augmented views, NuLo allows critical
> cross-scale alignment, thus unlocking the capacity of models for fine-grained
> nucleus-level representation. To support MUSE, we design a simple yet effective
> encoder-decoder architecture and a large field-of-view semi-supervised
> fine-tuning strategy that together maximize the value of unlabeled pathology
> images. Extensive experiments on three widely used benchmarks demonstrate that
> MUSE effectively addresses the core challenges of histopathological NDC. The
> resulting models not only surpass state-of-the-art supervised baselines but
> also outperform generic pathology foundation models.

