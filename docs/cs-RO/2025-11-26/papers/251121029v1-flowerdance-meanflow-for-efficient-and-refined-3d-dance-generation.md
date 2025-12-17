---
layout: default
title: FlowerDance: MeanFlow for Efficient and Refined 3D Dance Generation
---

# FlowerDance: MeanFlow for Efficient and Refined 3D Dance Generation

**arXiv**: [2511.21029v1](https://arxiv.org/abs/2511.21029) | [PDF](https://arxiv.org/pdf/2511.21029.pdf)

**作者**: Kaixing Yang, Xulong Tang, Ziqiao Peng, Xiangyue Zhang, Puwei Wang, Jun He, Hongyan Liu

---

## 💡 一句话要点

**提出FlowerDance以高效生成高质量3D舞蹈动作，解决现有方法效率不足问题。**

**关键词**: `3D舞蹈生成` `音乐到运动` `高效推理` `非自回归生成` `运动编辑` `跨模态融合`

## 📋 核心要点

1. 核心问题：现有音乐到舞蹈生成方法效率低，限制3D渲染和表达性。
2. 方法要点：结合MeanFlow与物理一致性约束，实现少步采样高质量生成。
3. 实验效果：在AIST++和FineDance数据集上取得运动质量和效率SOTA结果。

## 📄 摘要（原文）

> Music-to-dance generation aims to translate auditory signals into expressive human motion, with broad applications in virtual reality, choreography, and digital entertainment. Despite promising progress, the limited generation efficiency of existing methods leaves insufficient computational headroom for high-fidelity 3D rendering, thereby constraining the expressiveness of 3D characters during real-world applications. Thus, we propose FlowerDance, which not only generates refined motion with physical plausibility and artistic expressiveness, but also achieves significant generation efficiency on inference speed and memory utilization . Specifically, FlowerDance combines MeanFlow with Physical Consistency Constraints, which enables high-quality motion generation with only a few sampling steps. Moreover, FlowerDance leverages a simple but efficient model architecture with BiMamba-based backbone and Channel-Level Cross-Modal Fusion, which generates dance with efficient non-autoregressive manner. Meanwhile, FlowerDance supports motion editing, enabling users to interactively refine dance sequences. Extensive experiments on AIST++ and FineDance show that FlowerDance achieves state-of-the-art results in both motion quality and generation efficiency. Code will be released upon acceptance.

