---
layout: default
title: Q-Doc: Benchmarking Document Image Quality Assessment Capabilities in Multi-modal Large Language Models
---

# Q-Doc: Benchmarking Document Image Quality Assessment Capabilities in Multi-modal Large Language Models

**arXiv**: [2511.11410v1](https://arxiv.org/abs/2511.11410) | [PDF](https://arxiv.org/pdf/2511.11410.pdf)

**作者**: Jiaxi Huang, Dongxu Wu, Hanwei Zhu, Lingyu Zhu, Jun Xing, Xu Wang, Baoliang Chen

---

## 💡 一句话要点

**提出Q-Doc框架以评估多模态大语言模型的文档图像质量评估能力**

**关键词**: `文档图像质量评估` `多模态大语言模型` `评估框架` `思维链提示` `失真识别`

## 📋 核心要点

1. 核心问题：多模态大语言模型在文档图像质量评估方面的潜力未被充分探索。
2. 方法要点：设计三层评估框架，包括粗粒度评分、中粒度失真类型识别和细粒度失真强度分类。
3. 实验或效果：评估显示模型存在评分不一致等问题，但思维链提示显著提升性能。

## 📄 摘要（原文）

> The rapid advancement of Multi-modal Large Language Models (MLLMs) has expanded their capabilities beyond high-level vision tasks. Nevertheless, their potential for Document Image Quality Assessment (DIQA) remains underexplored. To bridge this gap, we propose Q-Doc, a three-tiered evaluation framework for systematically probing DIQA capabilities of MLLMs at coarse, middle, and fine granularity levels. a) At the coarse level, we instruct MLLMs to assign quality scores to document images and analyze their correlation with Quality Annotations. b) At the middle level, we design distortion-type identification tasks, including single-choice and multi-choice tests for multi-distortion scenarios. c) At the fine level, we introduce distortion-severity assessment where MLLMs classify distortion intensity against human-annotated references. Our evaluation demonstrates that while MLLMs possess nascent DIQA abilities, they exhibit critical limitations: inconsistent scoring, distortion misidentification, and severity misjudgment. Significantly, we show that Chain-of-Thought (CoT) prompting substantially enhances performance across all levels. Our work provides a benchmark for DIQA capabilities in MLLMs, revealing pronounced deficiencies in their quality perception and promising pathways for enhancement. The benchmark and code are publicly available at:
>   https://github.com/cydxf/Q-Doc.

