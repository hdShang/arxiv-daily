---
layout: default
title: Stress-Testing Causal Claims via Cardinality Repairs
---

# Stress-Testing Causal Claims via Cardinality Repairs

**arXiv**: [2512.02491v1](https://arxiv.org/abs/2512.02491) | [PDF](https://arxiv.org/pdf/2512.02491.pdf)

**作者**: Yarden Gabbay, Haoquan Guan, Shaull Almagor, El Kindi Rezig, Brit Youngmann, Babak Salimi

---

## 💡 一句话要点

**提出SubCure框架，通过基数修复对因果分析进行鲁棒性审计，以应对数据错误导致的脆弱性。**

**关键词**: `因果分析鲁棒性` `基数修复` `数据错误敏感性` `机器学习遗忘技术` `NP完全问题` `高影响子集识别`

## 📋 核心要点

1. 核心问题：因果分析对数据错误敏感，微小修改可能大幅改变结论，需评估鲁棒性。
2. 方法要点：基于基数修复，识别移除少量元组或子群即可使因果效应估计落入目标范围的子集。
3. 实验或效果：在四个真实数据集上验证，揭示传统方法未检测的脆弱性，高效识别高影响子集。

## 📄 摘要（原文）

> Causal analyses derived from observational data underpin high-stakes decisions in domains such as healthcare, public policy, and economics. Yet such conclusions can be surprisingly fragile: even minor data errors - duplicate records, or entry mistakes - may drastically alter causal relationships. This raises a fundamental question: how robust is a causal claim to small, targeted modifications in the data? Addressing this question is essential for ensuring the reliability, interpretability, and reproducibility of empirical findings. We introduce SubCure, a framework for robustness auditing via cardinality repairs. Given a causal query and a user-specified target range for the estimated effect, SubCure identifies a small set of tuples or subpopulations whose removal shifts the estimate into the desired range. This process not only quantifies the sensitivity of causal conclusions but also pinpoints the specific regions of the data that drive those conclusions. We formalize this problem under both tuple- and pattern-level deletion settings and show both are NP-complete. To scale to large datasets, we develop efficient algorithms that incorporate machine unlearning techniques to incrementally update causal estimates without retraining from scratch. We evaluate SubCure across four real-world datasets covering diverse application domains. In each case, it uncovers compact, high-impact subsets whose removal significantly shifts the causal conclusions, revealing vulnerabilities that traditional methods fail to detect. Our results demonstrate that cardinality repair is a powerful and general-purpose tool for stress-testing causal analyses and guarding against misleading claims rooted in ordinary data imperfections.

