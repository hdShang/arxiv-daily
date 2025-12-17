---
layout: default
title: SP-Det: Self-Prompted Dual-Text Fusion for Generalized Multi-Label Lesion Detection
---

# SP-Det: Self-Prompted Dual-Text Fusion for Generalized Multi-Label Lesion Detection

**arXiv**: [2512.04875v1](https://arxiv.org/abs/2512.04875) | [PDF](https://arxiv.org/pdf/2512.04875.pdf)

**作者**: Qing Xu, Yanqian Wang, Xiangjian Hea, Yue Li, Yixuan Zhang, Rong Qu, Wenting Duan, Zhen Chen

---

## 💡 一句话要点

**提出SP-Det框架，通过自生成双文本提示实现无需专家标注的胸部X光多标签病灶检测。**

**关键词**: `病灶检测` `自提示学习` `双文本融合` `胸部X光分析` `多标签检测`

## 📋 核心要点

1. 现有可提示检测方法依赖人工标注，临床应用中成本高且不实用。
2. SP-Det引入无专家双文本提示生成器，结合语义上下文和疾病信标提示自动生成文本指导。
3. 在多个胸部X光数据集上实验，SP-Det优于先进方法，完全消除对专家标注提示的依赖。

## 📄 摘要（原文）

> Automated lesion detection in chest X-rays has demonstrated significant potential for improving clinical diagnosis by precisely localizing pathological abnormalities. While recent promptable detection frameworks have achieved remarkable accuracy in target localization, existing methods typically rely on manual annotations as prompts, which are labor-intensive and impractical for clinical applications. To address this limitation, we propose SP-Det, a novel self-prompted detection framework that automatically generates rich textual context to guide multi-label lesion detection without requiring expert annotations. Specifically, we introduce an expert-free dual-text prompt generator (DTPG) that leverages two complementary textual modalities: semantic context prompts that capture global pathological patterns and disease beacon prompts that focus on disease-specific manifestations. Moreover, we devise a bidirectional feature enhancer (BFE) that synergistically integrates comprehensive diagnostic context with disease-specific embeddings to significantly improve feature representation and detection accuracy. Extensive experiments on two chest X-ray datasets with diverse thoracic disease categories demonstrate that our SP-Det framework outperforms state-of-the-art detection methods while completely eliminating the dependency on expert-annotated prompts compared to existing promptable architectures.

