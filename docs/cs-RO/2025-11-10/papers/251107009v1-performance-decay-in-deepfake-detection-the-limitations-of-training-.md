---
layout: default
title: Performance Decay in Deepfake Detection: The Limitations of Training on Outdated Data
---

# Performance Decay in Deepfake Detection: The Limitations of Training on Outdated Data

**arXiv**: [2511.07009v1](https://arxiv.org/abs/2511.07009) | [PDF](https://arxiv.org/pdf/2511.07009.pdf)

**作者**: Jack Richings, Margaux Leblanc, Ian Groves, Victoria Nockles

---

## 💡 一句话要点

**提出两阶段检测方法以应对深度伪造威胁，但性能随技术更新快速衰减**

**关键词**: `深度伪造检测` `性能衰减` `两阶段方法` `数据集更新` `帧级特征` `AUROC评估`

## 📋 核心要点

1. 深度伪造技术不断进步，加剧虚假信息和欺诈威胁，检测模型面临性能快速衰减问题。
2. 开发简单有效的两阶段检测方法，在当代深度伪造上AUROC超过99.8%。
3. 模型在六个月后新技术生成的深度伪造上召回率下降超30%，强调需持续更新数据集。

## 📄 摘要（原文）

> The continually advancing quality of deepfake technology exacerbates the
> threats of disinformation, fraud, and harassment by making
> maliciously-generated synthetic content increasingly difficult to distinguish
> from reality. We introduce a simple yet effective two-stage detection method
> that achieves an AUROC of over 99.8% on contemporary deepfakes. However, this
> high performance is short-lived. We show that models trained on this data
> suffer a recall drop of over 30% when evaluated on deepfakes created with
> generation techniques from just six months later, demonstrating significant
> decay as threats evolve. Our analysis reveals two key insights for robust
> detection. Firstly, continued performance requires the ongoing curation of
> large, diverse datasets. Second, predictive power comes primarily from static,
> frame-level artifacts, not temporal inconsistencies. The future of effective
> deepfake detection therefore depends on rapid data collection and the
> development of advanced frame-level feature detectors.

