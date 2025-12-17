---
layout: default
title: Spatio-Temporal Hierarchical Causal Models
---

# Spatio-Temporal Hierarchical Causal Models

**arXiv**: [2511.20558v1](https://arxiv.org/abs/2511.20558) | [PDF](https://arxiv.org/pdf/2511.20558.pdf)

**作者**: Xintong Li, Haoran Zhang, Xiao Zhou

---

## 💡 一句话要点

**提出时空分层因果模型以处理未观测混杂下的因果推断问题**

**关键词**: `时空因果推断` `分层因果模型` `未观测混杂` `因果识别` `动态系统`

## 📋 核心要点

1. 核心问题：时空数据中未观测单元级混杂导致因果推断困难
2. 方法要点：引入分层因果模型，基于时空折叠定理简化识别
3. 实验或效果：在合成和真实数据集验证模型有效性

## 📄 摘要（原文）

> The abundance of fine-grained spatio-temporal data, such as traffic sensor networks, offers vast opportunities for scientific discovery. However, inferring causal relationships from such observational data remains challenging, particularly due to unobserved confounders that are specific to units (e.g., geographical locations) yet influence outcomes over time. Most existing methods for spatio-temporal causal inference assume that all confounders are observed, an assumption that is often violated in practice. In this paper, we introduce Spatio-Temporal Hierarchical Causal Models (ST-HCMs), a novel graphical framework that extends hierarchical causal modeling to the spatio-temporal domain. At the core of our approach is the Spatio-Temporal Collapse Theorem, which shows that a complex ST-HCM converges to a simpler flat causal model as the amount of subunit data increases. This theoretical result enables a general procedure for causal identification, allowing ST-HCMs to recover causal effects even in the presence of unobserved, time-invariant unit-level confounders, a scenario where standard non-hierarchical models fail. We validate the effectiveness of our framework on both synthetic and real-world datasets, demonstrating its potential for robust causal inference in complex dynamic systems.

