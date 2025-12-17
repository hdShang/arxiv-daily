---
layout: default
title: YingMusic-Singer: Zero-shot Singing Voice Synthesis and Editing with Annotation-free Melody Guidance
---

# YingMusic-Singer: Zero-shot Singing Voice Synthesis and Editing with Annotation-free Melody Guidance

**arXiv**: [2512.04779v1](https://arxiv.org/abs/2512.04779) | [PDF](https://arxiv.org/pdf/2512.04779.pdf)

**作者**: Junjie Zheng, Chunbo Hao, Guobin Ma, Xiaoyu Zhang, Gongyu Chen, Chaofan Ding, Zihao Chen, Lei Xie

---

## 💡 一句话要点

**提出基于扩散Transformer的歌声合成框架，通过无标注旋律指导实现零样本合成与编辑**

**关键词**: `歌声合成` `扩散Transformer` `零样本学习` `旋律提取` `无标注学习` `强化学习`

## 📋 核心要点

1. 核心问题：传统歌声合成依赖音素对齐和人工标注旋律，资源消耗大且难以扩展
2. 方法要点：采用扩散Transformer架构，结合旋律提取模块和隐式对齐机制，无需音素级对齐
3. 实验效果：在零样本和歌词适应场景下，客观指标和主观听感均优于现有方法，音频质量高

## 📄 摘要（原文）

> Singing Voice Synthesis (SVS) remains constrained in practical deployment due to its strong dependence on accurate phoneme-level alignment and manually annotated melody contours, requirements that are resource-intensive and hinder scalability. To overcome these limitations, we propose a melody-driven SVS framework capable of synthesizing arbitrary lyrics following any reference melody, without relying on phoneme-level alignment. Our method builds on a Diffusion Transformer (DiT) architecture, enhanced with a dedicated melody extraction module that derives melody representations directly from reference audio. To ensure robust melody encoding, we employ a teacher model to guide the optimization of the melody extractor, alongside an implicit alignment mechanism that enforces similarity distribution constraints for improved melodic stability and coherence. Additionally, we refine duration modeling using weakly annotated song data and introduce a Flow-GRPO reinforcement learning strategy with a multi-objective reward function to jointly enhance pronunciation clarity and melodic fidelity. Experiments show that our model achieves superior performance over existing approaches in both objective measures and subjective listening tests, especially in zero-shot and lyric adaptation settings, while maintaining high audio quality without manual annotation. This work offers a practical and scalable solution for advancing data-efficient singing voice synthesis. To support reproducibility, we release our inference code and model checkpoints.

