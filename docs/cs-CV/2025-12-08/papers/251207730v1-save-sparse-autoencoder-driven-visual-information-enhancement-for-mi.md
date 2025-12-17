---
layout: default
title: SAVE: Sparse Autoencoder-Driven Visual Information Enhancement for Mitigating Object Hallucination
---

# SAVE: Sparse Autoencoder-Driven Visual Information Enhancement for Mitigating Object Hallucination

**arXiv**: [2512.07730v1](https://arxiv.org/abs/2512.07730) | [PDF](https://arxiv.org/pdf/2512.07730.pdf)

**作者**: Sangha Park, Seungryong Yoo, Jisoo Mok, Sungroh Yoon

---

## 💡 一句话要点

**提出SAVE框架，利用稀疏自编码器特征增强视觉信息以缓解多模态大语言模型的对象幻觉问题**

**关键词**: `对象幻觉缓解` `稀疏自编码器` `视觉信息增强` `多模态大语言模型` `免训练方法`

## 📋 核心要点

1. 核心问题：多模态大语言模型因语言先验和视觉信息丢失易产生对象幻觉
2. 方法要点：通过二进制对象存在问答探针识别稀疏自编码器中的视觉理解特征，并沿这些特征引导模型
3. 实验或效果：在CHAIR_S基准上提升10%p，在POPE和MMHal-Bench上表现一致，优于现有免训练方法

## 📄 摘要（原文）

> Although Multimodal Large Language Models (MLLMs) have advanced substantially, they remain vulnerable to object hallucination caused by language priors and visual information loss. To address this, we propose SAVE (Sparse Autoencoder-Driven Visual Information Enhancement), a framework that mitigates hallucination by steering the model along Sparse Autoencoder (SAE) latent features. A binary object-presence question-answering probe identifies the SAE features most indicative of the model's visual information processing, referred to as visual understanding features. Steering the model along these identified features reinforces grounded visual understanding and effectively reduces hallucination. With its simple design, SAVE outperforms state-of-the-art training-free methods on standard benchmarks, achieving a 10\%p improvement in CHAIR\_S and consistent gains on POPE and MMHal-Bench. Extensive evaluations across multiple models and layers confirm the robustness and generalizability of our approach. Further analysis reveals that steering along visual understanding features suppresses the generation of uncertain object tokens and increases attention to image tokens, mitigating hallucination. Code is released at https://github.com/wiarae/SAVE.

