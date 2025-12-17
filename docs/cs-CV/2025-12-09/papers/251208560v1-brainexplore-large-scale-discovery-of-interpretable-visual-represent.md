---
layout: default
title: BrainExplore: Large-Scale Discovery of Interpretable Visual Representations in the Human Brain
---

# BrainExplore: Large-Scale Discovery of Interpretable Visual Representations in the Human Brain

**arXiv**: [2512.08560v1](https://arxiv.org/abs/2512.08560) | [PDF](https://arxiv.org/pdf/2512.08560.pdf)

**作者**: Navve Wasserman, Matias Cosarinsky, Yuval Golbari, Aude Oliva, Antonio Torralba, Tamar Rott Shaham, Michal Irani

---

## 💡 一句话要点

**提出大规模自动化框架BrainExplore，以发现和解释人脑视觉表征**

**关键词**: `脑视觉表征` `fMRI数据分析` `无监督分解` `自动化解释` `大规模发现` `可解释模式`

## 📋 核心要点

1. 核心问题：人脑如何编码视觉概念，现有研究规模小且依赖人工，缺乏系统验证。
2. 方法要点：通过无监督分解发现候选模式，自动化识别图像和生成语言描述，并评估可靠性。
3. 实验或效果：揭示数千个可解释模式，涵盖多种视觉概念，包括未报告的细粒度表征。

## 📄 摘要（原文）

> Understanding how the human brain represents visual concepts, and in which brain regions these representations are encoded, remains a long-standing challenge. Decades of work have advanced our understanding of visual representations, yet brain signals remain large and complex, and the space of possible visual concepts is vast. As a result, most studies remain small-scale, rely on manual inspection, focus on specific regions and properties, and rarely include systematic validation. We present a large-scale, automated framework for discovering and explaining visual representations across the human cortex. Our method comprises two main stages. First, we discover candidate interpretable patterns in fMRI activity through unsupervised, data-driven decomposition methods. Next, we explain each pattern by identifying the set of natural images that most strongly elicit it and generating a natural-language description of their shared visual meaning. To scale this process, we introduce an automated pipeline that tests multiple candidate explanations, assigns quantitative reliability scores, and selects the most consistent description for each voxel pattern. Our framework reveals thousands of interpretable patterns spanning many distinct visual concepts, including fine-grained representations previously unreported.

