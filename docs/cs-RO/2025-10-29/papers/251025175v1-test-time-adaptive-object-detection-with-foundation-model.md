---
layout: default
title: Test-Time Adaptive Object Detection with Foundation Model
---

# Test-Time Adaptive Object Detection with Foundation Model

**arXiv**: [2510.25175v1](https://arxiv.org/abs/2510.25175) | [PDF](https://arxiv.org/pdf/2510.25175.pdf)

**作者**: Yingjie Gao, Yanan Zhang, Zhi Cai, Di Huang

---

## 💡 一句话要点

**提出基于基础模型的测试时自适应目标检测方法，无需源数据并适应任意域和类别。**

**关键词**: `测试时自适应` `目标检测` `基础模型` `多模态提示` `伪标签增强`

## 📋 核心要点

1. 现有方法依赖源数据统计和闭集假设，不适应真实世界跨域跨类别场景。
2. 采用多模态提示均值教师框架，结合文本和视觉提示调优，高效适应测试数据。
3. 实验显示在跨损坏和跨数据集基准上优于现有方法，代码已开源。

## 📄 摘要（原文）

> In recent years, test-time adaptive object detection has attracted increasing
> attention due to its unique advantages in online domain adaptation, which
> aligns more closely with real-world application scenarios. However, existing
> approaches heavily rely on source-derived statistical characteristics while
> making the strong assumption that the source and target domains share an
> identical category space. In this paper, we propose the first foundation
> model-powered test-time adaptive object detection method that eliminates the
> need for source data entirely and overcomes traditional closed-set limitations.
> Specifically, we design a Multi-modal Prompt-based Mean-Teacher framework for
> vision-language detector-driven test-time adaptation, which incorporates text
> and visual prompt tuning to adapt both language and vision representation
> spaces on the test data in a parameter-efficient manner. Correspondingly, we
> propose a Test-time Warm-start strategy tailored for the visual prompts to
> effectively preserve the representation capability of the vision branch.
> Furthermore, to guarantee high-quality pseudo-labels in every test batch, we
> maintain an Instance Dynamic Memory (IDM) module that stores high-quality
> pseudo-labels from previous test samples, and propose two novel
> strategies-Memory Enhancement and Memory Hallucination-to leverage IDM's
> high-quality instances for enhancing original predictions and hallucinating
> images without available pseudo-labels, respectively. Extensive experiments on
> cross-corruption and cross-dataset benchmarks demonstrate that our method
> consistently outperforms previous state-of-the-art methods, and can adapt to
> arbitrary cross-domain and cross-category target data. Code is available at
> https://github.com/gaoyingjay/ttaod_foundation.

