---
layout: default
title: SHRUG-FM: Reliability-Aware Foundation Models for Earth Observation
---

# SHRUG-FM: Reliability-Aware Foundation Models for Earth Observation

**arXiv**: [2511.10370v1](https://arxiv.org/abs/2511.10370) | [PDF](https://arxiv.org/pdf/2511.10370.pdf)

**作者**: Kai-Hendrik Cohrs, Zuzanna Osika, Maria Gonzalez-Calabuig, Vishal Nedungadi, Ruben Cartuyvels, Steffen Knoblauch, Joppe Massant, Shruti Nath, Patrick Ebel, Vasileios Sitokonstantinou

---

## 💡 一句话要点

**提出SHRUG-FM框架以提升地球观测基础模型在未知环境中的可靠性**

**关键词**: `地球观测基础模型` `可靠性感知预测` `OOD检测` `不确定性量化` `烧伤疤痕分割` `地理空间分析`

## 📋 核心要点

1. 地球观测基础模型在预训练数据不足的环境中表现不可靠
2. 集成输入空间、嵌入空间OOD检测和任务不确定性信号
3. 应用于烧伤疤痕分割，显示OOD分数与性能下降相关，不确定性标志可过滤错误预测

## 📄 摘要（原文）

> Geospatial foundation models for Earth observation often fail to perform reliably in environments underrepresented during pretraining. We introduce SHRUG-FM, a framework for reliability-aware prediction that integrates three complementary signals: out-of-distribution (OOD) detection in the input space, OOD detection in the embedding space and task-specific predictive uncertainty. Applied to burn scar segmentation, SHRUG-FM shows that OOD scores correlate with lower performance in specific environmental conditions, while uncertainty-based flags help discard many poorly performing predictions. Linking these flags to land cover attributes from HydroATLAS shows that failures are not random but concentrated in certain geographies, such as low-elevation zones and large river areas, likely due to underrepresentation in pretraining data. SHRUG-FM provides a pathway toward safer and more interpretable deployment of GFMs in climate-sensitive applications, helping bridge the gap between benchmark performance and real-world reliability.

