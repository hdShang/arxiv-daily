---
layout: default
title: Quantifying the Privacy Implications of High-Fidelity Synthetic Network Traffic
---

# Quantifying the Privacy Implications of High-Fidelity Synthetic Network Traffic

**arXiv**: [2511.20497v1](https://arxiv.org/abs/2511.20497) | [PDF](https://arxiv.org/pdf/2511.20497.pdf)

**作者**: Van Tran, Shinan Liu, Tian Li, Nick Feamster

---

## 💡 一句话要点

**提出综合隐私指标以评估高保真合成网络流量的隐私泄露风险**

**关键词**: `合成网络流量` `隐私指标` `成员推理攻击` `数据提取攻击` `生成模型评估` `隐私泄露风险`

## 📋 核心要点

1. 核心问题：合成网络流量可能泄露敏感信息，隐私风险未充分量化。
2. 方法要点：结合成员推理攻击、数据提取攻击及网络特定标识符构建隐私指标。
3. 实验或效果：评估多种生成模型，隐私风险差异大，攻击成功率最高达100%。

## 📄 摘要（原文）

> To address the scarcity and privacy concerns of network traffic data, various generative models have been developed to produce synthetic traffic. However, synthetic traffic is not inherently privacy-preserving, and the extent to which it leaks sensitive information, and how to measure such leakage, remain largely unexplored. This challenge is further compounded by the diversity of model architectures, which shape how traffic is represented and synthesized. We introduce a comprehensive set of privacy metrics for synthetic network traffic, combining standard approaches like membership inference attacks (MIA) and data extraction attacks with network-specific identifiers and attributes. Using these metrics, we systematically evaluate the vulnerability of different representative generative models and examine the factors that influence attack success. Our results reveal substantial variability in privacy risks across models and datasets. MIA success ranges from 0% to 88%, and up to 100% of network identifiers can be recovered from generated traffic, highlighting serious privacy vulnerabilities. We further identify key factors that significantly affect attack outcomes, including training data diversity and how well the generative model fits the training data. These findings provide actionable guidance for designing and deploying generative models that minimize privacy leakage, establishing a foundation for safer synthetic network traffic generation.

