---
layout: default
title: TriDF: Evaluating Perception, Detection, and Hallucination for Interpretable DeepFake Detection
---

# TriDF: Evaluating Perception, Detection, and Hallucination for Interpretable DeepFake Detection

**arXiv**: [2512.10652v1](https://arxiv.org/abs/2512.10652) | [PDF](https://arxiv.org/pdf/2512.10652.pdf)

**作者**: Jian-Yu Jiang-Lin, Kang-Yang Huang, Ling Zou, Ling Lo, Sheng-Ping Yang, Yu-Wen Tseng, Kun-Hsiang Lin, Chia-Ling Chen, Yu-Ting Ta, Yan-Tsung Wang, Po-Ching Chen, Hongxia Xie, Hong-Han Shuai, Wen-Huang Cheng

---

## 💡 一句话要点

**提出TriDF基准以评估可解释DeepFake检测的感知、检测和幻觉方面**

**关键词**: `DeepFake检测` `可解释性评估` `多模态基准` `感知幻觉` `合成媒体威胁`

## 📋 核心要点

1. 核心问题：生成模型进步导致伪造内容威胁安全与信任，需可解释检测系统
2. 方法要点：TriDF基准包含多模态高质量伪造数据，评估感知、检测和幻觉三个关键方面
3. 实验或效果：实验表明准确感知对可靠检测至关重要，但幻觉会严重干扰决策

## 📄 摘要（原文）

> Advances in generative modeling have made it increasingly easy to fabricate realistic portrayals of individuals, creating serious risks for security, communication, and public trust. Detecting such person-driven manipulations requires systems that not only distinguish altered content from authentic media but also provide clear and reliable reasoning. In this paper, we introduce TriDF, a comprehensive benchmark for interpretable DeepFake detection. TriDF contains high-quality forgeries from advanced synthesis models, covering 16 DeepFake types across image, video, and audio modalities. The benchmark evaluates three key aspects: Perception, which measures the ability of a model to identify fine-grained manipulation artifacts using human-annotated evidence; Detection, which assesses classification performance across diverse forgery families and generators; and Hallucination, which quantifies the reliability of model-generated explanations. Experiments on state-of-the-art multimodal large language models show that accurate perception is essential for reliable detection, but hallucination can severely disrupt decision-making, revealing the interdependence of these three aspects. TriDF provides a unified framework for understanding the interaction between detection accuracy, evidence identification, and explanation reliability, offering a foundation for building trustworthy systems that address real-world synthetic media threats.

