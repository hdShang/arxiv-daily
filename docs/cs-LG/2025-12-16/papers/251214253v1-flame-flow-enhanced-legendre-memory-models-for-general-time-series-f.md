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

**提出FLAME时间序列基础模型，通过流增强的勒让德记忆实现高效稳健的确定性与概率性预测。**

**关键词**: `时间序列预测` `基础模型` `勒让德记忆` `归一化流` `概率建模` `零样本学习` `长程推理` `轻量级设计`

## 📋 核心要点

1. 现有时间序列预测方法在轻量化、泛化能力和概率建模方面存在不足，难以兼顾效率与准确性。
2. FLAME通过勒让德记忆变体捕捉数据归纳偏置，并结合归一化流头实现生成式概率预测，提升长程推理能力。
3. 实验显示FLAME在TSFM-Bench和ProbTS基准上实现零样本SOTA性能，验证了其高效稳健的预测效果。

## 📝 摘要（中文）

本文介绍了FLAME，一个极其轻量且强大的时间序列基础模型家族，支持通过生成式概率建模进行确定性和概率性预测，从而确保效率和鲁棒性。FLAME利用勒让德记忆实现强大的泛化能力。通过在编码和解码阶段采用勒让德记忆的变体，即平移勒让德（LegT）和缩放勒让德（LegS），FLAME能够有效捕捉数据中的固有归纳偏置，并进行高效的长程推理。为了在保持高效的同时增强概率性预测的准确性，FLAME采用基于归一化流的预测头，以生成方式建模预测范围内的任意复杂分布。在公认的基准测试（包括TSFM-Bench和ProbTS）上的全面实验表明，FLAME在确定性和概率性预测任务上均展现出持续的最先进零样本性能。

## 🔬 方法详解

FLAME的整体框架基于勒让德记忆单元构建，包含编码和解码阶段。关键创新在于引入平移勒让德（LegT）和缩放勒让德（LegS）变体，以自适应捕捉时间序列的动态模式，增强模型对数据固有结构的建模能力。与现有方法的主要区别在于：一方面，通过勒让德记忆的数学特性实现高效的长程依赖建模，降低计算复杂度；另一方面，采用归一化流作为预测头，以生成方式灵活建模复杂概率分布，避免了传统参数化分布的局限性，从而在轻量级设计中兼顾确定性与概率性预测需求。

## 📊 实验亮点

在TSFM-Bench和ProbTS基准测试中，FLAME在确定性和概率性预测任务上均取得零样本状态-of-the-art性能，显著优于现有方法，证明了其强大的泛化能力和预测准确性。

## 🎯 应用场景

该研究可应用于金融、气象、能源和物联网等领域的时间序列预测任务，如股票价格预测、天气预报、电力负荷分析和设备故障预警，其轻量高效特性适合边缘计算和实时系统部署。

## 📄 摘要（原文）

> In this work, we introduce FLAME, a family of extremely lightweight and capable Time Series Foundation Models, which support both deterministic and probabilistic forecasting via generative probabilistic modeling, thus ensuring both efficiency and robustness. FLAME utilizes the Legendre Memory for strong generalization capabilities. Through adapting variants of Legendre Memory, i.e., translated Legendre (LegT) and scaled Legendre (LegS), in the Encoding and Decoding phases, FLAME can effectively capture the inherent inductive bias within data and make efficient long-range inferences. To enhance the accuracy of probabilistic forecasting while keeping efficient, FLAME adopts a Normalization Flow based forecasting head, which can model the arbitrarily intricate distributions over the forecasting horizon in a generative manner. Comprehensive experiments on well-recognized benchmarks, including TSFM-Bench and ProbTS, demonstrate the consistent state-of-the-art zero-shot performance of FLAME on both deterministic and probabilistic forecasting tasks.

