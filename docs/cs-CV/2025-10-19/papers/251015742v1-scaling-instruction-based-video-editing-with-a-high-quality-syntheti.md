---
layout: default
title: Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset
---

# Scaling Instruction-Based Video Editing with a High-Quality Synthetic Dataset

**arXiv**: [2510.15742v1](https://arxiv.org/abs/2510.15742) | [PDF](https://arxiv.org/pdf/2510.15742.pdf)

**作者**: Qingyan Bai, Qiuyu Wang, Hao Ouyang, Yue Yu, Hanlin Wang, Wen Wang, Ka Leong Cheng, Shuailei Ma, Yanhong Zeng, Zichen Liu, Yinghao Xu, Yujun Shen, Qifeng Chen

---

## 💡 一句话要点

**提出Ditto框架以解决指令视频编辑中数据稀缺问题**

**关键词**: `指令视频编辑` `合成数据集` `数据生成管道` `蒸馏模型` `时间一致性增强`

## 📋 核心要点

1. 核心问题：指令视频编辑因缺乏大规模高质量训练数据而进展缓慢
2. 方法要点：融合图像编辑器与视频生成器，构建高效数据生成管道
3. 实验或效果：使用Ditto-1M数据集训练模型，实现指令跟随能力领先

## 📄 摘要（原文）

> Instruction-based video editing promises to democratize content creation, yet
> its progress is severely hampered by the scarcity of large-scale, high-quality
> training data. We introduce Ditto, a holistic framework designed to tackle this
> fundamental challenge. At its heart, Ditto features a novel data generation
> pipeline that fuses the creative diversity of a leading image editor with an
> in-context video generator, overcoming the limited scope of existing models. To
> make this process viable, our framework resolves the prohibitive cost-quality
> trade-off by employing an efficient, distilled model architecture augmented by
> a temporal enhancer, which simultaneously reduces computational overhead and
> improves temporal coherence. Finally, to achieve full scalability, this entire
> pipeline is driven by an intelligent agent that crafts diverse instructions and
> rigorously filters the output, ensuring quality control at scale. Using this
> framework, we invested over 12,000 GPU-days to build Ditto-1M, a new dataset of
> one million high-fidelity video editing examples. We trained our model, Editto,
> on Ditto-1M with a curriculum learning strategy. The results demonstrate
> superior instruction-following ability and establish a new state-of-the-art in
> instruction-based video editing.

