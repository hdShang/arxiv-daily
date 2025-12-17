---
layout: default
title: FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting
---

# FLAME: Flow Enhanced Legendre Memory Models for General Time Series Forecasting

**arXiv**: [2512.14253v1](https://arxiv.org/abs/2512.14253) | [PDF](https://arxiv.org/pdf/2512.14253.pdf)

**作者**: Xingjian Wu, Hanyin Cheng, Xiangfei Qiu, Zhengyu Li, Jilin Hu, Chenjuan Guo, Bin Yang

**分类**: cs.LG

**发布日期**: 2025-12-16

---

## 💡 一句话要点

**提出FLAME模型，通过流增强的勒让德记忆和归一化流预测头，实现高效且鲁棒的通用时间序列确定性及概率预测。**

🎯 **匹配领域**: **强化学习**

**关键词**: `时间序列预测` `勒让德记忆` `归一化流` `概率建模` `零样本学习` `基础模型` `长程推理` `轻量化模型`

## 📋 核心要点

1. 现有时间序列预测方法在泛化能力、长程推理效率和概率建模精度方面存在不足，难以兼顾轻量化和鲁棒性。
2. FLAME通过勒让德记忆变体（LegT和LegS）捕捉数据归纳偏置，并结合归一化流预测头生成复杂分布，实现高效且准确的预测。
3. 在TSFM-Bench和ProbTS基准测试中，FLAME在确定性和概率预测任务上均达到零样本最先进性能，验证了其优越性。

## 📝 摘要（中文）

本文介绍了FLAME，一个极其轻量且强大的时间序列基础模型家族，支持通过生成式概率建模进行确定性和概率预测，从而确保效率和鲁棒性。FLAME利用勒让德记忆实现强大的泛化能力。通过在编码和解码阶段采用勒让德记忆的变体，即平移勒让德（LegT）和缩放勒让德（LegS），FLAME能有效捕捉数据中的内在归纳偏置，并进行高效的长程推理。为了在保持高效的同时提升概率预测的准确性，FLAME采用基于归一化流的预测头，以生成方式建模预测范围内任意复杂的分布。在公认基准（如TSFM-Bench和ProbTS）上的全面实验表明，FLAME在确定性和概率预测任务上均展现出一致的零样本最先进性能。

## 🔬 方法详解

FLAME的整体框架基于勒让德记忆单元，在编码和解码阶段分别采用LegT和LegS变体，以增强对时间序列动态的建模能力。关键技术创新包括：利用勒让德记忆的数学特性实现强泛化和长程推理，以及引入归一化流作为预测头，以生成方式灵活建模预测分布。与现有方法的主要区别在于，FLAME将轻量化的基础模型设计与生成式概率预测相结合，避免了传统方法在复杂分布建模上的计算开销或精度损失。

## 📊 实验亮点

在TSFM-Bench和ProbTS基准测试中，FLAME在确定性和概率预测任务上均实现零样本最先进性能，显著提升了预测准确性和效率，证明了其作为时间序列基础模型的强大能力。

## 🎯 应用场景

该研究可应用于金融、能源、交通和医疗等领域的时间序列预测任务，如股票价格预测、电力负荷预测、交通流量分析和疾病趋势预测，提供高效且鲁棒的预测解决方案。

## 📄 摘要（原文）

> In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support both deterministic and probabilistic forecasting via generative probabilistic modeling, thus ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalization Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on well-recognized benchmarks, including TSFM-Bench and ProbTS, demonstrate the consistent state-of-the-art zero-shot performance of FLAME on both deterministic and probabilistic forecasting tasks.

