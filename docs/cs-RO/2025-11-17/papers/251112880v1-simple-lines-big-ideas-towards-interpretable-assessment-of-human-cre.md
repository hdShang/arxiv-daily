---
layout: default
title: Simple Lines, Big Ideas: Towards Interpretable Assessment of Human Creativity from Drawings
---

# Simple Lines, Big Ideas: Towards Interpretable Assessment of Human Creativity from Drawings

**arXiv**: [2511.12880v1](https://arxiv.org/abs/2511.12880) | [PDF](https://arxiv.org/pdf/2511.12880.pdf)

**作者**: Zihao Lin, Zhenshan Shi, Sasa Zhao, Hanwei Zhu, Lingyu Zhu, Baoliang Chen, Lei Mo

---

## 💡 一句话要点

**提出多模态多任务框架以自动评估绘画创造力，实现可解释性。**

**关键词**: `创造力评估` `多模态学习` `多任务学习` `可解释性` `绘画分析`

## 📋 核心要点

1. 核心问题：绘画创造力评估依赖专家主观评分，劳动密集且主观性强。
2. 方法要点：结合内容和风格维度，通过条件学习机制动态调整特征提取。
3. 实验或效果：模型性能优于现有回归方法，提供与人类判断一致的可视化。

## 📄 摘要（原文）

> Assessing human creativity through visual outputs, such as drawings, plays a critical role in fields including psychology, education, and cognitive science. However, current assessment practices still rely heavily on expert-based subjective scoring, which is both labor-intensive and inherently subjective. In this paper, we propose a data-driven framework for automatic and interpretable creativity assessment from drawings. Motivated by the cognitive understanding that creativity can emerge from both what is drawn (content) and how it is drawn (style), we reinterpret the creativity score as a function of these two complementary dimensions.Specifically, we first augment an existing creativity labeled dataset with additional annotations targeting content categories. Based on the enriched dataset, we further propose a multi-modal, multi-task learning framework that simultaneously predicts creativity scores, categorizes content types, and extracts stylistic features. In particular, we introduce a conditional learning mechanism that enables the model to adapt its visual feature extraction by dynamically tuning it to creativity-relevant signals conditioned on the drawing's stylistic and semantic cues.Experimental results demonstrate that our model achieves state-of-the-art performance compared to existing regression-based approaches and offers interpretable visualizations that align well with human judgments. The code and annotations will be made publicly available at https://github.com/WonderOfU9/CSCA_PRCV_2025

