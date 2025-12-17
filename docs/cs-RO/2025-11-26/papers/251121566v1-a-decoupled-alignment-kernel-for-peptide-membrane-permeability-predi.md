---
layout: default
title: A decoupled alignment kernel for peptide membrane permeability predictions
---

# A decoupled alignment kernel for peptide membrane permeability predictions

**arXiv**: [2511.21566v1](https://arxiv.org/abs/2511.21566) | [PDF](https://arxiv.org/pdf/2511.21566.pdf)

**作者**: Ali Amirahmadi, Gökçe Geylan, Leonardo De Maria, Farzaneh Etminani, Mattias Ohlsson, Alessandro Tibo

---

## 💡 一句话要点

**提出单体感知解耦全局对齐核以预测肽膜渗透性，并改进不确定性估计**

**关键词**: `肽膜渗透性预测` `解耦全局对齐核` `高斯过程` `不确定性估计` `序列对齐`

## 📋 核心要点

1. 核心问题：环肽靶向细胞内位点，但膜渗透性差，且数据有限、不确定性估计不准
2. 方法要点：设计MD-GAK核，结合残基相似性与序列对齐，解耦局部匹配与空位惩罚
3. 实验或效果：使用高斯过程，在实验中优于现有模型，PMD-GAK变体可减少校准误差

## 📄 摘要（原文）

> Cyclic peptides are promising modalities for targeting intracellular sites; however, cell-membrane permeability remains a key bottleneck, exacerbated by limited public data and the need for well-calibrated uncertainty. Instead of relying on data-eager complex deep learning architecture, we propose a monomer-aware decoupled global alignment kernel (MD-GAK), which couples chemically meaningful residue-residue similarity with sequence alignment while decoupling local matches from gap penalties. MD-GAK is a relatively simple kernel. To further demonstrate the robustness of our framework, we also introduce a variant, PMD-GAK, which incorporates a triangular positional prior. As we will show in the experimental section, PMD-GAK can offer additional advantages over MD-GAK, particularly in reducing calibration errors. Since our focus is on uncertainty estimation, we use Gaussian Processes as the predictive model, as both MD-GAK and PMD-GAK can be directly applied within this framework. We demonstrate the effectiveness of our methods through an extensive set of experiments, comparing our fully reproducible approach against state-of-the-art models, and show that it outperforms them across all metrics.

