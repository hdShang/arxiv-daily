---
layout: default
title: "Risk Map As Middleware: Towards Interpretable Cooperative End-to-end Autonomous Driving for Risk-Aware Planning"
---

# Risk Map As Middleware: Towards Interpretable Cooperative End-to-end Autonomous Driving for Risk-Aware Planning

<div class="paper-toolbar">
  <a href="https://arxiv.org/abs/2508.07686" class="toolbar-btn" target="_blank">📄 arXiv: 2508.07686v2</a>
  <a href="https://arxiv.org/pdf/2508.07686.pdf" class="toolbar-btn" target="_blank">📥 PDF</a>
  <button class="toolbar-btn favorite-btn" data-arxiv-id="2508.07686v2" data-paper-url="__CURRENT_PAGE__" onclick="toggleFavorite(this, '2508.07686v2', 'Risk Map As Middleware: Towards Interpretable Cooperative End-to-end Autonomous Driving for Risk-Aware Planning')" title="添加到收藏夹">☆ 收藏</button>
  <button class="toolbar-btn" onclick="copyLinkToClipboard(this)">🔗 分享</button>
</div>


**作者**: Mingyue Lei, Zewei Zhou, Hongchen Li, Jiaqi Ma, Jia Hu

**分类**: cs.RO

**发布日期**: 2025-08-11 (更新: 2025-11-20)

**备注**: IEEE RA-L

---

## 💡 一句话要点

**提出风险地图中介以解决自主驾驶中的可解释性问题**

🎯 **匹配领域**: **支柱一：机器人控制 (Robot Control)** **支柱八：物理动画 (Physics-based Animation)**

**关键词**: `自主驾驶` `风险感知` `可解释性` `模型预测控制` `Transformer` `多代理系统` `时空表示` `合作驾驶`

## 📋 核心要点

1. 现有的单一代理端到端自主驾驶方法受到遮挡和感知范围限制，导致驾驶风险和行为不可解释。
2. 本文提出风险地图中介（RiskMM），通过构建可解释的时空表示和建模环境交互来提升自主驾驶的安全性和可解释性。
3. 在真实世界数据集上的评估显示，RiskMM在风险感知轨迹规划中表现优越，显著提高了可解释性和稳健性。

## 📝 摘要（中文）

端到端的自主驾驶范式已成为一种有前景的方法。然而，现有的单一代理端到端管道常常受到遮挡和感知范围有限的限制，导致驾驶风险。此外，其黑箱特性使得驾驶行为缺乏可解释性，导致系统不可信。为了解决这些问题，本文提出了风险地图中介（RiskMM）并构建了一个可解释的合作端到端驾驶框架。风险地图直接从驾驶数据中学习，为下游规划提供了场景的可解释时空表示。RiskMM首先构建了一个基于Transformer的多代理时空表示，然后通过建模周围环境的交互来推导风险感知表示。这些表示随后被输入到基于学习的模型预测控制（MPC）模块中。MPC规划器能够内在地适应物理约束和不同的车辆类型，并通过将学习到的参数与显式MPC元素对齐来提供解释。对真实世界V2XPnP-Seq数据集的评估表明，RiskMM在风险感知轨迹规划中实现了优越且稳健的性能，显著增强了合作端到端驾驶框架的可解释性。

## 🔬 方法详解

**问题定义**：本文旨在解决现有自主驾驶方法的可解释性不足和风险感知能力弱的问题，尤其是在遮挡和感知范围有限的情况下，导致的危险驾驶行为。

**核心思路**：提出风险地图中介（RiskMM），通过直接从驾驶数据中学习，构建可解释的时空表示，增强自主驾驶系统的安全性和可解释性。

**技术框架**：RiskMM采用统一的基于Transformer的架构，首先构建多代理时空表示，然后通过注意力机制建模周围环境的交互，最后将这些表示输入到模型预测控制（MPC）模块中进行轨迹规划。

**关键创新**：RiskMM的主要创新在于其可解释性，通过将学习到的参数与显式MPC元素对齐，使得规划过程透明化，区别于传统的黑箱方法。

**关键设计**：在设计中，采用了Transformer架构来处理时空数据，注意力机制用于建模环境交互，MPC模块则考虑了物理约束和不同车辆类型的适应性。

## 📊 实验亮点

在真实世界的V2XPnP-Seq数据集上，RiskMM在风险感知轨迹规划中表现出色，显著提高了可解释性和稳健性，具体性能数据表明，相较于基线方法，提升幅度达到XX%。

## 🎯 应用场景

该研究具有广泛的应用潜力，尤其是在智能交通系统和自动驾驶车辆中。通过提高自主驾驶的可解释性和安全性，RiskMM可以为未来的自动驾驶技术提供更可靠的解决方案，促进其在城市交通和复杂环境中的应用。

## 📄 摘要（原文）

> End-to-end paradigm has emerged as a promising approach to autonomous driving. However, existing single-agent end-to-end pipelines are often constrained by occlusion and limited perception range, resulting in hazardous driving. Furthermore, their black-box nature prevents the interpretability of the driving behavior, leading to an untrustworthiness system. To address these limitations, we introduce Risk Map as Middleware (RiskMM) and propose an interpretable cooperative end-to-end driving framework. The risk map learns directly from the driving data and provides an interpretable spatiotemporal representation of the scenario from the upstream perception and the interactions between the ego vehicle and the surrounding environment for downstream planning. RiskMM first constructs a multi-agent spatiotemporal representation with unified Transformer-based architecture, then derives risk-aware representations by modeling interactions among surrounding environments with attention. These representations are subsequently fed into a learning-based Model Predictive Control (MPC) module. The MPC planner inherently accommodates physical constraints and different vehicle types and can provide interpretation by aligning learned parameters with explicit MPC elements. Evaluations conducted on the real-world V2XPnP-Seq dataset confirm that RiskMM achieves superior and robust performance in risk-aware trajectory planning, significantly enhancing the interpretability of the cooperative end-to-end driving framework. The codebase will be released to facilitate future research in this field.

